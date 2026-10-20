# CSC13003 - HW02: Domain Testing on EShop

Repository chứa báo cáo cá nhân, phân tích Domain/BVA, test cases, bug reports, evidence và AI audit của **HW02-AI**.

| Thông tin | Giá trị |
|---|---|
| Sinh viên | Tống Dương Thái Hòa |
| MSSV | 23120262 |
| Lớp | Software Testing - CQ2023/3 |
| SUT baseline | 85af3ba875c88283615e22cb108f13e2fccaf0e9 |
| Features | A FR-04; B FR-09; C FR-17 Create/View/Delete; D Mobile productDetail |

## Test Summary

| Scope | Designed | Executed đủ bằng chứng | PASS | FAIL | OBSERVATION | INCOMPLETE | NOT RUN |
|---|---|---|---|---|---|---|---|
| A - API | 29 | 29 | 8 | 18 | 3 | 0 | 0 |
| A - UI | 10 | 10 | 3 | 7 | 0 | 0 | 0 |
| A - HND | 5 | 5 | 2 | 3 | 0 | 0 | 0 |
| B - API | 26 | 26 | 14 | 12 | 0 | 0 | 0 |
| B - UI | 7 | 7 | 4 | 3 | 0 | 0 | 0 |
| C - API | 30 | 30 | 14 | 16 | 0 | 0 | 0 |
| C - UI | 7 | 7 | 4 | 3 | 0 | 0 | 0 |
| D - API | 3 | 3 | 2 | 0 | 1 | 0 | 0 |
| D - UI | 15 | 15 | 5 | 8 | 2 | 0 | 0 |
| **Tổng** | 132 | 132 | 56 | 70 | 6 | 0 | 0 |

Bộ kiểm thử gồm **132 TC: 88 API, 39 UI/evidence criteria và 5 Mobile source-handler checks**, với **56 PASS, 70 FAIL, 6 OBSERVATION**. Có **64 điều kiện lỗi** và **125 ảnh kiểm thử**. Trong 39 UI criteria, D-UI-15 là kiểm tra màu nút trên ảnh native gốc, không phải lượt thao tác native mới. Năm HND cases chạy handler nguyên bản với adapter Alert/HTTP, không được tính là native UI. 81 API cases cũ đã chạy lại và giữ nguyên kết quả; 18 cases mở rộng có record riêng. Số ảnh không được dùng thay số test.

## Danh mục artifact

| Artifact | Nội dung |
|---|---|
| [23120262_Report.md](23120262_Report.md) | Báo cáo chính có đầy đủ phân tích Domain/BVA bốn feature, results, AI gaps và requirement audit. |
| [reports/](reports/) | Bốn phân tích feature có domain/biên/traceability và kết quả. |
| [tests/](tests/) | 132 TC chi tiết: fixture, input, steps, expected, actual, evidence, verdict. |
| [Bug Report](bugs/bug-reports.md) | 64 bug files riêng, mỗi điều kiện có reproduction, impact, ảnh và Issue đã đăng. |
| [GitHub Issues](evidence/github-issues/README.md) | 64 Issues cá nhân, ảnh bug đính kèm và ảnh trang Issue có readback. |
| [Evidence Register](evidence/README.md) | Raw HTTP, source checksums và 125 ảnh kiểm thử có provenance. |
| [Prompt Log](Appendix_A_Prompt_Log.md) | Log kỹ thuật chọn lọc, timestamp và digest nguồn; công bố redaction. |
| [AI Audit](<ai-audit/[AI-02] - FIT@HCMUS - AI Audit Report_Vn.md>) | Verdict theo artifact, output trích dẫn và bản sửa. |
| [AI Disclosure](<ai-audit/[AI-03] - FIT@HCMUS - AI Disclosure Form_Vn.md>) | Công cụ, phạm vi đóng góp và xác nhận do sinh viên cung cấp. |
| [AI Reflection](<ai-audit/[AI-04] - FIT@HCMUS - AI Reflective Statement_Vn.md>) | Reflection và AI Critique245 từ. |
| [AI Privacy](<ai-audit/[AI-05] - FIT@HCMUS - AI Privacy Checklist_Vn.md>) | Checklist đã điền, ghi rõ mục không áp dụng và phạm vi dữ liệu. |
| [Agent Skill](.agents/skills/domain-bva-testing/SKILL.md) | Skill Domain/BVA dùng lại cho nhiều dự án: references, mẫu Markdown, Python helpers, schemas, dữ liệu mẫu, 12 tình huống đánh giá và metadata Codex. |
| [Video Links](Video_Links.md) | Video FR-04 và liên kết artifact đồng bộ. |
| [Git Log](git-commit-log.txt) | Snapshot lịch sử Git thực, ghi rõ HEAD phạm vi. |

## Kiểm tra bằng chứng và tái hiện

Mỗi test case/bug report ghi preconditions, request hoặc thao tác UI, expected, actual và hậu điều kiện. Raw HTTP trong `evidence/execution/` giữ timestamp, input/output và source hashes; ảnh thật được đối chiếu qua Evidence Register.

Các script hỗ trợ thực thi/kiểm tra được quản lý trong workspace bên ngoài repository nộp bài. Bộ nộp giữ tài liệu và evidence đã ghi nhận; người đọc có thể tái hiện qua các bước HTTP/UI đầy đủ trong từng case/bug, không phụ thuộc một liên kết ra ngoài gói nộp.

## Self-Assessment

Bảng tự đánh giá theo rubric của đề bài.

| No. | Criteria | Maximum | Self-Assessed Grade | Căn cứ |
|---|---|---|---|---|
| 1 | Feature A - Domain + Boundary | 25 | 25 | 18 domain groups; các độ dài phone 9/10/11/12; role/ownership; kết quả API và UI được đối chiếu với FR04-01 tới FR04-27. |
| 2 | Feature B - Domain + Boundary | 25 | 25 | Decision table C1-C5; money/expiry/usage boundaries; B-UI-06 đã có UI từ chối đúng user tại fixture used=2/limit=2. |
| 3 | Feature C - Domain + Boundary | 25 | 25 | Required/enum/numeric, code uniqueness và role theo từng operation; C-UI-02/C-UI-06 có ảnh dùng chung kết hợp xác nhận thao tác. |
| 4 | Feature D - Mobile, Domain + Boundary | 15 | 15 | Có ảnh native quantity/detail/feedback; mapping được công khai; D-UI-12 có ảnh hậu điều kiện và xác nhận case; exploratory limits giữ rõ. |
| 5 | Agent Skills | 10 | 10 | Skill tái sử dụng, ví dụ hoàn chỉnh, helpers, schemas, 26 regression tests và liên kết demonstration tại Mục 8. |
|  | Total | 100 | 100 | Tổng điểm tự đánh giá theo năm tiêu chí của rubric. |

## Video Demo

https://youtu.be/oQQsku1JBWM

Bản PDF báo cáo chính và bốn biểu mẫu AI được xuất từ Markdown tương ứng. README/report/tests cùng dùng một tập TC-ID; không cộng số ảnh thành số test. TASKS và ghi chú điều phối nằm ngoài repository nộp bài.
