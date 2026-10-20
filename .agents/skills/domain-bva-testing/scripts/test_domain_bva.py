"""Regression tests for arithmetic, traceability, record integrity and portability."""

import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
loader = importlib.util.spec_from_file_location("domain_bva", ROOT / "scripts/domain_bva.py")
bva = importlib.util.module_from_spec(loader)
loader.loader.exec_module(bva)


def example(name="parcel"):
    return bva.load_json(ROOT / "data/examples" / f"{name}.json")


def numeric_spec():
    spec = example()
    spec["dimensions"] = spec["dimensions"][:1]
    spec["rules"] = spec["rules"][:1]
    return spec


def points(design):
    return design["inventories"][0]["required_points"]


class BoundaryTests(unittest.TestCase):
    def test_adjacent_invalid_endpoints_are_in_full_three_value_inventory(self):
        spec = numeric_spec()
        spec["dimensions"][0].update(nominal="10", minimum={"value": "10", "inclusive": True},
                                      maximum={"value": "11", "inclusive": True})
        design = bva.generate(spec)
        self.assertEqual(design["inventories"][0]["partition_endpoints"], ["9", "10", "11", "12"])
        self.assertEqual(points(design), ["8", "9", "10", "11", "12", "13"])
        by_value = {c["inputs"]["quantity"]: c["expected"]["domain_valid"] for c in design["cases"]}
        self.assertEqual(by_value, {"10": True, "8": False, "9": False, "11": True, "12": False, "13": False})

    def test_two_value_inventory(self):
        spec = numeric_spec()
        spec["bva"] = "2-value"
        self.assertEqual(points(bva.generate(spec)), ["0", "1", "3", "4"])

    def test_singleton_deduplicates_shared_endpoints(self):
        spec = numeric_spec()
        spec["dimensions"][0].update(nominal="1", maximum={"value": "1", "inclusive": True})
        self.assertEqual(points(bva.generate(spec)), ["-1", "0", "1", "2", "3"])

    def test_exclusive_lower_and_upper(self):
        spec = numeric_spec()
        spec["dimensions"][0].update(minimum={"value": "0", "inclusive": False}, maximum={"value": "4", "inclusive": False})
        design = bva.generate(spec)
        self.assertEqual(design["inventories"][0]["partition_endpoints"], ["0", "1", "3", "4"])
        self.assertFalse(bva.accepted(spec["dimensions"][0], "0"))
        self.assertFalse(bva.accepted(spec["dimensions"][0], "4"))

    def test_one_sided_quota(self):
        spec = example("quota")
        self.assertEqual(points(bva.generate(spec)), ["6", "7", "8", "9"])
        self.assertTrue(bva.accepted(spec["dimensions"][0], "7"))
        self.assertFalse(bva.accepted(spec["dimensions"][0], "8"))

    def test_exact_decimal_neighbors(self):
        spec = example("measurement")
        self.assertEqual(points(bva.generate(spec)), ["0.08", "0.09", "0.1", "0.11", "0.12", "0.13"])
        self.assertFalse(bva.accepted(spec["dimensions"][0], "0.105"))

    def test_negative_origin(self):
        spec = example("measurement")
        spec["dimensions"][0].update(origin="-0.05", step="0.1", nominal="0.05",
                                      minimum={"value": "-0.05", "inclusive": True},
                                      maximum={"value": "0.15", "inclusive": True})
        self.assertEqual(points(bva.generate(spec)), ["-0.25", "-0.15", "-0.05", "0.05", "0.15", "0.25", "0.35"])

    def test_enum_valid_and_explicit_invalid_only(self):
        design = bva.generate(example())
        self.assertEqual(design["inventories"][1]["required_points"], ["VN", "SG", "XX"])
        self.assertFalse(next(c for c in design["cases"] if c["inputs"]["country"] == "XX")["expected"]["domain_valid"])

    def test_nominal_dedup_preserves_all_coverage_links(self):
        design = bva.generate(example())
        nominal = next(c for c in design["cases"] if c["inputs"] == {"quantity": "2", "country": "VN"})
        self.assertEqual(len(nominal["coverage"]), 3)
        self.assertEqual(len(design["cases"]), 9)
        self.assertEqual(len({json.dumps(c["inputs"], sort_keys=True) for c in design["cases"]}), 9)

    def test_one_dimension_changes_and_new_design_never_claims_execution(self):
        spec = example()
        design = bva.generate(spec)
        for case in design["cases"]:
            self.assertLessEqual(sum(case["inputs"][d["name"]] != d["nominal"] for d in spec["dimensions"]), 1)
            self.assertEqual((case["status"], case["actual"], case["evidence"]), ("NOT RUN", None, []))
            self.assertTrue(set(case["expected"]["violated_rule_ids"]) <= {"R-QUANTITY", "R-COUNTRY"})

    def test_numeric_representations_normalize_without_losing_coverage(self):
        spec = numeric_spec()
        spec["dimensions"][0]["nominal"] = "2.00"
        self.assertEqual(len(bva.generate(spec)["cases"]), 7)

    def test_extreme_supported_value_remains_exact(self):
        spec = numeric_spec()
        spec["dimensions"][0].update(nominal="1000000000000000000000000", minimum={"value": "1000000000000000000000000", "inclusive": True})
        del spec["dimensions"][0]["maximum"]
        self.assertEqual(points(bva.generate(spec)), ["999999999999999999999998", "999999999999999999999999", "1000000000000000000000000", "1000000000000000000000001"])

    def test_small_integer_ranges_against_independent_predicate(self):
        for lower in range(-2, 2):
            for upper in range(lower + 2, lower + 5):
                for include_lower in (False, True):
                    for include_upper in (False, True):
                        with self.subTest(lower=lower, upper=upper, include_lower=include_lower, include_upper=include_upper):
                            spec = numeric_spec()
                            spec["dimensions"][0].update(nominal=str(lower + 1),
                                minimum={"value": str(lower), "inclusive": include_lower},
                                maximum={"value": str(upper), "inclusive": include_upper})
                            design = bva.generate(spec)
                            first = lower if include_lower else lower + 1
                            last = upper if include_upper else upper - 1
                            independent_endpoints = {first - 1, first, last, last + 1}
                            expected_points = {p + delta for p in independent_endpoints for delta in (-1, 0, 1)}
                            self.assertEqual(set(map(int, points(design))), expected_points)
                            for case in design["cases"]:
                                value = int(case["inputs"]["quantity"])
                                expected = (value >= lower if include_lower else value > lower) and (value <= upper if include_upper else value < upper)
                                self.assertEqual(case["expected"]["domain_valid"], expected)


class SpecValidationTests(unittest.TestCase):
    def reject(self, mutate):
        spec = numeric_spec()
        mutate(spec)
        with self.assertRaises(bva.ContractError):
            bva.validate_spec(spec)

    def test_bad_nominal_empty_domain_and_reversed_bounds(self):
        for low, high in (("4", "3"), ("2", "1")):
            with self.subTest(low=low):
                self.reject(lambda s: s["dimensions"][0].update(minimum={"value": low, "inclusive": True}, maximum={"value": high, "inclusive": True}))

    def test_precision_type_step_and_nonfinite_values(self):
        for value in (0.1, True, "NaN", "1e2", "0.0000000000000000001", "01"):
            with self.subTest(value=value):
                self.reject(lambda s: s["dimensions"][0].update(step=value))
        self.reject(lambda s: s["dimensions"][0].update(step="0"))
        self.reject(lambda s: s["dimensions"][0].update(step="-1"))
        self.reject(lambda s: s["dimensions"][0].update(step="2"))

    def test_non_aligned_threshold_requires_explicit_manual_analysis(self):
        spec = example("measurement")
        spec["dimensions"][0]["minimum"]["value"] = "0.105"
        with self.assertRaisesRegex(bva.ContractError, "align"):
            bva.validate_spec(spec)

    def test_invalid_ids_duplicate_names_rules_and_unknown_keys(self):
        self.reject(lambda s: s["rules"].append(copy.deepcopy(s["rules"][0])))
        self.reject(lambda s: s["dimensions"].append(copy.deepcopy(s["dimensions"][0])))
        self.reject(lambda s: s["dimensions"][0].update(rule_ids=["UNKNOWN"]))
        self.reject(lambda s: s.update(coupled_expression="x+y<=10"))
        self.reject(lambda s: s["feature"].update(id="../escape"))

    def test_enum_overlap_and_invalid_nominal(self):
        for change in ({"invalid_values": ["VN"]}, {"nominal": "XX"}, {"valid_values": ["VN", "VN"]}):
            spec = example()
            spec["dimensions"][1].update(change)
            with self.assertRaises(bva.ContractError):
                bva.validate_spec(spec)

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as work:
            path = Path(work) / "bad.json"
            path.write_text('{"bva":"2-value","bva":"3-value"}', encoding="utf-8")
            with self.assertRaisesRegex(bva.ContractError, "duplicate"):
                bva.load_json(path)


class ResultAuditTests(unittest.TestCase):
    def test_mixed_status_totals_and_shared_finding(self):
        result = bva.audit_results(example("results"))
        self.assertEqual(result["designed"], 6)
        self.assertEqual(result["counts"], {"PASS": 1, "FAIL": 2, "OBSERVATION": 1, "INCOMPLETE": 1, "NOT RUN": 1})
        self.assertEqual(result["executed_with_sufficient_evidence_claimed"], 4)
        self.assertEqual(result["findings"], 1)

    def test_record_mutations_detect_missing_inventory_evidence_and_bug_mapping(self):
        mutations = [
            lambda r: r["cases"].append(copy.deepcopy(r["cases"][0])),
            lambda r: r["cases"].pop(),
            lambda r: r["cases"][0].update(evidence=[]),
            lambda r: r["cases"][0].update(actual=None),
            lambda r: r["cases"][1].update(finding_ids=[]),
            lambda r: r["findings"][0].update(case_ids=["T2"]),
            lambda r: r["findings"][0].update(case_ids=["UNKNOWN"]),
            lambda r: r["cases"][-1].update(actual="fabricated"),
            lambda r: r["cases"][-1].update(evidence=["unrelated.png"]),
            lambda r: r["cases"][0].update(status="DONE"),
            lambda r: r["cases"][0].update(rule_ids=["UNKNOWN"]),
        ]
        for index, mutation in enumerate(mutations):
            with self.subTest(index=index):
                result = example("results")
                mutation(result)
                with self.assertRaises(bva.ContractError):
                    bva.audit_results(result)

    def test_metadata_does_not_assert_evidence_content_verified(self):
        result = bva.audit_results(example("results"))
        self.assertIn("Record consistency only", result["limit"])
        self.assertNotIn("product_passed", result)


class CommandTests(unittest.TestCase):
    def invoke(self, *args, cwd=None, script=None):
        return subprocess.run([sys.executable, str(script or ROOT / "scripts/domain_bva.py"), *map(str, args)],
                              cwd=cwd, capture_output=True, text=True, encoding="utf-8")

    def test_generate_from_foreign_cwd_and_refuse_overwrite(self):
        with tempfile.TemporaryDirectory() as work:
            output = Path(work) / "design"
            result = self.invoke("generate", ROOT / "data/examples/parcel.json", "--output", output, cwd=work)
            self.assertEqual(result.returncode, 0, result.stderr)
            before = (output / "cases.json").read_bytes()
            self.assertEqual(json.loads(before)["counts"]["designed"], 9)
            self.assertIn("NOT RUN", (output / "design.md").read_text(encoding="utf-8"))
            refused = self.invoke("generate", ROOT / "data/examples/parcel.json", "--output", output, cwd=work)
            self.assertEqual(refused.returncode, 2)
            self.assertEqual((output / "cases.json").read_bytes(), before)

    def test_copy_entire_skill_to_another_path_and_run_all_examples(self):
        with tempfile.TemporaryDirectory() as work:
            copied = Path(work) / "portable skill"
            shutil.copytree(ROOT, copied, ignore=shutil.ignore_patterns("__pycache__"))
            for name in ("parcel", "measurement", "quota"):
                result = self.invoke("generate", copied / f"data/examples/{name}.json", "--output", Path(work) / name,
                                     cwd=work, script=copied / "scripts/domain_bva.py")
                self.assertEqual(result.returncode, 0, result.stderr)
            result = self.invoke("audit", copied / "data/examples/results.json", cwd=work, script=copied / "scripts/domain_bva.py")
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_invalid_input_leaves_output_uncreated_and_returns_nonzero(self):
        with tempfile.TemporaryDirectory() as work:
            source, output = Path(work) / "bad.json", Path(work) / "output"
            source.write_text('{"schema_version":true}', encoding="utf-8")
            result = self.invoke("generate", source, "--output", output)
            self.assertEqual(result.returncode, 2)
            self.assertFalse(output.exists())

    def test_missing_file_and_malformed_json_fail_cleanly(self):
        with tempfile.TemporaryDirectory() as work:
            self.assertEqual(self.invoke("validate", Path(work) / "missing.json").returncode, 2)
            source = Path(work) / "bad.json"
            source.write_text("{ broken", encoding="utf-8")
            self.assertEqual(self.invoke("validate", source).returncode, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
