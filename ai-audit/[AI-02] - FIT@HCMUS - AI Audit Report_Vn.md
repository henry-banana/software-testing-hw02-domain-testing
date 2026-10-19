# AI Audit Report — HW02

## 1. Thông tin Sinh viên và công cụ

Tống Dương Thái Hòa — MSSV23120262 — Software Testing CQ2023/3. Bài HW02-AI. OpenAI Codex có transcript nguồn cho planning, design, harness, execution và rewrite. Antigravity IDE/Claude Sonnet được khai trong bản sinh viên cung cấp; chưa có transcript tương ứng trong bộ nguồn để tự gán từng prompt/output cho công cụ này.

## 2. Provenance và phạm vi

[Appendix_A_Prompt_Log.md](../Appendix_A_Prompt_Log.md) chứa prompt và output messages nguyên văn cùng timestamp nguồn. API raw output là kết quả chương trình, không phải lời sinh viên tự viết. Appendix B dưới đây là snapshot output AI lịch sử giữ nguyên; mọi con số pending/NOT RUN bên trong fence thuộc bản cũ, không phải summary hiện tại. Không có interactions/.

## 3. Technical audit của bản viết lại

| Artifact | Vấn đề có evidence | Correction |
|---|---|---|
| A | Unicode ASCII assumption; UI/API khác nhau; A-UI-07 thiếu persistence | Oracle metadata sửa; A03 riêng; giữ incomplete |
| B | Sai tiền trong draft; nominal VIP100 bị thay thành exhausted test | Dùng raw literals; B-UI-06 incomplete; giữ original target |
| C | CamelCase/enum/endpoint sai; zero/negative đảo ID | Snake_case; fixed/percent; GET /api/coupons; map12/13,18/19 đúng |
| D | Detail category bị false PASS; cart suy từ alert; thiếu two-add sequence | D02 theo mapping; giới hạn kết luận1abc; D12 incomplete |
| Harness | scripts bị dời khỏi submission | Khôi phục3CJS; rerun81HTTP cases; original hashes unchanged |
| Summary | 114executed và counts không khớp | 114designed;109executed đủ evidence;49P/56F/4OBS/5incomplete |
| Video/Issues | Link video thật chưa có, nhóm chưa đăng Issues | Một link tạm thống nhất; group stage giữ cuối |
| AI provenance | Header Claude nhưng transcript Codex; human review lẫn version | Phân biệt tool theo record; student confirmation cũ không tự áp bản mới |

Các verdict này là technical review của Codex trong cùng phiên, không phải independent review hoặc human signoff. AI gap tables trong từng feature giải thích Prompt/Tool/Complexity cùng evidence, không bịa một thí nghiệm so sánh model.

## 4. Mức độ đáp ứng và human review

Bản trước có declaration/signature do sinh viên cung cấp và statement đã review. Lượt viết lại này thay đổi cases, verdicts, bug descriptions và summary, nên cần sinh viên đọc lại các thay đổi trước khi ký/xuất bản cuối. Không tự chuyển xác nhận bản cũ thành chữ ký cho bản mới. Technical completeness không phải tỷ lệ test PASS; SUT FAIL là finding, không phải lỗi AI tương ứng.

## 5. Kết luận sử dụng AI

AI giúp tổ chức constraint, đại diện, biên, fixture và traceability; hạn chế rõ nhất là giữ literal contract/số tiền và suy luận state qua ảnh. Chúng tôi kiểm bằng nguồn SRS, raw HTTP và ảnh thật, đồng thời giữ incomplete/observation. Giữ nguyên lịch sử output giúp thấy việc sửa sai thay vì xóa dấu vết; trách nhiệm kết luận và nộp bài thuộc sinh viên.

## 6. Mandatory Disclosure

I use AI tools for requirement analysis, Domain Testing and BVA design, scripts, API execution, evidence review, bug reporting and Markdown authoring. Ảnh UI do sinh viên cung cấp; không có ảnh/video do AI dựng, không có chữ ký mới được AI tạo. Bản nguồn cuối cần human review; video URL tạm và group Issues vẫn chờ bước được phân công.

## Appendix B — Full artifact output snapshot

Các source file snapshot dưới đây là output kỹ thuật nguyên văn tại thời điểm export. Student corrections về sau ghi trong Human Review và Git, không tự gán cho snapshot cũ. API raw evidence độc lập nằm trong evidence/execution/.

### Artifact `.agents/skills/domain-bva-testing/SKILL.md`

SHA-256: `9f4c5405cf9db46772d39a9707d6660442d50b0ca5c76df9f03406975660799a`

<details>
<summary>Full output</summary>

````text
---
name: domain-bva-testing
description: Design and audit Domain Testing and Boundary Value Analysis cases from a supplied feature specification; use for partitions, input constraints, boundary points, traceability, execution and AI gap review.
---

# Domain Testing and BVA

## Inputs

Obtain feature ID/pool, versioned SRS, relevant API/UI behavior, chosen execution seam, fixture state and available lecture guidance. Record missing requirements as open questions; proceed with independent work. Match the user's approved scope. For this homework, API execution is available; UI/device evidence belongs to the student and follows the manual handoff. Keep documents Markdown.

## Workflow

1. **Oracle.** Quote or paraphrase the exact applicable rule and source section. List inputs, outputs and state transitions. Completion: every expected result has a source or is explicitly an observation; no implementation behavior is its own oracle.
2. **Domains.** Identify valid/invalid classes for values, types, presence, identity and state. Express cross-input constraints. Hold other dimensions valid while isolating one invalid class; add meaningful interactions separately. Completion: each class has a representative and stable domain ID.
3. **Boundaries.** Identify ordered domains, inclusive/exclusive comparisons and precision. Select ON/OFF/IN points and neighbors, with numeric/date unit explicit. Include applicable intersections. Completion: boundary table maps every chosen point to a TC; enums and unspecified maxima are not invented numeric boundaries.
4. **Cases.** Assign unique IDs. Record technique (Domain/BVA/both), rule, preconditions/reset, exact input, numbered actions, expected and public seam. Count shared-coverage IDs once. Completion: another person can reproduce without guessing inputs or account state.
5. **Review.** Identify invalid assumptions, omitted classes, unrealistic data and masking failures. Preserve original AI output and a visible correction with reason. Technical model review and student human review are separate. Completion: each decision is accepted/rejected/incomplete with evidence; unresolved rules remain observations.
6. **Execute.** Isolate mutable fixtures, pin source version, redact credentials and capture request/response or genuine UI evidence. Completion: each executed TC has actual/time/status/evidence. Unexecuted UI stays NOT RUN; compiler/API success does not imply native UI success.
7. **Bugs.** Reproduce failures, group by behavior and retain expected/actual/steps/severity proposal/TC mapping. Completion: evidence supports each bug; missing screenshot/Issue URL is explicitly pending. Publish only to the user's designated repository.
8. **Audit.** Summarize counts by ID/seam, analyze actual design gaps without attributing invented human discoveries, and record AI tool/time/prompt/output/verdict/correction. Completion: designed/executed/status counts reconcile and every remaining manual action is specific.

## Outputs

One feature analysis, detailed cases, actual execution evidence, bug entries and AI gap analysis. Reuse existing homework files rather than create another plan inside the submission repo. The course templates keep their original filenames in ai-audit/; interactions are embedded in the audit document, with no interactions/ directory.

## Homework example

See [FR-17 analysis](../../../reports/C-FR17-domain.md), [cases](../../../tests/C-FR17-coupon-management.md), [raw execution](../../../evidence/execution/C-api.md) and [demonstration record](../../../reports/skill-demonstration.md). These are outputs of applying the procedure in this session, not an independent AI benchmark or a recorded video.

````

</details>

### Artifact `reports/A-FR04-domain.md`

SHA-256: `57183b9691e86092d25f6b3fef61b52118f2a2cab7e0c411032834353de36d2b`

<details>
<summary>Full output</summary>

````text
# A — FR-04: Personal profile management

## Requirements and test oracle

SRS FR-04: user đã đăng nhập được cập nhật name, phone, shipping_address của chính mình. Phone bắt đầu `0`, dài 10–11 chữ số. Email không đổi qua UI; role không được tự đổi (SEC-06). Quyền truy cập theo SEC-02. Nguồn: [SRS tại baseline](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md#fr-04-quản-lý-hồ-sơ-cá-nhân).

## Domain Testing — từng bước

1. Chọn public interfaces: PUT/GET `/api/users/me`; UI `/profile`. Fixture tạo user 2 và user 3 tách biệt.
2. Xác định vector input `(JWT, target identity, phone, name, address, role attempt)`. Outputs là chấp nhận/từ chối và trạng thái lưu sau thao tác; chỉ thông báo thành công chưa đủ chứng minh.
3. Miền hợp lệ của phone: `startsWith0 ∧ digitsOnly ∧ 10 ≤ length ≤ 11`. Miền có thể cập nhật giới hạn bởi `target = authenticated user` và `role unchanged`.
4. Chia các lớp bên dưới; thay một điều kiện mỗi lần trong khi giữ JWT/name/address hợp lệ để lỗi không bị điều kiện khác che.
5. Chọn đại diện rồi bổ sung các boundary. So sánh cập nhật qua API với UI riêng để nhận ra backend acceptance không chứng minh frontend acceptance.
6. Kiểm tra liên kết nhiều chiều: giữ length hợp lệ nhưng đổi prefix; giữ mọi trường hợp lệ nhưng thêm role/id của user khác. Đây là domain constraints, không phải chỉ kiểm tra độ dài.
7. Đọc lại hồ sơ qua GET bằng JWT tương ứng. Xác minh dữ liệu user khác không thay đổi. Không dùng database làm expected oracle.

| Domain ID | Lớp và đại diện | Kỳ vọng | Cases |
|---|---|---|---|
| A-D1 | Phone hợp lệ: 0912345678, 09123456789 | Lưu đúng giá trị | A-API-01/02 |
| A-D2 | Quá ngắn: rỗng, 1, 8, 9 chữ số | Từ chối, dữ liệu cũ giữ nguyên | A-API-03/05/06/07 |
| A-D3 | Quá dài: 12, 13 chữ số | Từ chối | A-API-04/08 |
| A-D4 | Prefix khác 0 dù length hợp lệ | Từ chối | A-API-09/10 |
| A-D5 | Chữ/khoảng trắng/+84/dấu gạch/null | Từ chối phone không hợp lệ | A-API-11–14/16 |
| A-D6 | Unicode digits | Quan sát riêng vì SRS chưa nói rõ numeral encoding | A-API-15 |
| A-D7 | Name/address tiếng Việt | Chấp nhận khi phone hợp lệ | A-API-17 |
| A-D8 | User cố đổi role | Giữ role=user hoặc từ chối | A-API-18 |
| A-D9 | Body chỉ định user khác | Chỉ sửa user xác thực | A-API-19 |
| A-D10 | Thiếu/JWT sai | Không đọc/sửa được profile | A-API-20–22 |
| A-D11 | Email trên UI | Không chỉnh sửa được | A-UI-06 |

## BVA

| Biến | Boundary / bước | Giá trị | Cases |
|---|---|---|---|
| Phone length | Lower=10, upper=11, delta=1 digit | 9 invalid, 10 valid, 11 valid, 12 invalid | A-API-03/01/02/04; A-UI-01–04 |

Đây là các điểm biên và lân cận theo đơn vị ký tự, không phải BVA trên giá trị số của phone. Kết hợp cả hai biên cho tập `{9,10,11,12}`; 8/13 là điểm sâu trong miền invalid, không tính là biên mới. Prefix và role là lớp rời rạc nên dùng Domain Testing, không bịa min/max số học. Name/address không có giới hạn chiều dài trong SRS; chưa gán max-length bug.

## Coverage and limitations

Cases và steps: [A-FR04-profile.md](../tests/A-FR04-profile.md). Raw API: [A-api.md](../evidence/execution/A-api.md). UI có ID riêng và chờ chạy. Lecture của môn chưa có trong workspace; phần phương pháp hiện dựa SRS và [ISTQB CTFL v4.0.1 §4.2.1–4.2.2](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), sinh viên đối chiếu slide khi review. Không nhận 100% coverage của toàn bộ hệ thống.

````

</details>

### Artifact `reports/A-FR04-review.md`

SHA-256: `e5cd76263354d61a0284396164390a8422ff3546fc423c40722be17c68ad50a7`

<details>
<summary>Full output</summary>

````text
# FR-04 — Technical review and AI gaps

## Actual API result

22 executed = 7 PASS + 14 FAIL + 1 OBSERVATION. Evidence: [A-api.md](../evidence/execution/A-api.md). Original SUT checksums unchanged. Seven separate Web UI cases remain NOT RUN.

- BUG-A01: invalid phones accepted and persisted (13 FAIL cases, excluding Unicode observation). A-API-03 is the minimal lower-bound reproduction: PUT phone=091234567 returns success; GET returns the same invalid phone rather than retaining 0912345678.
- BUG-A02: A-API-18 changes role from user to admin via profile update. GET returns role=admin. A current token retaining role=user does not negate database privilege escalation; no claim of downstream admin UI access has been made.
- Ownership body-id and missing/invalid authentication checks passed; a success finding does not cover every possible attack.

## AI gap analysis / corrections

1. Initial case metadata treated fullwidth Unicode digits as definitively invalid. SRS only states digits and prefix without encoding rules. Codex corrected A-API-15 to OBSERVATION before execution rather than inventing an extra bug.
2. Initial focus on phone length would miss role tampering and body identity; separate constraints in A-API-18/19 prevent valid phone data from masking ownership gaps.
3. Source inspection shows a frontend regex accepting a different pattern than SRS. That is only a static suspicion; A-UI cases must confirm actual UI rejection/acceptance. API results cannot establish this UI bug.
4. No known test/bug omission is attributed to a specific external AI model without an actual draft showing that omission. These are corrections to this Codex-produced design; student review is still pending.

## Review status

Codex technical review only. Sinh viên chưa xác nhận audit verdict, trải nghiệm cá nhân hoặc self-assessment. Screenshots và GitHub Issues chờ phần thủ công/nhóm cuối.

````

</details>

### Artifact `reports/B-FR09-domain.md`

SHA-256: `b523987f117f1e0310a5184209da9d6fefe4f2aee7e686b42c571a0b5305f6d0`

<details>
<summary>Full output</summary>

````text
# B — FR-09: Discount coupons

## Requirements and test oracle

[SRS baseline FR-09](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md#fr-09-mã-giảm-giá-coupon): chấp nhận khi C1 coupon tồn tại/active, C2 now < expiry, C3 total ≥ minimum, C4 JWT hợp lệ, C5 lượt dùng của user < limit. Giảm percent = total × value / 100; fixed = value; final = total − discount.

## Domain Testing — từng bước

1. Vector input gồm `(code/existence/active, now/expiry, total/minimum, JWT identity, usage/limit, type/value)`; output có reject hoặc discount/final.
2. Mô tả miền chấp nhận bằng `C1 ∧ C2 ∧ C3 ∧ C4 ∧ C5`. Sử dụng fixed coupon để tách validation khỏi lỗi công thức percent.
3. Dùng trạng thái hợp lệ nominal: BIGBUY active, expiry 2099, total=600000, user 2 có JWT hợp lệ và chưa dùng; expected discount=50000/final=550000 được tính độc lập từ SRS.
4. Lần lượt đảo mỗi điều kiện còn giữ bốn điều kiện kia đúng. Tách nonexistent và inactive vì hai nguyên nhân cùng nằm trong C1.
5. Mở rộng vào boundary ở minimum, expiry, usage; thêm giao điểm total=minimum và used=limit−1. Test nhiều điều kiện sai chỉ kỳ vọng reject, không đặt thứ tự thông báo lỗi vì SRS không yêu cầu.
6. Xác minh authenticated identity: user 2 đã hết lượt không được bypass bằng user_id=3 hoặc bỏ user_id. Fixture dùng DB để dựng lượt dùng, còn quan sát qua POST public.
7. Tính expected bằng literal theo SRS; không sao chép công thức implementation. Đầu vào có phần lẻ được ghi rõ SRS chưa định nghĩa rounding; case 400000×10% cho đáp số nguyên để kết luận lỗi không phụ thuộc rounding.

| Domain | Đại diện | Kỳ vọng | Cases |
|---|---|---|---|
| B-D1 | Fixed hợp lệ BIGBUY/600000 | 50000 / 550000 | B-API-01 |
| B-D2 | Total dưới/bằng/trên minimum | Reject / accept / accept | B-API-02–07 |
| B-D3 | Percent SAVE10/400000; P100/400000 | 40000/360000; 400000/0 | B-API-08/26 |
| B-D4 | Mã không có, inactive, missing | Reject | B-API-09–11 |
| B-D5 | Expiry trước/bằng/sau now | Reject / reject / accept | B-API-12–14 |
| B-D6 | used 0/1/2/3, limit 2 | Accept / accept / reject / reject | B-API-15–18 |
| B-D7 | Missing/invalid/expired JWT | 401/403 | B-API-19–21 |
| B-D8 | Spoof/omit body user_id khi user xác thực hết lượt | Reject | B-API-22/23 |
| B-D9 | Total=300000, VIP100 used=1 | Accept final=200000 | B-API-24 |
| B-D10 | Inactive + insufficient + unauthenticated | Reject; precedence unspecified | B-API-25 |

## BVA

| Boundary | ON/OFF và bước | Values | Cases |
|---|---|---|---|
| total ≥ M | ON=M, OFF=M−1, IN=M+1; delta=1 VND cho fixture integer | 499999/500000/500001; 299999/300000/300001 | B-API-02–07 |
| now < expiry | ON=now (invalid), neighbors ±1ms | 2026-10-19T07:59:59.999Z / 08:00:00.000Z / 08:00:00.001Z | B-API-12–14 |
| used < limit=2 | largest valid 1, first invalid 2 | 0/1/2/3 | B-API-15–18 |
| Giao hai mặt biên | total=M và used=limit−1 | VIP100, total=300000, used=1 | B-API-24 |

Đồng hồ SUT được cố định tại 2026-10-19T08:00:00.000Z cho boundary expiry; không nhầm thời gian mô phỏng với timestamp thật của execution. Các case là phủ từng boundary đã liệt kê và một giao điểm có ý nghĩa, không phải full Cartesian product. Chưa có rule rounding, max order hoặc discount cap nên không tự đặt thêm giới hạn.

## Evidence

Cases: [B-FR09-discount-coupons.md](../tests/B-FR09-discount-coupons.md). Raw API: [B-api.md](../evidence/execution/B-api.md). UI: separate pending cases. Phương pháp tham chiếu [ISTQB CTFL §4.2.1–4.2.2](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf); lecture chưa được cung cấp.

````

</details>

### Artifact `reports/B-FR09-review.md`

SHA-256: `343c9b053f385ce482cb94e31fd3d28c3c1ada6c64585cfa4cc60c48a7f41e31`

<details>
<summary>Full output</summary>

````text
# FR-09 — Technical review and AI gaps

26 API cases = 14 PASS + 12 FAIL. [Raw evidence](../evidence/execution/B-api.md). Six UI cases remain NOT RUN.

## Verified API bug groups

- BUG-B01: inclusive minimum is rejected (B-API-03/06/24). Fixed coupon exactly at minimum isolates this from percent calculation.
- BUG-B02: percent discount calculation wrong (B-API-07/08/26). SAVE10 at total=400000 must return 40000/360000; actual negative discount is recorded in raw evidence. This integer example avoids rounding ambiguity.
- BUG-B03: expiry exactly equal to frozen current time is accepted (B-API-13); C2 requires now strictly before expiry. ±1ms neighbor cases demonstrate the distinction under a deterministic SUT clock.
- BUG-B04: missing, invalid and expired JWT still permit valid fixed coupon application (B-API-19–21).
- BUG-B05: exhausted authenticated user bypasses usage limit by spoofing or omitting body user_id (B-API-22/23). This is distinct from missing JWT: a valid token is supplied but ignored for identity.

## AI gap analysis / corrections

Initial broad boundary choices could confuse validation, arithmetic and identity. The design isolates fixed minimum equality from percent formula; uses one integer arithmetic example; controls expiry clock; and separates valid JWT with spoofed body identity from missing authentication. The percent 300001 example follows the literal formula, but rounding is not specified, so the integer-result example is the decisive evidence.

This is Codex technical analysis of its own design and results. It does not claim a human discovered these cases or reviewed every output. No empirical external-model comparison was run. UI behavior and screenshots remain pending; no screen bug is declared from HTTP evidence alone.

````

</details>

### Artifact `reports/C-FR17-domain.md`

SHA-256: `de70fff776e255dfd4b68e6d9eb8f9531f89f9c31e7e4d18b755ca481203f312`

<details>
<summary>Full output</summary>

````text
# C — FR-17: Admin coupon management

## Requirements and scope

[SRS baseline FR-17](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md#fr-17-quản-lý-mã-giảm-giá-coupon-crud): Thêm/Xem/Xóa. Required: code unique, type percent/fixed, discount_value > 0, expired_at, min_order_amount ≥ 0, max_uses_per_user ≥ 1. FR-12 yêu cầu JWT hợp lệ và role=admin. Không tự nhận thiếu Update là bug chỉ vì tên “CRUD”.

## Domain Testing — từng bước

1. Chọn POST `/api/admin/coupons`, GET `/api/coupons`, DELETE `/api/admin/coupons/:id` và form Admin làm public seams.
2. Dùng nominal vector `{code:HW02_NEW,type:fixed,value:1,min:0,expiry:2099-12-31,maxUses:1}` với admin JWT. Mỗi case bắt đầu từ fixtures sạch; SAVE10 là code đã tồn tại.
3. Chia presence, uniqueness, enum, numeric và authorization thành các domain độc lập. Bỏ từng field required thay vì bỏ tất cả cùng lúc để nhận ra server default che missing input.
4. Dùng một invalid dimension mỗi lần. Với duplicate, xác minh số record không tăng; không tự yêu cầu HTTP 409 khi spec không quy định. HTTP 500 ở duplicate được ghi actual, nhưng unique constraint vẫn có thể đạt.
5. Với role, thử riêng create/list/delete bằng admin/user/no JWT. Việc token hợp lệ không thay thế yêu cầu role=admin.
6. Với create hợp lệ, đọc lại qua GET và so sánh đầy đủ giá trị; với delete, kiểm tra coupon mục tiêu biến mất và số lượng giảm đúng một.
7. Bổ sung giao lower corners `value=1,min=0,max=1` ở nominal; không cần đặt ràng buộc percent ≤100 hoặc mã phân biệt hoa/thường khi SRS chưa nói.

| Domain | Đại diện | Expected | Cases |
|---|---|---|---|
| C-D1 | Fixed/percent hợp lệ | Persist đúng fields | C-API-01/02 |
| C-D2 | Thiếu từng required field; empty code | Reject, không thêm record | C-API-03–09 |
| C-D3 | SAVE10 đã có | Reject, không nhân bản | C-API-10 |
| C-D4 | type=other | Reject | C-API-11 |
| C-D5 | value=-1/0/1 | Reject/reject/accept | C-API-12–14 |
| C-D6 | min=-1/0/1 | Reject/accept/accept | C-API-15–17 |
| C-D7 | maxUses=-1/0/1/2 | Reject/reject/accept/accept | C-API-18–21 |
| C-D8 | Create: none/user/invalid JWT | Deny | C-API-22–24 |
| C-D9 | List: admin/user/none | Allow/deny/deny | C-API-25–27 |
| C-D10 | Delete: admin/user/none | Remove/deny/deny | C-API-28–30 |

## BVA

| Variable | Boundary | Test values | Rationale |
|---|---|---|---|
| discount_value | >0 | −1, 0, 1 | integer fixture nearest neighbors; SRS says positive, not max=100 |
| min_order_amount | ≥0 | −1, 0, 1 | equality is valid |
| max_uses_per_user | ≥1 | 0, 1, 2; extra −1 | first valid count=1; invalid zero must not silently become default 1 |

Độ chính xác tiền cho fixtures hiện là integer VND; không nhận exhaustive real-number coverage. Missing expired_at là required-field test, không phải BVA ngày hết hạn của FR-09. Không tự kết luận coupon quá khứ phải bị cấm tạo nếu spec chỉ yêu cầu field tồn tại.

## Evidence

Cases: [C-FR17-coupon-management.md](../tests/C-FR17-coupon-management.md). Raw: [C-api.md](../evidence/execution/C-api.md). UI thao tác chờ sinh viên. [ISTQB CTFL §4.2.1–4.2.2](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf) là tham chiếu kỹ thuật; lecture chưa có trong workspace.

````

</details>

### Artifact `reports/C-FR17-review.md`

SHA-256: `08abababa0514ff7b7ce6f833ca6d677175c1fd41ac5eef973a8ec5a63959fe0`

<details>
<summary>Full output</summary>

````text
# FR-17 — Technical review and AI gaps

30 API cases = 14 PASS + 16 FAIL. [Raw execution](../evidence/execution/C-api.md). Six Admin UI cases NOT RUN.

## Verified API bug groups

- BUG-C01: seven required-field/empty-code cases accepted and create a record (C-API-03–09). Empty string and omitted field are separate domains even when grouped as missing validation.
- BUG-C03: unknown enum type accepted (C-API-11).
- BUG-C04: zero/negative discount accepted (C-API-12/13).
- BUG-C05: negative minimum accepted (C-API-15).
- BUG-C06: invalid usage limit accepted; zero silently becomes 1, negative persists (C-API-18/19).
- BUG-C07/C08/C09: regular authenticated user can create/list/delete coupons (C-API-23/26/29). Role failure differs by operation and is recorded separately so reproduction and impact are precise.

Duplicate code is rejected by a SQLite UNIQUE error (HTTP 500) and no row is added: C-API-10 PASS for the stated uniqueness requirement. The SRS does not mandate HTTP 409 or a friendly error body, so no BUG-C02 is reported. Missing/invalid JWT are denied on tested admin endpoints; a valid user token still bypasses role control.

## AI gaps and corrections

1. Generic CRUD naming could lead to a fabricated missing-Update defect; scope narrowed to actual SRS create/view/delete.
2. Defaults hide validation errors: max_uses=0 becoming 1 is not rejection of invalid input. Readback verifies the submitted/persisted fields.
3. Validation and role tests keep all other fields valid, avoiding a false conclusion that an invalid token test proves admin-role checks.
4. Duplicate status 500 was not automatically labeled a uniqueness bug; the test observes record count and requirement semantics.

Codex technical review only; student review/signoff pending. No UI screenshots or GitHub publication are claimed.

````

</details>

### Artifact `reports/D-mobile-domain.md`

SHA-256: `0341e8ce8cca309ea4913b2d0a1e4332f57230ec5e985dcf17503226ebaeaffd`

<details>
<summary>Full output</summary>

````text
# D — Mobile productDetail

## Requirement mapping and evidence boundary

[SRS baseline FR-20](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md#fr-20-tính-năng-mobile) mô tả chức năng mobile ở mức tổng quan. Bộ thiết kế này ánh xạ hành vi xem sản phẩm/giỏ hàng sang FR-06 (chi tiết, quantity nguyên dương ≥1, feedback) và FR-07 (gộp cùng sản phẩm), chờ sinh viên đối chiếu lecture/hướng dẫn áp dụng. Đây không phải FR-06 Web được tính như feature Pool A.

API hỗ trợ GET `/api/products/:id` được chạy bằng script; mọi thao tác React Native giữ NOT RUN cho đến khi có evidence thiết bị/emulator. Không dùng source inspection, build thành công hoặc API PASS để nhận Mobile E2E đã chạy.

## Domain Testing — từng bước

1. Tách product-data domain, quantity domain và trạng thái giỏ hàng. Input UI là lựa chọn sản phẩm, chuỗi quantity và số lần bấm; outputs là UI detail, feedback và giỏ hàng thực tế.
2. Fixture chuẩn: sản phẩm 1 iPhone 15 Pro Max, 30000000₫; sản phẩm 2 Samsung Galaxy S24 Ultra, 28000000₫; mỗi case quantity bắt đầu với giỏ trống.
3. Quantity valid là số nguyên dương theo mapping FR-06. Các lớp invalid: rỗng, âm, 0, số lẻ, chữ, mixed text. Keyboard numeric không chứng minh đã validate; nếu không nhập được loại dữ liệu nào trên thiết bị thì ghi cơ chế chặn hoặc BLOCKED với lý do, không giả đã nhập.
4. Kiểm tra hậu điều kiện ở giỏ: nhập 1/2 phải lưu đúng 1/2, thành tiền tương ứng 30000000/60000000. Nhập invalid không được tự chuyển thành một đơn vị rồi báo thành công theo oracle mapping.
5. Tách data contract API và display UI: numeric string price của sản phẩm 2 không tự là bug vì spec không chốt JSON type; cần quan sát định dạng và khả năng hiển thị thực tế.
6. Lặp thêm cùng sản phẩm để kiểm tra gộp một dòng quantity=2 theo mapping FR-07; quan sát feedback ngay sau Add.
7. Default reset khi đổi sản phẩm, very-large quantity và HTTP status cho product không có chưa có oracle đủ cụ thể: ghi OBSERVATION, không tăng số bug.

| Domain | Representative | Cases |
|---|---|---|
| D-D1 | Product tồn tại IDs 1/2 | D-API-01/02, D-UI-09/10 |
| D-D2 | Product không có 999999 | D-API-03 (observation) |
| D-D3 | Empty/−1/0 quantity | D-UI-01–03 |
| D-D4 | Positive integers 1/2 | D-UI-04/05 |
| D-D5 | Fraction 1.5, text abc, mixed 1abc | D-UI-06–08 |
| D-D6 | Add once / twice | D-UI-11/12 |
| D-D7 | Switching products, huge quantity | D-UI-13/14 (observations pending run) |

## BVA

Quantity trên miền số nguyên: minimum=1, OFF=0, ON=1, IN=2; thêm −1 cho invalid interior. Fraction 1.5 nằm ngoài miền integer, là Domain case chứ không phải nearest integer boundary. Không có upper bound/stock constraint trong SRS nên không tự đặt max. Empty input là missing-value domain, không phải số 0.

## Manual execution

Cases: [D-mobile-product-detail.md](../tests/D-mobile-product-detail.md). Hướng dẫn theo từng TC: [manual-handoff.md](../reports/manual-handoff.md). API support: [D-api.md](../evidence/execution/D-api.md). Khi review, sinh viên xác nhận mapping FR-20/06/07 rồi cập nhật kết quả UI thật. Không tạo ảnh minh họa thay screenshot.

````

</details>

### Artifact `reports/D-mobile-review.md`

SHA-256: `39a3b8871ddbf840c80d8ce76977d88dd38bbae1e5aabeb5fee3ce680edb5f2b`

<details>
<summary>Full output</summary>

````text
# Mobile — Technical review and AI gaps

Support API: 2 PASS + 1 OBSERVATION ([raw](../evidence/execution/D-api.md)). All 14 Mobile UI cases NOT RUN. No Mobile UI bugs are reported as verified.

## AI design corrections

- Empty and fractional inputs were initially tagged BVA too broadly. They are domain/type classes. The lower integer boundary uses −1/0/1/2; fractional 1.5 is not the nearest valid integer neighbor.
- FR-20 does not detail every screen. FR-06/07 behavior is explicitly marked as a mapping for student review, rather than silently importing Web-specific DOM requirements into React Native.
- Source `normalizeQuantity` suggests some inputs may be silently coerced. That is only a candidate for D-UI-01/02/03/06/08, not runtime evidence.
- Product API returns an empty object for a missing ID and a string price for an even ID. No mandatory HTTP schema was specified, so D-API-03 is an observation; even-ID string price is not itself a defect without display/runtime evidence.
- Extremely large quantities and default reset rules have no specified upper/default oracle; planned exploratory cases must remain observations unless requirements are clarified.

Human review, actual native-device behavior, screenshots and video remain pending. A Metro bundle/export or source-code inspection does not establish native interaction results.

````

</details>

### Artifact `reports/manual-handoff.md`

SHA-256: `1f9a47c9ca365ef520d7e399721836913b3a22802b9dab9d4b21b4ff809a611b`

<details>
<summary>Full output</summary>

````text
# Manual Handoff — làm sau phần Codex

## 1. Mở môi trường

Runtime là bản copy, dữ liệu thật ở `eshop-sut/` được giữ nguyên. Từ repo bài nộp chạy `node scripts/manual-runtime.cjs` nếu Codex chưa để server chạy. Giữ terminal mở; lệnh khởi động Web 5173, Admin 5174, backend 3000 và Expo 8081. Restart sẽ reset dữ liệu runtime; không restart giữa một case. API suite dùng database/port khác (3100).

Web: http://localhost:5173 ; Admin: http://localhost:5174 . Expo: terminal in ra `exp://<LAN-IP>:8081`; mở bằng development client tương thích Expo SDK54 trên điện thoại/emulator. Dùng cùng mạng với máy chạy backend; nếu IP khác, dừng runtime rồi đặt `$env:HW02_LAN_IP='<IP LAN thực tế>'` và chạy lại. Đây là hướng dẫn từ cấu hình project, không phải xác nhận thiết bị đã chạy.

Tài khoản riêng mỗi case: thay dấu `-` bằng `_`, chuyển lowercase, thêm `@hw02.invalid`; ví dụ A-UI-01 → `a_ui_01@hw02.invalid`. Demo password mọi account fixture: `Test1234!`. C accounts có quyền admin; A/B/D là user. Đây là dữ liệu giả, không phải thông tin cá nhân. Không chụp mật khẩu/token.

Nếu đăng nhập lỗi/Expo không mở, chụp nguyên lỗi, ghi device/OS và BLOCKED. Không đánh FAIL nghiệp vụ khi môi trường chưa vào được.

## 2. Cách chụp và ghi kết quả

- Tên file: `<TC-ID>_run-01_01-input.png`, `_02-response.png`, `_03-persisted.png` hoặc `_03-cart.png`; lần chạy lại dùng run-02. Lưu vào `evidence/screenshots/<A|B|C|D>/`.
- Web giữ URL và vùng form/result liên quan trong khung; Mobile giữ đầy đủ tên sản phẩm/quantity/feedback. Chữ và số phải đọc được; ảnh dài có thể chia phần.
- Ảnh input thấy dữ liệu trước bấm; ảnh response chụp khi alert/error/feedback đang hiện (chụp alert trước khi đóng); ảnh persisted/cart xác minh hậu điều kiện. Chỉ lấy những ảnh được yêu cầu cho case, không dựng ảnh thay evidence.
- Ghi actual, status, timestamp có timezone và đường dẫn ảnh vào `evidence/manual-results.md`. FAIL khi kết quả khác expected có oracle; OBSERVATION khi chưa có rule đủ rõ. Nếu bàn phím/ngăn nhập là cơ chế chặn thật, ghi cơ chế đó và cart không đổi; nếu không kiểm tra được điều kiện, ghi BLOCKED.
- Source đã gợi ý một số lỗi nhưng không xác nhận thay bạn. Expected dưới đây là theo requirements, không phải hướng dẫn phải chụp ra kết quả giống dự đoán.

## 3. Từng test UI

### A-UI-01 — Profile phone 091234567

Tài khoản: `a_ui_01@hw02.invalid` / demo password ở mục 1.

1. Mở Web `/login`, đăng nhập account của case; mở `/profile`.
2. Profile fixture ban đầu: phone=0912345678, name=TC-ID, address=1 Test Street.
3. Điền chính xác Họ Tên=A-UI-01; Số điện thoại=091234567; Địa chỉ=1 Test Street.
4. Chụp input; bấm Cập nhật một lần; chụp alert hoặc lỗi đang hiện.
5. Đóng alert, đăng xuất và đăng nhập lại cùng account (tránh dữ liệu cache); mở Hồ sơ, chụp giá trị đã lưu. Invalid input phải giữ giá trị cũ, valid input phải lưu đúng.

Expected: **Reject; saved profile remains unchanged**

Ảnh: 01-input: phone đầy đủ và form; 02-response: thông báo; 03-persisted: hồ sơ sau đăng nhập lại.

Nơi lưu: `evidence/screenshots/A/A-UI-01_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng A-UI-01 trong manual-results.md.

### A-UI-02 — Profile phone 0912345678

Tài khoản: `a_ui_02@hw02.invalid` / demo password ở mục 1.

1. Mở Web `/login`, đăng nhập account của case; mở `/profile`.
2. Profile fixture ban đầu: phone=0912345678, name=TC-ID, address=1 Test Street.
3. Điền chính xác Họ Tên=A-UI-02; Số điện thoại=0912345678; Địa chỉ=1 Test Street.
4. Chụp input; bấm Cập nhật một lần; chụp alert hoặc lỗi đang hiện.
5. Đóng alert, đăng xuất và đăng nhập lại cùng account (tránh dữ liệu cache); mở Hồ sơ, chụp giá trị đã lưu. Invalid input phải giữ giá trị cũ, valid input phải lưu đúng.

Expected: **Update succeeds; re-login shows the exact phone**

Ảnh: 01-input: phone đầy đủ và form; 02-response: thông báo; 03-persisted: hồ sơ sau đăng nhập lại.

Nơi lưu: `evidence/screenshots/A/A-UI-02_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng A-UI-02 trong manual-results.md.

### A-UI-03 — Profile phone 09123456789

Tài khoản: `a_ui_03@hw02.invalid` / demo password ở mục 1.

1. Mở Web `/login`, đăng nhập account của case; mở `/profile`.
2. Profile fixture ban đầu: phone=0912345678, name=TC-ID, address=1 Test Street.
3. Điền chính xác Họ Tên=A-UI-03; Số điện thoại=09123456789; Địa chỉ=1 Test Street.
4. Chụp input; bấm Cập nhật một lần; chụp alert hoặc lỗi đang hiện.
5. Đóng alert, đăng xuất và đăng nhập lại cùng account (tránh dữ liệu cache); mở Hồ sơ, chụp giá trị đã lưu. Invalid input phải giữ giá trị cũ, valid input phải lưu đúng.

Expected: **Update succeeds; re-login shows the exact phone**

Ảnh: 01-input: phone đầy đủ và form; 02-response: thông báo; 03-persisted: hồ sơ sau đăng nhập lại.

Nơi lưu: `evidence/screenshots/A/A-UI-03_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng A-UI-03 trong manual-results.md.

### A-UI-04 — Profile phone 091234567890

Tài khoản: `a_ui_04@hw02.invalid` / demo password ở mục 1.

1. Mở Web `/login`, đăng nhập account của case; mở `/profile`.
2. Profile fixture ban đầu: phone=0912345678, name=TC-ID, address=1 Test Street.
3. Điền chính xác Họ Tên=A-UI-04; Số điện thoại=091234567890; Địa chỉ=1 Test Street.
4. Chụp input; bấm Cập nhật một lần; chụp alert hoặc lỗi đang hiện.
5. Đóng alert, đăng xuất và đăng nhập lại cùng account (tránh dữ liệu cache); mở Hồ sơ, chụp giá trị đã lưu. Invalid input phải giữ giá trị cũ, valid input phải lưu đúng.

Expected: **Reject; saved profile remains unchanged**

Ảnh: 01-input: phone đầy đủ và form; 02-response: thông báo; 03-persisted: hồ sơ sau đăng nhập lại.

Nơi lưu: `evidence/screenshots/A/A-UI-04_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng A-UI-04 trong manual-results.md.

### A-UI-05 — Profile phone 1912345678

Tài khoản: `a_ui_05@hw02.invalid` / demo password ở mục 1.

1. Mở Web `/login`, đăng nhập account của case; mở `/profile`.
2. Profile fixture ban đầu: phone=0912345678, name=TC-ID, address=1 Test Street.
3. Điền chính xác Họ Tên=A-UI-05; Số điện thoại=1912345678; Địa chỉ=1 Test Street.
4. Chụp input; bấm Cập nhật một lần; chụp alert hoặc lỗi đang hiện.
5. Đóng alert, đăng xuất và đăng nhập lại cùng account (tránh dữ liệu cache); mở Hồ sơ, chụp giá trị đã lưu. Invalid input phải giữ giá trị cũ, valid input phải lưu đúng.

Expected: **Reject; saved profile remains unchanged**

Ảnh: 01-input: phone đầy đủ và form; 02-response: thông báo; 03-persisted: hồ sơ sau đăng nhập lại.

Nơi lưu: `evidence/screenshots/A/A-UI-05_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng A-UI-05 trong manual-results.md.

### A-UI-06 — Email field cannot be changed

Tài khoản: `a_ui_06@hw02.invalid` / demo password ở mục 1.

1. Mở Web `/login`, đăng nhập account của case; mở `/profile`.
2. Profile fixture ban đầu: phone=0912345678, name=TC-ID, address=1 Test Street.
3. Chụp form thấy trường Email. Thử focus/gõ địa chỉ other@example.invalid bằng thao tác UI bình thường; không sửa DOM/DevTools.
4. Nếu UI không cho sửa, ghi rõ disabled/read-only; đăng xuất/đăng nhập lại kiểm tra email ban đầu còn nguyên.

Expected: **Email is not editable via UI; original email unchanged**

Ảnh: 01-input: Email và URL; 02-response: trạng thái field khi thử nhập hoặc sau login. Không coi field chỉ nhìn giống readonly là đã thử.

Nơi lưu: `evidence/screenshots/A/A-UI-06_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng A-UI-06 trong manual-results.md.

### A-UI-07 — Unicode editable profile fields

Tài khoản: `a_ui_07@hw02.invalid` / demo password ở mục 1.

1. Mở Web `/login`, đăng nhập account của case; mở `/profile`.
2. Profile fixture ban đầu: phone=0912345678, name=TC-ID, address=1 Test Street.
3. Điền chính xác Họ Tên=Người Dùng HW02; Số điện thoại=0912345678; Địa chỉ=Đường Thử Nghiệm.
4. Chụp input; bấm Cập nhật một lần; chụp alert hoặc lỗi đang hiện.
5. Đóng alert, đăng xuất và đăng nhập lại cùng account (tránh dữ liệu cache); mở Hồ sơ, chụp giá trị đã lưu. Invalid input phải giữ giá trị cũ, valid input phải lưu đúng.

Expected: **Valid update accepted; name/address persist after fresh login**

Ảnh: 01-input: phone đầy đủ và form; 02-response: thông báo; 03-persisted: hồ sơ sau đăng nhập lại.

Nơi lưu: `evidence/screenshots/A/A-UI-07_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng A-UI-07 trong manual-results.md.

### B-UI-01 — Checkout BIGBUY / 499999

Tài khoản: `b_ui_01@hw02.invalid` / demo password ở mục 1.

1. Reload Web để giỏ trong memory về rỗng; đăng xuất/login đúng account case.
2. Mở `/product/101` (HW02 Total 499999), quantity=1, bấm Thêm vào giỏ hàng. Mở Giỏ hàng kiểm tra đúng một dòng và tổng 499999. Nếu click đầu không thêm, ghi setup observation rồi click lần hai để dựng giỏ; không gọi đó là kết quả FR-09.
3. Từ giỏ mở Thanh toán bằng điều hướng trong app; không reload vì cart nằm trong memory.
4. Nhập Mã Giảm Giá=BIGBUY; chụp tổng tiền gốc và mã; bấm Áp dụng một lần.
5. Chụp thông báo và tiền tiết kiệm/thành tiền/tổng thanh toán thực tế; không chỉnh total_amount để tạo kết quả.

Expected: **Reject below minimum**

Ảnh: 01-input: code và tổng gốc; 02-response: error hoặc đủ discount/final; thêm 03-total chỉ khi tổng thanh toán ngoài khung.

Nơi lưu: `evidence/screenshots/B/B-UI-01_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng B-UI-01 trong manual-results.md.

### B-UI-02 — Checkout BIGBUY / 500000

Tài khoản: `b_ui_02@hw02.invalid` / demo password ở mục 1.

1. Reload Web để giỏ trong memory về rỗng; đăng xuất/login đúng account case.
2. Mở `/product/102` (HW02 Total 500000), quantity=1, bấm Thêm vào giỏ hàng. Mở Giỏ hàng kiểm tra đúng một dòng và tổng 500000. Nếu click đầu không thêm, ghi setup observation rồi click lần hai để dựng giỏ; không gọi đó là kết quả FR-09.
3. Từ giỏ mở Thanh toán bằng điều hướng trong app; không reload vì cart nằm trong memory.
4. Nhập Mã Giảm Giá=BIGBUY; chụp tổng tiền gốc và mã; bấm Áp dụng một lần.
5. Chụp thông báo và tiền tiết kiệm/thành tiền/tổng thanh toán thực tế; không chỉnh total_amount để tạo kết quả.

Expected: **Discount 50000; final 450000**

Ảnh: 01-input: code và tổng gốc; 02-response: error hoặc đủ discount/final; thêm 03-total chỉ khi tổng thanh toán ngoài khung.

Nơi lưu: `evidence/screenshots/B/B-UI-02_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng B-UI-02 trong manual-results.md.

### B-UI-03 — Checkout BIGBUY / 500001

Tài khoản: `b_ui_03@hw02.invalid` / demo password ở mục 1.

1. Reload Web để giỏ trong memory về rỗng; đăng xuất/login đúng account case.
2. Mở `/product/103` (HW02 Total 500001), quantity=1, bấm Thêm vào giỏ hàng. Mở Giỏ hàng kiểm tra đúng một dòng và tổng 500001. Nếu click đầu không thêm, ghi setup observation rồi click lần hai để dựng giỏ; không gọi đó là kết quả FR-09.
3. Từ giỏ mở Thanh toán bằng điều hướng trong app; không reload vì cart nằm trong memory.
4. Nhập Mã Giảm Giá=BIGBUY; chụp tổng tiền gốc và mã; bấm Áp dụng một lần.
5. Chụp thông báo và tiền tiết kiệm/thành tiền/tổng thanh toán thực tế; không chỉnh total_amount để tạo kết quả.

Expected: **Discount 50000; final 450001**

Ảnh: 01-input: code và tổng gốc; 02-response: error hoặc đủ discount/final; thêm 03-total chỉ khi tổng thanh toán ngoài khung.

Nơi lưu: `evidence/screenshots/B/B-UI-03_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng B-UI-03 trong manual-results.md.

### B-UI-04 — Checkout SAVE10 / 400000

Tài khoản: `b_ui_04@hw02.invalid` / demo password ở mục 1.

1. Reload Web để giỏ trong memory về rỗng; đăng xuất/login đúng account case.
2. Mở `/product/104` (HW02 Total 400000), quantity=1, bấm Thêm vào giỏ hàng. Mở Giỏ hàng kiểm tra đúng một dòng và tổng 400000. Nếu click đầu không thêm, ghi setup observation rồi click lần hai để dựng giỏ; không gọi đó là kết quả FR-09.
3. Từ giỏ mở Thanh toán bằng điều hướng trong app; không reload vì cart nằm trong memory.
4. Nhập Mã Giảm Giá=SAVE10; chụp tổng tiền gốc và mã; bấm Áp dụng một lần.
5. Chụp thông báo và tiền tiết kiệm/thành tiền/tổng thanh toán thực tế; không chỉnh total_amount để tạo kết quả.

Expected: **Discount 40000; final 360000**

Ảnh: 01-input: code và tổng gốc; 02-response: error hoặc đủ discount/final; thêm 03-total chỉ khi tổng thanh toán ngoài khung.

Nơi lưu: `evidence/screenshots/B/B-UI-04_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng B-UI-04 trong manual-results.md.

### B-UI-05 — Checkout EXPIRED / 400000

Tài khoản: `b_ui_05@hw02.invalid` / demo password ở mục 1.

1. Reload Web để giỏ trong memory về rỗng; đăng xuất/login đúng account case.
2. Mở `/product/104` (HW02 Total 400000), quantity=1, bấm Thêm vào giỏ hàng. Mở Giỏ hàng kiểm tra đúng một dòng và tổng 400000. Nếu click đầu không thêm, ghi setup observation rồi click lần hai để dựng giỏ; không gọi đó là kết quả FR-09.
3. Từ giỏ mở Thanh toán bằng điều hướng trong app; không reload vì cart nằm trong memory.
4. Nhập Mã Giảm Giá=EXPIRED; chụp tổng tiền gốc và mã; bấm Áp dụng một lần.
5. Chụp thông báo và tiền tiết kiệm/thành tiền/tổng thanh toán thực tế; không chỉnh total_amount để tạo kết quả.

Expected: **Reject expired coupon**

Ảnh: 01-input: code và tổng gốc; 02-response: error hoặc đủ discount/final; thêm 03-total chỉ khi tổng thanh toán ngoài khung.

Nơi lưu: `evidence/screenshots/B/B-UI-05_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng B-UI-05 trong manual-results.md.

### B-UI-06 — Checkout VIP100 / 400000

Tài khoản: `b_ui_06@hw02.invalid` / demo password ở mục 1.

1. Reload Web để giỏ trong memory về rỗng; đăng xuất/login đúng account case.
2. Account này được fixture ghi sẵn đúng 2 lần dùng VIP100 (limit=2); không cần checkout hai lần nữa. Chỉ thử apply sau khi dựng giỏ.
3. Mở `/product/104` (HW02 Total 400000), quantity=1, bấm Thêm vào giỏ hàng. Mở Giỏ hàng kiểm tra đúng một dòng và tổng 400000. Nếu click đầu không thêm, ghi setup observation rồi click lần hai để dựng giỏ; không gọi đó là kết quả FR-09.
4. Từ giỏ mở Thanh toán bằng điều hướng trong app; không reload vì cart nằm trong memory.
5. Nhập Mã Giảm Giá=VIP100; chụp tổng tiền gốc và mã; bấm Áp dụng một lần.
6. Chụp thông báo và tiền tiết kiệm/thành tiền/tổng thanh toán thực tế; không chỉnh total_amount để tạo kết quả.

Expected: **After exactly 2 completed uses, third attempt rejected**

Ảnh: 01-input: code và tổng gốc; 02-response: error hoặc đủ discount/final; thêm 03-total chỉ khi tổng thanh toán ngoài khung.

Nơi lưu: `evidence/screenshots/B/B-UI-06_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng B-UI-06 trong manual-results.md.

### C-UI-01 — Admin coupon form 1

Tài khoản: `c_ui_01@hw02.invalid` / demo password ở mục 1.

1. Mở Admin, đăng nhập account case; chọn Mã Giảm Giá.
2. Điền form: {"code": "HW02_C_UI_01", "type": "fixed", "discount_value": 0, "min_order_amount": 0, "expired_at": "2099-12-31", "max_uses_per_user": 1}. Chọn Số tiền cố định (fixed); ngày là 31/12/2099 dù locale hiển thị khác ISO.
3. Chụp toàn bộ field trước submit; bấm Tạo mã; chụp lỗi/thành công; nếu cần, chụp validation tooltip khi trình duyệt chặn.
4. Reload Admin, mở lại Mã Giảm Giá; tìm đúng code và chụp dòng nếu được tạo. Invalid case phải không thêm dòng mới; duplicate SAVE10 phải giữ nguyên coupon cũ.

Expected: **Reject discount_value=0**

Ảnh: 01-input: 6 trường rõ giá trị; 02-response: phản hồi hoặc tooltip; 03-persisted: bảng sau reload. Case delete thêm 04-before-delete/05-after-delete.

Nơi lưu: `evidence/screenshots/C/C-UI-01_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng C-UI-01 trong manual-results.md.

### C-UI-02 — Admin coupon form 2

Tài khoản: `c_ui_02@hw02.invalid` / demo password ở mục 1.

1. Mở Admin, đăng nhập account case; chọn Mã Giảm Giá.
2. Điền form: {"code": "HW02_C_UI_02", "type": "fixed", "discount_value": 1, "min_order_amount": 0, "expired_at": "2099-12-31", "max_uses_per_user": 1}. Chọn Số tiền cố định (fixed); ngày là 31/12/2099 dù locale hiển thị khác ISO.
3. Chụp toàn bộ field trước submit; bấm Tạo mã; chụp lỗi/thành công; nếu cần, chụp validation tooltip khi trình duyệt chặn.
4. Reload Admin, mở lại Mã Giảm Giá; tìm đúng code và chụp dòng nếu được tạo. Invalid case phải không thêm dòng mới; duplicate SAVE10 phải giữ nguyên coupon cũ.

Expected: **Create coupon; same values visible after reload**

Ảnh: 01-input: 6 trường rõ giá trị; 02-response: phản hồi hoặc tooltip; 03-persisted: bảng sau reload. Case delete thêm 04-before-delete/05-after-delete.

Nơi lưu: `evidence/screenshots/C/C-UI-02_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng C-UI-02 trong manual-results.md.

### C-UI-03 — Admin coupon form 3

Tài khoản: `c_ui_03@hw02.invalid` / demo password ở mục 1.

1. Mở Admin, đăng nhập account case; chọn Mã Giảm Giá.
2. Điền form: {"code": "HW02_C_UI_03", "type": "fixed", "discount_value": 1, "min_order_amount": -1, "expired_at": "2099-12-31", "max_uses_per_user": 1}. Chọn Số tiền cố định (fixed); ngày là 31/12/2099 dù locale hiển thị khác ISO.
3. Chụp toàn bộ field trước submit; bấm Tạo mã; chụp lỗi/thành công; nếu cần, chụp validation tooltip khi trình duyệt chặn.
4. Reload Admin, mở lại Mã Giảm Giá; tìm đúng code và chụp dòng nếu được tạo. Invalid case phải không thêm dòng mới; duplicate SAVE10 phải giữ nguyên coupon cũ.

Expected: **Reject negative minimum**

Ảnh: 01-input: 6 trường rõ giá trị; 02-response: phản hồi hoặc tooltip; 03-persisted: bảng sau reload. Case delete thêm 04-before-delete/05-after-delete.

Nơi lưu: `evidence/screenshots/C/C-UI-03_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng C-UI-03 trong manual-results.md.

### C-UI-04 — Admin coupon form 4

Tài khoản: `c_ui_04@hw02.invalid` / demo password ở mục 1.

1. Mở Admin, đăng nhập account case; chọn Mã Giảm Giá.
2. Điền form: {"code": "HW02_C_UI_04", "type": "fixed", "discount_value": 1, "min_order_amount": 0, "expired_at": "2099-12-31", "max_uses_per_user": 0}. Chọn Số tiền cố định (fixed); ngày là 31/12/2099 dù locale hiển thị khác ISO.
3. Chụp toàn bộ field trước submit; bấm Tạo mã; chụp lỗi/thành công; nếu cần, chụp validation tooltip khi trình duyệt chặn.
4. Reload Admin, mở lại Mã Giảm Giá; tìm đúng code và chụp dòng nếu được tạo. Invalid case phải không thêm dòng mới; duplicate SAVE10 phải giữ nguyên coupon cũ.

Expected: **Reject zero usage limit**

Ảnh: 01-input: 6 trường rõ giá trị; 02-response: phản hồi hoặc tooltip; 03-persisted: bảng sau reload. Case delete thêm 04-before-delete/05-after-delete.

Nơi lưu: `evidence/screenshots/C/C-UI-04_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng C-UI-04 trong manual-results.md.

### C-UI-05 — Admin coupon form 5

Tài khoản: `c_ui_05@hw02.invalid` / demo password ở mục 1.

1. Mở Admin, đăng nhập account case; chọn Mã Giảm Giá.
2. Điền form: {"code": "SAVE10", "type": "fixed", "discount_value": 1, "min_order_amount": 0, "expired_at": "2099-12-31", "max_uses_per_user": 1}. Chọn Số tiền cố định (fixed); ngày là 31/12/2099 dù locale hiển thị khác ISO.
3. Chụp toàn bộ field trước submit; bấm Tạo mã; chụp lỗi/thành công; nếu cần, chụp validation tooltip khi trình duyệt chặn.
4. Reload Admin, mở lại Mã Giảm Giá; tìm đúng code và chụp dòng nếu được tạo. Invalid case phải không thêm dòng mới; duplicate SAVE10 phải giữ nguyên coupon cũ.

Expected: **Reject duplicate; original SAVE10 unchanged**

Ảnh: 01-input: 6 trường rõ giá trị; 02-response: phản hồi hoặc tooltip; 03-persisted: bảng sau reload. Case delete thêm 04-before-delete/05-after-delete.

Nơi lưu: `evidence/screenshots/C/C-UI-05_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng C-UI-05 trong manual-results.md.

### C-UI-06 — Admin delete lifecycle

Tài khoản: `c_ui_06@hw02.invalid` / demo password ở mục 1.

1. Mở Admin, đăng nhập account case; chọn Mã Giảm Giá.
2. Điền form: {"code": "HW02_DELETE_UI", "type": "fixed", "discount_value": 1, "min_order_amount": 0, "expired_at": "2099-12-31", "max_uses_per_user": 1}. Chọn Số tiền cố định (fixed); ngày là 31/12/2099 dù locale hiển thị khác ISO.
3. Chụp toàn bộ field trước submit; bấm Tạo mã; chụp lỗi/thành công; nếu cần, chụp validation tooltip khi trình duyệt chặn.
4. Reload Admin, mở lại Mã Giảm Giá; tìm đúng code và chụp dòng nếu được tạo. Invalid case phải không thêm dòng mới; duplicate SAVE10 phải giữ nguyên coupon cũ.
5. Chụp dòng HW02_DELETE_UI trước xóa; bấm Xóa đúng dòng, xử lý dialog nếu thực tế có; chụp sau reload không còn code đó và SAVE10 còn nguyên. Không xóa coupon khác.

Expected: **Create test coupon, delete it; disappears after reload; SAVE10 unchanged**

Ảnh: 01-input: 6 trường rõ giá trị; 02-response: phản hồi hoặc tooltip; 03-persisted: bảng sau reload. Case delete thêm 04-before-delete/05-after-delete.

Nơi lưu: `evidence/screenshots/C/C-UI-06_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng C-UI-06 trong manual-results.md.

### D-UI-01 — Mobile quantity ""

Tài khoản: `d_ui_01@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi ``; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Reject empty quantity; no new cart item**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-01_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-01 trong manual-results.md.

### D-UI-02 — Mobile quantity "-1"

Tài khoản: `d_ui_02@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `-1`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Reject negative; cart unchanged**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-02_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-02 trong manual-results.md.

### D-UI-03 — Mobile quantity "0"

Tài khoản: `d_ui_03@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `0`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Reject zero; cart unchanged**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-03_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-03 trong manual-results.md.

### D-UI-04 — Mobile quantity "1"

Tài khoản: `d_ui_04@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `1`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Cart contains quantity=1, total=30000000**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-04_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-04 trong manual-results.md.

### D-UI-05 — Mobile quantity "2"

Tài khoản: `d_ui_05@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `2`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Cart contains quantity=2, total=60000000**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-05_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-05 trong manual-results.md.

### D-UI-06 — Mobile quantity "1.5"

Tài khoản: `d_ui_06@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `1.5`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Reject fractional; cart unchanged**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-06_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-06 trong manual-results.md.

### D-UI-07 — Mobile quantity "abc"

Tài khoản: `d_ui_07@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `abc`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Reject nonnumeric; cart unchanged**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-07_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-07 trong manual-results.md.

### D-UI-08 — Mobile quantity "1abc"

Tài khoản: `d_ui_08@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `1abc`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Reject mixed text; cart unchanged**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-08_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-08 trong manual-results.md.

### D-UI-09 — Mobile complete product detail

Tài khoản: `d_ui_09@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Chụp đủ ảnh/tên/giá/mô tả/danh mục; cuộn nếu cần. Đối chiếu iPhone 15 Pro Max, 30000000₫, mô tả Điện thoại cao cấp của Apple, danh mục Điện thoại. Thiếu trường ghi actual, chưa suy từ source.

Expected: **Image/name/price/description/category visible and correct; mapped FR-06**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-09_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-09 trong manual-results.md.

### D-UI-10 — Mobile even-id price display

Tài khoản: `d_ui_10@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 2 (iPhone ID1; Samsung ID2).
3. Đối chiếu Samsung Galaxy S24 Ultra, 28000000₫, mô tả Màn hình hiển thị xuất sắc, camera siêu zoom; chụp giá và tên, ghi nếu crash/NaN.

Expected: **Samsung price displayed as 28,000,000 ₫ using locale separator; no crash**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-10_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-10 trong manual-results.md.

### D-UI-11 — Mobile add feedback

Tài khoản: `d_ui_11@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `1`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Visible feedback after Add; cart quantity 1**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-11_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-11 trong manual-results.md.

### D-UI-12 — Same product twice

Tài khoản: `d_ui_12@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `1`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **One cart line quantity=2; total=60000000**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-12_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-12 trong manual-results.md.

### D-UI-13 — Detail quantity resets after switching products

Tài khoản: `d_ui_13@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `2`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Record selected quantity for product 2; SRS does not specify default reset policy**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-13_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-13 trong manual-results.md.

### D-UI-14 — Very large quantity exploratory input

Tài khoản: `d_ui_14@hw02.invalid` / demo password ở mục 1.

1. Mở app Mobile trong Expo/emulator; đăng nhập account case nếu cần. Reload app trước mỗi case để giỏ memory về rỗng; không reload giữa các bước trong case.
2. Từ trang chủ bấm sản phẩm ID 1 (iPhone ID1; Samsung ID2).
3. Xóa nội dung ô Số lượng, nhập/dán đúng chuỗi `9007199254740992`; chuỗi rỗng nghĩa là xóa hết và không gõ gì. Nếu hệ điều hành ngăn loại input, chụp cơ chế và ghi actual rõ.
4. Chụp quantity trước Add; bấm Thêm vào giỏ hàng một lần; chụp alert/feedback trước khi đóng; mở Giỏ Hàng và chụp số dòng/quantity/thành tiền thực tế.

Expected: **Record behavior/precision; upper limit unspecified, do not declare violation solely from size**

Ảnh: 01-input/detail: product và quantity hoặc data fields; 02-response: feedback nếu đang kiểm tra Add; 03-cart: quantity và total. Các observation giữ rõ điều chưa có oracle.

Nơi lưu: `evidence/screenshots/D/D-UI-14_run-01_*.png`. Ghi actual/status/timestamp vào đúng dòng D-UI-14 trong manual-results.md.

## 4. Screenshots cho bugs API đã xác minh

Các bug API không nhất thiết có field tương ứng trong UI (ví dụ role tampering). Dùng ảnh terminal của bản ghi HTTP thật, không dựng form UI để giả chứng minh. Chạy `node scripts/show-bug.cjs <BUG-ID>` để hiển thị record đã chạy, có TC-ID/timestamp/request/response/expected; lệnh này hiển thị record, không giả là request mới.

Mỗi bug ở bugs/bug-reports.md: chụp cửa sổ terminal đủ Bug-ID, TC-ID, timestamp, endpoint, input quan trọng, HTTP status, actual readback và expected. Nếu dài, lấy 01-request và 02-response có cùng Bug-ID. Lưu `evidence/screenshots/api/<BUG-ID>_record-01.png` và `...record-02.png` nếu cần. Caption: “Screenshot of recorded API execution”, không gọi là Web/Mobile UI screenshot. Raw Markdown đi kèm để đối chiếu. Nếu giảng viên yêu cầu thêm ảnh UI cho một bug, chỉ bổ sung khi tái hiện được qua UI thật.

## 5. Review cá nhân và video

Review các bảng Domain/BVA, đặc biệt mapping Mobile FR-20/06/07 và lecture chưa có trong workspace. Đọc AI Audit, sửa/đánh giá đầu ra thật, điền họ tên/lớp và xác nhận cá nhân; AI Critique là draft chưa được sinh viên xác nhận. Điền self-assessment theo evidence. Quay demo theo evidence/video-links.md sau phần test.

## 6. Phần nhóm — làm cuối

Sau test/evidence/review cá nhân, chọn repo Issues nhóm. Mỗi bug Markdown đã có title, steps, expected/actual và raw evidence; có thể dùng làm issue body. Tìm Bug-ID trước để tránh trùng. Đăng/cập nhật đúng repo nhóm, đính kèm ảnh thật ở mục 4 hoặc ảnh UI phù hợp. Mở permalink Issue sau khi submit, kiểm tra ảnh hiển thị. Chụp `<BUG-ID>_issue-header.png` thấy repo/number/title/URL và `<BUG-ID>_issue-body-01.png` thấy steps/actual/screenshots. Lưu vào evidence/github-issues/. Gửi mapping Bug-ID → URL/number → ảnh để cập nhật báo cáo; chưa có URL thì ghi pending.

## 7. Định dạng cuối

Sinh viên tự xuất Markdown sang PDF theo đề/policies, tự đóng ZIP và nộp Moodle. Tên `<StudentID>_HW02_AI_DomainTesting_<SelfAssessedGrade>.zip`, điểm 000–100. Chỉ nộp deliverables, evidence, scripts/skills đã dùng và Git log; TASKS/references/runtime/.git/dependencies ở ngoài. Biên nhận Moodle phát sinh sau nộp lưu ngoài repo, không sửa ZIP chỉ để thêm ảnh đó.

````

</details>

### Artifact `reports/skill-demonstration.md`

SHA-256: `3af66d61e3d59c5d98471ed5dcecade4aa557c3a56f483c705d80c2015acbde5`

<details>
<summary>Full output</summary>

````text
# Agent Skill — FR-17 technical demonstration

## Scope of evidence

Skill: [domain-bva-testing](../.agents/skills/domain-bva-testing/SKILL.md). Codex read and applied this procedure to the existing FR-17 artifact pack in this session, then reran `node scripts/run-api.cjs C`. This is a technical workflow demonstration by the current agent, not a fresh independent model invocation, benchmark or completed video.

## Inputs

- Feature: FR-17 Coupon management; public API create/list/delete.
- Oracle: SRS required/unique/enum/positive/nonnegative/minimum constraints and FR-12 admin role, at SHA85af3ba875c88283615e22cb108f13e2fccaf0e9.
- Fixtures: admin/user/other accounts, valid nominal fields, per-case reset; isolated database and frozen time.
- UI and student video explicitly pending; missing Update is not an assumed defect.

## Procedure and outputs

| Skill step | Applied output / check |
|---|---|
| Oracle | reports/C-FR17-domain.md identifies FR-17 and FR-12; avoids unspecified HTTP409/max-percent/Update rules |
| Domains | Presence, unique code, enum, numeric and identity classes with representative cases |
| Boundaries | value−1/0/1, min−1/0/1, usage0/1/2, valid lower-corner vector |
| Cases | C-API-01–30 plus C-UI-01–06, exact inputs and independent expected results |
| Review | Readback required; duplicate500 not automatically a unique violation; unique UI codes avoid interference |
| Execute | 30 API cases rerun, 14 PASS/16 FAIL; original source/database unchanged |
| Bugs | Eight C groups from actual failures; screenshots/Issues not claimed |
| Audit | Technical corrections in C review and AI-02; student verdict pending |

## Result and remaining demo

[Raw rerun evidence](../evidence/execution/C-api.md) is timestamped by the runner. API scope is reproducible with the supplied scripts. [Video script](../evidence/video-links.md) asks the student to show the real workflow and UI execution, with their own review and explanation. No YouTube URL exists yet; the rubric's10-point skill component has not been self-awarded.

````

</details>

### Artifact `reports/technical-review.md`

SHA-256: `46daa291d1535a44edfcd16b9e5782685b691a4abf32fda194a18a8fdf071b18`

<details>
<summary>Full output</summary>

````text
# Technical Review — Standards and Spec

## Review scope

Baseline homework repository: `5b6516e254b4b90e455003023c1e0551beda48fb`; SUT baseline: `85af3ba875c88283615e22cb108f13e2fccaf0e9`. Reviewed the implementation commits plus remaining new files for this task against the supplied assignment/policies and user's latest instructions.

This is the same Codex agent's self-review using the two axes in mattpocock-skills:code-review. No subagents/independent review or Computer Use were used, in accordance with the user's instruction. Student human review is separate and pending.

## Standards

- Runtime copy instead of original backend: database initialization drops tables, so original source/database hashes are checked before/after execution.
- Corrected shared-runtime risk: API and manual servers now use distinct database directories. Verified API reruns do not reset the manual fixtures.
- Corrected child shutdown waiting: only wait for a process still running, avoiding waiting for an already-delivered close event.
- Corrected UI fixture interference: separate code per create case; separate user account per manual TC. Cases resetting usage/state do not pollute neighboring API cases.
- Adopted actual workspace moves to root REPORT.md and .agents/skills, then repaired links rather than recreate duplicates.
- Raw HTTP evidence omits password/token fields. Scripts use parameterized SQL to arrange fixtures; assertions observe public HTTP interfaces.
- Syntax/Markdown/case-count/template checks are automated. No unresolved code blocker was identified in this self-review; this is not a claim of exhaustive security validation of the harness.

## Spec

- Four assigned features each have Domain/BVA design; API executions remain distinct from Web/Admin/Mobile cases and observations.
- Observations used for unspecified Unicode encoding, invalid-product HTTP schema, quantity defaults/upper bounds. No fabricated Update requirement or stock cap.
- AI-02/03/04/05 keep exact template filenames inside ai-audit; no interactions directory. Prompt/output messages and artifact snapshots are embedded in AI-02.
- All authored documents are Markdown; final PDF/export/ZIP is assigned to the student per explicit instruction.
- Critique is a single245-word paragraph and marked AI draft pending student review; signatures and self-assessed grade remain unfilled.
- 33 manual tasks specify actual data/accounts/steps/expected/screenshot names and storage. Group Issues work stays at the end; feature allocation is accepted as already confirmed.
- 15 API bug groups have request/response/readback evidence and draft-ready Markdown bodies. Screenshots, Issue URLs, native UI execution and video are intentionally pending, not falsely marked delivered.

## Remaining completion gates

Manual UI/Mobile, real screenshot evidence, student human review/signoff, demo video, group Issue publication and student final formatting/submission. See manual-handoff.md and the external TASKS.md. These are the agreed manual phase, not completed by this self-review.

````

</details>

### Artifact `reports/test-environment.md`

SHA-256: `c389bc2d54127b8672590d3922807b53a8294241c0f2a0ce6058f7685d678611`

<details>
<summary>Full output</summary>

````text
# Test Environment

- Ngày thực hiện: 2026-10-19 (Asia/Saigon). Raw timestamps ghi UTC; cộng 07:00 khi đọc theo giờ Việt Nam.
- Host: Windows; Node v24.16.0, npm 12.0.2, Python 3.14.5.
- Original SUT Git SHA: `85af3ba875c88283615e22cb108f13e2fccaf0e9`.
- Original SUT đã có database.sqlite modified và .gitignore untracked trước lượt này. Không reset/stage/commit chúng.
- Dependencies đã có sẵn trong bốn component; không nhận đã thực hiện fresh npm ci. [Build log](../evidence/execution/build-checks.md) ghi compiler outcomes thực tế.
- API suite: `node scripts/run-api.cjs A` (hoặc B/C/D), copied backend, port3100, dedicated runtime database. API assertions qua HTTP; SQL chỉ dựng fixture.
- Backend gốc tự DROP/seed mỗi lần require database.js; adapter copy byte-identical server/database, redirect listen port và optionally freeze Date; không sửa logic route/validation/formula.
- SUT clock API: 2026-10-19T08:00:00.000Z để test expiry ±1ms. Runner timestamps là real clock.
- Manual runtime: `node scripts/manual-runtime.cjs`; copied frontend/backend dưới hw02/.hw02-runtime/manual, Web5173/Admin5174/backend3000/Expo8081, real clock. Chỉ thay Mobile API_URL trong bản copy theo IP LAN thực tế; node_modules junction dùng dependencies có sẵn. Không thay implementation validation.
- APIs và manual runtime dùng hai database khác nhau; rerun API không reset dữ liệu manual.
- Source SHA-256 và original database trước/sau mỗi API run ở evidence/execution/*-api.md. Raw logs lược password/token/reset_token để không lưu credential thật; test fixture inputs vẫn hiện.
- Manual devices/OS/browser: Windows 11 (Web/Admin — Chrome); Android (Expo Go trên Samsung). UI screenshots chụp thực tế từ SUT, lưu tại evidence/screenshots/.

## Commands

```powershell
node scripts/run-api.cjs A
node scripts/run-api.cjs B
node scripts/run-api.cjs C
node scripts/run-api.cjs D
node scripts/summarize.cjs
node scripts/manual-runtime.cjs
```

Chạy build checks sau `node scripts/manual-runtime.cjs --prepare`: `node scripts/check-builds.cjs`. Nếu port có owner khác, script dừng để xử lý thông tin; không tự tắt process không thuộc bài này.

## Limitations

Lecture Domain/BVA chưa có trong workspace. FR-17 Update, Mobile mapping, currency rounding, quantity upper bound và invalid-product HTTP schema có khoảng trống requirements. Danh sách testcase không chứng minh full path/security coverage.

````

</details>

### Artifact `reports/test-summary.md`

SHA-256: `be8aada684ed84162dda556dd24154dbe5f22b7ad12c91d36d105feeeefa8c87`

<details>
<summary>Full output</summary>

````text
# Test Summary

| Scope | Designed | Executed | PASS | FAIL | OBSERVATION | BLOCKED | NOT RUN |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 29 | 22 | 7 | 14 | 1 | 0 | 7 |
| B | 32 | 26 | 14 | 12 | 0 | 0 | 6 |
| C | 36 | 30 | 14 | 16 | 0 | 0 | 6 |
| D | 17 | 3 | 2 | 0 | 1 | 0 | 14 |
| API | 81 | 81 | 37 | 42 | 2 | 0 | 0 |
| UI | 33 | 0 | 0 | 0 | 0 | 0 | 33 |
| Total | 114 | 81 | 37 | 42 | 2 | 0 | 33 |

API verified bug groups: 15. Mobile UI execution is pending; product API support is counted separately. Observations have no definitive requirement oracle and are not counted as bugs.

Designed = PASS + FAIL + OBSERVATION + BLOCKED + NOT RUN. Executed = PASS + FAIL + OBSERVATION. Cases covering Domain and BVA count once by TC-ID.

## All TC results

| TC-ID | Status | Bug group |
|---|---|---|
| A-API-01 | PASS | — |
| A-API-02 | PASS | — |
| A-API-03 | FAIL | BUG-A01 |
| A-API-04 | FAIL | BUG-A01 |
| A-API-05 | FAIL | BUG-A01 |
| A-API-06 | FAIL | BUG-A01 |
| A-API-07 | FAIL | BUG-A01 |
| A-API-08 | FAIL | BUG-A01 |
| A-API-09 | FAIL | BUG-A01 |
| A-API-10 | FAIL | BUG-A01 |
| A-API-11 | FAIL | BUG-A01 |
| A-API-12 | FAIL | BUG-A01 |
| A-API-13 | FAIL | BUG-A01 |
| A-API-14 | FAIL | BUG-A01 |
| A-API-15 | OBSERVATION | — |
| A-API-16 | FAIL | BUG-A01 |
| A-API-17 | PASS | — |
| A-API-18 | FAIL | BUG-A02 |
| A-API-19 | PASS | — |
| A-API-20 | PASS | — |
| A-API-21 | PASS | — |
| A-API-22 | PASS | — |
| B-API-01 | PASS | — |
| B-API-02 | PASS | — |
| B-API-03 | FAIL | BUG-B01 |
| B-API-04 | PASS | — |
| B-API-05 | PASS | — |
| B-API-06 | FAIL | BUG-B01 |
| B-API-07 | FAIL | BUG-B02 |
| B-API-08 | FAIL | BUG-B02 |
| B-API-09 | PASS | — |
| B-API-10 | PASS | — |
| B-API-11 | PASS | — |
| B-API-12 | PASS | — |
| B-API-13 | FAIL | BUG-B03 |
| B-API-14 | PASS | — |
| B-API-15 | PASS | — |
| B-API-16 | PASS | — |
| B-API-17 | PASS | — |
| B-API-18 | PASS | — |
| B-API-19 | FAIL | BUG-B04 |
| B-API-20 | FAIL | BUG-B04 |
| B-API-21 | FAIL | BUG-B04 |
| B-API-22 | FAIL | BUG-B05 |
| B-API-23 | FAIL | BUG-B05 |
| B-API-24 | FAIL | BUG-B01 |
| B-API-25 | PASS | — |
| B-API-26 | FAIL | BUG-B02 |
| C-API-01 | PASS | — |
| C-API-02 | PASS | — |
| C-API-03 | FAIL | BUG-C01 |
| C-API-04 | FAIL | BUG-C01 |
| C-API-05 | FAIL | BUG-C01 |
| C-API-06 | FAIL | BUG-C01 |
| C-API-07 | FAIL | BUG-C01 |
| C-API-08 | FAIL | BUG-C01 |
| C-API-09 | FAIL | BUG-C01 |
| C-API-10 | PASS | — |
| C-API-11 | FAIL | BUG-C03 |
| C-API-12 | FAIL | BUG-C04 |
| C-API-13 | FAIL | BUG-C04 |
| C-API-14 | PASS | — |
| C-API-15 | FAIL | BUG-C05 |
| C-API-16 | PASS | — |
| C-API-17 | PASS | — |
| C-API-18 | FAIL | BUG-C06 |
| C-API-19 | FAIL | BUG-C06 |
| C-API-20 | PASS | — |
| C-API-21 | PASS | — |
| C-API-22 | PASS | — |
| C-API-23 | FAIL | BUG-C07 |
| C-API-24 | PASS | — |
| C-API-25 | PASS | — |
| C-API-26 | FAIL | BUG-C08 |
| C-API-27 | PASS | — |
| C-API-28 | PASS | — |
| C-API-29 | FAIL | BUG-C09 |
| C-API-30 | PASS | — |
| D-API-01 | PASS | — |
| D-API-02 | PASS | — |
| D-API-03 | OBSERVATION | — |
| A-UI-01 | NOT RUN | — |
| A-UI-02 | NOT RUN | — |
| A-UI-03 | NOT RUN | — |
| A-UI-04 | NOT RUN | — |
| A-UI-05 | NOT RUN | — |
| A-UI-06 | NOT RUN | — |
| A-UI-07 | NOT RUN | — |
| B-UI-01 | NOT RUN | — |
| B-UI-02 | NOT RUN | — |
| B-UI-03 | NOT RUN | — |
| B-UI-04 | NOT RUN | — |
| B-UI-05 | NOT RUN | — |
| B-UI-06 | NOT RUN | — |
| C-UI-01 | NOT RUN | — |
| C-UI-02 | NOT RUN | — |
| C-UI-03 | NOT RUN | — |
| C-UI-04 | NOT RUN | — |
| C-UI-05 | NOT RUN | — |
| C-UI-06 | NOT RUN | — |
| D-UI-01 | NOT RUN | — |
| D-UI-02 | NOT RUN | — |
| D-UI-03 | NOT RUN | — |
| D-UI-04 | NOT RUN | — |
| D-UI-05 | NOT RUN | — |
| D-UI-06 | NOT RUN | — |
| D-UI-07 | NOT RUN | — |
| D-UI-08 | NOT RUN | — |
| D-UI-09 | NOT RUN | — |
| D-UI-10 | NOT RUN | — |
| D-UI-11 | NOT RUN | — |
| D-UI-12 | NOT RUN | — |
| D-UI-13 | NOT RUN | — |
| D-UI-14 | NOT RUN | — |

````

</details>

### Artifact `scripts/bugs.cjs`

SHA-256: `56538a5b9551f57181ef21053fcde7f959de61d848590e63ffdc7857129af4d1`

<details>
<summary>Full output</summary>

````text
const fs=require('node:fs'),path=require('node:path');
const {cases}=require('./cases.cjs'),{load}=require('./summarize.cjs');
const root=path.resolve(__dirname,'..');
const definitions={
 'BUG-A01':['Invalid phone values are accepted and persisted','A-API-03','High'],
 'BUG-A02':['Profile update permits client role escalation','A-API-18','Critical'],
 'BUG-B01':['Coupon minimum equality is incorrectly rejected','B-API-03','High'],
 'BUG-B02':['Percent coupon uses an incorrect discount formula','B-API-08','High'],
 'BUG-B03':['Coupon remains valid exactly at expiry','B-API-13','Medium'],
 'BUG-B04':['Coupon application ignores missing invalid or expired JWT','B-API-19','High'],
 'BUG-B05':['Client user_id can bypass authenticated user usage limit','B-API-22','High'],
 'BUG-C01':['Missing mandatory coupon fields and empty code are accepted','C-API-03','High'],
 'BUG-C03':['Coupon creation accepts unknown type','C-API-11','Medium'],
 'BUG-C04':['Coupon creation accepts nonpositive discount','C-API-13','High'],
 'BUG-C05':['Coupon creation accepts negative minimum amount','C-API-15','Medium'],
 'BUG-C06':['Coupon creation accepts invalid per-user usage limit','C-API-19','High'],
 'BUG-C07':['Regular user can create an admin coupon','C-API-23','High'],
 'BUG-C08':['Regular user can list admin coupons','C-API-26','Medium'],
 'BUG-C09':['Regular user can delete admin coupons','C-API-29','High']
};
function record(id){
 const c=cases.find(c=>c.id===id);if(!c)throw Error('Unknown TC '+id);
 const md=fs.readFileSync(path.join(root,'evidence','execution',c.feature+'-api.md'),'utf8');
 const block=md.split('\n## '+id+'\n')[1]?.split('\n## ')[0];
 if(!block)throw Error('No execution block '+id);
 const match=block.match(/```json\n([\s\S]*?)\n```/);if(!match)throw Error('No request trace');
 return {c,at:block.match(/Timestamp \(UTC\): (.+)/)?.[1],trace:JSON.parse(match[1])};
}
function compact(id){
 const data=record(id);let targetId;
 for(const t of data.trace)if(t.method==='DELETE')targetId=Number(t.url.split('/').at(-1));
 const trace=data.trace.map(t=>{
  if(!Array.isArray(t.body))return t;
  const mutation=data.trace.find(x=>x.method==='POST'&&x.url==='/api/admin/coupons');
  const code=mutation?.input?.code;
  const filtered=t.body.filter(row=>targetId?row.id===targetId:code?row.code===code||row.id===mutation?.body?.id:row.code==='SAVE10');
  return {...t,body:{totalRecords:t.body.length,relevantRows:filtered},note:'Full list retained in original raw execution evidence'};
 });
 return {...data,trace};
}
function render(){
 const summary=load();let index='# Bug Reports\n\nAPI runtime verified only; screenshots, student review and group Issues pending. Severity is a technical proposal, not an instructor-approved score. One root behavior groups multiple failed cases. No BUG-C02: duplicate uniqueness passed.\n\n| Bug | Title | Feature | Failing TC count | Status |\n|---|---|---|---:|---|\n';
 for(const bug of summary.bugs){
  const [title,example,severity]=definitions[bug];const all=summary.rows.filter(c=>c.bug===bug&&c.status==='FAIL');
  const r=compact(example);
  let md=`# ${bug} — ${title}\n\nStatus: API verified; screenshot pending; Issue URL pending; student review pending.\n\nSeverity (proposed): ${severity}\n\nFeature: ${r.c.feature}; oracle: ${r.c.rule}.\n\nAffected TC IDs: ${all.map(c=>c.id).join(', ')}.\n\n## Environment and preconditions\n\nSUT SHA 85af3ba875c88283615e22cb108f13e2fccaf0e9; Node24.16.0; isolated source copy; API port3100; frozen SUT time2026-10-19T08:00:00.000Z. Timestamp of representative execution (real UTC): ${r.at}. Each case resets users/coupons/usage fixtures. Authentication user/admin labels describe test accounts; actual tokens are not stored.\n\n## Steps to reproduce\n\n1. From the homework repository run \`node scripts/run-api.cjs ${r.c.feature}\` against the isolated copy; script owns the server and fixtures.\n2. Locate ${example}; request/readback sequence below is the exact captured public HTTP trace, reduced only to relevant list rows for readability.\n3. Compare status/body/persisted fields with the expected behavior. Full raw evidence retains every returned list row.\n\nInput:\n\n\`\`\`json\n${JSON.stringify(r.c.input,null,2)}\n\`\`\`\n\n## Expected\n\n${r.c.expected}\n\n## Actual\n\n\`\`\`json\n${JSON.stringify(r.trace,null,2)}\n\`\`\`\n\n[Full raw record](../evidence/execution/${r.c.feature}-api.md#${example.toLowerCase()}).\n\n## Screenshots and GitHub Issue\n\nPending real screenshot of this API execution record (terminal via \`node scripts/show-bug.cjs ${bug}\`) or an actual UI reproduction if possible. Do not present an API record screenshot as Web/Mobile interaction. Target image path: \`evidence/screenshots/api/${bug}_record-01.png\`. Group Issue publication happens after individual evidence/review; Issue URL/number and page screenshots are pending. This Markdown may be used as the issue body once the screenshot is attached.\n`;
  fs.mkdirSync(path.join(root,'bugs'),{recursive:true});fs.writeFileSync(path.join(root,'bugs',bug+'.md'),md);
  index+=`| [${bug}](${bug}.md) | ${title} | ${r.c.feature} | ${all.length} | API verified / manual evidence pending |\n`;
 }
 fs.writeFileSync(path.join(root,'bugs','bug-reports.md'),index+'\nIssue publication count: 0. Verified API bug count: '+summary.bugs.length+'.\n');
 console.log('Generated '+summary.bugs.length+' bug reports from FAIL records.');
}
if(require.main===module)render();else module.exports={definitions,record,compact};

````

</details>

### Artifact `scripts/cases.cjs`

SHA-256: `0626739a5b68050b64a4bcdcd5341d60f2a3790ee985ca817b62d386038f0a93`

<details>
<summary>Full output</summary>

````text
// Test inputs/expected behavior come from SRS FR-04/09/12/17/20 (+ mapped FR-06/07).
// Fixtures arrange state; public HTTP/UI observations determine outcomes.
const cases=[];
function add(feature,id,title,technique,rule,kind,input,expected,extra={}){cases.push({feature,id,title,technique,rule,kind,input,expected,...extra});}
function a(n,title,phone,valid,technique='Domain',extra={}){add('A',`A-API-${String(n).padStart(2,'0')}`,title,technique,'FR-04 phone: starts 0, 10–11 ASCII digits','profile',{name:'HW02 User',shipping_address:'1 Test Street',phone},valid?'Accept and persist the exact valid phone':'Reject; stored phone stays 0912345678',{valid,bug:'BUG-A01',...extra});}
a(1,'10 digits: lower ON boundary','0912345678',true,'Domain+BVA');
a(2,'11 digits: upper ON boundary','09123456789',true,'Domain+BVA');
a(3,'9 digits: lower OFF boundary','091234567',false,'Domain+BVA');
a(4,'12 digits: upper OFF boundary','091234567890',false,'Domain+BVA');
a(5,'Empty phone','',false);a(6,'One digit','0',false);a(7,'8 digits: invalid IN point','09123456',false);
a(8,'13 digits: invalid IN point','0912345678901',false);
a(9,'Wrong leading digit, length 10','1912345678',false);
a(10,'Wrong leading digit, length 11','19123456789',false);
a(11,'Alphabetic character','091234567a',false);a(12,'Embedded space','09123 5678',false);
a(13,'Country prefix instead of 0','+84912345678',false);a(14,'Hyphenated digits','09123-5678',false);
a(15,'Unicode fullwidth digits','０９１２３４５６７８',false,'Domain',{observation:true});
cases.at(-1).expected='Record Unicode numeral acceptance; SRS does not explicitly specify numeral encoding';
a(16,'Null phone',null,false);
add('A','A-API-17','Unicode name and address','Domain','FR-04 editable fields','profile',{name:'Người Dùng HW02',phone:'0912345678',shipping_address:'Đường Thử Nghiệm'},'Persist Unicode name and address exactly',{valid:true});
add('A','A-API-18','Client role escalation','Domain','FR-04 + SEC-06: cannot self-edit role','profile-role',{name:'HW02 User',phone:'0912345678',shipping_address:'1 Test Street',role:'admin'},'Reject or ignore role; GET /users/me remains role=user',{bug:'BUG-A02'});
add('A','A-API-19','Body user id cannot redirect update','Domain','FR-04 own profile only','profile-owner',{name:'Owner Only',phone:'0912345678',shipping_address:'1 Test Street',id:3,user_id:3},'Update authenticated user 2; user 3 unchanged');
for(const [id,auth] of [[20,'none'],[21,'invalid']]) add('A',`A-API-${id}`,'Profile update: '+auth+' token','Domain','FR-04 + SEC-02','profile-auth',{phone:'0912345678'},'Reject unauthenticated update (401/403); profile unchanged',{auth});
add('A','A-API-22','Profile read needs authentication','Domain','SEC-02','profile-read',{},'GET profile without JWT returns 401/403',{auth:'none'});

function b(n,title,input,expected,extra={}){add('B',`B-API-${String(n).padStart(2,'0')}`,title,extra.technique||'Domain','FR-09 C1–C5 + discount formula','coupon',input,expected,{auth:'user',...extra});}
b(1,'Fixed discount nominal',{code:'BIGBUY',total_amount:600000,user_id:2},'discount=50000; final=550000',{money:[50000,550000]});
b(2,'Below fixed minimum',{code:'BIGBUY',total_amount:499999,user_id:2},'Reject insufficient total',{reject:true,technique:'Domain+BVA'});
b(3,'Exactly fixed minimum',{code:'BIGBUY',total_amount:500000,user_id:2},'discount=50000; final=450000',{money:[50000,450000],bug:'BUG-B01',technique:'Domain+BVA'});
b(4,'Above fixed minimum',{code:'BIGBUY',total_amount:500001,user_id:2},'discount=50000; final=450001',{money:[50000,450001],technique:'Domain+BVA'});
b(5,'Below percent minimum',{code:'SAVE10',total_amount:299999,user_id:2},'Reject insufficient total',{reject:true,technique:'Domain+BVA'});
b(6,'Exactly percent minimum',{code:'SAVE10',total_amount:300000,user_id:2},'discount=30000; final=270000',{money:[30000,270000],bug:'BUG-B01',technique:'Domain+BVA'});
b(7,'Above percent minimum',{code:'SAVE10',total_amount:300001,user_id:2},'discount=30000.1; final=270000.9 (SRS has no rounding rule)',{money:[30000.1,270000.9],bug:'BUG-B02',technique:'Domain+BVA'});
b(8,'Percent formula with integer result',{code:'SAVE10',total_amount:400000,user_id:2},'discount=40000; final=360000',{money:[40000,360000],bug:'BUG-B02'});
b(9,'Nonexistent code',{code:'NO_SUCH_CODE',total_amount:600000,user_id:2},'Reject nonexistent code',{reject:true});
b(10,'Inactive code',{code:'OFF',total_amount:600000,user_id:2},'Reject inactive code',{reject:true});
b(11,'Missing code',{total_amount:600000,user_id:2},'Reject missing code',{reject:true});
b(12,'Expired before current time by 1 ms',{code:'TIME',total_amount:400000,user_id:2},'Reject expired coupon',{reject:true,expiry:-1,technique:'Domain+BVA'});
b(13,'Expiry exactly equals current time',{code:'TIME',total_amount:400000,user_id:2},'Reject: current time must be strictly before expiry',{reject:true,expiry:0,bug:'BUG-B03',technique:'Domain+BVA'});
b(14,'Expiry after current time by 1 ms',{code:'TIME',total_amount:400000,user_id:2},'discount=10000; final=390000',{money:[10000,390000],expiry:1,technique:'Domain+BVA'});
for(const [n,used] of [[15,0],[16,1],[17,2],[18,3]]) b(n,`VIP100 used=${used}, limit=2`,{code:'VIP100',total_amount:400000,user_id:2},used<2?'discount=100000; final=300000':'Reject exhausted coupon',{used,...(used<2?{money:[100000,300000]}:{reject:true}),technique:'Domain+BVA'});
for(const [n,auth]of[[19,'none'],[20,'invalid'],[21,'expired']])b(n,'Coupon with '+auth+' JWT',{code:'BIGBUY',total_amount:600000,user_id:2},'Reject invalid/missing authentication (401/403)',{auth,rejectAuth:true,bug:'BUG-B04'});
b(22,'Exhausted authenticated user spoofs user_id=3',{code:'VIP100',total_amount:400000,user_id:3},'Reject: user 2 already used limit; client user_id is not identity',{used:2,reject:true,bug:'BUG-B05'});
b(23,'Exhausted authenticated user omits user_id',{code:'VIP100',total_amount:400000},'Reject: authenticated user 2 already used limit',{used:2,reject:true,bug:'BUG-B05'});
b(24,'Intersection: minimum equality and last eligible use',{code:'VIP100',total_amount:300000,user_id:2},'discount=100000; final=200000',{used:1,money:[100000,200000],bug:'BUG-B01',technique:'Domain+BVA'});
b(25,'Multiple invalid conditions',{code:'OFF',total_amount:0},'Reject; no error precedence is specified',{auth:'none',reject:true});
b(26,'Percent 100 formula',{code:'P100',total_amount:400000,user_id:2},'discount=400000; final=0',{money:[400000,0],bug:'BUG-B02'});

const base={code:'HW02_NEW',type:'fixed',discount_value:1,min_order_amount:0,expired_at:'2099-12-31',max_uses_per_user:1};
function c(n,title,patch,valid,extra={}){const input={...base,...patch};if(extra.omit)delete input[extra.omit];add('C',`C-API-${String(n).padStart(2,'0')}`,title,extra.technique||'Domain','FR-17 required fields/constraints; FR-12 admin role','admin-create',input,valid?'Admin creates coupon and list contains exact supplied values':'Reject invalid coupon; list has no newly created record',{valid,auth:'admin',bug:'BUG-C01',...extra});}
c(1,'Nominal fixed coupon',{},true);c(2,'Nominal percent coupon',{type:'percent',discount_value:10},true);
let cn=3;
for(const field of Object.keys(base))c(cn++,`Missing mandatory ${field}`,{},false,{omit:field,bug:'BUG-C01'});
c(9,'Empty code',{code:''},false,{bug:'BUG-C01'});
c(10,'Duplicate code',{code:'SAVE10'},false,{bug:'BUG-C02'});
c(11,'Unknown type',{type:'other'},false,{bug:'BUG-C03'});
c(12,'discount_value=-1',{discount_value:-1},false,{bug:'BUG-C04',technique:'Domain+BVA'});
c(13,'discount_value=0',{discount_value:0},false,{bug:'BUG-C04',technique:'Domain+BVA'});
c(14,'discount_value=1',{discount_value:1},true,{technique:'Domain+BVA'});
c(15,'min_order_amount=-1',{min_order_amount:-1},false,{bug:'BUG-C05',technique:'Domain+BVA'});
c(16,'min_order_amount=0',{min_order_amount:0},true,{technique:'Domain+BVA'});
c(17,'min_order_amount=1',{min_order_amount:1},true,{technique:'Domain+BVA'});
c(18,'max_uses_per_user=-1',{max_uses_per_user:-1},false,{bug:'BUG-C06',technique:'Domain+BVA'});
c(19,'max_uses_per_user=0',{max_uses_per_user:0},false,{bug:'BUG-C06',technique:'Domain+BVA'});
c(20,'max_uses_per_user=1',{max_uses_per_user:1},true,{technique:'Domain+BVA'});
c(21,'max_uses_per_user=2',{max_uses_per_user:2},true,{technique:'Domain+BVA'});
c(22,'No JWT creates coupon',{},false,{auth:'none',authCase:true,bug:'BUG-C07'});
c(23,'User role creates coupon',{},false,{auth:'user',authCase:true,bug:'BUG-C07'});
c(24,'Invalid JWT creates coupon',{},false,{auth:'invalid',authCase:true,bug:'BUG-C07'});
for(const [n,auth]of[[25,'admin'],[26,'user'],[27,'none']])add('C',`C-API-${n}`,'List coupons as '+auth,'Domain','FR-12/FR-17','admin-list',{},auth==='admin'?'Return coupon list':'Reject non-admin access (401/403)',{auth,valid:auth==='admin',bug:'BUG-C08'});
for(const [n,auth]of[[28,'admin'],[29,'user'],[30,'none']])add('C',`C-API-${n}`,'Delete coupon as '+auth,'Domain','FR-12/FR-17','admin-delete',{code:'DELETE_ME'},auth==='admin'?'Coupon removed; other coupons unchanged':'Reject non-admin delete; coupon remains',{auth,valid:auth==='admin',bug:'BUG-C09'});
add('D','D-API-01','Product 1 support API','Domain','FR-20 + FR-06 mapped detail data','product',{id:1},'Product 1 name/price/description/image/category ID match fixture',{valid:true});
add('D','D-API-02','Product 2 support API','Domain','FR-20 + FR-06 mapped detail data','product',{id:2},'Product 2 data usable; price numerically 28000000 (JSON type not specified)',{valid:true});
add('D','D-API-03','Missing product support API observation','Domain','FR-20: missing-product HTTP schema unspecified','product',{id:999999},'Record HTTP/body; no mandated status code in SRS',{observation:true});

function ui(feature,id,title,input,expected,extra={}){add(feature,id,title,extra.technique||'Domain','UI '+(feature==='A'?'FR-04':feature==='B'?'FR-09':feature==='C'?'FR-17/FR-12':'FR-20 with mapped FR-06/07'), 'manual',input,expected,{status:'NOT RUN',...extra});}
for(const[n,phone,valid]of[[1,'091234567',false],[2,'0912345678',true],[3,'09123456789',true],[4,'091234567890',false],[5,'1912345678',false]])ui('A',`A-UI-0${n}`,'Profile phone '+phone,{phone},valid?'Update succeeds; re-login shows the exact phone':'Reject; saved profile remains unchanged',{technique:'Domain+BVA'});
ui('A','A-UI-06','Email field cannot be changed',{email:'other@example.invalid'},'Email is not editable via UI; original email unchanged');
ui('A','A-UI-07','Unicode editable profile fields',{name:'Người Dùng HW02',shipping_address:'Đường Thử Nghiệm',phone:'0912345678'},'Valid update accepted; name/address persist after fresh login');
for(const[n,code,total,expected]of[[1,'BIGBUY',499999,'Reject below minimum'],[2,'BIGBUY',500000,'Discount 50000; final 450000'],[3,'BIGBUY',500001,'Discount 50000; final 450001'],[4,'SAVE10',400000,'Discount 40000; final 360000'],[5,'EXPIRED',400000,'Reject expired coupon'],[6,'VIP100',400000,'After exactly 2 completed uses, third attempt rejected']])ui('B',`B-UI-0${n}`,'Checkout '+code+' / '+total,{code,total},expected,{technique:n<=3?'Domain+BVA':'Domain'});
for(const[n,patch,expected]of[[1,{discount_value:0},'Reject discount_value=0'],[2,{},'Create coupon; same values visible after reload'],[3,{min_order_amount:-1},'Reject negative minimum'],[4,{max_uses_per_user:0},'Reject zero usage limit'],[5,{code:'SAVE10'},'Reject duplicate; original SAVE10 unchanged']])ui('C',`C-UI-0${n}`,'Admin coupon form '+n,{...base,code:`HW02_C_UI_0${n}`,...patch},expected,{technique:n<=4?'Domain+BVA':'Domain'});
ui('C','C-UI-06','Admin delete lifecycle',{code:'HW02_DELETE_UI'},'Create test coupon, delete it; disappears after reload; SAVE10 unchanged');
for(const[n,q,expected]of[[1,'','Reject empty quantity; no new cart item'],[2,'-1','Reject negative; cart unchanged'],[3,'0','Reject zero; cart unchanged'],[4,'1','Cart contains quantity=1, total=30000000'],[5,'2','Cart contains quantity=2, total=60000000'],[6,'1.5','Reject fractional; cart unchanged'],[7,'abc','Reject nonnumeric; cart unchanged'],[8,'1abc','Reject mixed text; cart unchanged']])ui('D',`D-UI-0${n}`,'Mobile quantity '+JSON.stringify(q),{product:1,quantity:q},expected,{technique:n>=2&&n<=5?'Domain+BVA':'Domain',mapping:'FR-20 functionality + FR-06 positive integer; student confirms mapping'});
ui('D','D-UI-09','Mobile complete product detail',{product:1},'Image/name/price/description/category visible and correct; mapped FR-06',{mapping:'FR-20 + FR-06'});
ui('D','D-UI-10','Mobile even-id price display',{product:2},'Samsung price displayed as 28,000,000 ₫ using locale separator; no crash');
ui('D','D-UI-11','Mobile add feedback',{product:1,quantity:'1'},'Visible feedback after Add; cart quantity 1');
ui('D','D-UI-12','Same product twice',{product:1,quantity:'1',repetitions:2},'One cart line quantity=2; total=60000000',{mapping:'FR-07 reused through FR-20'});
ui('D','D-UI-13','Detail quantity resets after switching products',{products:[1,2],quantity:'2'},'Record selected quantity for product 2; SRS does not specify default reset policy',{observation:true});
ui('D','D-UI-14','Very large quantity exploratory input',{product:1,quantity:'9007199254740992'},'Record behavior/precision; upper limit unspecified, do not declare violation solely from size',{observation:true});
module.exports={cases,base};

````

</details>

### Artifact `scripts/check-builds.cjs`

SHA-256: `007cf9ae4c97f16279d251a7eeae5e7a31e2b4f9af4529948a270480948b9f37`

<details>
<summary>Full output</summary>

````text
const fs=require('node:fs'),path=require('node:path'),{spawn}=require('node:child_process');
const rt=require('./runtime.cjs');
const base=path.join(rt.runtime,'manual');
const jobs=[
 ['Web build',path.join(base,'frontend-web'),path.join(rt.sut,'frontend-web','node_modules','vite','bin','vite.js'),['build','--outDir',path.join(rt.runtime,'build-web')]],
 ['Admin build',path.join(base,'frontend-admin'),path.join(rt.sut,'frontend-admin','node_modules','vite','bin','vite.js'),['build','--outDir',path.join(rt.runtime,'build-admin')]],
 ['Android Metro export',path.join(base,'frontend-mobile'),path.join(rt.sut,'frontend-mobile','node_modules','expo','bin','cli'),['export','--platform','android','--output-dir',path.join(rt.runtime,'build-mobile-android')]]
];
async function run([name,cwd,entry,args]){
 const at=new Date().toISOString();
 return new Promise(resolve=>{
  let output='';const child=spawn(process.execPath,[entry,...args],{cwd,env:{...process.env,CI:'1'},stdio:['ignore','pipe','pipe']});
  child.stdout.on('data',d=>output+=d);child.stderr.on('data',d=>output+=d);child.on('error',e=>output+=String(e));
  const timer=setTimeout(()=>{output+='\nTIMEOUT 180 seconds';child.kill();},180000);
  child.on('close',code=>{clearTimeout(timer);console.log(name+': '+(code===0?'PASS':'FAIL'));resolve({name,at,cwd,entry,args,code,output});});
 });
}
(async()=>{
 const results=await Promise.all(jobs.map(run));
 let md='# Build checks\n\nThese are compiler/bundler checks only, not browser or native-device interaction evidence. Outputs stay outside submission repository. Dependencies were already installed; no claim of a fresh npm ci installation.\n';
 for(const r of results)md+=`\n## ${r.name}\n\nTimestamp (UTC): ${r.at}\n\nExit code: ${r.code}\n\nCommand: node ${r.entry} ${r.args.join(' ')}\n\n\`\`\`text\n${r.output.replaceAll('\x1b','[ESC]')}\n\`\`\`\n`;
 fs.mkdirSync(path.join(rt.repo,'evidence','execution'),{recursive:true});fs.writeFileSync(path.join(rt.repo,'evidence','execution','build-checks.md'),md);
 if(results.some(r=>r.code!==0))process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});

````

</details>

### Artifact `scripts/export-git-log.cjs`

SHA-256: `195ba542767164da6f20cb85171603df958ff7af2b4daa0afa555d81109874dd`

<details>
<summary>Full output</summary>

````text
const fs=require('node:fs'),path=require('node:path'),{execFileSync}=require('node:child_process');
const root=path.resolve(__dirname,'..');
const git=args=>execFileSync('git',args,{cwd:root,encoding:'utf8'}).trim();
const head=git(['rev-parse','HEAD']);
const log=git(['log','--date=iso-strict','--format=commit %H%nAuthor: %an%nDate: %ad%n%n    %s%n']);
fs.writeFileSync(path.join(root,'git-commit-log.md'),`# Git Commit Log\n\nSnapshot HEAD: ${head}\n\nExported at: ${new Date().toISOString()} (UTC). This text-based Markdown snapshot includes all implementation/testing commits through the stated HEAD; a later commit recording this export itself is outside the snapshot. No commit dates/history were rewritten.\n\nCommand: git log --date=iso-strict --format=commit/author/date/subject\n\n\`\`\`text\n${log}\n\`\`\`\n`);
console.log('Exported Git log through '+head);

````

</details>

### Artifact `scripts/manual-runtime.cjs`

SHA-256: `63279e81185930d6523b92dc8b5be280fc424a52da2ab6ab6366852507c8c669`

<details>
<summary>Full output</summary>

````text
// Prepares a disposable manual-test environment; never runs database.js in original SUT.
const fs=require('node:fs'),path=require('node:path'),os=require('node:os');
const {spawn}=require('node:child_process');
const {once}=require('node:events');
const rt=require('./runtime.cjs');
const {cases}=require('./cases.cjs');
const prefix=path.join(rt.runtime,'manual');
const candidates=Object.entries(os.networkInterfaces()).flatMap(([name,rows])=>rows.filter(x=>x.family==='IPv4'&&!x.internal&&!name.toLowerCase().includes('vethernet')).map(x=>x.address));
const ip=process.env.HW02_LAN_IP||candidates.find(x=>/^(192\.168\.|10\.|172\.(1[6-9]|2\d|3[01])\.)/.test(x))||'127.0.0.1';
function stage(){
  fs.mkdirSync(prefix,{recursive:true});
  for(const folder of ['frontend-web','frontend-admin','frontend-mobile']){
    const source=path.join(rt.sut,folder),target=path.join(prefix,folder);
    fs.cpSync(source,target,{recursive:true,filter:p=>!p.split(path.sep).some(part=>['node_modules','.git','dist','.expo'].includes(part))});
    const deps=path.join(target,'node_modules');if(!fs.existsSync(deps))fs.symlinkSync(path.join(source,'node_modules'),deps,'junction');
  }
  const app=path.join(prefix,'frontend-mobile','App.js');
  fs.writeFileSync(app,fs.readFileSync(app,'utf8').replace(/const API_URL = "[^"]+"/,`const API_URL = "http://${ip}:3000/api"`));
  fs.writeFileSync(path.join(prefix,'frontend-mobile','metro.config.js'),`const {getDefaultConfig}=require('expo/metro-config');const config=getDefaultConfig(__dirname);config.watchFolders=[${JSON.stringify(path.join(rt.sut,'frontend-mobile','node_modules'))}];module.exports=config;\n`);
}
async function seed(){
  const sqlite=rt.dependency('sqlite3');
  const db=await new Promise((resolve,reject)=>{const d=new sqlite.Database(path.join(prefix,'backend','database.sqlite'),e=>e?reject(e):resolve(d));});
  const sql=(q,args=[])=>new Promise((resolve,reject)=>db.run(q,args,e=>e?reject(e):resolve()));
  try{
    for(const tc of cases.filter(x=>x.kind==='manual')){
      const email=tc.id.toLowerCase().replaceAll('-','_')+'@hw02.invalid';
      await sql('INSERT INTO users(name,email,password,role,phone,shipping_address) VALUES(?,?,?,?,?,?)',[tc.id,email,'Test1234!',tc.feature==='C'?'admin':'user','0912345678','1 Test Street']);
    }
    for(const[id,price]of[[101,499999],[102,500000],[103,500001],[104,400000]])await sql('INSERT INTO products(id,name,price,description,imageUrl,category_id) VALUES(?,?,?,?,?,?)',[id,'HW02 Total '+price,price,'Fixture for coupon boundary','https://placehold.co/300x300/png?text=HW02',3]);
    await sql("INSERT INTO coupon_usage(coupon_id,user_id) SELECT c.id,u.id FROM coupons c,users u WHERE c.code='VIP100' AND u.email='b_ui_06@hw02.invalid'");
    await sql("INSERT INTO coupon_usage(coupon_id,user_id) SELECT c.id,u.id FROM coupons c,users u WHERE c.code='VIP100' AND u.email='b_ui_06@hw02.invalid'");
  }finally{await new Promise(resolve=>db.close(resolve));}
}
async function main(){
  stage();
  if(process.argv.includes('--prepare')){console.log('Staged frontend copies at '+prefix);console.log('Mobile API http://'+ip+':3000/api');return;}
  const net=require('node:net');
  for(const port of (process.argv.includes('--check')?[3000]:[3000,5173,5174,8081]))await new Promise((resolve,reject)=>{const probe=net.createServer();probe.once('error',reject);probe.listen(port,'127.0.0.1',()=>probe.close(resolve));});
  const children=[];const backend=rt.start(3000,false,'manual');children.push(backend.child);
  const stop=()=>children.forEach(c=>{if(c.exitCode===null)c.kill();});process.on('SIGINT',stop);process.on('SIGTERM',stop);
  try{
    await rt.ready(3000,backend.child);await seed();
    if(process.argv.includes('--check')){
      const res=await fetch('http://127.0.0.1:3000/api/products');const products=await res.json();
      if(products.length!==9)throw Error('Manual fixture product count');
      const login=await fetch('http://127.0.0.1:3000/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email:'b_ui_06@hw02.invalid',password:'Test1234!'})});
      if(!(await login.json()).token)throw Error('Manual account login failed');
      console.log('PASS manual fixture smoke: 9 products, per-case accounts, B-UI-06 login.');
      return;
    }
    for(const[folder,port]of[['frontend-web',5173],['frontend-admin',5174]]){
      const bin=path.join(rt.sut,folder,'node_modules','vite','bin','vite.js');
      const child=spawn(process.execPath,[bin,'--host','127.0.0.1','--port',String(port),'--strictPort'],{cwd:path.join(prefix,folder),stdio:'inherit'});children.push(child);
    }
    const expo=spawn(process.execPath,[path.join(rt.sut,'frontend-mobile','node_modules','expo','bin','cli'),'start','--lan','--port','8081'],{cwd:path.join(prefix,'frontend-mobile'),env:{...process.env,CI:'1'},stdio:'inherit'});children.push(expo);
    console.log('Web http://localhost:5173 | Admin http://localhost:5174 | Expo exp://'+ip+':8081');
    console.log('Per-case email: a_ui_01@hw02.invalid etc; demo password: Test1234! (all manual fixtures).');
    console.log('This process must stay running. Restart resets only disposable runtime data. Ctrl+C stops owned servers.');
    await new Promise((resolve,reject)=>{for(const child of children){child.once('error',reject);child.once('exit',(code)=>code?reject(Error('Service exited '+code)):resolve());}});
  }finally{const running=children.filter(c=>c.exitCode===null&&c.signalCode===null);const closing=running.map(c=>once(c,'close'));stop();await Promise.all(closing);}
}
main().catch(e=>{console.error(e);process.exitCode=1;});

````

</details>

### Artifact `scripts/render-cases.cjs`

SHA-256: `68f4d2a79ba415c14525cfa2bb95b878e5b4fe01e701b8db29cab69728347994`

<details>
<summary>Full output</summary>

````text
const fs=require('node:fs'),path=require('node:path');
const {cases}=require('./cases.cjs');
const root=path.resolve(__dirname,'..');
const names={A:'A-FR04-profile',B:'B-FR09-discount-coupons',C:'C-FR17-coupon-management',D:'D-mobile-product-detail'};
function steps(tc){
 const common='Reset fixtures; keep non-target fields valid. ';
 if(tc.kind==='manual')return 'Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.';
 if(tc.kind.startsWith('profile'))return common+'Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.';
 if(tc.kind==='coupon')return common+`Arrange VIP100 used=${tc.used||0}; ${tc.expiry===undefined?'future expiry':'TIME expiry offset '+tc.expiry+' ms from fixed clock'}. POST /api/apply-coupon with authentication=${tc.auth}; compare rejection or discount/final literals.`;
 if(tc.kind==='admin-create')return common+`GET /api/coupons as admin; POST /api/admin/coupons as ${tc.auth}; GET list as admin and compare count/persisted values.`;
 if(tc.kind==='admin-list')return common+`GET /api/coupons as ${tc.auth}; verify authorization.`;
 if(tc.kind==='admin-delete')return common+`GET coupons as admin to locate DELETE_ME; DELETE /api/admin/coupons/:id as ${tc.auth}; GET list as admin to verify target and count.`;
 return common+`GET /api/products/${tc.input.id}; compare seeded expected data. This is API support, not a Mobile UI execution.`;
}
for(const feature of process.argv[2]?[process.argv[2]]:['A','B','C','D']){
 const selected=cases.filter(c=>c.feature===feature);
 let md=`# ${names[feature]} — Test Cases\n\nDesign source: scripts/cases.cjs. Expected is frozen from SRS before execution. Techniques may overlap; each TC-ID counts once. API and UI have separate IDs and observations.\n\nPreconditions: isolated copied SUT; fixtures reset per API case; user 2/admin 1/other 3 tokens; SUT test clock 2026-10-19T08:00:00.000Z. Manual runtime uses the real clock and dedicated fixtures.\n\n| ID | Technique | Title | Seam |\n|---|---|---|---|\n`;
 for(const tc of selected)md+=`| ${tc.id} | ${tc.technique} | ${tc.title.replaceAll('|','/')} | ${tc.kind==='manual'?'UI pending':'HTTP API'} |\n`;
 for(const tc of selected)md+=`\n## ${tc.id} — ${tc.title}\n\nTechnique: ${tc.technique}\n\nOracle: ${tc.rule}${tc.mapping?' ('+tc.mapping+')':''}\n\nSteps: ${steps(tc)}\n\nInput:\n\n\`\`\`json\n${JSON.stringify(tc.input,null,2)}\n\`\`\`\n\nExpected: ${tc.expected}\n\nExecution: ${tc.kind==='manual'?'NOT RUN; complete manual-results.md with actual screenshots.':'See evidence/execution/'+feature+'-api.md; current summary is generated separately.'}\n`;
 fs.mkdirSync(path.join(root,'tests'),{recursive:true});fs.writeFileSync(path.join(root,'tests',names[feature]+'.md'),md);
}

````

</details>

### Artifact `scripts/run-api.cjs`

SHA-256: `f0c5fd2d79200bc257576a42b502ac80fce6c1378873dd776f023abdb1ecac8c`

<details>
<summary>Full output</summary>

````text
const fs=require('node:fs');
const path=require('node:path');
const {once}=require('node:events');
const {cases}=require('./cases.cjs');
const rt=require('./runtime.cjs');
const feature=process.argv[2];
if(!['A','B','C','D'].includes(feature))throw Error('Usage: node scripts/run-api.cjs A|B|C|D');
const port=3100,origin=`http://127.0.0.1:${port}`;
const started=new Date().toISOString();
const sourceFiles=['backend/server.js','backend/database.js','backend/database.sqlite','frontend-web/src/pages/Profile.jsx','frontend-web/src/pages/Checkout.jsx','frontend-admin/src/App.jsx','frontend-mobile/App.js'];
const hashes=Object.fromEntries(sourceFiles.map(f=>[f,rt.hash(path.join(rt.sut,f))]));
const clean=(value)=>Array.isArray(value)?value.map(clean):value&&typeof value==='object'?Object.fromEntries(Object.entries(value).filter(([k])=>!['password','token','reset_token','authorization'].includes(k.toLowerCase())).map(([k,v])=>[k,clean(v)])):value;
let database,server,trace=[],tokens={};
async function request(method,url,input,auth='user',record=true){
  const headers={'Content-Type':'application/json'};
  if(auth!=='none')headers.Authorization='Bearer '+(auth==='invalid'?'not-a-valid-jwt':tokens[auth]);
  const response=await fetch(origin+url,{method,headers,...(input===undefined?{}:{body:JSON.stringify(input)}),signal:AbortSignal.timeout(5000)});
  const raw=await response.text();let body;try{body=JSON.parse(raw);}catch{body=raw;}
  if(record)trace.push({method,url,authentication:auth,input:clean(input??null),status:response.status,body:clean(body)});
  return {status:response.status,body};
}
function sql(query,args=[]){return new Promise((resolve,reject)=>database.run(query,args,function(err){err?reject(err):resolve({id:this.lastID,changes:this.changes});}));}
async function fixtures(tc){
  await sql('DELETE FROM coupon_usage');
  await sql('DELETE FROM coupons');
  for(const row of [
    ['SAVE10','percent',10,300000,'2099-12-31',1,1],['BIGBUY','fixed',50000,500000,'2099-12-31',1,1],
    ['VIP100','fixed',100000,300000,'2099-12-31',1,2],['EXPIRED','percent',20,100000,'2020-01-01',1,1],
    ['OFF','fixed',10000,0,'2099-12-31',0,1],['TIME','fixed',10000,0,new Date(Date.parse(rt.fixed)+(tc.expiry??1000)).toISOString(),1,1],
    ['P100','percent',100,0,'2099-12-31',1,1],['DELETE_ME','fixed',1,0,'2099-12-31',1,1]
  ])await sql('INSERT INTO coupons(code,type,discount_value,min_order_amount,expired_at,is_active,max_uses_per_user) VALUES(?,?,?,?,?,?,?)',row);
  await sql("UPDATE users SET name='Test User',phone='0912345678',shipping_address='1 Test Street',role='user' WHERE id=2");
  await sql("UPDATE users SET name='Other User',phone='0987654321',shipping_address='Other Street',role='user' WHERE id=3");
  for(let i=0;i<(tc.used||0);i++)await sql("INSERT INTO coupon_usage(coupon_id,user_id) SELECT id,2 FROM coupons WHERE code='VIP100'");
}
function ok(r){return r.status>=200&&r.status<300;}
function denied(r){return r.status===401||r.status===403;}
function rejection(r){return r.status>=400&&r.status<500;}
async function execute(tc){
  switch(tc.kind){
    case 'profile':{
      const r=await request('PUT','/api/users/me',tc.input);
      const read=await request('GET','/api/users/me');
      const matches=Object.entries(tc.input).every(([k,v])=>read.body[k]===v);
      return tc.valid?ok(r)&&matches:rejection(r)&&read.body.phone==='0912345678';
    }
    case 'profile-role':{
      await request('PUT','/api/users/me',tc.input);
      return (await request('GET','/api/users/me')).body.role==='user';
    }
    case 'profile-owner':{
      const r=await request('PUT','/api/users/me',tc.input);
      const own=await request('GET','/api/users/me');const other=await request('GET','/api/users/me',undefined,'other');
      return ok(r)&&own.body.name==='Owner Only'&&other.body.name==='Other User';
    }
    case 'profile-auth':{
      const r=await request('PUT','/api/users/me',tc.input,tc.auth);
      const read=await request('GET','/api/users/me');
      return denied(r)&&read.body.phone==='0912345678';
    }
    case 'profile-read':return denied(await request('GET','/api/users/me',undefined,tc.auth));
    case 'coupon':{
      const r=await request('POST','/api/apply-coupon',tc.input,tc.auth);
      if(tc.rejectAuth)return denied(r);
      if(tc.reject)return rejection(r);
      return ok(r)&&Math.abs(r.body.discount_amount-tc.money[0])<1e-6&&Math.abs(r.body.final_amount-tc.money[1])<1e-6;
    }
    case 'admin-create':{
      const before=await request('GET','/api/coupons',undefined,'admin');
      const r=await request('POST','/api/admin/coupons',tc.input,tc.auth);
      const after=await request('GET','/api/coupons',undefined,'admin');
      if(!tc.valid)return (tc.authCase?denied(r):r.status>=400)&&after.body.length===before.body.length;
      const row=after.body.find(x=>x.id===r.body.id);
      return ok(r)&&row&&Object.entries(tc.input).every(([k,v])=>row[k]===v);
    }
    case 'admin-list':{
      const r=await request('GET','/api/coupons',undefined,tc.auth);
      return tc.valid?ok(r)&&Array.isArray(r.body):denied(r);
    }
    case 'admin-delete':{
      const before=await request('GET','/api/coupons',undefined,'admin');
      const id=before.body.find(x=>x.code==='DELETE_ME').id;
      const r=await request('DELETE',`/api/admin/coupons/${id}`,undefined,tc.auth);
      const after=await request('GET','/api/coupons',undefined,'admin');
      const removed=!after.body.some(x=>x.id===id);
      return tc.valid?ok(r)&&removed&&after.body.length===before.body.length-1:denied(r)&&!removed;
    }
    case 'product':{
      const r=await request('GET',`/api/products/${tc.input.id}`,undefined,'none');
      if(tc.observation)return true;
      const expected=tc.input.id===1?['iPhone 15 Pro Max',30000000]:['Samsung Galaxy S24 Ultra',28000000];
      return ok(r)&&r.body.name===expected[0]&&Number(r.body.price)===expected[1]&&typeof r.body.description==='string'&&typeof r.body.imageUrl==='string'&&r.body.category_id===1;
    }
    default:throw Error('Unsupported kind '+tc.kind);
  }
}
(async()=>{
  const results=[];
  try{
    // Never attach to a pre-existing listener: every run owns its runtime.
    const net=require('node:net');await new Promise((resolve,reject)=>{const p=net.createServer();p.once('error',reject);p.listen(port,'127.0.0.1',()=>p.close(resolve));});
    server=rt.start(port,true);await rt.ready(port,server.child);
    const sqlite3=rt.dependency('sqlite3').verbose();
    database=await new Promise((resolve,reject)=>{const db=new sqlite3.Database(path.join(server.target,'database.sqlite'),e=>e?reject(e):resolve(db));});
    await sql("INSERT INTO users(id,name,email,password,role,phone,shipping_address) VALUES(3,'Other User','other@hw02.invalid','Test1234!','user','0987654321','Other Street')");
    for(const[role,email,password]of[['admin','admin@eshop.com','Admin123!'],['user','test@eshop.com','Test1234!'],['other','other@hw02.invalid','Test1234!']]){
      const r=await request('POST','/api/login',{email,password},'none',false);if(!r.body.token)throw Error('Fixture login failed '+role);tokens[role]=r.body.token;
    }
    const source=fs.readFileSync(path.join(rt.sut,'backend','server.js'),'utf8');
    const secret=source.match(/const SECRET_KEY = "([^"]+)"/)[1];
    tokens.expired=rt.dependency('jsonwebtoken').sign({id:2,role:'user',exp:Math.floor(Date.parse(rt.fixed)/1000)-1},secret,{noTimestamp:true});
    for(const tc of cases.filter(x=>x.feature===feature&&x.kind!=='manual')){
      trace=[];const at=new Date().toISOString();let status,reason='';
      try{await fixtures(tc);const passed=await execute(tc);status=tc.observation?'OBSERVATION':passed?'PASS':'FAIL';}catch(e){status='BLOCKED';reason=String(e);}
      results.push({id:tc.id,status,at,expected:tc.expected,bug:status==='FAIL'?tc.bug:null,reason,trace});
      console.log(tc.id,status);
    }
  }finally{
    if(database)await new Promise(r=>database.close(r));
    if(server&&server.child.exitCode===null&&server.child.signalCode===null){const closed=once(server.child,'close');server.child.kill();await closed;}
  }
  const unchanged=Object.entries(hashes).every(([f,h])=>rt.hash(path.join(rt.sut,f))===h);
  const count={};for(const r of results)count[r.status]=(count[r.status]||0)+1;
  let md=`# ${feature} — Raw API execution\n\nStarted (UTC): ${started}\n\nFinished (UTC): ${new Date().toISOString()}\n\nHost timezone labels use UTC explicitly; add 07:00 for Asia/Saigon. SUT clock frozen at ${rt.fixed}; runner timestamp uses real clock.\n\nOrigin: ${origin}. Byte-identical copied backend source; HTTP listen port and global Date adapter only. SQLite fixtures are test setup; assertions observe public API. Password/token fields are omitted from evidence.\n\nOriginal SUT files unchanged after run: **${unchanged?'PASS':'FAIL'}**.\n\n## Source hashes\n\n| File | SHA-256 before (= after when PASS) |\n|---|---|\n`;
  for(const[f,h]of Object.entries(hashes))md+=`| ${f} | ${h} |\n`;
  md+=`\n## Results\n\n| ID | Status | Bug group |\n|---|---|---|\n`;
  for(const r of results)md+=`| ${r.id} | ${r.status} | ${r.bug||'—'} |\n`;
  for(const r of results)md+=`\n## ${r.id}\n\nStatus: ${r.status}\n\nTimestamp (UTC): ${r.at}\n\nExpected: ${r.expected}\n\n${r.reason?'Blocker: '+r.reason+'\n\n':''}Requests/responses (sanitized):\n\n\`\`\`json\n${JSON.stringify(r.trace,null,2)}\n\`\`\`\n`;
  fs.mkdirSync(path.join(rt.repo,'evidence','execution'),{recursive:true});
  fs.writeFileSync(path.join(rt.repo,'evidence','execution',`${feature}-api.md`),md);
  console.log(JSON.stringify({feature,count,originalUnchanged:unchanged}));
  if(!unchanged||results.some(r=>r.status==='BLOCKED'))process.exitCode=2;
})().catch(e=>{console.error(e);process.exitCode=2;});

````

</details>

### Artifact `scripts/runtime.cjs`

SHA-256: `85968c9839e86387e47716e7892c4cfee1dd724906aa4f26211fc1efdf31e5c6`

<details>
<summary>Full output</summary>

````text
// Runtime adapter: source bytes are copied unchanged; only port and test clock differ.
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const {spawn} = require('node:child_process');
const {createRequire} = require('node:module');
const repo = path.resolve(__dirname, '..');
const sut = path.resolve(process.env.HW02_SUT || path.join(repo, '..', 'eshop-sut'));
const runtime = path.resolve(process.env.HW02_RUNTIME || path.join(repo, '..', '.hw02-runtime'));
const fixed = '2026-10-19T08:00:00.000Z';
function hash(file) { return crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex'); }
function dependency(name) { return createRequire(path.join(sut, 'backend', 'package.json'))(name); }
function stage(label='api') {
  // Refuse to stage on the original backend: database.js drops tables at import.
  if(!/^[a-z-]+$/.test(label))throw Error('Invalid runtime label');
  const target = path.join(runtime, label, 'backend');
  if (target.toLowerCase() === path.join(sut, 'backend').toLowerCase() || !target.startsWith(runtime + path.sep)) throw Error('Unsafe runtime path');
  fs.mkdirSync(target, {recursive:true});
  for (const file of ['server.js','database.js']) fs.copyFileSync(path.join(sut,'backend',file),path.join(target,file));
  return target;
}
function start(port=3100, freeze=true, label='api') {
  const target=stage(label);
  const child=spawn(process.execPath,[__filename,'child'],{env:{...process.env,NODE_PATH:path.join(sut,'backend','node_modules'),HW02_SERVER:path.join(target,'server.js'),HW02_PORT:String(port),HW02_CLOCK:freeze?fixed:''},stdio:['ignore','pipe','pipe']});
  let log=''; child.stdout.on('data',d=>log+=d);child.stderr.on('data',d=>log+=d);
  child.on('error',e=>log+=String(e));
  return {child, target, log:()=>log};
}
async function ready(port, child) {
  for(let i=0;i<100;i++) {
    if(child.exitCode!==null)throw Error('Backend exited '+child.exitCode);
    try {const r=await fetch(`http://127.0.0.1:${port}/api/products`,{signal:AbortSignal.timeout(500)});const a=await r.json();if(Array.isArray(a)&&a.length===5)return;}catch{}
    await new Promise(r=>setTimeout(r,100));
  }
  throw Error('Backend readiness timeout');
}
if(require.main===module&&process.argv[2]==='child'){
  require('node:module').Module._initPaths();
  if(process.env.HW02_CLOCK){
    const RealDate=Date, now=RealDate.parse(process.env.HW02_CLOCK);
    global.Date=class extends RealDate{constructor(...args){super(...(args.length?args:[now]));}static now(){return now;}};
  }
  const http=require('node:http'),listen=http.Server.prototype.listen;
  http.Server.prototype.listen=function(...args){args[0]=Number(process.env.HW02_PORT);return listen.apply(this,args);};
  require(process.env.HW02_SERVER);
}else module.exports={repo,sut,runtime,fixed,hash,dependency,start,ready};

````

</details>

### Artifact `scripts/show-bug.cjs`

SHA-256: `db6f9f02ef6edc8b74ea0b03e8734178f70c7587422a94ac4e7ee2d7a56edfbc`

<details>
<summary>Full output</summary>

````text
const {definitions,compact}=require('./bugs.cjs');
const id=process.argv[2];
if(!definitions[id])throw Error('Use a Bug-ID listed in bugs/bug-reports.md');
const [title,tc]=definitions[id],r=compact(tc);
console.log(`${id}: ${title}\nRECORDED EXECUTION (not a new request)\nTC: ${tc}\nReal UTC: ${r.at}\nExpected: ${r.c.expected}\nActual public HTTP trace:`);
for(const trace of r.trace)console.log(JSON.stringify(trace,null,2));
console.log('Full raw record: evidence/execution/'+r.c.feature+'-api.md');

````

</details>

### Artifact `scripts/summarize.cjs`

SHA-256: `47816ba8c50b3c9cda2ce82ab9b7e6019e819af91205a3258e0258310adc2678`

<details>
<summary>Full output</summary>

````text
const fs=require('node:fs'),path=require('node:path');
const {cases}=require('./cases.cjs');const root=path.resolve(__dirname,'..');
function load(){
 const statuses=new Map();
 for(const f of ['A','B','C','D']){
  const file=path.join(root,'evidence','execution',f+'-api.md');
  if(!fs.existsSync(file))continue;
  for(const m of fs.readFileSync(file,'utf8').matchAll(/^\| ([A-D]-API-\d+) \| (PASS|FAIL|BLOCKED|OBSERVATION) \| ([^|]+) \|$/gm)){
   if(statuses.has(m[1]))throw Error('Duplicate actual '+m[1]);statuses.set(m[1],{status:m[2],bug:m[3].trim()});
  }
 }
 const manual=path.join(root,'evidence','manual-results.md');
 if(fs.existsSync(manual))for(const m of fs.readFileSync(manual,'utf8').matchAll(/^\| ([A-D]-UI-\d+) \| (PASS|FAIL|BLOCKED|NOT RUN|OBSERVATION) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|$/gm)){
  if(statuses.has(m[1]))throw Error('Duplicate manual '+m[1]);
  if(['PASS','FAIL','OBSERVATION'].includes(m[2])&&(!m[3].trim()||!m[4].trim()||m[5].trim()==='—'||!m[5].trim()))throw Error('Executed manual row needs actual timestamp/result/evidence: '+m[1]);
  statuses.set(m[1],{status:m[2],bug:'—'});
 }
 for(const id of statuses.keys())if(!cases.some(c=>c.id===id))throw Error('Unknown result ID '+id);
 const rows=cases.map(c=>({...c,...(statuses.get(c.id)||{status:'NOT RUN',bug:'—'})}));
 const count=selected=>{const out={designed:selected.length,executed:0,PASS:0,FAIL:0,BLOCKED:0,'NOT RUN':0,OBSERVATION:0};for(const r of selected){out[r.status]++;if(['PASS','FAIL','OBSERVATION'].includes(r.status))out.executed++;}return out;};
 return {rows,count,totals:count(rows),bugs:[...new Set(rows.filter(r=>r.status==='FAIL'&&r.bug!=='—'&&r.bug).map(r=>r.bug))].sort()};
}
function render(){
 const {rows,count,totals,bugs}=load();
 let table='| Scope | Designed | Executed | PASS | FAIL | OBSERVATION | BLOCKED | NOT RUN |\n|---|---:|---:|---:|---:|---:|---:|---:|\n';
 for(const label of ['A','B','C','D','API','UI','Total']){const group=label==='Total'?rows:label==='API'?rows.filter(r=>r.kind!=='manual'):label==='UI'?rows.filter(r=>r.kind==='manual'):rows.filter(r=>r.feature===label);const c=count(group);table+=`| ${label} | ${c.designed} | ${c.executed} | ${c.PASS} | ${c.FAIL} | ${c.OBSERVATION} | ${c.BLOCKED} | ${c['NOT RUN']} |\n`;}
 const text='# Test Summary\n\n'+table+`\nAPI verified bug groups: ${bugs.length}. Mobile UI execution is pending; product API support is counted separately. Observations have no definitive requirement oracle and are not counted as bugs.\n\nDesigned = PASS + FAIL + OBSERVATION + BLOCKED + NOT RUN. Executed = PASS + FAIL + OBSERVATION. Cases covering Domain and BVA count once by TC-ID.\n\n## All TC results\n\n| TC-ID | Status | Bug group |\n|---|---|---|\n`+rows.map(r=>`| ${r.id} | ${r.status} | ${r.bug||'—'} |`).join('\n')+'\n';
 fs.mkdirSync(path.join(root,'reports'),{recursive:true});fs.writeFileSync(path.join(root,'reports','test-summary.md'),text);
 const readme=`# HW02 — Domain Testing on EShop\n\n## Student\n\n- Student ID: 23120262 (from the initial repository README).\n- Name / class: sinh viên điền và xác nhận.\n- Status: Codex API/design work prepared; UI screenshots, native interaction, human review, video and group Issues pending.\n\n## Confirmed Feature Scope\n\n| Pool | Feature |\n|---|---|\n| A | FR-04 Personal profile management |\n| B | FR-09 Discount coupons |\n| C | FR-17 Admin coupon management (Create/View/Delete) |\n| D | Mobile productDetail |\n\nNgười dùng xác nhận feature đã chia và không trùng nhóm.\n\n## Current Test Summary\n\n${table}\nAPI verified bug groups: **${bugs.length}**. GitHub Issues published: **0**. Actual screenshots/video: **pending**. UI results are not inferred from API results or source inspection.\n\n## Required Final Assessment Table\n\n| No. | Criteria | Maximum grade | Self-assessed grade |\n|---|---|---:|---|\n| 1 | Feature A (Domain + Boundary) | 25 | Chờ sinh viên |\n| 2 | Feature B (Domain + Boundary) | 25 | Chờ sinh viên |\n| 3 | Feature C (Domain + Boundary) | 25 | Chờ sinh viên |\n| 4 | Feature D (Mobile, Domain + Boundary) | 15 | Chờ sinh viên |\n| 5 | Agent Skills | 10 | Chờ demo video / sinh viên |\n| | Total | 100 | Chưa chốt |\n\n## Main Deliverables\n\n- [Main report](REPORT.md), [test summary](reports/test-summary.md), [environment](reports/test-environment.md).\n- [Test cases](tests/), [API execution evidence](evidence/execution/), [bug reports](bugs/bug-reports.md).\n- [AI audit forms](ai-audit/) (filenames match source templates exactly).\n- [Manual handoff](reports/manual-handoff.md) and [manual results](evidence/manual-results.md).\n- [Reusable skill](.agents/skills/domain-bva-testing/SKILL.md), [skill demonstration](reports/skill-demonstration.md).\n- [Git commit log](git-commit-log.md).\n\n## Demonstration Video\n\n[Recording instructions and pending link](evidence/video-links.md). No video has been recorded/uploaded by Codex.\n\n## GitHub Issues\n\nGroup repository/publication handled after individual work. Draft-ready bug bodies are in bugs/; all Issue URLs remain pending.\n\n## Strict Submission Gates\n\n1. Execute pending UI/Mobile cases; attach real screenshots and review requirement mapping.\n2. Sinh viên review AI outputs/Critique, complete disclosure/signatures and self-assessment.\n3. Record the end-to-end skill demonstration and supply a working YouTube URL.\n4. Publish bugs with screenshots to the group Issues repository; retain page screenshots and URLs.\n5. Sinh viên tự xuất PDF/định dạng cuối, đóng ZIP đúng tên và nộp Moodle trước hạn. Codex chỉ viết tài liệu Markdown.\n\n## Source Documents\n\nAssignment and policies are supplied outside this repository; the work plan also stays outside. SUT baseline: 85af3ba875c88283615e22cb108f13e2fccaf0e9. Source links and assumptions are recorded in the feature reports.\n\nThis work used OpenAI Codex to draft design, scripts and reports. Technical review by Codex is recorded separately from the student's pending human review in ai-audit/.\n`;
 fs.writeFileSync(path.join(root,'README.md'),readme);console.log(JSON.stringify({totals,verifiedBugs:bugs.length}));
}
if(require.main===module)render();else module.exports={load};

````

</details>

### Artifact `scripts/validate-deliverables.py`

SHA-256: `2b110aa5ec958ecd1d63aafc8f7236e3dfaa23254efbba67ca889aa031a9d33e`

<details>
<summary>Full output</summary>

````text
"""Validate submission-source consistency without inventing missing manual results."""
from pathlib import Path
import subprocess,json,re,urllib.parse

repo=Path(__file__).resolve().parents[1]
errors=[]
def check(ok,label):
    print(('PASS: 'if ok else 'FAIL: ')+label)
    if not ok:errors.append(label)
cases=json.loads(subprocess.check_output(['node','-e','process.stdout.write(JSON.stringify(require("./scripts/cases.cjs").cases))'],cwd=repo,text=True,encoding='utf-8'))
check(len({c['id']for c in cases})==len(cases),'Unique TC IDs')
results=json.loads(subprocess.check_output(['node','-e','const x=require("./scripts/summarize.cjs").load(); process.stdout.write(JSON.stringify({totals:x.totals,bugs:x.bugs}))'],cwd=repo,text=True,encoding='utf-8'))
t=results['totals'];check(t['designed']==sum(t[k]for k in ('PASS','FAIL','OBSERVATION','BLOCKED','NOT RUN')),'Designed count reconciles with statuses')
check(t['executed']==t['PASS']+t['FAIL']+t['OBSERVATION'],'Executed count reconciles')
check(t['BLOCKED']==0,'No API harness blockers in current result set')
check(all((repo/'bugs'/f'{b}.md').is_file()for b in results['bugs']),'Every failed bug group has a report')
expected={f'[AI-{i:02}] - FIT@HCMUS - {name}_Vn.md'for i,name in [(2,'AI Audit Report'),(3,'AI Disclosure Form'),(4,'AI Reflective Statement'),(5,'AI Privacy Checklist')]}
actual={p.name for p in (repo/'ai-audit').iterdir()if p.is_file()}
templates=repo.parents[1]/'templates'
check(expected==actual and all((templates/f).is_file()for f in expected),'Exact selected template filenames; no extra files in ai-audit')
check(not(repo/'ai').exists()and not list(repo.rglob('interactions')),'ai-audit structure has no legacy ai or interactions directory')
check(not(repo/'TASKS.md').exists()and not(repo/'references').exists(),'Plan and reference copies stay outside submission repo')
check(not [p for p in repo.rglob('*')if '.git'not in p.parts and p.is_file()and p.suffix.lower()in ('.pdf','.docx','.xlsx','.zip','.txt','.json','.log')],'Authored docs are Markdown; final formats not generated in repo')
crit=(repo/'ai-audit'/'[AI-04] - FIT@HCMUS - AI Reflective Statement_Vn.md').read_text(encoding='utf-8')
body=crit.split('### AI Critique — ',1)[1].split('\n\n',1)[1].split('\n## 3.',1)[0]
check(200<=len(body.split())<=300,f'Critique word count {len(body.split())} in 200–300')
broken=[];unbalanced=[]
for file in repo.rglob('*.md'):
    if '.git'in file.parts:continue
    fence=None;plain=[]
    for line in file.read_text(encoding='utf-8').splitlines():
        match=re.match(r'^\s*(`{3,}|~{3,})',line)
        if match:
            mark=match.group(1)
            if fence is None:fence=mark
            elif mark[0]==fence[0]and len(mark)>=len(fence):fence=None
            continue
        if fence is None:plain.append(line)
    if fence:unbalanced.append(str(file.relative_to(repo)))
    for m in re.finditer(r'\[[^\]\n]*\]\((<[^>\n]+>|[^)\s]+)\)', '\n'.join(plain)):
        link=m[1].strip('<>');target=urllib.parse.unquote(link.split('#',1)[0])
        if not target or re.match(r'^[a-zA-Z][\w+.-]*:',target):continue
        path=(file.parent/target).resolve()
        if not path.exists():broken.append((str(file.relative_to(repo)),link))
check(not broken,'Local Markdown links outside code fences resolve: '+str(broken[:6]))
check(not unbalanced,'Markdown code fences balanced: '+str(unbalanced[:6]))
for f in 'ABCD':
    raw=(repo/'evidence'/'execution'/f'{f}-api.md').read_text(encoding='utf-8')
    check('Original SUT files unchanged after run: **PASS**'in raw,f'{f}: original SUT preserved')
    check(not re.search(r'"(token|password|reset_token)"\s*:',raw),f'{f}: credential fields absent in raw evidence')
check(all(c['id']in (repo/'reports'/'manual-handoff.md').read_text(encoding='utf-8')for c in cases if c['kind']=='manual'),'All manual TC IDs have detailed handoff instructions')
if errors:raise SystemExit(1)
print('DELIVERABLE VALIDATION PASS (manual completion remains pending).')

````

</details>

### Artifact `tests/A-FR04-profile.md`

SHA-256: `3d676ab93a56699f02db0e47394fda94a925bcf5e6b988c0f0265a06b9c10749`

<details>
<summary>Full output</summary>

````text
# A-FR04-profile — Test Cases

Design source: scripts/cases.cjs. Expected is frozen from SRS before execution. Techniques may overlap; each TC-ID counts once. API and UI have separate IDs and observations.

Preconditions: isolated copied SUT; fixtures reset per API case; user 2/admin 1/other 3 tokens; SUT test clock 2026-10-19T08:00:00.000Z. Manual runtime uses the real clock and dedicated fixtures.

| ID | Technique | Title | Seam |
|---|---|---|---|
| A-API-01 | Domain+BVA | 10 digits: lower ON boundary | HTTP API |
| A-API-02 | Domain+BVA | 11 digits: upper ON boundary | HTTP API |
| A-API-03 | Domain+BVA | 9 digits: lower OFF boundary | HTTP API |
| A-API-04 | Domain+BVA | 12 digits: upper OFF boundary | HTTP API |
| A-API-05 | Domain | Empty phone | HTTP API |
| A-API-06 | Domain | One digit | HTTP API |
| A-API-07 | Domain | 8 digits: invalid IN point | HTTP API |
| A-API-08 | Domain | 13 digits: invalid IN point | HTTP API |
| A-API-09 | Domain | Wrong leading digit, length 10 | HTTP API |
| A-API-10 | Domain | Wrong leading digit, length 11 | HTTP API |
| A-API-11 | Domain | Alphabetic character | HTTP API |
| A-API-12 | Domain | Embedded space | HTTP API |
| A-API-13 | Domain | Country prefix instead of 0 | HTTP API |
| A-API-14 | Domain | Hyphenated digits | HTTP API |
| A-API-15 | Domain | Unicode fullwidth digits | HTTP API |
| A-API-16 | Domain | Null phone | HTTP API |
| A-API-17 | Domain | Unicode name and address | HTTP API |
| A-API-18 | Domain | Client role escalation | HTTP API |
| A-API-19 | Domain | Body user id cannot redirect update | HTTP API |
| A-API-20 | Domain | Profile update: none token | HTTP API |
| A-API-21 | Domain | Profile update: invalid token | HTTP API |
| A-API-22 | Domain | Profile read needs authentication | HTTP API |
| A-UI-01 | Domain+BVA | Profile phone 091234567 | UI pending |
| A-UI-02 | Domain+BVA | Profile phone 0912345678 | UI pending |
| A-UI-03 | Domain+BVA | Profile phone 09123456789 | UI pending |
| A-UI-04 | Domain+BVA | Profile phone 091234567890 | UI pending |
| A-UI-05 | Domain+BVA | Profile phone 1912345678 | UI pending |
| A-UI-06 | Domain | Email field cannot be changed | UI pending |
| A-UI-07 | Domain | Unicode editable profile fields | UI pending |

## A-API-01 — 10 digits: lower ON boundary

Technique: Domain+BVA

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "0912345678"
}
```

Expected: Accept and persist the exact valid phone

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-02 — 11 digits: upper ON boundary

Technique: Domain+BVA

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "09123456789"
}
```

Expected: Accept and persist the exact valid phone

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-03 — 9 digits: lower OFF boundary

Technique: Domain+BVA

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "091234567"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-04 — 12 digits: upper OFF boundary

Technique: Domain+BVA

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "091234567890"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-05 — Empty phone

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": ""
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-06 — One digit

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "0"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-07 — 8 digits: invalid IN point

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "09123456"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-08 — 13 digits: invalid IN point

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "0912345678901"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-09 — Wrong leading digit, length 10

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "1912345678"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-10 — Wrong leading digit, length 11

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "19123456789"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-11 — Alphabetic character

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "091234567a"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-12 — Embedded space

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "09123 5678"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-13 — Country prefix instead of 0

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "+84912345678"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-14 — Hyphenated digits

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "09123-5678"
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-15 — Unicode fullwidth digits

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "０９１２３４５６７８"
}
```

Expected: Record Unicode numeral acceptance; SRS does not explicitly specify numeral encoding

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-16 — Null phone

Technique: Domain

Oracle: FR-04 phone: starts 0, 10–11 ASCII digits

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": null
}
```

Expected: Reject; stored phone stays 0912345678

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-17 — Unicode name and address

Technique: Domain

Oracle: FR-04 editable fields

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "Người Dùng HW02",
  "phone": "0912345678",
  "shipping_address": "Đường Thử Nghiệm"
}
```

Expected: Persist Unicode name and address exactly

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-18 — Client role escalation

Technique: Domain

Oracle: FR-04 + SEC-06: cannot self-edit role

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "HW02 User",
  "phone": "0912345678",
  "shipping_address": "1 Test Street",
  "role": "admin"
}
```

Expected: Reject or ignore role; GET /users/me remains role=user

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-19 — Body user id cannot redirect update

Technique: Domain

Oracle: FR-04 own profile only

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "name": "Owner Only",
  "phone": "0912345678",
  "shipping_address": "1 Test Street",
  "id": 3,
  "user_id": 3
}
```

Expected: Update authenticated user 2; user 3 unchanged

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-20 — Profile update: none token

Technique: Domain

Oracle: FR-04 + SEC-02

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "phone": "0912345678"
}
```

Expected: Reject unauthenticated update (401/403); profile unchanged

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-21 — Profile update: invalid token

Technique: Domain

Oracle: FR-04 + SEC-02

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{
  "phone": "0912345678"
}
```

Expected: Reject unauthenticated update (401/403); profile unchanged

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-API-22 — Profile read needs authentication

Technique: Domain

Oracle: SEC-02

Steps: Reset fixtures; keep non-target fields valid. Use user 2 JWT unless auth is specified. PUT /api/users/me (GET only for profile-read); GET /api/users/me as needed to verify persistence/ownership. Auth cases use missing or invalid JWT. Other-user check logs in user 3.

Input:

```json
{}
```

Expected: GET profile without JWT returns 401/403

Execution: See evidence/execution/A-api.md; current summary is generated separately.

## A-UI-01 — Profile phone 091234567

Technique: Domain+BVA

Oracle: UI FR-04

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "phone": "091234567"
}
```

Expected: Reject; saved profile remains unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## A-UI-02 — Profile phone 0912345678

Technique: Domain+BVA

Oracle: UI FR-04

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "phone": "0912345678"
}
```

Expected: Update succeeds; re-login shows the exact phone

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## A-UI-03 — Profile phone 09123456789

Technique: Domain+BVA

Oracle: UI FR-04

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "phone": "09123456789"
}
```

Expected: Update succeeds; re-login shows the exact phone

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## A-UI-04 — Profile phone 091234567890

Technique: Domain+BVA

Oracle: UI FR-04

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "phone": "091234567890"
}
```

Expected: Reject; saved profile remains unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## A-UI-05 — Profile phone 1912345678

Technique: Domain+BVA

Oracle: UI FR-04

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "phone": "1912345678"
}
```

Expected: Reject; saved profile remains unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## A-UI-06 — Email field cannot be changed

Technique: Domain

Oracle: UI FR-04

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "email": "other@example.invalid"
}
```

Expected: Email is not editable via UI; original email unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## A-UI-07 — Unicode editable profile fields

Technique: Domain

Oracle: UI FR-04

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "name": "Người Dùng HW02",
  "shipping_address": "Đường Thử Nghiệm",
  "phone": "0912345678"
}
```

Expected: Valid update accepted; name/address persist after fresh login

Execution: NOT RUN; complete manual-results.md with actual screenshots.

````

</details>

### Artifact `tests/B-FR09-discount-coupons.md`

SHA-256: `5b599feea9754a74c5e7d47f90116a171a5993c20400522cd1f6818287dd7262`

<details>
<summary>Full output</summary>

````text
# B-FR09-discount-coupons — Test Cases

Design source: scripts/cases.cjs. Expected is frozen from SRS before execution. Techniques may overlap; each TC-ID counts once. API and UI have separate IDs and observations.

Preconditions: isolated copied SUT; fixtures reset per API case; user 2/admin 1/other 3 tokens; SUT test clock 2026-10-19T08:00:00.000Z. Manual runtime uses the real clock and dedicated fixtures.

| ID | Technique | Title | Seam |
|---|---|---|---|
| B-API-01 | Domain | Fixed discount nominal | HTTP API |
| B-API-02 | Domain+BVA | Below fixed minimum | HTTP API |
| B-API-03 | Domain+BVA | Exactly fixed minimum | HTTP API |
| B-API-04 | Domain+BVA | Above fixed minimum | HTTP API |
| B-API-05 | Domain+BVA | Below percent minimum | HTTP API |
| B-API-06 | Domain+BVA | Exactly percent minimum | HTTP API |
| B-API-07 | Domain+BVA | Above percent minimum | HTTP API |
| B-API-08 | Domain | Percent formula with integer result | HTTP API |
| B-API-09 | Domain | Nonexistent code | HTTP API |
| B-API-10 | Domain | Inactive code | HTTP API |
| B-API-11 | Domain | Missing code | HTTP API |
| B-API-12 | Domain+BVA | Expired before current time by 1 ms | HTTP API |
| B-API-13 | Domain+BVA | Expiry exactly equals current time | HTTP API |
| B-API-14 | Domain+BVA | Expiry after current time by 1 ms | HTTP API |
| B-API-15 | Domain+BVA | VIP100 used=0, limit=2 | HTTP API |
| B-API-16 | Domain+BVA | VIP100 used=1, limit=2 | HTTP API |
| B-API-17 | Domain+BVA | VIP100 used=2, limit=2 | HTTP API |
| B-API-18 | Domain+BVA | VIP100 used=3, limit=2 | HTTP API |
| B-API-19 | Domain | Coupon with none JWT | HTTP API |
| B-API-20 | Domain | Coupon with invalid JWT | HTTP API |
| B-API-21 | Domain | Coupon with expired JWT | HTTP API |
| B-API-22 | Domain | Exhausted authenticated user spoofs user_id=3 | HTTP API |
| B-API-23 | Domain | Exhausted authenticated user omits user_id | HTTP API |
| B-API-24 | Domain+BVA | Intersection: minimum equality and last eligible use | HTTP API |
| B-API-25 | Domain | Multiple invalid conditions | HTTP API |
| B-API-26 | Domain | Percent 100 formula | HTTP API |
| B-UI-01 | Domain+BVA | Checkout BIGBUY / 499999 | UI pending |
| B-UI-02 | Domain+BVA | Checkout BIGBUY / 500000 | UI pending |
| B-UI-03 | Domain+BVA | Checkout BIGBUY / 500001 | UI pending |
| B-UI-04 | Domain | Checkout SAVE10 / 400000 | UI pending |
| B-UI-05 | Domain | Checkout EXPIRED / 400000 | UI pending |
| B-UI-06 | Domain | Checkout VIP100 / 400000 | UI pending |

## B-API-01 — Fixed discount nominal

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "BIGBUY",
  "total_amount": 600000,
  "user_id": 2
}
```

Expected: discount=50000; final=550000

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-02 — Below fixed minimum

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "BIGBUY",
  "total_amount": 499999,
  "user_id": 2
}
```

Expected: Reject insufficient total

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-03 — Exactly fixed minimum

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "BIGBUY",
  "total_amount": 500000,
  "user_id": 2
}
```

Expected: discount=50000; final=450000

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-04 — Above fixed minimum

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "BIGBUY",
  "total_amount": 500001,
  "user_id": 2
}
```

Expected: discount=50000; final=450001

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-05 — Below percent minimum

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "SAVE10",
  "total_amount": 299999,
  "user_id": 2
}
```

Expected: Reject insufficient total

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-06 — Exactly percent minimum

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "SAVE10",
  "total_amount": 300000,
  "user_id": 2
}
```

Expected: discount=30000; final=270000

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-07 — Above percent minimum

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "SAVE10",
  "total_amount": 300001,
  "user_id": 2
}
```

Expected: discount=30000.1; final=270000.9 (SRS has no rounding rule)

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-08 — Percent formula with integer result

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "SAVE10",
  "total_amount": 400000,
  "user_id": 2
}
```

Expected: discount=40000; final=360000

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-09 — Nonexistent code

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "NO_SUCH_CODE",
  "total_amount": 600000,
  "user_id": 2
}
```

Expected: Reject nonexistent code

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-10 — Inactive code

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "OFF",
  "total_amount": 600000,
  "user_id": 2
}
```

Expected: Reject inactive code

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-11 — Missing code

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "total_amount": 600000,
  "user_id": 2
}
```

Expected: Reject missing code

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-12 — Expired before current time by 1 ms

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; TIME expiry offset -1 ms from fixed clock. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "TIME",
  "total_amount": 400000,
  "user_id": 2
}
```

Expected: Reject expired coupon

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-13 — Expiry exactly equals current time

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; TIME expiry offset 0 ms from fixed clock. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "TIME",
  "total_amount": 400000,
  "user_id": 2
}
```

Expected: Reject: current time must be strictly before expiry

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-14 — Expiry after current time by 1 ms

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; TIME expiry offset 1 ms from fixed clock. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "TIME",
  "total_amount": 400000,
  "user_id": 2
}
```

Expected: discount=10000; final=390000

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-15 — VIP100 used=0, limit=2

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "VIP100",
  "total_amount": 400000,
  "user_id": 2
}
```

Expected: discount=100000; final=300000

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-16 — VIP100 used=1, limit=2

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=1; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "VIP100",
  "total_amount": 400000,
  "user_id": 2
}
```

Expected: discount=100000; final=300000

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-17 — VIP100 used=2, limit=2

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=2; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "VIP100",
  "total_amount": 400000,
  "user_id": 2
}
```

Expected: Reject exhausted coupon

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-18 — VIP100 used=3, limit=2

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=3; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "VIP100",
  "total_amount": 400000,
  "user_id": 2
}
```

Expected: Reject exhausted coupon

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-19 — Coupon with none JWT

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=none; compare rejection or discount/final literals.

Input:

```json
{
  "code": "BIGBUY",
  "total_amount": 600000,
  "user_id": 2
}
```

Expected: Reject invalid/missing authentication (401/403)

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-20 — Coupon with invalid JWT

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=invalid; compare rejection or discount/final literals.

Input:

```json
{
  "code": "BIGBUY",
  "total_amount": 600000,
  "user_id": 2
}
```

Expected: Reject invalid/missing authentication (401/403)

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-21 — Coupon with expired JWT

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=expired; compare rejection or discount/final literals.

Input:

```json
{
  "code": "BIGBUY",
  "total_amount": 600000,
  "user_id": 2
}
```

Expected: Reject invalid/missing authentication (401/403)

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-22 — Exhausted authenticated user spoofs user_id=3

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=2; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "VIP100",
  "total_amount": 400000,
  "user_id": 3
}
```

Expected: Reject: user 2 already used limit; client user_id is not identity

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-23 — Exhausted authenticated user omits user_id

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=2; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "VIP100",
  "total_amount": 400000
}
```

Expected: Reject: authenticated user 2 already used limit

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-24 — Intersection: minimum equality and last eligible use

Technique: Domain+BVA

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=1; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "VIP100",
  "total_amount": 300000,
  "user_id": 2
}
```

Expected: discount=100000; final=200000

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-25 — Multiple invalid conditions

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=none; compare rejection or discount/final literals.

Input:

```json
{
  "code": "OFF",
  "total_amount": 0
}
```

Expected: Reject; no error precedence is specified

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-API-26 — Percent 100 formula

Technique: Domain

Oracle: FR-09 C1–C5 + discount formula

Steps: Reset fixtures; keep non-target fields valid. Arrange VIP100 used=0; future expiry. POST /api/apply-coupon with authentication=user; compare rejection or discount/final literals.

Input:

```json
{
  "code": "P100",
  "total_amount": 400000,
  "user_id": 2
}
```

Expected: discount=400000; final=0

Execution: See evidence/execution/B-api.md; current summary is generated separately.

## B-UI-01 — Checkout BIGBUY / 499999

Technique: Domain+BVA

Oracle: UI FR-09

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "BIGBUY",
  "total": 499999
}
```

Expected: Reject below minimum

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## B-UI-02 — Checkout BIGBUY / 500000

Technique: Domain+BVA

Oracle: UI FR-09

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "BIGBUY",
  "total": 500000
}
```

Expected: Discount 50000; final 450000

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## B-UI-03 — Checkout BIGBUY / 500001

Technique: Domain+BVA

Oracle: UI FR-09

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "BIGBUY",
  "total": 500001
}
```

Expected: Discount 50000; final 450001

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## B-UI-04 — Checkout SAVE10 / 400000

Technique: Domain

Oracle: UI FR-09

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "SAVE10",
  "total": 400000
}
```

Expected: Discount 40000; final 360000

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## B-UI-05 — Checkout EXPIRED / 400000

Technique: Domain

Oracle: UI FR-09

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "EXPIRED",
  "total": 400000
}
```

Expected: Reject expired coupon

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## B-UI-06 — Checkout VIP100 / 400000

Technique: Domain

Oracle: UI FR-09

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "VIP100",
  "total": 400000
}
```

Expected: After exactly 2 completed uses, third attempt rejected

Execution: NOT RUN; complete manual-results.md with actual screenshots.

````

</details>

### Artifact `tests/C-FR17-coupon-management.md`

SHA-256: `4ce016a75ac476a847034c44fe6b83893b2944f8f71353af50ea65a8e3b7577d`

<details>
<summary>Full output</summary>

````text
# C-FR17-coupon-management — Test Cases

Design source: scripts/cases.cjs. Expected is frozen from SRS before execution. Techniques may overlap; each TC-ID counts once. API and UI have separate IDs and observations.

Preconditions: isolated copied SUT; fixtures reset per API case; user 2/admin 1/other 3 tokens; SUT test clock 2026-10-19T08:00:00.000Z. Manual runtime uses the real clock and dedicated fixtures.

| ID | Technique | Title | Seam |
|---|---|---|---|
| C-API-01 | Domain | Nominal fixed coupon | HTTP API |
| C-API-02 | Domain | Nominal percent coupon | HTTP API |
| C-API-03 | Domain | Missing mandatory code | HTTP API |
| C-API-04 | Domain | Missing mandatory type | HTTP API |
| C-API-05 | Domain | Missing mandatory discount_value | HTTP API |
| C-API-06 | Domain | Missing mandatory min_order_amount | HTTP API |
| C-API-07 | Domain | Missing mandatory expired_at | HTTP API |
| C-API-08 | Domain | Missing mandatory max_uses_per_user | HTTP API |
| C-API-09 | Domain | Empty code | HTTP API |
| C-API-10 | Domain | Duplicate code | HTTP API |
| C-API-11 | Domain | Unknown type | HTTP API |
| C-API-12 | Domain+BVA | discount_value=-1 | HTTP API |
| C-API-13 | Domain+BVA | discount_value=0 | HTTP API |
| C-API-14 | Domain+BVA | discount_value=1 | HTTP API |
| C-API-15 | Domain+BVA | min_order_amount=-1 | HTTP API |
| C-API-16 | Domain+BVA | min_order_amount=0 | HTTP API |
| C-API-17 | Domain+BVA | min_order_amount=1 | HTTP API |
| C-API-18 | Domain+BVA | max_uses_per_user=-1 | HTTP API |
| C-API-19 | Domain+BVA | max_uses_per_user=0 | HTTP API |
| C-API-20 | Domain+BVA | max_uses_per_user=1 | HTTP API |
| C-API-21 | Domain+BVA | max_uses_per_user=2 | HTTP API |
| C-API-22 | Domain | No JWT creates coupon | HTTP API |
| C-API-23 | Domain | User role creates coupon | HTTP API |
| C-API-24 | Domain | Invalid JWT creates coupon | HTTP API |
| C-API-25 | Domain | List coupons as admin | HTTP API |
| C-API-26 | Domain | List coupons as user | HTTP API |
| C-API-27 | Domain | List coupons as none | HTTP API |
| C-API-28 | Domain | Delete coupon as admin | HTTP API |
| C-API-29 | Domain | Delete coupon as user | HTTP API |
| C-API-30 | Domain | Delete coupon as none | HTTP API |
| C-UI-01 | Domain+BVA | Admin coupon form 1 | UI pending |
| C-UI-02 | Domain+BVA | Admin coupon form 2 | UI pending |
| C-UI-03 | Domain+BVA | Admin coupon form 3 | UI pending |
| C-UI-04 | Domain+BVA | Admin coupon form 4 | UI pending |
| C-UI-05 | Domain | Admin coupon form 5 | UI pending |
| C-UI-06 | Domain | Admin delete lifecycle | UI pending |

## C-API-01 — Nominal fixed coupon

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Admin creates coupon and list contains exact supplied values

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-02 — Nominal percent coupon

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "percent",
  "discount_value": 10,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Admin creates coupon and list contains exact supplied values

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-03 — Missing mandatory code

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-04 — Missing mandatory type

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-05 — Missing mandatory discount_value

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-06 — Missing mandatory min_order_amount

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-07 — Missing mandatory expired_at

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-08 — Missing mandatory max_uses_per_user

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31"
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-09 — Empty code

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-10 — Duplicate code

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "SAVE10",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-11 — Unknown type

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "other",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-12 — discount_value=-1

Technique: Domain+BVA

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": -1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-13 — discount_value=0

Technique: Domain+BVA

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 0,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-14 — discount_value=1

Technique: Domain+BVA

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Admin creates coupon and list contains exact supplied values

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-15 — min_order_amount=-1

Technique: Domain+BVA

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": -1,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-16 — min_order_amount=0

Technique: Domain+BVA

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Admin creates coupon and list contains exact supplied values

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-17 — min_order_amount=1

Technique: Domain+BVA

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 1,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Admin creates coupon and list contains exact supplied values

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-18 — max_uses_per_user=-1

Technique: Domain+BVA

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": -1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-19 — max_uses_per_user=0

Technique: Domain+BVA

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 0
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-20 — max_uses_per_user=1

Technique: Domain+BVA

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Admin creates coupon and list contains exact supplied values

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-21 — max_uses_per_user=2

Technique: Domain+BVA

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as admin; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 2
}
```

Expected: Admin creates coupon and list contains exact supplied values

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-22 — No JWT creates coupon

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as none; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-23 — User role creates coupon

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as user; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-24 — Invalid JWT creates coupon

Technique: Domain

Oracle: FR-17 required fields/constraints; FR-12 admin role

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; POST /api/admin/coupons as invalid; GET list as admin and compare count/persisted values.

Input:

```json
{
  "code": "HW02_NEW",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject invalid coupon; list has no newly created record

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-25 — List coupons as admin

Technique: Domain

Oracle: FR-12/FR-17

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as admin; verify authorization.

Input:

```json
{}
```

Expected: Return coupon list

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-26 — List coupons as user

Technique: Domain

Oracle: FR-12/FR-17

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as user; verify authorization.

Input:

```json
{}
```

Expected: Reject non-admin access (401/403)

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-27 — List coupons as none

Technique: Domain

Oracle: FR-12/FR-17

Steps: Reset fixtures; keep non-target fields valid. GET /api/coupons as none; verify authorization.

Input:

```json
{}
```

Expected: Reject non-admin access (401/403)

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-28 — Delete coupon as admin

Technique: Domain

Oracle: FR-12/FR-17

Steps: Reset fixtures; keep non-target fields valid. GET coupons as admin to locate DELETE_ME; DELETE /api/admin/coupons/:id as admin; GET list as admin to verify target and count.

Input:

```json
{
  "code": "DELETE_ME"
}
```

Expected: Coupon removed; other coupons unchanged

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-29 — Delete coupon as user

Technique: Domain

Oracle: FR-12/FR-17

Steps: Reset fixtures; keep non-target fields valid. GET coupons as admin to locate DELETE_ME; DELETE /api/admin/coupons/:id as user; GET list as admin to verify target and count.

Input:

```json
{
  "code": "DELETE_ME"
}
```

Expected: Reject non-admin delete; coupon remains

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-API-30 — Delete coupon as none

Technique: Domain

Oracle: FR-12/FR-17

Steps: Reset fixtures; keep non-target fields valid. GET coupons as admin to locate DELETE_ME; DELETE /api/admin/coupons/:id as none; GET list as admin to verify target and count.

Input:

```json
{
  "code": "DELETE_ME"
}
```

Expected: Reject non-admin delete; coupon remains

Execution: See evidence/execution/C-api.md; current summary is generated separately.

## C-UI-01 — Admin coupon form 1

Technique: Domain+BVA

Oracle: UI FR-17/FR-12

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "HW02_C_UI_01",
  "type": "fixed",
  "discount_value": 0,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject discount_value=0

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## C-UI-02 — Admin coupon form 2

Technique: Domain+BVA

Oracle: UI FR-17/FR-12

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "HW02_C_UI_02",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Create coupon; same values visible after reload

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## C-UI-03 — Admin coupon form 3

Technique: Domain+BVA

Oracle: UI FR-17/FR-12

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "HW02_C_UI_03",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": -1,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject negative minimum

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## C-UI-04 — Admin coupon form 4

Technique: Domain+BVA

Oracle: UI FR-17/FR-12

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "HW02_C_UI_04",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 0
}
```

Expected: Reject zero usage limit

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## C-UI-05 — Admin coupon form 5

Technique: Domain

Oracle: UI FR-17/FR-12

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "SAVE10",
  "type": "fixed",
  "discount_value": 1,
  "min_order_amount": 0,
  "expired_at": "2099-12-31",
  "max_uses_per_user": 1
}
```

Expected: Reject duplicate; original SAVE10 unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## C-UI-06 — Admin delete lifecycle

Technique: Domain

Oracle: UI FR-17/FR-12

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "code": "HW02_DELETE_UI"
}
```

Expected: Create test coupon, delete it; disappears after reload; SAVE10 unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

````

</details>

### Artifact `tests/D-mobile-product-detail.md`

SHA-256: `25a4f1ce2bfa819939fda6086e8692dd2bc5ed35baee9fcb7612044011b09993`

<details>
<summary>Full output</summary>

````text
# D-mobile-product-detail — Test Cases

Design source: scripts/cases.cjs. Expected is frozen from SRS before execution. Techniques may overlap; each TC-ID counts once. API and UI have separate IDs and observations.

Preconditions: isolated copied SUT; fixtures reset per API case; user 2/admin 1/other 3 tokens; SUT test clock 2026-10-19T08:00:00.000Z. Manual runtime uses the real clock and dedicated fixtures.

| ID | Technique | Title | Seam |
|---|---|---|---|
| D-API-01 | Domain | Product 1 support API | HTTP API |
| D-API-02 | Domain | Product 2 support API | HTTP API |
| D-API-03 | Domain | Missing product support API observation | HTTP API |
| D-UI-01 | Domain | Mobile quantity "" | UI pending |
| D-UI-02 | Domain+BVA | Mobile quantity "-1" | UI pending |
| D-UI-03 | Domain+BVA | Mobile quantity "0" | UI pending |
| D-UI-04 | Domain+BVA | Mobile quantity "1" | UI pending |
| D-UI-05 | Domain+BVA | Mobile quantity "2" | UI pending |
| D-UI-06 | Domain | Mobile quantity "1.5" | UI pending |
| D-UI-07 | Domain | Mobile quantity "abc" | UI pending |
| D-UI-08 | Domain | Mobile quantity "1abc" | UI pending |
| D-UI-09 | Domain | Mobile complete product detail | UI pending |
| D-UI-10 | Domain | Mobile even-id price display | UI pending |
| D-UI-11 | Domain | Mobile add feedback | UI pending |
| D-UI-12 | Domain | Same product twice | UI pending |
| D-UI-13 | Domain | Detail quantity resets after switching products | UI pending |
| D-UI-14 | Domain | Very large quantity exploratory input | UI pending |

## D-API-01 — Product 1 support API

Technique: Domain

Oracle: FR-20 + FR-06 mapped detail data

Steps: Reset fixtures; keep non-target fields valid. GET /api/products/1; compare seeded expected data. This is API support, not a Mobile UI execution.

Input:

```json
{
  "id": 1
}
```

Expected: Product 1 name/price/description/image/category ID match fixture

Execution: See evidence/execution/D-api.md; current summary is generated separately.

## D-API-02 — Product 2 support API

Technique: Domain

Oracle: FR-20 + FR-06 mapped detail data

Steps: Reset fixtures; keep non-target fields valid. GET /api/products/2; compare seeded expected data. This is API support, not a Mobile UI execution.

Input:

```json
{
  "id": 2
}
```

Expected: Product 2 data usable; price numerically 28000000 (JSON type not specified)

Execution: See evidence/execution/D-api.md; current summary is generated separately.

## D-API-03 — Missing product support API observation

Technique: Domain

Oracle: FR-20: missing-product HTTP schema unspecified

Steps: Reset fixtures; keep non-target fields valid. GET /api/products/999999; compare seeded expected data. This is API support, not a Mobile UI execution.

Input:

```json
{
  "id": 999999
}
```

Expected: Record HTTP/body; no mandated status code in SRS

Execution: See evidence/execution/D-api.md; current summary is generated separately.

## D-UI-01 — Mobile quantity ""

Technique: Domain

Oracle: UI FR-20 with mapped FR-06/07 (FR-20 functionality + FR-06 positive integer; student confirms mapping)

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": ""
}
```

Expected: Reject empty quantity; no new cart item

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-02 — Mobile quantity "-1"

Technique: Domain+BVA

Oracle: UI FR-20 with mapped FR-06/07 (FR-20 functionality + FR-06 positive integer; student confirms mapping)

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": "-1"
}
```

Expected: Reject negative; cart unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-03 — Mobile quantity "0"

Technique: Domain+BVA

Oracle: UI FR-20 with mapped FR-06/07 (FR-20 functionality + FR-06 positive integer; student confirms mapping)

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": "0"
}
```

Expected: Reject zero; cart unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-04 — Mobile quantity "1"

Technique: Domain+BVA

Oracle: UI FR-20 with mapped FR-06/07 (FR-20 functionality + FR-06 positive integer; student confirms mapping)

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": "1"
}
```

Expected: Cart contains quantity=1, total=30000000

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-05 — Mobile quantity "2"

Technique: Domain+BVA

Oracle: UI FR-20 with mapped FR-06/07 (FR-20 functionality + FR-06 positive integer; student confirms mapping)

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": "2"
}
```

Expected: Cart contains quantity=2, total=60000000

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-06 — Mobile quantity "1.5"

Technique: Domain

Oracle: UI FR-20 with mapped FR-06/07 (FR-20 functionality + FR-06 positive integer; student confirms mapping)

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": "1.5"
}
```

Expected: Reject fractional; cart unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-07 — Mobile quantity "abc"

Technique: Domain

Oracle: UI FR-20 with mapped FR-06/07 (FR-20 functionality + FR-06 positive integer; student confirms mapping)

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": "abc"
}
```

Expected: Reject nonnumeric; cart unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-08 — Mobile quantity "1abc"

Technique: Domain

Oracle: UI FR-20 with mapped FR-06/07 (FR-20 functionality + FR-06 positive integer; student confirms mapping)

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": "1abc"
}
```

Expected: Reject mixed text; cart unchanged

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-09 — Mobile complete product detail

Technique: Domain

Oracle: UI FR-20 with mapped FR-06/07 (FR-20 + FR-06)

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1
}
```

Expected: Image/name/price/description/category visible and correct; mapped FR-06

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-10 — Mobile even-id price display

Technique: Domain

Oracle: UI FR-20 with mapped FR-06/07

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 2
}
```

Expected: Samsung price displayed as 28,000,000 ₫ using locale separator; no crash

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-11 — Mobile add feedback

Technique: Domain

Oracle: UI FR-20 with mapped FR-06/07

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": "1"
}
```

Expected: Visible feedback after Add; cart quantity 1

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-12 — Same product twice

Technique: Domain

Oracle: UI FR-20 with mapped FR-06/07 (FR-07 reused through FR-20)

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": "1",
  "repetitions": 2
}
```

Expected: One cart line quantity=2; total=60000000

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-13 — Detail quantity resets after switching products

Technique: Domain

Oracle: UI FR-20 with mapped FR-06/07

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "products": [
    1,
    2
  ],
  "quantity": "2"
}
```

Expected: Record selected quantity for product 2; SRS does not specify default reset policy

Execution: NOT RUN; complete manual-results.md with actual screenshots.

## D-UI-14 — Very large quantity exploratory input

Technique: Domain

Oracle: UI FR-20 with mapped FR-06/07

Steps: Follow the numbered task in reports/manual-handoff.md; enter the exact values below; record actual/evidence. No UI run has been performed by Codex.

Input:

```json
{
  "product": 1,
  "quantity": "9007199254740992"
}
```

Expected: Record behavior/precision; upper limit unspecified, do not declare violation solely from size

Execution: NOT RUN; complete manual-results.md with actual screenshots.

````

</details>

### Artifact `REPORT.md`

SHA-256: `c450dd49e6b301fa8fc7656e12a0b0ece5356d223fd075f205d444af596cbef0`

<details>
<summary>Full output</summary>

````text
# HW02 — Domain Testing on EShop

## Student and scope

MSSV: 23120262. Họ tên/lớp: sinh viên xác nhận. Bài cá nhân, bốn feature đã được chia không trùng nhóm: FR-04, FR-09, FR-17, Mobile productDetail. Phần nhóm GitHub Issues xử lý sau.

## Method

Quy trình áp dụng cho từng feature: xác định SRS/oracle và vector input/output → chia miền valid/invalid → ghi ràng buộc/giao miền → chọn đại diện → xác định boundary và lân cận → hướng dẫn AI sinh cases theo từng bước → review → thực thi public API → đọc lại hậu điều kiện → group bugs → phân tích gaps. Không coi một prompt “generate all tests” là toàn bộ phương pháp.

Domain Testing xem xét cả partitions và ràng buộc nhiều chiều; BVA nhắm các mặt biên được chỉ rõ, không gán min/max cho enum hoặc rule không có giới hạn. Các cases thuộc cả hai kỹ thuật vẫn đếm một TC-ID. Fixture SQL dùng để dựng trạng thái; kết quả được quan sát qua HTTP/API hoặc UI thật khi sinh viên chạy sau.

Tham chiếu kỹ thuật: [ISTQB CTFL v4.0.1 §4.2.1–4.2.2](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf). Lecture môn chưa có trong workspace; chưa nhận đã đối chiếu lecture. [Environment](reports/test-environment.md) ghi baseline, clocks và adapters.

## A — Personal profile

[Domain/BVA analysis](reports/A-FR04-domain.md), [detailed test cases](tests/A-FR04-profile.md), [raw API evidence](evidence/execution/A-api.md), [technical review and AI gaps](reports/A-FR04-review.md).

Miền phone hợp lệ có length10–11, prefix0, digits; boundary9/10/11/12. Tách user ownership, JWT và role tampering để valid phone không che lỗi authorization. API có 7 PASS/14 FAIL/1 OBSERVATION; 7 UI cases chờ chạy. Hai bug groups: invalid phone validation và role escalation.

## B — Discount coupons

[Domain/BVA analysis](reports/B-FR09-domain.md), [test cases](tests/B-FR09-discount-coupons.md), [raw evidence](evidence/execution/B-api.md), [review/gaps](reports/B-FR09-review.md).

Miền hợp lệ là giao C1–C5. Boundary total=minimum inclusive, now=expiry exclusive, used=limit exclusive. Nominal fixed tách validation khỏi percent formula; thêm corner total=minimum/used=limit−1 và identity spoof. API14 PASS/12 FAIL; 6 UI cases chưa chạy. Năm bug groups: equality minimum, percent formula, equality expiry, JWT missing/invalid/expired và client identity bypass.

## C — Admin coupon management

[Domain/BVA analysis](reports/C-FR17-domain.md), [test cases](tests/C-FR17-coupon-management.md), [raw evidence](evidence/execution/C-api.md), [review/gaps](reports/C-FR17-review.md).

Presence/uniqueness/enum/numeric/auth domains; boundary value0, minimum0, usage1 và lân cận. Scope create/view/delete; không tự gọi thiếu Update là bug. API14 PASS/16 FAIL; 6 UI cases chưa chạy. Tám bug groups: mandatory, enum, discount, minimum, usage và create/list/delete role control. Duplicate returns500 nhưng uniqueness vẫn đạt; không biến unspecified HTTP status thành bug.

## D — Mobile productDetail

[Domain/BVA analysis](reports/D-mobile-domain.md), [test cases](tests/D-mobile-product-detail.md), [support API evidence](evidence/execution/D-api.md), [review/gaps](reports/D-mobile-review.md).

Quantity integer≥1: boundary0/1/2; missing/fraction/text là domain riêng. Data display và Add feedback/cart postcondition kiểm tra bằng UI. Mapping FR-20 với FR-06/07 được ghi rõ để review. Chỉ2 API PASS và1 API OBSERVATION; cả14 Mobile cases NOT RUN. Chưa xác minh bug Mobile.

## Results and bug reports

Snapshot ban đầu: 114 designed; 81 executed = 37 PASS + 42 FAIL + 2 OBSERVATION; 33 NOT RUN. [Test summary](reports/test-summary.md) là bảng cập nhật từ execution records; snapshot đoạn này phải cập nhật nếu chạy thêm manual. Có15 API verified bug groups, không đồng nhất42 failed cases với42 bugs. [Bug index](bugs/bug-reports.md) dẫn reproduction, expected/actual và raw records cho từng nhóm. Screenshots và Issue URLs còn chờ.

## AI usage and critique

OpenAI Codex hỗ trợ phân tích, thiết kế, scripts và báo cáo. [AI Audit](ai-audit/) giữ tên template; transcript snapshot và technical review tách khỏi human review chưa có. AI Critique200–300 từ nằm trong AI-04, là draft chờ sinh viên sửa/xác nhận; không coi model tự review là đã hoàn tất yêu cầu human review.

## Agent Skill

[Skill](.agents/skills/domain-bva-testing/SKILL.md) và [demonstration record](reports/skill-demonstration.md) mô tả cách tái áp dụng. [Video plan](evidence/video-links.md) là kịch bản, chưa phải video đã quay. Không tự cho điểm tối đa10 khi video chưa có.

## Remaining work and final format

[Manual handoff](reports/manual-handoff.md) nêu từng TC, dữ liệu, expected, điểm chụp và tên file. Sinh viên chạy UI/Mobile, chụp thật, review cá nhân/Critique/self-assessment và quay video. Nhóm Issues làm cuối. Sau khi cập nhật Markdown, sinh viên tự xuất PDF/định dạng cuối, đóng ZIP đúng tên và nộp Moodle. Bài chưa đủ điều kiện nộp ở trạng thái hiện tại.

## Disclosure

Phiên bản đầu của các bảng test, scripts và báo cáo được soạn với OpenAI Codex. Các sửa đổi kỹ thuật của Codex được ghi trong audit/review; phần sinh viên tự kiểm chứng, bổ sung và ký xác nhận hiện đang chờ. Không có screenshots, video, signatures hoặc human verdict được tạo thay sinh viên.

````

</details>


## Appendix C — Current rewrite output manifest

Snapshot UTC: `2026-10-19T20:10:22.349219+00:00`. Git revision trước khi commit audit này: `575a342c51bc3446e36c26a7a3887fe5f3319641`. Các file hiện tại là output của lượt rewrite; Git giữ bản cụ thể để phân biệt chỉnh sửa về sau. Prompt/output messages được liên kết trong Appendix A; không tạo output hoặc timestamp model giả.

| Artifact output | SHA-256 current source bytes |
|---|---|
| [.agents/skills/domain-bva-testing/SKILL.md](../.agents/skills/domain-bva-testing/SKILL.md) | 61cd724844f7cc154822b20c0ad47d55428278e3629fc3444047e967a6808368 |
| [23120262_Report.md](../23120262_Report.md) | 6c296c6b35166626c7447ce489c673fae3db551b89920d43ad2ec206ff651e23 |
| [bugs/BUG-A01.md](../bugs/BUG-A01.md) | caee6c5cae18c9f39ac689fcbfda544af43393c367e8706a876b2e437a9608e8 |
| [bugs/BUG-A02.md](../bugs/BUG-A02.md) | 3770202e435c24c745cc3440e7ba6e8c55b96bc0835c52743b49b23d76f2d717 |
| [bugs/BUG-A03.md](../bugs/BUG-A03.md) | fe501487b3a57ddc42fede98477cf2bb092e1ad93e455d1a758ffdc6d0483286 |
| [bugs/BUG-B01.md](../bugs/BUG-B01.md) | 9152cb7874587998a9848a10d0f324c883edf8697540b15b9f9cc8bbb96c64a8 |
| [bugs/BUG-B02.md](../bugs/BUG-B02.md) | dbb68b166e6864d023cdb66658197d9a9571ad04d2040e433f032e8120514cc4 |
| [bugs/BUG-B03.md](../bugs/BUG-B03.md) | 221fe89097a719a76c3512c5245cb541a28693f5787cb60a2a40029ac406a6bd |
| [bugs/BUG-B04.md](../bugs/BUG-B04.md) | 057fee79c0e802a11c004844f713855d2bbb2d7cacecd6241d577aee95181d50 |
| [bugs/BUG-B05.md](../bugs/BUG-B05.md) | a476d38a93650dae1584338ce212b13c5cc88f72684be02e75d44e5bcaab8896 |
| [bugs/BUG-C01.md](../bugs/BUG-C01.md) | d5689ff122a0c8e429e73a724b9a48c84e4157f64eb6d0b44ac000465e53f930 |
| [bugs/BUG-C03.md](../bugs/BUG-C03.md) | 2d7c16c28c36703ff4eb2331db0aef9a95a100653b89f907af630b5509757ec3 |
| [bugs/BUG-C04.md](../bugs/BUG-C04.md) | 09b9f96f8b9caeb9b80725ec6f1ccef8964b1c09113f6dc28bf381f697ab6420 |
| [bugs/BUG-C05.md](../bugs/BUG-C05.md) | f8256b7709db33d1746967234ae4f16d2c01833d8f17a5eb9268c4b7ab0d6151 |
| [bugs/BUG-C06.md](../bugs/BUG-C06.md) | b1d7f4b9eecf7e4a324f1532dbfbdade67df3b10b12595ab8d97cd0465f9c949 |
| [bugs/BUG-C07.md](../bugs/BUG-C07.md) | 5691c248bbee5e81ed1368e79809ba7c4d7f6dbafefb2a04aa34fc22f7596ac0 |
| [bugs/BUG-C08.md](../bugs/BUG-C08.md) | 09af0be64ffed96b2bf812f369c82b081a93a04af54779458c391eb5eb38ef74 |
| [bugs/BUG-C09.md](../bugs/BUG-C09.md) | 56628da40f8b33e9d192e5142641d331230f19d79b38664342ca40863546b6b5 |
| [bugs/BUG-D01.md](../bugs/BUG-D01.md) | 270ecb703e29157d82d4cba181e851751ba365e4effc1af75b722eed6de6c93d |
| [bugs/BUG-D02.md](../bugs/BUG-D02.md) | 64d3f68f5254e89d2dc988627eec589a553f842cee62494cd43f7ae20a7adb02 |
| [bugs/bug-reports.md](../bugs/bug-reports.md) | 3e165ae9424acdf3884dbc6d851dd631c005e3786b3ad9cdab7cc6608c51f5ea |
| [evidence/execution/A-api.md](../evidence/execution/A-api.md) | 12e950603f397b64e2dd5c2502570397ccb0fd45ba43bb8403797873b64a575b |
| [evidence/execution/B-api.md](../evidence/execution/B-api.md) | 430607fbbf0eb7e189028cd9ace9ff8a324d4c8f7a72417d944e52f7f287a38c |
| [evidence/execution/C-api.md](../evidence/execution/C-api.md) | 615a2b8e9209f27c009c6c3a9da4d45fc5b28d8dea58ab76f7915b8663978f97 |
| [evidence/execution/D-api.md](../evidence/execution/D-api.md) | f66dbf18b3d52d89f3908156faf90b4f74f0aaf8f74f8c580370d96b658424cf |
| [evidence/README.md](../evidence/README.md) | 8e84fb71c193bb0e56f1ab321090cf7d1e50f19b3e1eb7cb9f70adb055592b6e |
| [README.md](../README.md) | 56e7ca5530c43eb6a8c253ba4e76826c14d02e40a5280a250d8500891b8351dd |
| [reports/A-FR04-domain.md](../reports/A-FR04-domain.md) | 7b7d670491209e7695c900fd928e60377aa245ba7ce8f13a20303f2b4604677d |
| [reports/B-FR09-domain.md](../reports/B-FR09-domain.md) | 9ec56b05e4c61f45d8e92242bd580a83c06fbf10eccd393f64f40a169dff80f6 |
| [reports/C-FR17-domain.md](../reports/C-FR17-domain.md) | 7ce076dc00c71ae709d5bd603af7b4ff607269168bb4be1648197e65d2171fca |
| [reports/D-mobile-domain.md](../reports/D-mobile-domain.md) | 63d6886f24ccd93b5df531b7bd45ca37d18b6b4383651a3019a281ea8a01891b |
| [scripts/cases.cjs](../scripts/cases.cjs) | bf47927bbcf4a153a73f38f89a10afb4621365edad931d2d1a991dbbd9e30c26 |
| [scripts/export-git-log.cjs](../scripts/export-git-log.cjs) | e7fc12c2f9e77d5b9926351289f36c3695b5c41c619f581fd479c4f4dd135492 |
| [scripts/run-api.cjs](../scripts/run-api.cjs) | f0c5fd2d79200bc257576a42b502ac80fce6c1378873dd776f023abdb1ecac8c |
| [scripts/runtime.cjs](../scripts/runtime.cjs) | 85968c9839e86387e47716e7892c4cfee1dd724906aa4f26211fc1efdf31e5c6 |
| [scripts/show-bug.cjs](../scripts/show-bug.cjs) | d7af1132dc0aacaaced8f2d03edbb6934965d37a05bf0ef698a1229c9ebcee23 |
| [scripts/validate-deliverables.py](../scripts/validate-deliverables.py) | 97e5ff917d9e7fc925eab99e755cb067ed537360e1bd7dc18ba9c46d45826c2d |
| [tests/A-FR04-profile.md](../tests/A-FR04-profile.md) | cf6e92d212e32d050aea5a8fb97dc820ef28d2fb0ee344dfa11c90ca249b8ec0 |
| [tests/B-FR09-discount-coupons.md](../tests/B-FR09-discount-coupons.md) | afbdc19853f4723f7507211f4576bebbaa82efcbb83cea05efee4ee526b767ac |
| [tests/C-FR17-coupon-management.md](../tests/C-FR17-coupon-management.md) | 859a340fe67a8791b1077de44a71f58656a2a369b7e85b1e82e4ef688a3227f6 |
| [tests/D-mobile-product-detail.md](../tests/D-mobile-product-detail.md) | 10e01bdc6b3549e7ca2674b68c8d610249dfd2af4a104e65537ece451571ac9d |
| [Video_Links.md](../Video_Links.md) | a368e67977bf5f9f007527e82caf453f04ecc6a2c8d284ee8cba395fb1b8cd84 |
