**Khoa Công nghệ Thông tin (FIT) - Trường Đại học Khoa học Tự nhiên (HCMUS)**

**CS423 / CSC15003 - Kiểm chứng Phần mềm (AI-augmented, 2026)**

**CHÍNH SÁCH AI, BIỂU MẪU - 2026 v1.0**

# Biểu mẫu Khai báo Sử dụng AI

*Đính kèm cho mọi bài tập có dùng AI ở bất kỳ mức nào.*

*Tài liệu được biên soạn lại từ Med Kharbach, PhD (2026) - Mẫu Chính sách Sử dụng AI cho Giáo dục Đại học. Giấy phép CC BY-NC-SA 4.0. Phiên bản này được FIT@HCMUS điều chỉnh cho môn CS423 / CSC15003 Kiểm chứng Phần mềm.*

## 1. Thông tin Môn học & Sinh viên

| Mục               | Giá trị                                |
|-------------------|----------------------------------------|
| Môn học:          | CS423 / CSC13003 - Kiểm chứng Phần mềm |
| Mã bài tập:       | HW02-AI |
| Tên bài tập:      | Domain Testing and Boundary Value Analysis on EShop |
| Cấp độ AI (1-5):  | Cấp4 - AI hỗ trợ sản xuất; Bloom-AI G9.2/G9.3 theo đề |
| Ngày:             | 20/10/2026 (ngày cập nhật; không phải ngày ký) |
| Họ tên sinh viên: | Tống Dương Thái Hòa |
|                   |                                        |
| MSSV:             | 23120262 |

## 2. Câu hỏi Khai báo

### 1. Công cụ AI đã dùng:

*Liệt kê mọi công cụ AI dùng cho bài tập này (ví dụ AI Tool (e.g., ChatGPT, Claude, Gemini), ChatGPT, GitHub Copilot, Cursor, Gemini).*

OpenAI Codex: có transcript kèm timestamp trong Appendix_A_Prompt_Log.md. Antigravity IDE / Claude Sonnet: theo khai báo của sinh viên ở bản trước; chưa có transcript tương ứng để gán từng tương tác cho Claude.

### 2. Giai đoạn nào của bài tập có dùng AI:

*Tick tất cả: [ ] brainstorm [ ] outline [ ] viết nháp [ ] phản hồi [ ] sửa chữa [ ] code [ ] phân tích dữ liệu [ ] thiết kế đồ hoạ [ ] khác (ghi rõ).*

[x] brainstorm [x] outline [x] viết nháp [x] phản hồi [x] sửa chữa [x] code [x] phân tích dữ liệu [ ] thiết kế đồ hoạ [x] khác: phân tích SRS, Domain/BVA, HTTP test execution và kiểm chứng evidence. Ảnh UI và video do sinh viên thực hiện.

### 3. Prompt / nhiệm vụ chính cho AI:

*Dán nguyên văn 2-3 prompt quan trọng nhất. Để xem đầy đủ, đính kèm Phụ lục A (prompt_log.md).*

**Prompt1, OpenAI Codex, 19/10/2026 14:50:32 +07:00:**

````text
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Bắt đầu làm full đi. Đổi phần ai/ thành ai-audit, xóa interactions/, và các file kia phải giữa nguyên đúng tên của [templates](templates/). Lưu ý mọi doc bạn viết đều ở dạng markdown hết, còn định dạng cuối ra sao thì tui sẽ tự thực hiện. À có thể tham khảo [https://github.com/bingsu1103/23120205-HW02-AI-DomainTesting](https://github.com/bingsu1103/23120205-HW02-AI-DomainTesting) để xem họ sắp xếp ra sao? Soạn lại tasks chi tiết hơn để bạn nắm đi
````

**Prompt2, OpenAI Codex, 20/10/2026 02:48:53 +07:00:**

````text
[@mattpocock-skills](plugin://mattpocock-skills@mattpocock) Hãy viết lại thật đầy đủ, chi tiết cho từng loại, bugs có thể chia thành từng id cho từng file luôn hoặc chung 1 file theo domain tùy bạn. Sau khi viết lại toàn bộ thì kiểm tra lại tất cả và so sánh với yêu cầu của đề bài xem còn thiếu sót gì nữa không? Video thì cứ cho link temp vậy đi, vì tôi đang quay, đảm bảo có nên cứ đặt đó và tui sẽ tự đặt link vào sau.
````

Nội dung gốc và timestamp đối chiếu tại [Appendix A](../Appendix_A_Prompt_Log.md); bản Markdown chuẩn hóa dấu câu, dữ liệu gốc giữ trong [source-records.json](../evidence/ai-originals/source-records.json).

### 4. Phần cụ thể AI đóng góp:

*Càng cụ thể càng tốt. Ví dụ: 'AI sinh TC01-TC15 ở Mục 3.2; tôi viết lại TC04 và TC11; AI KHÔNG đóng góp vào Mục 1, 2, 4, hoặc AI Critique.'*

AI hỗ trợ bốn phân tích reports/,114test cases,18bug reports, báo cáo chính, script ngoài repo và skill domain-bva-testing. API có81TC thực thi thật trên backend copy; không dùng API/build để nhận là UI đã chạy. Sinh viên cung cấp71ảnh UI, xác nhận các case dùng ảnh chung, quay video và quyết định nộp. Đoạn AI Critique245từ giữ theo bản đã cung cấp; không tự viết trải nghiệm hoặc ký thay. Việc điền lại biểu mẫu lần này cũng có AI hỗ trợ. Đã đăng18Issues #31-#48 bằngCLI; sinh viên tự đính kèm ảnh và chụp trangIssue, không dùngComputerUse hoặc tạo nhánh repo nhóm.

### 5. Cách tôi rà soát / chỉnh sửa / xác minh đầu ra AI:

*Mô tả phương pháp xác minh (chạy test, kiểm tra spec, hỏi TA, tra RFC, đối chiếu ISTQB syllabus, v.v.).*

Đã đối chiếu oracle SRS baseline85af3ba, payload/response/readback thật và nội dung ảnh. Source chỉ giải thích nguyên nhân, không tạo expected. Các sửa kỹ thuật có bằng chứng gồm contractFR17, literal tiền giảm, mappingcase, phonefrontend và usagefixture. Hiện có114TC:53PASS/57FAIL/4OBSERVATION,0INCOMPLETE. Lecture và phê duyệt cuối của sinh viên vẫn cần xác nhận riêng; không coi technical validator là chữ ký humanreview.

### 6. Trích dẫn (nếu môn yêu cầu):

*Môn Kiểm chứng Phần mềm dùng phong cách IEEE. Ví dụ: Anthropic. (2026). AI Tool (e.g., ChatGPT, Claude, Gemini) \[Large language model\]. https://claude.ai*

[1] OpenAI, "Codex," công cụ AI hỗ trợ phân tích và soạn thảo; transcript nguồn kèm timestamp tại Appendix A. [Online]. Available: https://openai.com/codex/

[2] ISTQB, "Certified Tester Foundation Level Syllabus v4.0.1," 2024, mục4.2.1-4.2.2. [Online]. Available: https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf

[3] Đề HW02 và EShop SRS baseline85af3ba là nguồn yêu cầu; tool Claude/Antigravity chỉ được khai theo thông tin sinh viên đã cung cấp, không bịa phiên bản model hoặc timestamp.

## 3. Cam đoan Trung thực

*Bằng việc ký tên dưới đây, tôi cam đoan thông tin khai báo ở trên là chính xác và đầy đủ. Tôi hiểu rằng việc không khai báo hoặc khai báo sai lệch về việc dùng AI sẽ bị coi là vi phạm liêm chính học thuật và có thể dẫn đến điểm 0 cho bài tập cùng việc bị chuyển lên hội đồng kỷ luật.*


Thông tin hành chính đã được điền; ngày ký và chữ ký của bản cập nhật này để sinh viên xác nhận sau khi đọc lại. Chữ ký cũ ngày2026-10-19 được bảo toàn trong dữ liệu nguồn, không tự chuyển thành chữ ký mới.

## Chữ ký

| Họ tên sinh viên (in hoa): | TỐNG DƯƠNG THÁI HÒA |
|----------------------------|----------------------------------------|
| MSSV:                      | 23120262 |
| Lớp / Khoá:                | Software Testing - CQ2023/3 |
| Môn học:                   | CS423 / CSC13003 - Kiểm chứng Phần mềm |
| Giảng viên:                |                                        |
| Ngày:                      |                                        |
| Chữ ký:                    |                                        |

## Tham khảo

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.

- ISTQB Foundation Level Syllabus (latest version).

- Hardman, P. (2025). A Post-AI Learning Taxonomy.

- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.

- Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.

- Anthropic (2025). Building reliable AI test agents - engineering blog.

- DeepEval & Promptfoo documentation - testing frameworks for LLM systems.
