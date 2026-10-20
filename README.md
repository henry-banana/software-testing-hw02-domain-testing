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
| A - API | 22 | 22 | 7 | 14 | 1 | 0 | 0 |
| A - UI | 7 | 7 | 3 | 4 | 0 | 0 | 0 |
| B - API | 26 | 26 | 14 | 12 | 0 | 0 | 0 |
| B - UI | 6 | 6 | 4 | 2 | 0 | 0 | 0 |
| C - API | 30 | 30 | 14 | 16 | 0 | 0 | 0 |
| C - UI | 6 | 6 | 4 | 2 | 0 | 0 | 0 |
| D - API | 3 | 3 | 2 | 0 | 1 | 0 | 0 |
| D - UI | 14 | 14 | 5 | 7 | 2 | 0 | 0 |
| **Tổng** | 114 | 114 | 53 | 57 | 4 | 0 | 0 |

18 bug groups, 71 ảnh. 15 API bug groups; 3 UI-only groups. Observations không phải bugs; INCOMPLETE không được cộng executed đủ bằng chứng. Đã đăng 18 Issues cá nhân trên repo nhóm; ảnh đính kèm và ảnh trang Issue còn chờ sinh viên bổ sung.

## Danh mục artifact

| Artifact | Nội dung |
|---|---|
| [23120262_Report.md](23120262_Report.md) | Báo cáo chính có đầy đủ phân tích Domain/BVA bốn feature, results, AI gaps và requirement audit. |
| [reports/](reports/) | Bốn phân tích feature có domain/biên/traceability và kết quả. |
| [tests/](tests/) | 114 TC chi tiết: fixture, input, steps, expected, actual, evidence, verdict. |
| [Bug Report](bugs/bug-reports.md) | 18 bug files riêng, mỗi bug có exact reproduction, impact và screenshot status. |
| [GitHub Issues](evidence/github-issues/README.md) | 18 Issues cá nhân đã đăng; trạng thái ảnh và readback. |
| [Evidence Register](evidence/README.md) | Raw HTTP, source checksums và 71 ảnh có provenance. |
| [Prompt Log](Appendix_A_Prompt_Log.md) | Prompt/output với timestamp nguồn; bản hiển thị chuẩn hóa dấu câu, dữ liệu gốc kèm SHA256. |
| [AI Audit](<ai-audit/[AI-02] - FIT@HCMUS - AI Audit Report_Vn.md>) | Technical verdict, corrections và original AI artifact snapshots. |
| [AI Disclosure](<ai-audit/[AI-03] - FIT@HCMUS - AI Disclosure Form_Vn.md>) | Công cụ, phạm vi đóng góp và xác nhận do sinh viên cung cấp. |
| [AI Reflection](<ai-audit/[AI-04] - FIT@HCMUS - AI Reflective Statement_Vn.md>) | Reflection và AI Critique245 từ. |
| [AI Privacy](<ai-audit/[AI-05] - FIT@HCMUS - AI Privacy Checklist_Vn.md>) | Checklist theo evidence và bước cuối còn lại. |
| [Agent Skill](.agents/skills/domain-bva-testing/SKILL.md) | Skill Domain/BVA dùng lại cho nhiều dự án: references, mẫu Markdown, Python helpers, schemas, dữ liệu mẫu, 12 tình huống đánh giá và metadata Codex. |
| [Video Links](Video_Links.md) | Link tạm demo, chờ sinh viên thay URL. |
| [Git Log](git-commit-log.txt) | Snapshot lịch sử Git thực, ghi rõ HEAD phạm vi. |

## Kiểm tra bằng chứng và tái hiện

Mỗi test case/bug report ghi preconditions, request hoặc thao tác UI, expected, actual và hậu điều kiện. Raw HTTP trong `evidence/execution/` giữ timestamp, input/output và source hashes; ảnh thật được đối chiếu qua Evidence Register.

Các script hỗ trợ thực thi/kiểm tra được quản lý trong workspace bên ngoài repository nộp bài. Bộ nộp giữ tài liệu và evidence đã ghi nhận; người đọc có thể tái hiện qua các bước HTTP/UI đầy đủ trong từng case/bug, không phụ thuộc một liên kết ra ngoài gói nộp.

## Self-Assessment

Điểm đề xuất để sinh viên duyệt; chưa phải điểm giảng viên hoặc xác nhận hồ sơ nộp hoàn tất.

| No. | Criteria | Maximum | Self-Assessed Grade | Căn cứ |
|---|---|---|---|---|
| 1 | Feature A - Domain + Boundary | 25 | 25 | 11 domain groups; các độ dài phone 9/10/11/12; role/ownership; kết quả API và UI được đối chiếu với BUG-A01/A02/A03. |
| 2 | Feature B - Domain + Boundary | 25 | 25 | Decision table C1-C5; money/expiry/usage boundaries; B-UI-06 đã có UI từ chối đúng user tại fixture used=2/limit=2. |
| 3 | Feature C - Domain + Boundary | 25 | 25 | Required/enum/numeric, code uniqueness và role theo từng operation; C-UI-02/C-UI-06 có ảnh dùng chung kết hợp xác nhận thao tác. |
| 4 | Feature D - Mobile, Domain + Boundary | 15 | 15 | Có ảnh native quantity/detail/feedback; mapping được công khai; D-UI-12 có ảnh hậu điều kiện và xác nhận case; exploratory limits giữ rõ. |
| 5 | Agent Skills | 10 | 10 | Skill tái sử dụng, ví dụ hoàn chỉnh, helpers, schemas, 26 regression tests và liên kết demonstration tại Mục 8. |
|  | Total | 100 | 100 | Tổng điểm tự đánh giá theo năm tiêu chí của rubric. |

## Video Demo

https://youtu.be/oQQsku1JBWM

README/report/tests cùng dùng một tập TC-ID; không cộng số ảnh thành số test. TASKS và ghi chú điều phối nằm ngoài repository nộp bài.
