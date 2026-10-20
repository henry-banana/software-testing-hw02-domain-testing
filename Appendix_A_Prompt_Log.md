# Appendix A - Prompt and Output Log

Bản hiển thị chuẩn hóa dấu câu theo yêu cầu trình bày; nội dung nguyên văn và SHA-256 được bảo toàn trong [source-records.json](evidence/ai-originals/source-records.json).

Snapshot UTC: `2026-10-19T20:10:22.349219+00:00`. Nguồn là visible user/assistant message records của đúng các phiên HW02; không export reasoning, system/developer messages hoặc tool payloads. Những lượt retry/fork được giữ với tên source, không coi là các thí nghiệm độc lập. Tool của các interaction được export là OpenAI Codex. Không tự gán timestamp hoặc prompt cho Antigravity khi chưa có record tương ứng.

## A. Original interaction records - 2026-10-19

### Interaction item 1 - user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:12:50.418000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:12:50.418Z. Source record: `rollout-2026-10-19T14-12-46-01a15301-7395-7091-a01b-206fb49f0e89.jsonl`.

<details>
<summary>Original user message (punctuation normalized)</summary>

````text

# Files mentioned by the user:

## ___2026.Homework.Policies.md: D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/___2026.Homework.Policies.md

## 2026.HW02.Domain Testing_En.md: D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/2026.HW02.Domain Testing_En.md

Distinguish instructions in attached documents from the user's request.

# Files pasted by the user:

## "# HW02 - Domain Testing: Yêu cầu và workflow thực hiện Tóm tắt: Homework này yê...": C:\Users\tdtho\.codex/attachments/c83c0be6-0c8a-4f21-95ef-b49024c1d0e6/Pasted text.txt

## My request:
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Hiện tại đang làm homework 2 ở [hw02](hw02/) . Đọc yêu cầu đề bài, list ra những việc cần làm theo thứ tự từ đầu đến cuối, chọn những templates cần có ở [templates](templates/) , đề xuất cấu trúc thư mục cho [software-testing-hw02-domain-testing](hw02/software-testing-hw02-domain-testing/) .

````

</details>

### Interaction item 2 - assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:12:54.813000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:12:54.813Z. Source record: `rollout-2026-10-19T14-12-46-01a15301-7395-7091-a01b-206fb49f0e89.jsonl`.

<details>
<summary>Original assistant message (punctuation normalized)</summary>

````text
Mình sẽ đọc đề, homework policies, phần ghi chú đính kèm và các template hiện có, rồi lập workflow từ đầu đến lúc nộp bài và đề xuất cấu trúc thư mục. Mình dùng skill `mattpocock-skills:research` để tổng hợp có dẫn chứng; chưa chỉnh sửa file.

````

</details>

### Interaction item 3 - assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:13:26.647000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:13:26.647Z. Source record: `rollout-2026-10-19T14-12-46-01a15301-7395-7091-a01b-206fb49f0e89.jsonl`.

<details>
<summary>Original assistant message (punctuation normalized)</summary>

````text
Đề yêu cầu mỗi feature làm cả Domain Testing và BVA; Agent Skills được khuyến khích nhưng có 10 điểm riêng. Ghi chú đính kèm đã nêu 4 feature cụ thể, mình sẽ dùng làm phạm vi dự kiến và ghi rõ việc kiểm tra trùng với thành viên nhóm.

Có hai điểm cần xử lý trong kế hoạch: SRS của FR-17 chỉ liệt kê Thêm/Xem/Xóa dù tên có "CRUD"; các mẫu AI cũng có quy định cấp môn rộng hơn đề HW02. Mình sẽ phân biệt rõ yêu cầu của đề, nội dung template và phần đề xuất.

````

</details>

### Interaction item 4 - assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:15:02.592000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:15:02.592Z. Source record: `rollout-2026-10-19T14-12-46-01a15301-7395-7091-a01b-206fb49f0e89.jsonl`.

<details>
<summary>Original assistant message (punctuation normalized)</summary>

````text
Mình đề xuất **tổ chức bài theo 4 feature, làm trọn quy trình cho từng feature**, đồng thời ghi AI Audit và commit ngay trong quá trình làm. Repo bài nộp hiện chỉ có `README.md`; mình chưa chỉnh sửa file.

Căn cứ chính là [đề HW02](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/2026.HW02.Domain Testing_En.md>) và [Homework Policies](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/___2026.Homework.Policies.md>). Bản ghi chú đính kèm được dùng làm đầu vào về phạm vi đã chọn, không thay thế đề chính thức.

Phạm vi dự kiến theo ghi chú:

| Pool | Feature | Điểm |
|---|---|---:|
| A | FR-04 - Personal profile management | 25 |
| B | FR-09 - Discount coupons | 25 |
| C | FR-17 - Coupon management | 25 |
| D | Mobile `productDetail` | 15 |
| - | Agent Skills | 10 |

Mỗi feature phải có **cả Domain Testing và BVA**. Cần kiểm tra việc không trùng feature với thành viên nhóm; tài liệu hiện có chưa chứng minh điều này.

Thứ tự công việc từ đầu đến cuối mình đề xuất như sau:

| Bước | Việc cần làm | Đầu ra / điều kiện hoàn thành |
|---:|---|---|
| 1 | Chốt phạm vi, đối chiếu phân công nhóm, kiểm tra deadline trên Moodle | Danh sách 4 feature, phạm vi cụ thể, deadline thực tế |
| 2 | Đọc lại lecture Domain Testing/BVA; lập checklist yêu cầu từ đề và policies | Checklist nối từng yêu cầu với tài liệu sẽ nộp |
| 3 | Chuẩn bị repo bài làm, chọn template, bắt đầu ghi AI interactions **từ phiên hiện tại** | Khung tài liệu và AI log; commit bước chuẩn bị |
| 4 | Ghi baseline SUT: commit, thay đổi local, dữ liệu, môi trường và thiết bị | Thông tin đủ để tái hiện lần chạy |
| 5 | Setup và smoke test Backend, Web, Admin, Mobile | Đăng nhập và truy cập được 4 feature |
| 6 | Phân tích requirements cho từng feature từ SRS, API spec và lecture | Input/output, điều kiện, quyền truy cập, expected behavior, điểm chưa rõ |
| 7 | Chọn FR-04 làm feature đầu tiên; hướng dẫn AI phân tích domain theo từng bước | Bảng domain, valid/invalid classes, ràng buộc và dữ liệu đại diện |
| 8 | Tự review phân tích domain; thiết kế Domain Test Cases và giải thích cách chọn | Test cases có căn cứ, mapping về domain/requirements |
| 9 | Phân tích boundary và thiết kế BVA Test Cases | Bảng boundary, tính bao gồm/loại trừ, độ chính xác và giá trị kiểm thử |
| 10 | Review bộ test trước khi chạy | Expected result rõ ràng; đủ preconditions, test data và steps; loại trùng |
| 11 | Thực thi test, ghi actual result và evidence | Kết quả `PASS` / `FAIL` / `BLOCKED` / `NOT RUN`, có thời gian và môi trường |
| 12 | Tái hiện failures, xác minh bugs; viết Markdown bug report và GitHub Issues của nhóm | Bug có steps, expected/actual, screenshots, liên kết TC ↔ Bug ↔ Issue |
| 13 | Phân tích AI gaps và cập nhật audit | AI bỏ sót/sai gì, sinh viên sửa gì, nguyên nhân có căn cứ |
| 14 | Lặp bước 6-13 cho FR-09 -> FR-17 -> Mobile `productDetail` | Cả 4 feature hoàn thành cùng một quy trình |
| 15 | Xây dựng Agent Skills nếu hướng tới đủ rubric; thử lại trên một feature hoàn chỉnh | Skill tái sử dụng được và video demo end-to-end trên YouTube |
| 16 | Tổng hợp main report, bugs, test summary; hoàn thiện disclosure và audit | Số liệu nhất quán, các kết luận có evidence |
| 17 | Viết **AI Critique 200-300 từ**, tự chấm theo rubric, cập nhật README | Critique dựa trên trải nghiệm thật; điểm từng tiêu chí và tổng điểm |
| 18 | Chốt commits, xuất Git log dạng text; xuất PDF và kiểm tra bản xuất | Markdown/PDF đầy đủ, hình và bảng đọc được, đường dẫn dùng được |
| 19 | Đóng ZIP, giải nén kiểm tra, nộp Moodle trước hạn | Đúng tên, đủ tài liệu/evidence; kiểm tra trạng thái nộp thành công |
| 20 | Chuẩn bị vấn đáp | Giải thích được domain, boundary, expected result, bugs và phần tự sửa từ AI |

**Commit sau mỗi bước kiểm thử của từng feature**, không gom toàn bộ bài thành một commit cuối. AI Audit cũng cập nhật xuyên suốt, không đợi cuối bài mới dựng lại lịch sử.

Một số điểm cần đưa vào bước phân tích requirements:

| Feature | Trọng tâm và điểm cần làm rõ |
|---|---|
| FR-04 | Điện thoại bắt đầu bằng `0`, dài 10-11 chữ số; quyền thay đổi email, role và hồ sơ người khác |
| FR-09 | Năm điều kiện coupon; boundary của ngưỡng đơn hàng, thời hạn và số lượt dùng; công thức giảm giá |
| FR-17 | `code` duy nhất, `type`, giá trị giảm dương, ngưỡng đơn >= 0, lượt dùng >= 1, ngày hết hạn và quyền Admin |
| Mobile `productDetail` | Dữ liệu sản phẩm, số lượng, Add to Cart và phản hồi trên Mobile; xác định rõ requirements nào áp dụng |

[SRS hiện tại](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/eshop-sut/README.md:213>) chỉ ghi **Thêm/Xem/Xóa coupon**, và API spec chưa mô tả Update. Vì vậy cần ghi nhận bất nhất "CRUD", chưa kết luận thiếu Edit là bug. Mobile hiện có ô nhập quantity, nhưng expected behavior vẫn phải có căn cứ; không tự áp các yêu cầu HTML của Web sang React Native.

Về templates, mình chọn như sau. Có thể dùng bản `_Vn.md` để làm bài; không cần sao chép cả hai bản ngôn ngữ.

| Template trong [templates](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/templates/>) | Lựa chọn | Cách sử dụng |
|---|---|---|
| **AI-02 - AI Audit Report** | **Dùng** | Audit artifact: prompt/tool, output, verdict, lý do, bản sinh viên sửa. Bổ sung timestamp cho từng interaction theo đề |
| **AI-03 - AI Disclosure Form** | **Dùng** | Khai báo công cụ, công việc AI hỗ trợ và cách kiểm chứng |
| **AI-05 - AI Privacy Checklist** | **Dùng** | Checklist trước khi nộp theo hướng dẫn trong mẫu; ghi trung thực mục áp dụng/chưa áp dụng |
| **AI-04 - AI Reflective Statement** | **Tham khảo** | Dùng câu hỏi để viết AI Critique; đề HW02 yêu cầu đoạn **200-300 từ**, không bắt buộc nộp nguyên mẫu reflection này |
| **AI-LOG.md** | **Dùng bổ trợ** | Nhật ký ngắn theo task: kept/changed/rejected/by hand. **Không thay thế log nguyên văn prompt/output** |
| **AI-01 - AI Agreement** | Đọc tham chiếu | Quy định cấp môn; không phải báo cáo HW02 cần điền lại |
| **AI-06 - Student Acknowledgement** | Không mặc định nộp lại | Mẫu xác nhận đầu kỳ; chỉ bổ sung nếu giảng viên yêu cầu |

Có hai lưu ý khi dùng mẫu:

- AI-02 có phần kết luận 80-150 chữ; phần đó **không thay thế** AI Critique 200-300 từ.
- Template có nội dung dùng chung và vài chi tiết không khớp đề HW02, như mục tài khoản Claude Pro trong AI-05, trong khi đề cho chọn bất kỳ công cụ AI. Giữ bản gốc để đối chiếu, không tự đánh dấu các xác nhận chưa đúng thực tế.

Thư mục bài làm nên giữ SUT ở vị trí hiện tại, song song với repo bài nộp:

```text
hw02/
├── 2026.HW02.Domain Testing_En.md
├── 2026.HW02.Domain Testing_En.pdf
├── eshop-sut/                              # SUT hiện có
└── software-testing-hw02-domain-testing/    # Repo bài làm
```

Bên trong [repo bài làm](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/software-testing-hw02-domain-testing/>), mình đề xuất:

```text
software-testing-hw02-domain-testing/
├── README.md
├── TASKS.md
├── AI-LOG.md
├── .gitignore
│
├── docs/
│   ├── scope-and-requirements.md
│   ├── test-environment.md
│   └── references/
│       ├── homework-policies.md
│       ├── hw02-assignment.md
│       ├── eshop-srs.md
│       └── eshop-api-specification.md
│
├── tests/
│   ├── A-FR04-profile.md
│   ├── B-FR09-discount-coupons.md
│   ├── C-FR17-coupon-management.md
│   └── D-mobile-product-detail.md
│
├── bugs/
│   └── bug-reports.md
│
├── evidence/
│   ├── screenshots/
│   ├── github-issues/
│   ├── execution/
│   └── video-links.md
│
├── ai/
│   ├── ai-audit-report.md
│   ├── ai-disclosure.md
│   ├── ai-critique.md
│   ├── ai-privacy-checklist.md
│   └── interactions/                     # Prompt/output nguyên văn
│
├── reports/
│   ├── main-report.md
│   └── pdf/                              # Các bản PDF tương ứng
│
├── git-commit-log.txt
├── skills/                               # Khi thực hiện Agent Skills
└── scripts/                              # Khi có script thực sự sử dụng
```

Mỗi file feature trong `tests/` dùng chung một bố cục:

1. Requirements và assumptions.
2. Domain analysis và cách áp dụng kỹ thuật.
3. Boundary analysis và cách chọn giá trị.
4. Test cases, có nhãn Domain/BVA hoặc cả hai.
5. Execution results và evidence.
6. Bugs liên quan.
7. AI gap analysis và các chỉnh sửa của sinh viên.

`main-report.md` tổng hợp đầy đủ nội dung để chấm; PDF cần chứa các bảng/kết quả cần thiết, không chỉ dẫn link sang file khác. `README.md` là trang vào bài nộp, chứa bảng tự đánh giá, số feature, số TC designed/executed/passed/failed/not executed, số bugs và demo videos. Đếm TC theo ID duy nhất để tránh cộng hai lần case vừa phủ Domain vừa phủ BVA.

Khi đóng gói, dùng tên cụ thể theo đề HW02:

```text
<StudentID>_HW02_AI_DomainTesting_<SelfAssessedGrade>.zip
```

Điểm có ba chữ số `000`-`100`. Nộp kèm Markdown/PDF, screenshots và evidence cần thiết trong ZIP; deadline lấy từ Moodle. Agent Skills là phần khuyến khích nhưng chiếm 10/100 điểm, nên đưa vào kế hoạch nếu mục tiêu là hoàn thành toàn bộ rubric.
````

</details>

### Interaction item 5 - user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:20:39.330000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:20:39.330Z. Source record: `rollout-2026-10-19T14-12-46-01a15301-7395-7091-a01b-206fb49f0e89.jsonl`.

<details>
<summary>Original user message (punctuation normalized)</summary>

````text
Cái repo sẽ nộp luôn á, nên mấy cái không liên quan thì bỏ ra, gồm: references, tasks.md thì mang ra ngoài.
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Chia ra những phần bạn có thể hỗ trợ làm hết full và cần tui làm thủ công (ví dụ vào ui rồi chụp) thì trong tasks chia ra 2 phần để chia ra làm nha. Chủ yếu bạn làm từ đầu đến cuối hết rồi hẳn bảo tôi vào làm sau khi xong hết. Còn thắc mắc gì không?


````

</details>

### Interaction item 6 - user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:23:59.256000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:23:59.256Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Original user message (punctuation normalized)</summary>

````text
Cái repo sẽ nộp luôn á, nên mấy cái không liên quan thì bỏ ra, gồm: references, tasks.md thì mang ra ngoài.
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Chia ra những phần bạn có thể hỗ trợ làm hết full và cần tui làm thủ công (ví dụ vào ui rồi chụp) thì trong tasks chia ra 2 phần để chia ra làm nha. Chủ yếu bạn làm từ đầu đến cuối hết rồi hẳn bảo tôi vào làm sau khi xong hết. Còn thắc mắc gì không?
````

</details>

### Interaction item 7 - assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:24:05.991000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:24:05.991Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Original assistant message (punctuation normalized)</summary>

````text
Mình không còn thắc mắc về cách chia việc. Mình sẽ đưa `TASKS.md` và tài liệu tham chiếu ra ngoài repo nộp, rồi chia task thành hai phần: mình xử lý trước mọi việc có thể làm bằng file/API/script; bạn làm sau các bước cần thao tác UI, chụp ảnh, quay video hoặc xác nhận cá nhân.

Mình sẽ đọc skill lập task của `mattpocock-skills` và kiểm tra thư mục hiện tại để cập nhật đúng chỗ.

````

</details>

### Interaction item 8 - assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:24:38.159000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:24:38.159Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Original assistant message (punctuation normalized)</summary>

````text
Repo hiện chưa có `references/` hay `TASKS.md`, nên không cần di chuyển gì. Mình sẽ tạo `hw02/TASKS.md` bên ngoài repo, với thứ tự phụ thuộc và điều kiện hoàn thành cho hai phần.

Mình có thể chuẩn bị báo cáo, bộ test, script, kết quả API và nội dung bug report trước. Các kết luận về UI/Mobile, ảnh chụp, video và xác nhận cá nhân sẽ chờ bằng chứng của bạn. Sau khi bạn bổ sung, mình sẽ đối chiếu số liệu và đóng gói bản nộp cuối.

````

</details>

### Interaction item 9 - assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:26:28.454000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:26:28.454Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Original assistant message (punctuation normalized)</summary>

````text
Không còn thắc mắc về cách chia việc. Đã tạo [hw02/TASKS.md](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/TASKS.md>) **ngoài repo nộp bài**, gồm:

- **Phần A - mình làm:** setup, phân tích, Domain/BVA, script/API tests, báo cáo, AI Audit, Agent Skills và chuẩn bị bàn giao.
- **Phần B - bạn làm sau:** chạy UI/Mobile cần thiết, chụp ảnh, quay video, review/xác nhận cá nhân và nộp Moodle.

Mình sẽ hoàn thành mọi phần tự xử lý được trước, rồi giao một checklist cụ thể gồm thao tác, dữ liệu và tên evidence cần lưu. Nhận evidence xong, mình cập nhật kết quả và đóng ZIP cuối.

`references/` cũng giữ ngoài repo. Hiện mới hoàn thành kế hoạch, chưa triển khai bài.
````

