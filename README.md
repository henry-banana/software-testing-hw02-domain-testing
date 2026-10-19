# CSC13003 — HW02: Domain Testing on EShop

Repository chứa báo cáo cá nhân, phân tích Domain/BVA, test cases, bug reports, evidence và AI audit của **HW02-AI**.

| Thông tin | Giá trị |
|---|---|
| Sinh viên | Tống Dương Thái Hòa |
| MSSV | 23120262 |
| Lớp | Software Testing — CQ2023/3 |
| SUT baseline | 85af3ba875c88283615e22cb108f13e2fccaf0e9 |
| Features | A FR-04; B FR-09; C FR-17 Create/View/Delete; D Mobile productDetail |

## Test Summary

| Scope | Designed | Executed đủ bằng chứng | PASS | FAIL | OBSERVATION | INCOMPLETE | NOT RUN |
|---|---|---|---|---|---|---|---|
| A — API | 22 | 22 | 7 | 14 | 1 | 0 | 0 |
| A — UI | 7 | 6 | 3 | 3 | 0 | 1 | 0 |
| B — API | 26 | 26 | 14 | 12 | 0 | 0 | 0 |
| B — UI | 6 | 5 | 3 | 2 | 0 | 1 | 0 |
| C — API | 30 | 30 | 14 | 16 | 0 | 0 | 0 |
| C — UI | 6 | 4 | 2 | 2 | 0 | 2 | 0 |
| D — API | 3 | 3 | 2 | 0 | 1 | 0 | 0 |
| D — UI | 14 | 13 | 4 | 7 | 2 | 1 | 0 |
| **Tổng** | 114 | 109 | 49 | 56 | 4 | 5 | 0 |

18 bug groups, 68 ảnh. 15 API bug groups; 3 UI-only groups. Observations không phải bugs; INCOMPLETE không được cộng executed đủ bằng chứng. Group Issues chưa đăng; phần nhóm thực hiện cuối.

## Danh mục artifact

| Artifact | Nội dung |
|---|---|
| [23120262_Report.md](23120262_Report.md) | Báo cáo chính có đầy đủ phân tích Domain/BVA bốn feature, results, AI gaps và requirement audit. |
| [reports/](reports/) | Bốn phân tích feature có domain/biên/traceability và kết quả. |
| [tests/](tests/) | 114 TC chi tiết: fixture, input, steps, expected, actual, evidence, verdict. |
| [Bug Report](bugs/bug-reports.md) | 18 bug files riêng, mỗi bug có exact reproduction, impact và screenshot status. |
| [Evidence Register](evidence/README.md) | Raw HTTP, source checksums và68ảnh có provenance. |
| [Prompt Log](Appendix_A_Prompt_Log.md) | Prompt/output messages nguyên văn với timestamp nguồn. |
| [AI Audit](<ai-audit/[AI-02] - FIT@HCMUS - AI Audit Report_Vn.md>) | Technical verdict, corrections và original AI artifact snapshots. |
| [AI Disclosure](<ai-audit/[AI-03] - FIT@HCMUS - AI Disclosure Form_Vn.md>) | Công cụ, phạm vi đóng góp và xác nhận do sinh viên cung cấp. |
| [AI Reflection](<ai-audit/[AI-04] - FIT@HCMUS - AI Reflective Statement_Vn.md>) | Reflection và AI Critique245 từ. |
| [AI Privacy](<ai-audit/[AI-05] - FIT@HCMUS - AI Privacy Checklist_Vn.md>) | Checklist theo evidence và bước cuối còn lại. |
| [Agent Skill](.agents/skills/domain-bva-testing/SKILL.md) | Workflow tái sử dụng với FR-17 làm example. |
| [Video Links](Video_Links.md) | Link tạm demo, chờ sinh viên thay URL. |
| [Git Log](git-commit-log.txt) | Snapshot lịch sử Git thực, ghi rõ HEAD phạm vi. |
| [API runner](scripts/run-api.cjs) | Harness reset/isolation,81public HTTP cases; dependencies từ SUT. |

## Tái chạy API

Cần Node và dependencies của baseline EShop đã cài tại `../eshop-sut/backend/node_modules` (hoặc đặt `HW02_SUT` đến checkout tương ứng). Kiểm tra SUT đang ở SHA trên. Không chạy file database.js gốc để dựng harness vì file này drop/seed. Runner tạo bản copy và database riêng, dùng port3100; nếu port bận, runner từ chối thay vì dùng server khác.

```powershell
node scripts/run-api.cjs A
node scripts/run-api.cjs B
node scripts/run-api.cjs C
node scripts/run-api.cjs D
python scripts/validate-deliverables.py
```

Suite có expected theo SRS nên các FAIL là SUT defects đã ghi, không phải lý do đổi expected theo implementation. Exit2 dành cho BLOCKED, lỗi harness hoặc source bị thay đổi. Mỗi lần chạy ghi lại raw evidence với timestamp mới; giữ Git snapshot nếu muốn so sánh run trước.

## Self-Assessment

Điểm đề xuất để sinh viên duyệt; chưa phải điểm giảng viên hoặc xác nhận hồ sơ nộp hoàn tất.

| No. | Criteria | Maximum | Self-Assessed Grade (draft) | Giải trình |
|---|---|---|---|---|
| 1 | Feature A — Domain + Boundary | 25 | 22 | 11 domain groups; đủ biên9/10/11/12 và role/ownership; A-UI-07 còn thiếu persistence evidence. |
| 2 | Feature B — Domain + Boundary | 25 | 22 | Decision table C1–C5; money/expiry/usage boundaries; B-UI-06 chưa chứng minh exhausted usage. |
| 3 | Feature C — Domain + Boundary | 25 | 22 | Required/enum/numeric và từng operation role; C-UI-02 thiếu reload, C-UI-06 thiếu after-delete. |
| 4 | Feature D — Mobile, Domain + Boundary | 15 | 12 | Có ảnh native quantity/detail/feedback; mapping được công khai; D-UI-12 thiếu sequence; exploratory limits giữ rõ. |
| 5 | Agent Skills | 10 | 8 | Có skill và ví dụ xuyên suốt; video đang quay, link tạm chưa được xác nhận truy cập. |
|  | Total | 100 | 86 | Video/Issues/PDF/ZIP và evidence thiếu cần hoàn tất trước submission. |

## Video Demo

[Video end-to-end — URL tạm](https://www.youtube.com/watch?v=HW02_TEMP_ID). Sinh viên đang quay và sẽ thay link; chưa xác nhận URL truy cập được.

## Các yêu cầu còn thiếu

| Yêu cầu đề | Artifact / bằng chứng | Trạng thái hiện tại |
|---|---|---|
| §5: 4 features, 1/pool, không trùng | Scope A/B/C/D; phân công đã được xác nhận | Đạt phạm vi đã chọn |
| §6.1: Domain Testing từng bước | Main report §3–6 + reports/*-domain.md | Có vector/partition/representatives/cross-constraints/TC mapping |
| §6.2: BVA từng bước | Bảng biến/rule/delta/biên/neighbors cho cả4 feature | Có; lecture chưa có để đối chiếu quy ước lớp |
| §6: Comprehensive execution/evidence | 114 designed; 81 API tái chạy; 33 UI IDs gắn ảnh | Còn5 TC INCOMPLETE; không claim114 executed |
| §6.3: AI gap analysis và nguyên nhân | Mỗi feature có gap/evidence/cause/correction | Có technical review; sinh viên đọc lại bản viết mới |
| §6.4/§14: Markdown bugs + group Issues + screenshot | 18 files bugs/; raw API và ảnh UI | Markdown có; chưa đăng Issue/ảnh trang Issue; API-only bugs thiếu ảnh terminal |
| §7: Skill + video end-to-end | .agents/skills/domain-bva-testing/SKILL.md; Video_Links.md | Skill có; video đang quay, link tạm theo yêu cầu |
| §9: AI tool/date-time/prompt/output | AI-02 + Appendix_A_Prompt_Log.md; nguồn timestamp thực | Có log/snapshot; final response sau snapshot chưa nằm trong export |
| §10: AI Critique200–300 words | AI-04 và main report §9 | 245 từ đếm whitespace; giữ đoạn sinh viên đã cung cấp |
| §2: Human review/AI-first | Stepwise workflow và correction tables; declaration | Bản trước đã có xác nhận; bản viết lại cần sinh viên đọc lại, không ký thay |
| §12: Git commits từng bước + log | Git history thực của lượt viết lại; git-commit-log.txt | Ghi commits hiện tại theo bước; không phục dựng23commits từ log cũ |
| §14: README summary/self-assessment | README + main report §2/10 | Có; self-assessment là draft chờ sinh viên duyệt |
| §14/Policies: Markdown+PDF và ZIP đúng tên | Markdown sources đầy đủ; 23120262_HW02_AI_DomainTesting_<grade>.zip | PDF/ZIP và điểm cuối do sinh viên thực hiện |
| §13: Vấn đáp5–7phút nếu được chọn | SRS→domain→boundary→actual→bug có truy vết | Sinh viên tự chuẩn bị; chưa xác nhận đã diễn tập |

README/report/tests cùng dùng một tập TC-ID; không cộng số ảnh thành số test. TASKS và ghi chú điều phối nằm ngoài repository nộp bài.
