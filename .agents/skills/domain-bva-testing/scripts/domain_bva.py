#!/usr/bin/env python3
"""Offline Domain/BVA helpers. Python 3.10+, standard library only."""

import argparse
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction
import json
from pathlib import Path
import re
import sys

VERSION = 1
STATUSES = ("PASS", "FAIL", "OBSERVATION", "INCOMPLETE", "NOT RUN")
IDENTIFIER = re.compile(r"[A-Za-z][A-Za-z0-9_-]{0,63}\Z")
NUMBER = re.compile(r"-?(?:0|[1-9][0-9]*)(?:\.[0-9]{1,18})?\Z")


class ContractError(ValueError):
    """An input violates the documented machine-readable contract."""


def require(condition, message):
    if not condition:
        raise ContractError(message)


def record(value, required, optional=(), where="record"):
    require(isinstance(value, dict), f"{where}: expected an object")
    missing = set(required) - value.keys()
    extra = value.keys() - set(required) - set(optional)
    require(not missing, f"{where}: missing keys {sorted(missing)}")
    require(not extra, f"{where}: unsupported keys {sorted(extra)}")


def text(value, where):
    require(isinstance(value, str) and bool(value.strip()), f"{where}: expected nonempty text")


def identifier(value, where):
    require(isinstance(value, str) and bool(IDENTIFIER.fullmatch(value)), f"{where}: invalid identifier")


def strings(value, where, nonempty=False, ids=False):
    require(isinstance(value, list), f"{where}: expected an array")
    require(not nonempty or bool(value), f"{where}: cannot be empty")
    for item in value:
        (identifier if ids else text)(item, where)
    require(len(value) == len(set(value)), f"{where}: duplicate entries")


def number(value, where):
    # Decimal strings preserve caller precision; floats, exponents and NaN are refused.
    require(isinstance(value, str) and len(value) <= 48 and bool(NUMBER.fullmatch(value)),
            f"{where}: use a plain decimal string, at most 48 characters and 18 fractional digits")
    return Fraction(Decimal(value))


def numeric_text(value):
    with localcontext() as context:
        context.prec = 120
        result = format(Decimal(value.numerator) / Decimal(value.denominator), "f")
    if "." in result:
        result = result.rstrip("0").rstrip(".")
    return "0" if result == "-0" else result


def grid(dimension):
    return number(dimension["origin"], "origin"), number(dimension["step"], "step")


def accepted(dimension, value):
    if dimension["kind"] == "enum":
        return value in dimension["valid_values"]
    current = number(value, dimension["name"])
    origin, step = grid(dimension)
    if ((current - origin) / step).denominator != 1:
        return False
    for key, lower in (("minimum", True), ("maximum", False)):
        bound = dimension.get(key)
        if bound is None:
            continue
        endpoint = number(bound["value"], key)
        if current == endpoint and not bound["inclusive"]:
            return False
        if (lower and current < endpoint) or (not lower and current > endpoint):
            return False
    return True


def endpoints(dimension):
    """All endpoints of adjacent ordered partitions in the declared lattice."""
    _, step = grid(dimension)
    result = set()
    if "minimum" in dimension:
        bound = dimension["minimum"]
        first = number(bound["value"], "minimum") + (0 if bound["inclusive"] else step)
        result.update((first - step, first))
    if "maximum" in dimension:
        bound = dimension["maximum"]
        last = number(bound["value"], "maximum") - (0 if bound["inclusive"] else step)
        result.update((last, last + step))
    return sorted(result)


def validate_spec(spec):
    record(spec, ("schema_version", "feature", "rules", "fixture", "bva", "dimensions"), where="spec")
    require(type(spec["schema_version"]) is int and spec["schema_version"] == VERSION, "unsupported schema_version")
    record(spec["feature"], ("id", "title"), where="feature")
    identifier(spec["feature"]["id"], "feature.id")
    text(spec["feature"]["title"], "feature.title")
    require(spec["bva"] in ("2-value", "3-value"), "bva: select 2-value or 3-value")
    require(isinstance(spec["rules"], list) and bool(spec["rules"]), "rules: expected nonempty array")
    rule_ids = []
    for rule in spec["rules"]:
        record(rule, ("id", "source", "requirement"), where="rule")
        identifier(rule["id"], "rule.id")
        text(rule["source"], "rule.source")
        text(rule["requirement"], "rule.requirement")
        rule_ids.append(rule["id"])
    require(len(rule_ids) == len(set(rule_ids)), "rules: duplicate IDs")
    fixture_keys = ("actor", "interface", "initial_state", "setup", "action", "readback")
    record(spec["fixture"], fixture_keys, where="fixture")
    for key in fixture_keys:
        text(spec["fixture"][key], f"fixture.{key}")
    dimensions = spec["dimensions"]
    require(isinstance(dimensions, list) and 1 <= len(dimensions) <= 100, "dimensions: need 1-100 entries")
    names = []
    used_rules = set()
    for dim in dimensions:
        require(isinstance(dim, dict), "dimension: expected an object")
        kind = dim.get("kind")
        common = ("name", "kind", "nominal", "rule_ids")
        if kind == "enum":
            record(dim, common + ("valid_values",), ("invalid_values",), "enum dimension")
            strings(dim["valid_values"], "valid_values", nonempty=True)
            strings(dim.get("invalid_values", []), "invalid_values")
            require(not set(dim["valid_values"]) & set(dim.get("invalid_values", [])), "enum: valid/invalid overlap")
        else:
            require(kind in ("integer", "decimal"), "dimension.kind: expected integer, decimal or enum")
            record(dim, common + ("unit", "step", "origin"), ("minimum", "maximum"), "numeric dimension")
            text(dim["unit"], "unit")
            origin, step = grid(dim)
            require(step > 0, "step must be positive")
            declared = [dim["nominal"], dim["origin"], dim["step"]] + [dim[k]["value"] for k in ("minimum", "maximum")
                         if isinstance(dim.get(k), dict) and "value" in dim[k]]
            require(all(abs(number(v, "numeric value")) <= 10 ** 24 for v in declared), "numeric magnitudes above 10^24 require manual analysis")
            require(kind != "integer" or (step == 1 and origin == 0), "integer uses step 1 and origin 0")
            require("minimum" in dim or "maximum" in dim, "numeric dimension needs at least one bound")
            for key in ("minimum", "maximum"):
                if key not in dim:
                    continue
                record(dim[key], ("value", "inclusive"), where=key)
                bound = number(dim[key]["value"], key)
                require(type(dim[key]["inclusive"]) is bool, f"{key}.inclusive must be boolean")
                require(((bound - origin) / step).denominator == 1, f"{key}: threshold must align with lattice")
        identifier(dim["name"], "dimension.name")
        names.append(dim["name"])
        strings(dim["rule_ids"], "dimension.rule_ids", nonempty=True, ids=True)
        require(set(dim["rule_ids"]) <= set(rule_ids), "dimension: unknown rule ID")
        used_rules.update(dim["rule_ids"])
        require(accepted(dim, dim["nominal"]), f"{dim['name']}: nominal must be valid (check range, type and lattice)")
    require(len(names) == len(set(names)), "dimensions: duplicate names")
    require(used_rules == set(rule_ids), "rules: every rule must map to a supported independent dimension; handle other rules manually")
    return spec


def partition(dimension, value):
    if dimension["kind"] == "enum":
        return "allowed" if accepted(dimension, value) else "disallowed"
    if accepted(dimension, value):
        return "within"
    bound = dimension.get("minimum")
    current = number(value, "value")
    if bound and (current < number(bound["value"], "minimum") or
                  (current == number(bound["value"], "minimum") and not bound["inclusive"])):
        return "below"
    return "above"


def generate(spec):
    validate_spec(spec)
    nominal = {d["name"]: d["nominal"] if d["kind"] == "enum" else
               numeric_text(number(d["nominal"], "nominal")) for d in spec["dimensions"]}
    cases = []
    cases_by_input = {}
    inventories = []
    for dim in spec["dimensions"]:
        if dim["kind"] == "enum":
            points = dim["valid_values"] + dim.get("invalid_values", [])
            boundary_values = []
        else:
            boundary_values = endpoints(dim)
            _, step = grid(dim)
            shifts = (0,) if spec["bva"] == "2-value" else (-step, 0, step)
            points = [numeric_text(v) for v in sorted({b + delta for b in boundary_values for delta in shifts})]
        inventories.append({"dimension": dim["name"], "rule_ids": dim["rule_ids"],
                            "criterion": "enumerated representatives" if dim["kind"] == "enum" else spec["bva"],
                            "partition_endpoints": [numeric_text(v) for v in boundary_values],
                            "required_points": points})
    # Include a valid control even if it is not a required boundary point.
    selections = [(None, None)] + [(dim, value) for dim, inv in zip(spec["dimensions"], inventories)
                                  for value in inv["required_points"]]
    for dim, value in selections:
        inputs = dict(nominal)
        if dim is not None:
            inputs[dim["name"]] = value
        key = tuple(inputs.items())
        if key not in cases_by_input:
            violated = sorted({rule for d in spec["dimensions"] if not accepted(d, inputs[d["name"]])
                               for rule in d["rule_ids"]})
            case = {"id": f"TC-{len(cases) + 1:03d}", "inputs": inputs,
                    "techniques": ["EP"], "coverage": [],
                    "expected": {"domain_valid": not violated, "violated_rule_ids": violated},
                    "status": "NOT RUN", "actual": None, "evidence": []}
            cases.append(case)
            cases_by_input[key] = case
        case = cases_by_input[key]
        if dim is None:
            case["coverage"].append({"kind": "nominal-control"})
        else:
            case["coverage"].append({"dimension": dim["name"], "value": value,
                                     "partition": partition(dim, value), "rule_ids": dim["rule_ids"]})
            if dim["kind"] != "enum" and "BVA" not in case["techniques"]:
                case["techniques"].append("BVA")
    return {"schema_version": VERSION, "mode": "Design", "feature": spec["feature"],
            "rules": spec["rules"], "fixture": spec["fixture"],
            "value_encoding": "Logical values as strings; map types to the target interface before execution.",
            "limits": ["Independent declared numeric lattices and string enums only.",
                       "Review presence, types, off-grid values, interactions, state, time and postconditions separately.",
                       "Modeled domain validity is not a complete product response or execution verdict."],
            "inventories": inventories, "cases": cases,
            "counts": {"designed": len(cases), "NOT RUN": len(cases), "executed_with_sufficient_evidence": 0}}


def markdown(design):
    def cell(value):
        return str(value).replace("|", "&#124;").replace("\r", " ").replace("\n", " ")
    lines = [f"# {cell(design['feature']['title'])}", "", "Mode: Design. Every case is NOT RUN.", "",
             "Values are logical strings. Adapt them to the actual interface contract before execution.", "",
             "## Rules", "", "| ID | Source | Requirement |", "|---|---|---|"]
    lines += [f"| {cell(r['id'])} | {cell(r['source'])} | {cell(r['requirement'])} |" for r in design["rules"]]
    lines += ["", "## Fixture", ""] + [f"- {key}: {cell(value)}" for key, value in design["fixture"].items()]
    lines += ["", "## Inventories", "", "| Dimension | Criterion | Endpoints | Required values |", "|---|---|---|---|"]
    lines += [f"| {cell(i['dimension'])} | {cell(i['criterion'])} | {cell(', '.join(i['partition_endpoints']))} | {cell(', '.join(i['required_points']))} |"
              for i in design["inventories"]]
    lines += ["", "## Cases", "", "| ID | Logical inputs | Modeled domain | Violated rules | Status |", "|---|---|---|---|---|"]
    for case in design["cases"]:
        inputs = ", ".join(f"{key}={value}" for key, value in case["inputs"].items())
        expected = case["expected"]
        lines.append(f"| {case['id']} | {cell(inputs)} | {'valid' if expected['domain_valid'] else 'invalid'} | {cell(', '.join(expected['violated_rule_ids']))} | NOT RUN |")
    lines += ["", "## Manual completion", ""] + [f"- {limit}" for limit in design["limits"]]
    lines += ["- Add sourced expected response/postcondition, exact steps and reset per case using the feature record template.",
              "- Full coverage here refers only to listed modeled value inventories, not all feature behavior.", ""]
    return "\n".join(lines)


def audit_results(results):
    record(results, ("schema_version", "rule_ids", "designed_case_ids", "cases", "findings"), where="results")
    require(type(results["schema_version"]) is int and results["schema_version"] == VERSION, "unsupported schema_version")
    strings(results["rule_ids"], "rule_ids", nonempty=True, ids=True)
    strings(results["designed_case_ids"], "designed_case_ids", nonempty=True, ids=True)
    require(isinstance(results["cases"], list), "cases: expected an array")
    require(isinstance(results["findings"], list), "findings: expected an array")
    cases = {}
    for case in results["cases"]:
        record(case, ("id", "status", "rule_ids", "expected", "actual", "evidence", "reason", "finding_ids"), where="case")
        identifier(case["id"], "case.id")
        require(case["id"] not in cases, "cases: duplicate ID")
        cases[case["id"]] = case
        require(case["status"] in STATUSES, "case: unknown status")
        strings(case["rule_ids"], "case.rule_ids", nonempty=True, ids=True)
        require(set(case["rule_ids"]) <= set(results["rule_ids"]), "case: unknown rule ID")
        text(case["expected"], "case.expected")
        text(case["reason"], "case.reason")
        strings(case["evidence"], "case.evidence")
        strings(case["finding_ids"], "case.finding_ids", ids=True)
        if case["status"] == "NOT RUN":
            require(case["actual"] is None and not case["evidence"] and not case["finding_ids"], "NOT RUN cannot claim actual/evidence/findings")
        elif case["status"] in ("PASS", "FAIL", "OBSERVATION"):
            text(case["actual"], "executed case.actual")
            require(bool(case["evidence"]), "evidenced statuses require evidence references")
        else:
            require(case["actual"] is None or isinstance(case["actual"], str), "INCOMPLETE actual must be text or null")
        require((case["status"] == "FAIL") == bool(case["finding_ids"]), "FAIL requires findings; other statuses cannot map to confirmed defects")
    require(set(cases) == set(results["designed_case_ids"]), "cases do not match designed_case_ids inventory")
    findings = {}
    for finding in results["findings"]:
        record(finding, ("id", "case_ids"), where="finding")
        identifier(finding["id"], "finding.id")
        require(finding["id"] not in findings, "findings: duplicate ID")
        strings(finding["case_ids"], "finding.case_ids", nonempty=True, ids=True)
        findings[finding["id"]] = finding
        for case_id in finding["case_ids"]:
            require(case_id in cases and finding["id"] in cases[case_id]["finding_ids"], "finding: missing reciprocal case mapping")
    for case in cases.values():
        for finding_id in case["finding_ids"]:
            require(finding_id in findings and case["id"] in findings[finding_id]["case_ids"], "case: missing reciprocal finding mapping")
    counts = Counter(c["status"] for c in cases.values())
    return {"record_consistent": True, "designed": len(cases),
            "counts": {status: counts[status] for status in STATUSES},
            "executed_with_sufficient_evidence_claimed": sum(counts[s] for s in ("PASS", "FAIL", "OBSERVATION")),
            "findings": len(findings),
            "limit": "Record consistency only. Evidence content, existence and oracle correctness still require review."}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"JSON: duplicate key {key!r}")
        result[key] = value
    return result


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=unique_object,
                      parse_constant=lambda value: (_ for _ in ()).throw(ContractError(f"JSON: invalid constant {value}")))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for command, help_text in (("validate", "Check spec structure and semantic preconditions"),
                               ("generate", "Generate NOT RUN candidates into a new directory"),
                               ("audit", "Check supplied results and reciprocal defect mappings")):
        child = commands.add_parser(command, help=help_text)
        child.add_argument("input", type=Path)
        if command == "generate":
            child.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        payload = load_json(args.input)
        if args.command == "validate":
            validate_spec(payload)
            result = {"valid": True, "schema_version": VERSION}
        elif args.command == "audit":
            result = audit_results(payload)
        else:
            design = generate(payload)
            rendered = markdown(design)
            # Exclusive creation also refuses existing empty directories and symlink targets.
            args.output.mkdir(parents=True, exist_ok=False)
            (args.output / "cases.json").write_text(json.dumps(design, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            (args.output / "design.md").write_text(rendered, encoding="utf-8")
            result = {"output": str(args.output.resolve()), **design["counts"]}
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (ContractError, OSError, ValueError, TypeError, KeyError, ArithmeticError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
