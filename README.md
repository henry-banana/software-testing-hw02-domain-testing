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
| [Agent Skill](.agents/skills/domain-bva-testing/SKILL.md) | Domain/BVA tám bước, guides theo ngữ cảnh, mẫu đầu ra, ví dụ FR-17 và10tình huống đánh giá. |
| [Video Links](Video_Links.md) | Link tạm demo, chờ sinh viên thay URL. |
| [Git Log](git-commit-log.txt) | Snapshot lịch sử Git thực, ghi rõ HEAD phạm vi. |

## Kiểm tra bằng chứng và tái hiện

Mỗi test case/bug report ghi preconditions, request hoặc thao tác UI, expected, actual và hậu điều kiện. Raw HTTP trong `evidence/execution/` giữ timestamp, input/output và source hashes; ảnh thật được đối chiếu qua Evidence Register.

Các script hỗ trợ thực thi/kiểm tra được quản lý trong workspace bên ngoài repository nộp bài. Bộ nộp giữ tài liệu và evidence đã ghi nhận; người đọc có thể tái hiện qua các bước HTTP/UI đầy đủ trong từng case/bug, không phụ thuộc một liên kết ra ngoài gói nộp.

## Self-Assessment

Điểm đề xuất để sinh viên duyệt; chưa phải điểm giảng viên hoặc xác nhận hồ sơ nộp hoàn tất.

| No. | Criteria | Maximum | Self-Assessed Grade (draft) | Giải trình |
|---|---|---|---|---|
| 1 | Feature A - Domain + Boundary | 25 | 22 | 11 domain groups; đủ biên9/10/11/12 và role/ownership; A-UI-07 đã có input hợp lệ và lỗi chặn BUG-A03; persistence cần regression sau sửa. |
| 2 | Feature B - Domain + Boundary | 25 | 22 | Decision table C1-C5; money/expiry/usage boundaries; B-UI-06 đã có UI từ chối đúng user tại fixture used=2/limit=2. |
| 3 | Feature C - Domain + Boundary | 25 | 22 | Required/enum/numeric và từng operation role; C-UI-02/C-UI-06 đã có ảnh dùng chung và xác nhận của sinh viên. |
| 4 | Feature D - Mobile, Domain + Boundary | 15 | 12 | Có ảnh native quantity/detail/feedback; mapping được công khai; D-UI-12 có ảnh hậu điều kiện và xác nhận case; exploratory limits giữ rõ. |
| 5 | Agent Skills | 10 | 8 | Có skill và ví dụ xuyên suốt; video đang quay, link tạm chưa được xác nhận truy cập. |
|  | Total | 100 | 86 | Còn ảnh Issues, video URL thật, human review và PDF/ZIP trước khi nộp. |

## Video Demo

[Video end-to-end - URL tạm](https://www.youtube.com/watch?v=HW02_TEMP_ID). Sinh viên đang quay và sẽ thay link; chưa xác nhận URL truy cập được.

## Các yêu cầu còn thiếu

| Yêu cầu đề | Artifact / bằng chứng | Trạng thái hiện tại |
|---|---|---|
| mục 5: 4 features, 1/pool, không trùng | Scope A/B/C/D; phân công đã được xác nhận | Đạt phạm vi đã chọn |
| mục 6.1: Domain Testing từng bước | Main report mục 3-6 + reports/*-domain.md | Có vector/partition/representatives/cross-constraints/TC mapping |
| mục 6.2: BVA từng bước | Bảng biến/rule/delta/biên/neighbors cho cả4 feature | Có; lecture chưa có để đối chiếu quy ước lớp |
| mục 6: Comprehensive execution/evidence | 114 designed; 81 API tái chạy; 33 UI IDs gắn ảnh | 114 executed đủ evidence: 53 PASS / 57 FAIL / 4 OBSERVATION; 0 INCOMPLETE |
| mục 6.3: AI gap analysis và nguyên nhân | Mỗi feature có gap/evidence/cause/correction | Có technical review; sinh viên đọc lại bản viết mới |
| mục 6.4/mục 14: Markdown bugs + group Issues + screenshot | 18 files bugs/; raw API và ảnh UI | Đã có18Markdown bug reports và18 Issues (#31-#48); còn ảnh đính kèm/ảnh trang Issue và ảnh terminal cho11 API-only bugs |
| mục 7: Skill + video end-to-end | .agents/skills/domain-bva-testing/SKILL.md; Video_Links.md | Skill có; video đang quay, link tạm theo yêu cầu |
| mục 9: AI tool/date-time/prompt/output | AI-02 + Appendix_A_Prompt_Log.md; nguồn timestamp thực | Có log/snapshot; final response sau snapshot chưa nằm trong export |
| mục 10: AI Critique200-300 words | AI-04 và main report mục 9 | 245 từ đếm whitespace; giữ đoạn sinh viên đã cung cấp |
| mục 2: Human review/AI-first | Stepwise workflow và correction tables; declaration | Bản trước đã có xác nhận; bản viết lại cần sinh viên đọc lại, không ký thay |
| mục 12: Git commits từng bước + log | Git history thực của lượt viết lại; git-commit-log.txt | Ghi commits hiện tại theo bước; không phục dựng23commits từ log cũ |
| mục 14: README summary/self-assessment | README + main report mục 2/10 | Có; self-assessment là draft chờ sinh viên duyệt |
| mục 14/Policies: Markdown+PDF và ZIP đúng tên | Markdown sources đầy đủ; 23120262_HW02_AI_DomainTesting_<grade>.zip | PDF/ZIP và điểm cuối do sinh viên thực hiện |
| mục 13: Vấn đáp5-7phút nếu được chọn | SRS->domain->boundary->actual->bug có truy vết | Sinh viên tự chuẩn bị; chưa xác nhận đã diễn tập |

README/report/tests cùng dùng một tập TC-ID; không cộng số ảnh thành số test. TASKS và ghi chú điều phối nằm ngoài repository nộp bài.
