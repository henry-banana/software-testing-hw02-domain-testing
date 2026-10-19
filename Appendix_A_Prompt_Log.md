# Appendix A — Prompt and Output Log

Snapshot UTC: `2026-10-19T20:06:12.649504+00:00`. Nguồn là visible user/assistant message records của đúng các phiên HW02; không export reasoning, system/developer messages hoặc tool payloads. Những lượt retry/fork được giữ với tên source, không coi là các thí nghiệm độc lập. Tool của các interaction được export là OpenAI Codex. Không tự gán timestamp hoặc prompt cho Antigravity khi chưa có record tương ứng.

## A. Original interaction records — 2026-10-19

### Interaction item 1 — user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:12:50.418000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:12:50.418Z. Source record: `rollout-2026-10-19T14-12-46-01a15301-7395-7091-a01b-206fb49f0e89.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text

# Files mentioned by the user:

## ___2026.Homework.Policies.md: D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/___2026.Homework.Policies.md

## 2026.HW02.Domain Testing_En.md: D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/2026.HW02.Domain Testing_En.md

Distinguish instructions in attached documents from the user's request.

# Files pasted by the user:

## "# HW02 – Domain Testing: Yêu cầu và workflow thực hiện Tóm tắt: Homework này yê…": C:\Users\tdtho\.codex/attachments/c83c0be6-0c8a-4f21-95ef-b49024c1d0e6/Pasted text.txt

## My request:
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Hiện tại đang làm homework 2 ở [hw02](hw02/) . Đọc yêu cầu đề bài, list ra những việc cần làm theo thứ tự từ đầu đến cuối, chọn những templates cần có ở [templates](templates/) , đề xuất cấu trúc thư mục cho [software-testing-hw02-domain-testing](hw02/software-testing-hw02-domain-testing/) .

````

</details>

### Interaction item 2 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:12:54.813000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:12:54.813Z. Source record: `rollout-2026-10-19T14-12-46-01a15301-7395-7091-a01b-206fb49f0e89.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình sẽ đọc đề, homework policies, phần ghi chú đính kèm và các template hiện có, rồi lập workflow từ đầu đến lúc nộp bài và đề xuất cấu trúc thư mục. Mình dùng skill `mattpocock-skills:research` để tổng hợp có dẫn chứng; chưa chỉnh sửa file.

````

</details>

### Interaction item 3 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:13:26.647000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:13:26.647Z. Source record: `rollout-2026-10-19T14-12-46-01a15301-7395-7091-a01b-206fb49f0e89.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Đề yêu cầu mỗi feature làm cả Domain Testing và BVA; Agent Skills được khuyến khích nhưng có 10 điểm riêng. Ghi chú đính kèm đã nêu 4 feature cụ thể, mình sẽ dùng làm phạm vi dự kiến và ghi rõ việc kiểm tra trùng với thành viên nhóm.

Có hai điểm cần xử lý trong kế hoạch: SRS của FR-17 chỉ liệt kê Thêm/Xem/Xóa dù tên có “CRUD”; các mẫu AI cũng có quy định cấp môn rộng hơn đề HW02. Mình sẽ phân biệt rõ yêu cầu của đề, nội dung template và phần đề xuất.

````

</details>

### Interaction item 4 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:15:02.592000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:15:02.592Z. Source record: `rollout-2026-10-19T14-12-46-01a15301-7395-7091-a01b-206fb49f0e89.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình đề xuất **tổ chức bài theo 4 feature, làm trọn quy trình cho từng feature**, đồng thời ghi AI Audit và commit ngay trong quá trình làm. Repo bài nộp hiện chỉ có `README.md`; mình chưa chỉnh sửa file.

Căn cứ chính là [đề HW02](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/2026.HW02.Domain Testing_En.md>) và [Homework Policies](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/___2026.Homework.Policies.md>). Bản ghi chú đính kèm được dùng làm đầu vào về phạm vi đã chọn, không thay thế đề chính thức.

Phạm vi dự kiến theo ghi chú:

| Pool | Feature | Điểm |
|---|---|---:|
| A | FR-04 — Personal profile management | 25 |
| B | FR-09 — Discount coupons | 25 |
| C | FR-17 — Coupon management | 25 |
| D | Mobile `productDetail` | 15 |
| — | Agent Skills | 10 |

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
| 14 | Lặp bước 6–13 cho FR-09 → FR-17 → Mobile `productDetail` | Cả 4 feature hoàn thành cùng một quy trình |
| 15 | Xây dựng Agent Skills nếu hướng tới đủ rubric; thử lại trên một feature hoàn chỉnh | Skill tái sử dụng được và video demo end-to-end trên YouTube |
| 16 | Tổng hợp main report, bugs, test summary; hoàn thiện disclosure và audit | Số liệu nhất quán, các kết luận có evidence |
| 17 | Viết **AI Critique 200–300 từ**, tự chấm theo rubric, cập nhật README | Critique dựa trên trải nghiệm thật; điểm từng tiêu chí và tổng điểm |
| 18 | Chốt commits, xuất Git log dạng text; xuất PDF và kiểm tra bản xuất | Markdown/PDF đầy đủ, hình và bảng đọc được, đường dẫn dùng được |
| 19 | Đóng ZIP, giải nén kiểm tra, nộp Moodle trước hạn | Đúng tên, đủ tài liệu/evidence; kiểm tra trạng thái nộp thành công |
| 20 | Chuẩn bị vấn đáp | Giải thích được domain, boundary, expected result, bugs và phần tự sửa từ AI |

**Commit sau mỗi bước kiểm thử của từng feature**, không gom toàn bộ bài thành một commit cuối. AI Audit cũng cập nhật xuyên suốt, không đợi cuối bài mới dựng lại lịch sử.

Một số điểm cần đưa vào bước phân tích requirements:

| Feature | Trọng tâm và điểm cần làm rõ |
|---|---|
| FR-04 | Điện thoại bắt đầu bằng `0`, dài 10–11 chữ số; quyền thay đổi email, role và hồ sơ người khác |
| FR-09 | Năm điều kiện coupon; boundary của ngưỡng đơn hàng, thời hạn và số lượt dùng; công thức giảm giá |
| FR-17 | `code` duy nhất, `type`, giá trị giảm dương, ngưỡng đơn ≥ 0, lượt dùng ≥ 1, ngày hết hạn và quyền Admin |
| Mobile `productDetail` | Dữ liệu sản phẩm, số lượng, Add to Cart và phản hồi trên Mobile; xác định rõ requirements nào áp dụng |

[SRS hiện tại](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/eshop-sut/README.md:213>) chỉ ghi **Thêm/Xem/Xóa coupon**, và API spec chưa mô tả Update. Vì vậy cần ghi nhận bất nhất “CRUD”, chưa kết luận thiếu Edit là bug. Mobile hiện có ô nhập quantity, nhưng expected behavior vẫn phải có căn cứ; không tự áp các yêu cầu HTML của Web sang React Native.

Về templates, mình chọn như sau. Có thể dùng bản `_Vn.md` để làm bài; không cần sao chép cả hai bản ngôn ngữ.

| Template trong [templates](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/templates/>) | Lựa chọn | Cách sử dụng |
|---|---|---|
| **AI-02 — AI Audit Report** | **Dùng** | Audit artifact: prompt/tool, output, verdict, lý do, bản sinh viên sửa. Bổ sung timestamp cho từng interaction theo đề |
| **AI-03 — AI Disclosure Form** | **Dùng** | Khai báo công cụ, công việc AI hỗ trợ và cách kiểm chứng |
| **AI-05 — AI Privacy Checklist** | **Dùng** | Checklist trước khi nộp theo hướng dẫn trong mẫu; ghi trung thực mục áp dụng/chưa áp dụng |
| **AI-04 — AI Reflective Statement** | **Tham khảo** | Dùng câu hỏi để viết AI Critique; đề HW02 yêu cầu đoạn **200–300 từ**, không bắt buộc nộp nguyên mẫu reflection này |
| **AI-LOG.md** | **Dùng bổ trợ** | Nhật ký ngắn theo task: kept/changed/rejected/by hand. **Không thay thế log nguyên văn prompt/output** |
| **AI-01 — AI Agreement** | Đọc tham chiếu | Quy định cấp môn; không phải báo cáo HW02 cần điền lại |
| **AI-06 — Student Acknowledgement** | Không mặc định nộp lại | Mẫu xác nhận đầu kỳ; chỉ bổ sung nếu giảng viên yêu cầu |

Có hai lưu ý khi dùng mẫu:

- AI-02 có phần kết luận 80–150 chữ; phần đó **không thay thế** AI Critique 200–300 từ.
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

Điểm có ba chữ số `000`–`100`. Nộp kèm Markdown/PDF, screenshots và evidence cần thiết trong ZIP; deadline lấy từ Moodle. Agent Skills là phần khuyến khích nhưng chiếm 10/100 điểm, nên đưa vào kế hoạch nếu mục tiêu là hoàn thành toàn bộ rubric.
````

</details>

### Interaction item 5 — user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:20:39.330000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:20:39.330Z. Source record: `rollout-2026-10-19T14-12-46-01a15301-7395-7091-a01b-206fb49f0e89.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
Cái repo sẽ nộp luôn á, nên mấy cái không liên quan thì bỏ ra, gồm: references, tasks.md thì mang ra ngoài.
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Chia ra những phần bạn có thể hỗ trợ làm hết full và cần tui làm thủ công (ví dụ vào ui rồi chụp) thì trong tasks chia ra 2 phần để chia ra làm nha. Chủ yếu bạn làm từ đầu đến cuối hết rồi hẳn bảo tôi vào làm sau khi xong hết. Còn thắc mắc gì không?


````

</details>

### Interaction item 6 — user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:23:59.256000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:23:59.256Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
Cái repo sẽ nộp luôn á, nên mấy cái không liên quan thì bỏ ra, gồm: references, tasks.md thì mang ra ngoài.
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Chia ra những phần bạn có thể hỗ trợ làm hết full và cần tui làm thủ công (ví dụ vào ui rồi chụp) thì trong tasks chia ra 2 phần để chia ra làm nha. Chủ yếu bạn làm từ đầu đến cuối hết rồi hẳn bảo tôi vào làm sau khi xong hết. Còn thắc mắc gì không?
````

</details>

### Interaction item 7 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:24:05.991000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:24:05.991Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình không còn thắc mắc về cách chia việc. Mình sẽ đưa `TASKS.md` và tài liệu tham chiếu ra ngoài repo nộp, rồi chia task thành hai phần: mình xử lý trước mọi việc có thể làm bằng file/API/script; bạn làm sau các bước cần thao tác UI, chụp ảnh, quay video hoặc xác nhận cá nhân.

Mình sẽ đọc skill lập task của `mattpocock-skills` và kiểm tra thư mục hiện tại để cập nhật đúng chỗ.

````

</details>

### Interaction item 8 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:24:38.159000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:24:38.159Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Repo hiện chưa có `references/` hay `TASKS.md`, nên không cần di chuyển gì. Mình sẽ tạo `hw02/TASKS.md` bên ngoài repo, với thứ tự phụ thuộc và điều kiện hoàn thành cho hai phần.

Mình có thể chuẩn bị báo cáo, bộ test, script, kết quả API và nội dung bug report trước. Các kết luận về UI/Mobile, ảnh chụp, video và xác nhận cá nhân sẽ chờ bằng chứng của bạn. Sau khi bạn bổ sung, mình sẽ đối chiếu số liệu và đóng gói bản nộp cuối.

````

</details>

### Interaction item 9 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:26:28.454000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:26:28.454Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Không còn thắc mắc về cách chia việc. Đã tạo [hw02/TASKS.md](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/TASKS.md>) **ngoài repo nộp bài**, gồm:

- **Phần A — mình làm:** setup, phân tích, Domain/BVA, script/API tests, báo cáo, AI Audit, Agent Skills và chuẩn bị bàn giao.
- **Phần B — bạn làm sau:** chạy UI/Mobile cần thiết, chụp ảnh, quay video, review/xác nhận cá nhân và nộp Moodle.

Mình sẽ hoàn thành mọi phần tự xử lý được trước, rồi giao một checklist cụ thể gồm thao tác, dữ liệu và tên evidence cần lưu. Nhận evidence xong, mình cập nhật kết quả và đóng ZIP cuối.

`references/` cũng giữ ngoài repo. Hiện mới hoàn thành kế hoạch, chưa triển khai bài.
````

</details>

### Interaction item 10 — user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:34:54.043000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:34:54.043Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
Phần của nhóm thì để khúc cuối rồi làm sau, vì đã chia rồi nên chắc chắn kh trùng nữa. Những tasks cần thao tác thủ công thì bạn viết chi tiết cần làm cái gì và screenshots ra sao nữa nha.

````

</details>

### Interaction item 11 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:34:58.067000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:34:58.067Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình sẽ ghi nhận 4 feature đã được chia và không trùng, chuyển phần GitHub Issues của nhóm về cuối. Checklist thủ công sẽ nêu rõ từng thao tác, nội dung cần thấy trong screenshot, tên file và nơi lưu; các TC/bug cụ thể sẽ được điền sau khi có kết quả kiểm thử.

````

</details>

### Interaction item 12 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:36:48.843000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:36:48.843Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Đã cập nhật [TASKS.md](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/TASKS.md>):

- Ghi nhận feature **đã chia, không trùng**, bỏ bước xác nhận lại.
- Chuyển phần nhóm/GitHub Issues về cuối, trước đóng gói.
- Bổ sung hướng dẫn thủ công cho từng feature: thao tác, thời điểm chụp, nội dung phải thấy, tên ảnh và thư mục lưu.
- Thêm hướng dẫn quay demo, chụp Issues và xác nhận nộp Moodle.

Khi bàn giao, mình sẽ điền **TC-ID, dữ liệu nhập, expected result và từng bước cụ thể** từ bộ test đã hoàn thiện để bạn làm theo.
````

</details>

### Interaction item 13 — user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:46:16.865000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:46:16.865Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Bắt đầu làm full đi.

````

</details>

### Interaction item 14 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:46:22.048000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:46:22.048Z. Source record: `rollout-2026-10-19T14-23-55-01a15301-7395-7091-a01b-206fb49f0e89_01a1530b-aa56-7392-b740-1c92f697a73f.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình bắt đầu làm toàn bộ Phần A theo `hw02/TASKS.md`: chốt baseline, chuẩn bị tài liệu, thiết kế Domain/BVA, chạy phần kiểm thử qua API/script, rồi tổng hợp báo cáo và checklist UI chi tiết cho bạn. Phần nhóm để cuối như đã thống nhất.

Mình sẽ dùng workflow triển khai của `mattpocock-skills`, tự thực hiện trong phiên này; không dùng subagent hay Computer Use.

````

</details>

### Interaction item 15 — user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:47:15.782000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:47:15.782Z. Source record: `rollout-2026-10-19T14-47-12-01a15301-7395-7091-a01b-206fb49f0e89_01a15320-f9dc-7d02-a30c-e71cab863a0d.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Bắt đầu làm full đi. Đổi phần ai/ thành ai-audit, và các file kia phải giữa nguyên đúng tên của [templates](templates/)
````

</details>

### Interaction item 16 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:47:23.232000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:47:23.232Z. Source record: `rollout-2026-10-19T14-47-12-01a15301-7395-7091-a01b-206fb49f0e89_01a15320-f9dc-7d02-a30c-e71cab863a0d.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình bắt đầu làm toàn bộ phần có thể xử lý bằng file, terminal và API, rồi mới bàn giao phần UI/ảnh/video cho bạn. Mình sẽ dùng `ai-audit/` và giữ nguyên tên các file lấy từ `templates/`; phần nhóm vẫn để cuối.

Mình sẽ đọc skill triển khai của `mattpocock-skills`, kiểm tra thay đổi hiện có và ghi baseline trước khi setup/chạy test.

````

</details>

### Interaction item 17 — user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:48:03.395000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:48:03.395Z. Source record: `rollout-2026-10-19T14-47-59-01a15301-7395-7091-a01b-206fb49f0e89_01a15321-b288-7281-af77-b241f028fbd8.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Bắt đầu làm full đi. Đổi phần ai/ thành ai-audit, xóa interactions/, và các file kia phải giữa nguyên đúng tên của [templates](templates/)
````

</details>

### Interaction item 18 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:48:09.569000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:48:09.569Z. Source record: `rollout-2026-10-19T14-47-59-01a15301-7395-7091-a01b-206fb49f0e89_01a15321-b288-7281-af77-b241f028fbd8.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình bắt đầu phần có thể tự làm đến hết: setup, phân tích, thiết kế/chạy test, báo cáo, AI Audit và Agent Skills. Mình sẽ đổi thành `ai-audit/`, bỏ `interactions/`, giữ nguyên tên file template; prompt/output sẽ nằm trong báo cáo audit. Các bước cần UI, ảnh và video sẽ được chuẩn bị chi tiết để bạn làm sau.

````

</details>

### Interaction item 19 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:48:58.067000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:48:58.067Z. Source record: `rollout-2026-10-19T14-47-59-01a15301-7395-7091-a01b-206fb49f0e89_01a15321-b288-7281-af77-b241f028fbd8.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình thấy backend tự xóa và seed lại database mỗi lần khởi động. Mình sẽ chạy trên bản runtime riêng ngoài repo nộp để giữ nguyên database hiện tại của bạn.

Mình dùng `mattpocock-skills:implement` cho phần triển khai, cùng skill tạo báo cáo PDF và Agent Skill. Việc review sẽ do mình thực hiện trong phiên này, không dùng subagent hay Computer Use.

````

</details>

### Interaction item 20 — user

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:50:32.053000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:50:32.053Z. Source record: `rollout-2026-10-19T14-50-28-01a15301-7395-7091-a01b-206fb49f0e89_01a15323-f792-7b70-98b0-0c2d51f05b6e.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Bắt đầu làm full đi. Đổi phần ai/ thành ai-audit, xóa interactions/, và các file kia phải giữa nguyên đúng tên của [templates](templates/). Lưu ý mọi doc bạn viết đều ở dạng markdown hết, còn định dạng cuối ra sao thì tui sẽ tự thực hiện. À có thể tham khảo [https://github.com/bingsu1103/23120205-HW02-AI-DomainTesting](https://github.com/bingsu1103/23120205-HW02-AI-DomainTesting) để xem họ sắp xếp ra sao? Soạn lại tasks chi tiết hơn để bạn nắm đi
````

</details>

### Interaction item 21 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:50:37.543000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:50:37.543Z. Source record: `rollout-2026-10-19T14-50-28-01a15301-7395-7091-a01b-206fb49f0e89_01a15323-f792-7b70-98b0-0c2d51f05b6e.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình sẽ cập nhật `TASKS.md` chi tiết theo các yêu cầu mới rồi bắt đầu triển khai phần mình làm được: dùng `ai-audit/`, bỏ `interactions/`, giữ đúng tên các file template được chọn và chỉ viết tài liệu Markdown. Mình cũng sẽ xem repo tham khảo để học cách sắp xếp, không lấy nội dung bài làm hay prompts của họ.

````

</details>

### Interaction item 22 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:51:16.653000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:51:16.653Z. Source record: `rollout-2026-10-19T14-50-28-01a15301-7395-7091-a01b-206fb49f0e89_01a15323-f792-7b70-98b0-0c2d51f05b6e.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình dùng `mattpocock-skills:implement` để triển khai và sẽ review trước khi chốt. Repo tham khảo tách test cases, bug reports, evidence và skills; mình sẽ giữ cách phân loại đó, còn kế hoạch và tài liệu tham chiếu vẫn nằm ngoài repo nộp.

Có một điểm ảnh hưởng trực tiếp đến setup: backend hiện tự xóa và seed lại database mỗi lần khởi động. Mình sẽ chạy trên bản SUT tách riêng, giữ nguyên database bạn đang có.

````

</details>

### Interaction item 23 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T14:56:21.041000+07:00 (Asia/Saigon); original UTC 2026-10-19T07:56:21.041Z. Source record: `rollout-2026-10-19T14-50-28-01a15301-7395-7091-a01b-206fb49f0e89_01a15323-f792-7b70-98b0-0c2d51f05b6e.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Đã cập nhật kế hoạch theo yêu cầu Markdown và giữ đúng tên template. Bộ thiết kế ban đầu có 81 case API và 33 case UI/Mobile; mình sẽ kiểm tra coverage trước khi chốt số lượng.

Các case API sẽ kiểm tra dữ liệu lưu lại qua API public, không chỉ nhìn HTTP status. UI/Mobile vẫn để `NOT RUN` đến khi có thao tác và bằng chứng thật của bạn.

````

</details>

### Interaction item 24 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T15:00:03.123000+07:00 (Asia/Saigon); original UTC 2026-10-19T08:00:03.123Z. Source record: `rollout-2026-10-19T14-50-28-01a15301-7395-7091-a01b-206fb49f0e89_01a15323-f792-7b70-98b0-0c2d51f05b6e.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Đã chạy xong API cho FR-04 và FR-09. FR-04 có 7 pass, 14 fail và 1 observation; FR-09 có 14 pass, 12 fail. Các lỗi đã tái hiện gồm lưu số điện thoại sai, đổi `role` qua profile, từ chối coupon ngay tại ngưỡng tối thiểu và tính sai phần trăm giảm giá.

Các lần chạy đều xác nhận source và database SUT gốc không đổi. Mình đang tiếp tục FR-17, rồi chuẩn bị phần Mobile và hướng dẫn chụp theo từng TC.

````

</details>

### Interaction item 25 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T15:04:11.325000+07:00 (Asia/Saigon); original UTC 2026-10-19T08:04:11.325Z. Source record: `rollout-2026-10-19T14-50-28-01a15301-7395-7091-a01b-206fb49f0e89_01a15323-f792-7b70-98b0-0c2d51f05b6e.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
FR-17 đã chạy xong: 14 pass, 16 fail. Tổng phần API hiện có 81 case đã chạy và 15 nhóm bug; 33 case UI/Mobile vẫn chờ evidence.

Mình đang chuẩn bị runtime riêng cho lượt thủ công: tài khoản theo từng case, sản phẩm đúng các mức tiền biên và trạng thái coupon đã dùng sẵn. Web và Admin build đã pass; bản bundle Android còn đang chạy.

````

</details>

### Interaction item 26 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T15:08:53.281000+07:00 (Asia/Saigon); original UTC 2026-10-19T08:08:53.281Z. Source record: `rollout-2026-10-19T14-50-28-01a15301-7395-7091-a01b-206fb49f0e89_01a15323-f792-7b70-98b0-0c2d51f05b6e.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Web, Admin và bundle Android đều build pass. Mình đã viết hướng dẫn thao tác và chụp ảnh cho cả 33 case UI/Mobile, gồm dữ liệu nhập, tài khoản, expected result, điểm chụp và tên file.

Phần còn lại mình đang hoàn thiện là AI Audit, kịch bản demo skill và kiểm tra chéo số liệu, liên kết, tên template. Các xác nhận cá nhân và verdict của sinh viên sẽ để bạn review sau.

````

</details>

### Interaction item 27 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T15:13:52.457000+07:00 (Asia/Saigon); original UTC 2026-10-19T08:13:52.457Z. Source record: `rollout-2026-10-19T14-50-28-01a15301-7395-7091-a01b-206fb49f0e89_01a15323-f792-7b70-98b0-0c2d51f05b6e.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Trong lúc kiểm tra, mình thấy báo cáo chính đã được chuyển thành `REPORT.md` ở root và skill nằm tại `.agents/skills/domain-bva-testing/`. Mình sẽ giữ hai vị trí hiện tại, cập nhật toàn bộ đường dẫn liên quan và kiểm tra lại, không tạo bản trùng.

````

</details>

### Interaction item 28 — assistant

Tool: OpenAI Codex. Timestamp: 2026-10-19T15:15:42.544000+07:00 (Asia/Saigon); original UTC 2026-10-19T08:15:42.544Z. Source record: `rollout-2026-10-19T14-50-28-01a15301-7395-7091-a01b-206fb49f0e89_01a15323-f792-7b70-98b0-0c2d51f05b6e.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Kiểm tra Markdown hiện đã pass: số liệu khớp, tên bốn file AI đúng template, không còn `ai/` hay `interactions/`, và các liên kết nội bộ đều mở đúng file. AI Critique có 245 từ, đang ghi rõ là bản nháp chờ bạn review.

Runtime Web/Admin/Expo đang chạy để bạn dùng sau khi nhận bàn giao. Mình đang chốt review, cập nhật trạng thái `TASKS.md` và xuất Git log; chưa push lên remote.

````

</details>


## B. Review và detailed rewrite — interaction records

### Record R001 — user

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T09:09:57.565Z`. Source: `rollout-2026-10-19T16-06-40-01a15369-b96b-7cb2-8351-4a091cdedffe.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Giờ hãy đọc lại toàn bộ yêu cầu và kiểm tra còn thiếu những gì? Liệt kê toàn bộ.
T đã up toàn bộ screenshot vào D:\Workspace\1. Study\courses-fit-hcmus\2026-2027\csc13003-testing\hw02\tmp, tự dò và đưa vào đúng chỗ của chúng + đặt tên lại.
Phần report cùng các docs nên làm chuẩn như [hw01](hw01/) vậy.
Xóa những doc markdown mà nó không liên quan để nộp bài như manual gì nè, hoặc những cái chỉ để bạn mô tả như góc nhìn thứ 3 chứ không phải đang làm??
Dời hoặc xóa thì tùy bạn.
List toàn bộ cần thực hiện công việc ra sao đi.

````

</details>

### Record R002 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T09:10:05.114Z`. Source: `rollout-2026-10-19T16-06-40-01a15369-b96b-7cb2-8351-4a091cdedffe.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình sẽ rà lại đề và policies, đối chiếu bài hiện tại với cách trình bày HW01, rồi xem toàn bộ ảnh trong `hw02/tmp`. Sau đó mình sẽ liệt kê đầy đủ phần còn thiếu và danh sách file cần sửa, chuyển hoặc loại khỏi bài nộp để bạn xem trước.

````

</details>

### Record R003 — user

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T09:10:30.869Z`. Source: `rollout-2026-10-19T16-10-28-01a15369-b96b-7cb2-8351-4a091cdedffe_01a1536d-33a0-79f0-a888-0a12cfaf679b.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Giờ hãy đọc lại toàn bộ yêu cầu và kiểm tra còn thiếu những gì? Liệt kê toàn bộ.
T đã up toàn bộ screenshot vào D:\Workspace\1. Study\courses-fit-hcmus\2026-2027\csc13003-testing\hw02\tmp, tự dò và đưa vào đúng chỗ của chúng + đặt tên lại.
Phần report cùng các docs nên làm chuẩn như [hw01](hw01/) vậy.
Xóa những doc markdown mà nó không liên quan để nộp bài như manual gì nè, hoặc những cái chỉ để bạn mô tả như góc nhìn thứ 3 chứ không phải đang làm??
Dời hoặc xóa thì tùy bạn.
--> Cấu trúc giờ cần chuẩn hơn chứ không có nhiều cái không liên quan như hiện tại.
List toàn bộ cần thực hiện công việc ra sao đi.
````

</details>

### Record R004 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T09:10:43.978Z`. Source: `rollout-2026-10-19T16-10-28-01a15369-b96b-7cb2-8351-4a091cdedffe_01a1536d-33a0-79f0-a888-0a12cfaf679b.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình sẽ đọc lại đề và policies, đối chiếu toàn bộ repo hiện tại, mẫu bài HW01 và ảnh trong `hw02/tmp`. Trước tiên mình sẽ liệt kê đầy đủ phần còn thiếu, cách phân loại ảnh và cấu trúc nộp bài đề xuất; chưa di chuyển hay xóa file trong lượt rà soát này.

````

</details>

### Record R005 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T09:12:22.058Z`. Source: `rollout-2026-10-19T16-10-28-01a15369-b96b-7cb2-8351-4a091cdedffe_01a1536d-33a0-79f0-a888-0a12cfaf679b.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình thấy có 69 ảnh trong `tmp`, nhưng các báo cáo vẫn ghi cả 33 case UI/Mobile là `NOT RUN`. Một số ảnh đã chứng minh lỗi UI mới; cũng có ảnh dùng dữ liệu khác TC đã thiết kế và một ảnh bị cắt còn 5×63 px. Mình sẽ phân loại theo nội dung nhìn thấy, không tự coi mọi TC đã đủ bằng chứng chỉ vì đã có ảnh.

````

</details>

### Record R006 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T09:15:03.724Z`. Source: `rollout-2026-10-19T16-10-28-01a15369-b96b-7cb2-8351-4a091cdedffe_01a1536d-33a0-79f0-a888-0a12cfaf679b.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Đã xem hết 69 ảnh: 13 ảnh Profile, 15 ảnh Checkout, 12 ảnh Admin và 29 ảnh Mobile. Các điểm cần xử lý rõ nhất là ảnh VIP100 dùng account `B-UI-01` nên chưa chứng minh user đã hết lượt; ảnh coupon delete chưa có trạng thái sau xóa; và nhiều ảnh Mobile dùng Samsung/MacBook thay fixture iPhone trong TC ban đầu.

Hai nhóm lỗi UI có bằng chứng rõ để bổ sung là Profile kiểm tra sai mẫu số điện thoại và Mobile chấp nhận quantity không hợp lệ. Mình cũng đang lập danh sách các tài liệu cần gộp hoặc đưa ra ngoài để repo chỉ còn hồ sơ nộp bài.

````

</details>

### Record R007 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T09:22:26.812Z`. Source: `rollout-2026-10-19T16-10-28-01a15369-b96b-7cb2-8351-4a091cdedffe_01a1536d-33a0-79f0-a888-0a12cfaf679b.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Repo hiện cần **tích hợp evidence, hoàn thiện nội dung bài làm và dọn cấu trúc**. Mình đã đọc lại đề/policies, đối chiếu HW01 và xem toàn bộ **69 ảnh**.

Danh sách đầy đủ nằm trong [REVIEW_PLAN.md](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/REVIEW_PLAN.md>), gồm **16 công việc, mapping đổi tên cả 69 ảnh và 12 liên kết đang hỏng**. `TASKS.md` cũng đã dẫn sang kế hoạch mới. **Chưa di chuyển/xóa ảnh hoặc tài liệu bài nộp trong lượt rà soát này.**

Các phần còn thiếu hoặc chưa hoàn chỉnh:

| Phần | Vấn đề hiện tại |
|---|---|
| Kết quả UI/Mobile | Có ảnh thực thi nhưng tài liệu vẫn ghi toàn bộ 33 case `NOT RUN`; số liệu 81 executed/15 bugs chưa cập nhật |
| Mapping ảnh | 69 ảnh chưa được đặt tên/gắn TC; có **1 ảnh chỉ 5×63 px**, không dùng làm evidence |
| Dữ liệu thực thi | Một số ảnh dùng account, sản phẩm hoặc input khác thiết kế; phải ghi đúng biến thể thực tế |
| Bug reports | Chưa nhúng ảnh; chưa tích hợp nhóm lỗi UI Profile và Mobile quantity |
| Báo cáo chính | Phương pháp nằm rải rác trong các file; `REPORT.md` còn chủ yếu là tóm tắt/link và lời điều phối |
| AI documents | Còn placeholder, giọng người thứ ba; AI-02 dài hơn 5.000 dòng vì dump lại artifacts |
| README | Thiếu thông tin cá nhân đầy đủ, kết quả mới, điểm tự đánh giá và video |
| Git log/tooling | `.md` đã đổi sang `.txt` nhưng links/scripts chưa theo; validator hiện lỗi và crash vì đọc manual đã xóa |
| Phần cuối | Chưa có video YouTube, Issue URLs/screenshots của nhóm, xác nhận cá nhân và định dạng nộp cuối |

Những điểm thiếu evidence cụ thể, không cần làm lại toàn bộ 33 case:

- **Profile:** ảnh Unicode dùng phone `1912345678`, khác fixture hợp lệ trong TC. Các kết luận về lưu dữ liệu sau đăng nhập lại cần đối chiếu thêm.
- **Coupon:** ảnh VIP100 dùng account `B-UI-01`, chưa chứng minh điều kiện đã hết lượt của `B-UI-06`. Case 500001 có chỉnh tổng tiền trong khi dòng sản phẩm vẫn 500000; phải ghi rõ thao tác này.
- **Admin:** `C-UI-06` mới thấy tạo coupon, chưa có trạng thái sau xóa. Ảnh browser chặn usage=0 không được dùng để minh họa backend cũng đã chặn.
- **Mobile:** cần ghi đúng các biến thể Samsung/MacBook; chuỗi hai lần Add và chuyển sản phẩm chưa đủ rõ. Input quantity rất lớn khác literal thiết kế, cần giữ đúng mức kết luận observation.
- **API bugs:** nhiều lỗi JWT/role/identity/expiry/mandatory fields chưa có screenshot tương ứng; ảnh UI hiện tại không thay được mọi bằng chứng này.
- **Nhóm:** Issue URLs và ảnh trang Issue vẫn để khúc cuối như đã thống nhất.

Thứ tự thực hiện đầy đủ:

| Bước | Công việc |
|---:|---|
| 1 | Chốt inventory/hash ảnh và trạng thái Git, giữ các thay đổi bạn đang có |
| 2 | Chuẩn bị cấu trúc và nơi gộp nội dung trước khi dọn file |
| 3 | Đưa ảnh vào đúng thư mục, đổi tên theo mapping, kiểm tra không đổi nội dung; ảnh lỗi giữ ngoài repo |
| 4 | Ghi actual/status/evidence cho từng UI case, nêu rõ biến thể và phần chưa chứng minh |
| 5 | Bổ sung bug UI có căn cứ, gắn ảnh vào các bug hiện có |
| 6 | Viết lại báo cáo chính và README theo cách trình bày HW01 |
| 7 | Chuẩn hóa AI forms, Critique 200–300 từ và prompt log |
| 8 | Gộp/dời tài liệu working khỏi repo nộp |
| 9 | Sửa scripts, generators, validator và các links theo cấu trúc mới |
| 10 | Tính lại toàn bộ số TC/kết quả/bug theo ID duy nhất |
| 11 | Chốt danh sách evidence còn thiếu nhỏ nhất |
| 12 | Bạn bổ sung evidence cần thiết, review cá nhân và video |
| 13 | Làm phần GitHub Issues của nhóm cuối cùng |
| 14 | Cập nhật báo cáo cuối, giải trình và điểm tự đánh giá |
| 15 | Kiểm tra repo, commit từng bước và xuất Git log mới |
| 16 | Bạn tự xuất PDF/định dạng cuối, đóng ZIP, nộp Moodle |

Cấu trúc mình đề xuất:

```text
software-testing-hw02-domain-testing/
├── README.md
├── 23120262_Report.md
├── Video_Links.md
├── Appendix_A_Prompt_Log.md
├── git-commit-log.txt
├── ai-audit/                 # Giữ nguyên tên 4 templates
├── tests/                    # 4 feature files
├── bugs/                     # Index + bug reports
├── evidence/
│   ├── screenshots/{A,B,C,D,api}/
│   ├── github-issues/
│   └── execution/            # API records + kết quả UI thực tế
├── scripts/                  # Code cần để tái hiện
└── .agents/skills/domain-bva-testing/SKILL.md
```

Về dọn tài liệu:

- **Gộp 4 `*-domain.md`** vào bốn chương báo cáo chính.
- **Gộp 4 `*-review.md`** vào phần AI gap analysis/Audit, rồi đưa bản working ra ngoài.
- **Không tạo lại** manual-handoff, technical-review, skill-demonstration và các doc vận hành bạn vừa xóa.
- **Gộp contribution từ `AI-LOG.md`** vào hồ sơ AI rồi đưa bản tóm tắt điều phối ra ngoài.
- **Tách AI-02 và prompt log như HW01**, bỏ phần dump trùng artifacts nhưng giữ đầy đủ provenance.
- Giữ test cases, bug reports, raw execution và skill vì đây là sản phẩm phục vụ chấm bài.

Báo cáo sẽ dùng thông tin đã có từ HW01 và giọng bài làm cá nhân: trình bày phương pháp, thao tác, kết quả và phân tích. Những câu giao việc như “Codex đã chuẩn bị”, “sinh viên cần làm…” sẽ đưa về kế hoạch ngoài repo; các thiếu sót thực tế vẫn được ghi trung thực tại trạng thái liên quan.
````

</details>

### Record R008 — user

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T09:24:40.113Z`. Source: `rollout-2026-10-19T16-10-28-01a15369-b96b-7cb2-8351-4a091cdedffe_01a1536d-33a0-79f0-a888-0a12cfaf679b.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
Cái kia giữa là ai-log như hiện tại đi, tui chỉ kêu bạn tham khảo cho cái report thôi, thêm 1 kịch bản quay video bên ngoài để tui làm theo.
Bắt đầu viết lại doc chi tiết rõ ràng và fill vào những phần còn thiếu đi

````

</details>

### Record R009 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T09:24:46.031Z`. Source: `rollout-2026-10-19T16-10-28-01a15369-b96b-7cb2-8351-4a091cdedffe_01a1536d-33a0-79f0-a888-0a12cfaf679b.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình sẽ giữ `AI-LOG.md` và cách tổ chức hồ sơ AI hiện tại; chỉ tham khảo HW01 cho cách viết báo cáo. Mình bắt đầu tích hợp ảnh, cập nhật kết quả và bug reports, viết lại docs theo giọng bài làm cá nhân, rồi dọn tài liệu điều phối ra ngoài. Kịch bản quay video cũng sẽ đặt ngoài repo nộp bài.

````

</details>

### Record R010 — user

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T19:41:48.381Z`. Source: `rollout-2026-10-20T02-41-42-01a15369-b96b-7cb2-8351-4a091cdedffe_01a155af-20a2-7fe1-b0e4-6ad2d65641e3.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Tui đã tự làm hết nhưng cảm thấy  xem sự chi tiết của toàn bộ đã đầy đủ và ổn chưa, tui thấy tham khảo người ta rất chi tiết nè.
https://github.com/NgBaoAnn/hw02-domain-testing/blob/master/REPORT.md
https://github.com/nhaajtdajt/eshop-hw02-domain-testing/blob/main/submission/01_BaoCao_chinh/BaoCao_HW02_23120231.md
Mô tả bugs có tả ít so với tests nhỉ.
````

</details>

### Record R011 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T19:42:01.380Z`. Source: `rollout-2026-10-20T02-41-42-01a15369-b96b-7cb2-8351-4a091cdedffe_01a155af-20a2-7fe1-b0e4-6ad2d65641e3.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình sẽ đọc bản bài làm hiện tại, đối chiếu lại đề và hai báo cáo bạn gửi, rồi đánh giá độ đầy đủ của từng phần, nhất là bug reports so với test cases. Mình dùng cách rà soát của `mattpocock-skills:code-review`, tự kiểm tra trong chat này; chưa sửa nội dung khi chưa chốt được các thiếu sót cụ thể.

````

</details>

### Record R012 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T19:43:56.829Z`. Source: `rollout-2026-10-20T02-41-42-01a15369-b96b-7cb2-8351-4a091cdedffe_01a155af-20a2-7fe1-b0e4-6ad2d65641e3.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Bản hiện tại đã có nhiều chi tiết, nhưng mình thấy vài chỗ cần sửa độ chính xác trước khi viết dài thêm: BUG-A03 và BUG-D01 đã được tính vào tổng nhưng chưa có báo cáo riêng; số tiền của BUG-B02 chưa khớp bằng chứng; một số case thiếu bước xác nhận đang bị ghi FAIL. Mình đang đối chiếu từng bug với test, dữ liệu API và ảnh để phân biệt lỗi mô tả với bằng chứng còn thiếu.
````

</details>

### Record R013 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T19:45:14.568Z`. Source: `rollout-2026-10-20T02-41-42-01a15369-b96b-7cb2-8351-4a091cdedffe_01a155af-20a2-7fe1-b0e4-6ad2d65641e3.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình đã xác nhận lỗi mô tả ảnh hưởng khả năng tái hiện: nhiều bug FR-17 dùng tên field và giá trị enum khác API thật; BUG-B05 dùng coupon khác case đã chạy; toàn bộ 33 UI cases trong `tests/` vẫn ghi `NOT RUN`, trong khi README ghi đã chạy hết. Hai bài tham khảo có cách trình bày đáng học ở bảng truy vết và giải thích từng bước, nhưng bài mình cần đồng bộ các dữ liệu này trước khi tăng độ dài.
````

</details>

### Record R014 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T19:47:18.241Z`. Source: `rollout-2026-10-20T02-41-42-01a15369-b96b-7cb2-8351-4a091cdedffe_01a155af-20a2-7fe1-b0e4-6ad2d65641e3.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
**Phần bug hiện yếu hơn phần test, và bài chưa nên chốt bản cuối.** Tuy nhiên, vấn đề chính là **độ chính xác, khả năng tái hiện và sự thống nhất giữa các tài liệu**, chứ không phải số trang.

Nhiều test cùng phát hiện một lỗi nên số bug ít hơn số test là bình thường. Bài tham khảo thứ hai cũng giải thích điều này. Điểm đáng học là bảng truy vết **requirement → domain → test → actual → bug**, cùng cách giải thích vì sao chọn từng trường hợp. [Bài NgBaoAnn](https://github.com/NgBaoAnn/hw02-domain-testing/blob/master/REPORT.md), [bài nhaajtdajt](https://github.com/nhaajtdajt/eshop-hw02-domain-testing/blob/main/submission/01_BaoCao_chinh/BaoCao_HW02_23120231.md).

Mình đã đối chiếu đề, báo cáo chính, bốn bộ test, 15 báo cáo bug, các analysis/review, raw API evidence và AI forms. Bài có nền tảng tốt: đủ bốn pool, 114 test được thiết kế, 81 API execution records, 68 ảnh và AI Critique đúng 245 từ. Những điểm cần xử lý cụ thể như sau.

1. **Bước tái hiện của nhiều bug FR-17 đang sai contract API.**

   Trong [BUG-C01.md:22](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/software-testing-hw02-domain-testing/bugs/BUG-C01.md:22>), request dùng `discountValue`, `minimumAmount`, `expiryDate`, `maxUses`, `type="FIXED"` và đọc lại bằng `GET /api/admin/coupons`.

   API thật dùng `discount_value`, `min_order_amount`, `expired_at`, `max_uses_per_user`, `type="fixed"` và **`GET /api/coupons`**. Người đọc làm theo sẽ gửi một request khác với case đã chạy, thậm chí vô tình thiếu nhiều field cùng lúc. Cần sửa đồng bộ các bug C01/C03/C04/C05/C06 và phần trích SRS trong report.

2. **BUG-B02 ghi sai kết quả thực tế, dù bằng chứng đã rõ.**

   [BUG-B02.md:15](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/software-testing-hw02-domain-testing/bugs/BUG-B02.md:15>) ghi thành tiền `4,360,000`, discount `−3,960,000`. Raw API và ảnh UI đều cho:

   | Giá trị | Expected | Actual |
   |---|---:|---:|
   | Tổng ban đầu | 400.000 | 400.000 |
   | Tiền giảm | 40.000 | −3.600.000 |
   | Thành tiền | 360.000 | 4.000.000 |

   Cần dùng đúng tên response `discount_amount`, `final_amount`; bỏ dấu `≈` khi đã có số chính xác. B-API-26 dùng coupon **P100**, không phải VIP100 như bug đang mô tả.

3. **Một số bug chưa khớp test mà chúng dẫn tới.**

   - BUG-B05 mô tả BIGBUY/600000, nhưng B-API-22/23 thực tế dùng **VIP100/400000**, với user xác thực đã dùng đủ hai lượt.
   - BUG-C04 đảo C-API-12/13: thực tế **12 là −1, 13 là 0**, không phải zero/negative như đang ghi.
   - BUG-C06 đảo C-API-18/19: thực tế **18 là −1, 19 là 0**.
   - BUG-C09 đúng case **C-API-29**, nhưng báo cáo chính dẫn C-API-27/28.
   - BUG-C07 ghi expected “Reject invalid coupon”, trong khi coupon hợp lệ; điều cần từ chối là **quyền tạo coupon của user thường**.

   Đây là các lỗi truy vết cần sửa trước khi bổ sung diễn giải.

4. **Kết quả UI và tổng thống kê chưa đáng tin cậy.**

   [Báo cáo chính:95](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/software-testing-hw02-domain-testing/23120262_Report.md:95>) ghi A UI `2 PASS / 4 FAIL / 1 OBS`, nhưng chính bảng bên dưới có **3 PASS / 3 FAIL / 1 OBS**.

   Ngoài ra:

   - **C-UI-06:** chưa xác nhận bước xóa thì chưa thể kết luận FAIL. Thiếu evidence không đồng nghĩa SUT có lỗi.
   - **B-UI-06:** ảnh VIP100 áp dụng thành công ở trạng thái nominal chưa chứng minh test “đã dùng hai lượt, lần thứ ba bị từ chối”. Report đang đổi nội dung case để ghi PASS.
   - **A-UI-07:** test gốc kiểm tra Unicode name/address; report đổi thành “Unicode phone”.
   - **D-UI-08:** có ảnh phản hồi thành công nhưng không có ảnh cart; chưa đủ chứng minh riêng hậu điều kiện `cart=1`.
   - **D-UI-09:** expected gồm category, nhưng ảnh detail được dẫn không hiển thị category; chưa đủ cơ sở ghi “đầy đủ thông tin — PASS”.

   Cần phân biệt **kết quả quan sát**, **mức đủ bằng chứng** và **trạng thái thực thi**.

5. **Toàn bộ 33 UI cases trong `tests/` vẫn ghi `NOT RUN`.**

   README/report lại ghi **114/114 đã thực thi**. Các file review cũng còn nói UI chưa chạy; steps trong test trỏ đến `manual-handoff.md` đã bị xóa.

   Ví dụ [test B:733](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/software-testing-hw02-domain-testing/tests/B-FR09-discount-coupons.md:733>) vẫn giữ expected usage-limit và `NOT RUN`. Cần cập nhật actual, variant dữ liệu, verdict và đường dẫn ảnh ngay tại từng case, rồi tính lại summary.

6. **Có hai bug được tính vào tổng nhưng chưa có báo cáo riêng.**

   Report/README tính **17 bug groups**, nhưng `bugs/` mới có **15**:

   - Thiếu **BUG-A03:** frontend kiểm tra phone trái SRS.
   - Thiếu **BUG-D01:** quantity không hợp lệ vẫn được thêm vào giỏ.

   [Bug index](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/software-testing-hw02-domain-testing/bugs/bug-reports.md>) cũng chưa cập nhật hai bug này và trạng thái ảnh mới. Đây là phần cần viết thêm thực sự.

7. **Root cause và impact có chỗ suy đoán vượt bằng chứng.**

   [BUG-A02.md:17](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/software-testing-hw02-domain-testing/bugs/BUG-A02.md:17>) đoán `Object.assign`/spread, nhưng source thực tế chủ động lấy `role` rồi thêm vào câu UPDATE. BUG-C06 đoán `Math.max`, trong khi source dùng `max_uses_per_user || 1`.

   Nên ghi nguyên nhân đúng source khi đã đọc được. Các tác động như truy cập toàn bộ admin features, làm cạn lượt coupon của người khác hoặc lỗi SMS cần tách thành **rủi ro dự kiến** nếu chưa kiểm chứng. Expected cũng không nên tự đặt chuỗi lỗi chính xác khi SRS chỉ yêu cầu từ chối.

8. **Phần phương pháp có chi tiết nhưng chưa thống nhất.**

   Cùng `A-D8`, báo cáo chính dùng cho name/address, còn [analysis A:26](<D:/Workspace/1. Study/courses-fit-hcmus/2026-2027/csc13003-testing/hw02/software-testing-hw02-domain-testing/reports/A-FR04-domain.md:26>) dùng cho role escalation. Các feature khác cũng có việc đánh lại domain ID.

   BVA cần thống nhất biến đang xét, biên, đơn vị và cách gọi ON/OFF/IN. Ví dụ phone length **11 là biên trên hợp lệ**, không nên chỉ ghi IN; bảng expiry và phần giải thích đang dùng nhãn khác nhau. Giữ một bảng domain/BVA chuẩn rồi tham chiếu lại sẽ dễ bảo vệ khi vấn đáp.

9. **Một số thành phần bàn giao còn chưa đồng bộ.**

   - Không còn `scripts/`, nhưng bug reports và video script vẫn yêu cầu chạy `node scripts/run-api.cjs ...`; người chấm chưa thể tái chạy harness từ repo hiện tại.
   - README và disclosure dẫn `Appendix_A_Prompt_Log.md` không tồn tại.
   - Khai báo công cụ ghi Antigravity/Claude, trong khi audit chứa các tương tác Codex. Nếu dùng cả hai, cần khai báo rõ cả hai.
   - AI-03/AI-05 đã xác nhận human review, nhưng AI-02 và các review vẫn ghi chưa có.
   - Git hiện chỉ có **Initial commit**, còn log đính kèm liệt kê **23 commits**; cần làm rõ và bảo đảm log khớp lịch sử được nộp.
   - Video vẫn chờ upload; GitHub Issues vẫn chưa có. Phần nhóm tiếp tục để cuối theo cách bạn đã chọn. PDF/đóng gói là bước bạn tự thực hiện sau.

**Mỗi bug nên được hoàn thiện đến mức người khác tái hiện được mà không phải đoán:**

| Phần | Chi tiết cần có |
|---|---|
| Bối cảnh | Baseline, môi trường, tài khoản/quyền và trạng thái dữ liệu |
| Oracle | Rule SRS cụ thể bị vi phạm |
| Reproduction | Bước đánh số, endpoint/header/body đầy đủ hoặc thao tác UI chính xác |
| Expected/Actual | Số liệu, response và hậu điều kiện đúng bằng chứng |
| Evidence | Ảnh cụ thể kèm chú thích; link raw record đúng TC |
| Phạm vi lỗi | Các biến thể đã xác nhận, TC liên quan |
| Tác động | Hậu quả đã quan sát và rủi ro dự kiến được phân biệt |
| Trạng thái | Xác minh, screenshot, Issue URL và retest |

Thứ tự nên làm là **sửa dữ liệu sai → đồng bộ test/report/summary → viết BUG-A03 và BUG-D01 → hoàn thiện khả năng tái hiện của 15 bug còn lại → bổ sung đúng những evidence còn thiếu → video và phần nhóm**. Không cần tăng số test hoặc kéo dài mô tả để giống bài tham khảo.

Mình chưa chỉnh sửa file hay chạy lại SUT trong lượt review này.
````

</details>

### Record R015 — user

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T19:48:53.386Z`. Source: `rollout-2026-10-20T02-41-42-01a15369-b96b-7cb2-8351-4a091cdedffe_01a155af-20a2-7fe1-b0e4-6ad2d65641e3.jsonl`.

<details>
<summary>Verbatim user message</summary>

````text
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Hãy viết lại thật đầy đủ, chi tiết cho từng loại, bugs có thể chia thành từng id cho từng file luôn hoặc chung 1 file theo domain tùy bạn. Sau khi viết lại toàn bộ thì kiểm tra lại tất cả và so sánh với yêu cầu của đề bài xem còn thiếu sót gì nữa không? Video thì cứ cho link temp vậy đi, vì tôi đang quay, đảm bảo có nên cứ đặt đó và tui sẽ tự đặt link vào sau.

````

</details>

### Record R016 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T19:48:58.325Z`. Source: `rollout-2026-10-20T02-41-42-01a15369-b96b-7cb2-8351-4a091cdedffe_01a155af-20a2-7fe1-b0e4-6ad2d65641e3.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình sẽ viết lại toàn bộ báo cáo, phân tích Domain/BVA, test cases và bug reports; giữ mỗi bug một file để dễ đối chiếu và đăng Issue. Sau đó mình sẽ kiểm tra chéo số liệu, bằng chứng, liên kết và từng yêu cầu của đề. Video sẽ để một link tạm thống nhất để bạn thay sau.

Mình dùng `mattpocock-skills:implement` cho lượt chỉnh sửa này; tự làm trong chat, không dùng subagent hay Computer Use.
````

</details>

### Record R017 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T19:50:49.702Z`. Source: `rollout-2026-10-20T02-41-42-01a15369-b96b-7cb2-8351-4a091cdedffe_01a155af-20a2-7fe1-b0e4-6ad2d65641e3.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Mình đã giữ bản sao trước khi sửa ở ngoài repo và khôi phục các script API cần thiết để bài có thể tái chạy. Mình cũng đã kiểm tra lại ảnh: case BIGBUY 500001 đủ chứng minh kết quả áp mã qua ô tổng tiền, nên sẽ ghi rõ biến thể đó; case VIP100 chưa chứng minh trạng thái hết lượt thì vẫn để thiếu bằng chứng. Màn Mobile còn thiếu hiển thị danh mục theo mapping FR-20 → FR-06 đang dùng, mình sẽ ghi thành bug riêng thay vì giữ PASS cho case “đầy đủ thông tin”.
````

</details>

### Record R018 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T19:59:29.544Z`. Source: `rollout-2026-10-20T02-41-42-01a15369-b96b-7cb2-8351-4a091cdedffe_01a155af-20a2-7fe1-b0e4-6ad2d65641e3.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
81 API cases đã chạy lại xong, kết quả vẫn là **37 PASS / 42 FAIL / 2 OBSERVATION**, không có case bị chặn; hash source và database SUT gốc đều giữ nguyên.

Bản viết lại đang dùng chung TC-ID, domain ID và verdict giữa các tài liệu. Mình tách rõ case đã xác nhận, quan sát chưa có oracle và case thiếu bằng chứng; đồng thời giữ prompt/output cũ nguyên văn để audit thể hiện đúng lịch sử chỉnh sửa.
````

</details>

### Record R019 — assistant

Tool: OpenAI Codex. Timestamp UTC: `2026-10-19T20:05:37.494Z`. Source: `rollout-2026-10-20T02-41-42-01a15369-b96b-7cb2-8351-4a091cdedffe_01a155af-20a2-7fe1-b0e4-6ad2d65641e3.jsonl`.

<details>
<summary>Verbatim assistant message</summary>

````text
Bản nội dung mới đã hoàn tất: **18 bug files**, bốn phân tích Domain/BVA và 114 test cases chi tiết. Kiểm tra liên kết, số liệu và truy vết hiện đều qua; tổng đúng là **109 case đủ bằng chứng kết luận**, còn năm case thiếu một phần bằng chứng.

Mình đang rà soát lượt cuối theo đề và ghi Git history thực của lần viết lại. Các bước còn cần bạn bổ sung sẽ nằm trong `hw02/TASKS.md`, ngoài repo nộp bài; video dùng link tạm như bạn yêu cầu.
````

</details>

## C. Output artifacts và snapshot boundary

Full original AI artifact outputs được giữ nguyên trong AI-02 Appendix B, kể cả nội dung draft đã được sửa hoặc dời khỏi submission. Bản hiện tại nằm trong report/reports/tests/bugs/scripts và Git commits của lượt viết lại; không dùng nội dung snapshot lịch sử để mô tả trạng thái hiện tại. Final assistant response sau thời điểm snapshot chưa thể nằm trong export này.
