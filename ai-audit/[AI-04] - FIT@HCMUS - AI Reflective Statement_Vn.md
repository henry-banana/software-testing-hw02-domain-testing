**Khoa Công nghệ Thông tin (FIT) - Trường Đại học Khoa học Tự nhiên (HCMUS)**

**CS423 / CSC15003 - Kiểm chứng Phần mềm (AI-augmented, 2026)**

**CHÍNH SÁCH AI, BIỂU MẪU - 2026 v1.0**

# Bài Suy ngẫm về Sử dụng AI

*Bắt buộc cho Project lớn, Seminar, Đồ án Tốt nghiệp. Áp dụng khi bài nộp ở Cấp độ AI 4 hoặc 5.*

*Tài liệu được biên soạn lại từ Med Kharbach, PhD (2026) - Mẫu Chính sách Sử dụng AI cho Giáo dục Đại học. Giấy phép CC BY-NC-SA 4.0. Phiên bản này được FIT@HCMUS điều chỉnh cho môn CS423 / CSC13003 Kiểm chứng Phần mềm.*

## 1. Thông tin Project & Tác giả

| Mục                            | Giá trị                                |
|--------------------------------|----------------------------------------|
| Môn học:                       | CS423 / CSC13003 - Kiểm chứng Phần mềm |
| Tên Project / Đồ án:           | HW02-AI - Domain Testing on EShop |
| Thành viên nhóm (nếu là nhóm): | Bài cá nhân; dùng GitHub Issues nhóm tkob-team/eshop-sut |
| Họ tên sinh viên:              | Tống Dương Thái Hòa |
| MSSV:                          | 23120262 |
| Ngày nộp:                      | Sinh viên điền khi nộp |

## 2. Câu hỏi Suy ngẫm

### 1. AI đã hỗ trợ công việc của bạn như thế nào?

*Mô tả cụ thể AI đóng góp ở đâu trong project: thiết kế test, brainstorm scenario, sinh code, phân tích log, triage defect, viết tài liệu, chuẩn bị slide, v.v.*

AI hỗ trợ phân tích SRS choFR04/FR09/FR17/MobileproductDetail, phân lớp domain, lựa chọn biên và thiết kế114TC. AI còn hỗ trợ harness/APIexecution, đọc log, đối chiếu ảnh, nhóm18bugs và soạn tài liệu. Ảnh giao diện, quay video và xác nhận thao tác thực tế thuộc phần sinh viên thực hiện.

### 2. Bạn chấp nhận / từ chối / sửa gì từ đầu ra AI?

*Liệt kê đề xuất AI bạn dùng, đề xuất bạn loại bỏ, và cách bạn điều chỉnh cho phù hợp với spec, nguyên tắc ISTQB, hoặc phân tích của bạn.*

Chúng tôi giữ cách phân rã input/state và traceability; loại bỏ yêu cầu Edit không có trongFR17 và kết luận Mobile đã chạy chỉ dựa trên API/build. Các bản sửa gồm snake_case/enum/endpoint, literal tiền giảm, domainID và phân biệt fixtureused2 với hai đơn mới. Bảng audit ghi rõ verdict và phần sửa, không dùng số FAIL của SUT làm số lỗi AI.

### 3. Bạn nhận ra lỗi / bias / giới hạn nào trong đầu ra AI?

*Ví dụ cụ thể: AI bịa hàm, sai boundary, miss security case, hiểu sai metric (p95 vs top 5%), bịa trích dẫn, v.v.*

Các thiếu sót đã quan sát gồm coi Unicode digits là invalid khiSRS chưa quy định, dùng nhãn BVA cho empty/decimal ngoài miền nguyên, suy persistence từ alert và suy usageexhausted từ một ảnh nominal. Đây là vấn đề giả định và trạng thái, không đủ căn cứ để kết luận model nào tốt hơn qua một thí nghiệm chưa thực hiện.

### 4. Bạn xác minh thông tin / nguồn / claim của AI như thế nào?

*Mô tả phương pháp xác minh (chạy test, kiểm tra spec, tra RFC, hỏi TA, đối chiếu công cụ khác, thực thi trên SUT thật).*

Chúng tôi dùng SRS làm oracle, kiểm rawHTTP/readback và71ảnh thật; kiểmsource để giải thích nguyên nhân. Baseline vàsource/databasehash được ghi riêng; timestampUI không tự dựng từ tên ảnh. Tính nhất quán được kiểm bằngTC-ID, mappingbug, số liệu, links vàSHA256. Kết quả validator không thay phần đọc lecture và phê duyệt nội dung của sinh viên.

### 5. Bạn học được điều gì qua project này mà nếu chỉ chấp nhận đầu ra AI thì sẽ không học được?

*Suy ngẫm về đóng góp trí tuệ của chính bạn. AI đã định hình (hay không) sự hiểu của bạn về testing như thế nào? Một nguyên tắc bạn sẽ giữ cho tương lai?*

Nguyên tắc rút ra là giữ expected độc lập với implementation và chỉ kết luận đến mức evidence chứng minh. Đoạn AI Critique đã cung cấp được giữ dưới đây; câu trả lời biểu mẫu hiện tại cần sinh viên đọc lại trước khi ký.

**AI Critique (245 từ, giữ đoạn đã cung cấp):**

<!-- AI-CRITIQUE-BEGIN -->
Trong bài HW02, AI hỗ trợ chuyển yêu cầu thành bảng domain, boundary và test cases. Tuy nhiên, đầu ra đầu tiên vẫn chứa giả định cần sửa. Ví dụ, chữ số Unicode ban đầu bị xem chắc chắn không hợp lệ, trong khi SRS chưa quy định encoding. Case này được chuyển thành observation, thay vì dùng để tăng số bug. Một giới hạn khác là AI dễ dùng nhãn BVA quá rộng. Input rỗng hoặc số thập phân không phải điểm lân cận của biên trên miền số nguyên. Thiết kế đã tách các lớp này khỏi boundary số lượng 0, 1, 2. Với coupon, ví dụ phần trăm có đáp số nguyên giúp kết luận lỗi công thức mà không phụ thuộc quy tắc làm tròn chưa được đặc tả. Nguyên nhân các thiếu sót là yêu cầu chưa đầy đủ và xu hướng bổ sung hành vi quen thuộc khi AI nhận ra tên chức năng. Tên CRUD có thể khiến AI tự yêu cầu Edit, còn kết quả API có thể bị diễn giải thành Mobile đã chạy. Báo cáo vì vậy giới hạn kết luận theo nguồn và loại bằng chứng. Nguyên tắc rút ra là giữ expected độc lập với implementation, kiểm tra hậu điều kiện và phân biệt kết quả đã chạy với phần chưa quan sát. Human review vẫn cần thiết; sinh viên phải kiểm tra UI và giải thích các quyết định trước khi nộp.
<!-- AI-CRITIQUE-END -->

## 3. Các Cấp độ AI đã dùng

Đánh dấu mọi cấp độ đã áp dụng ở bất kỳ giai đoạn nào:

- [ ] Cấp 1 - Không AI

- [x] Cấp 2 - AI cho chuẩn bị

- [x] Cấp 3 - AI cho phản hồi / chỉnh sửa

- [x] Cấp 4 - AI hỗ trợ sản xuất

- [ ] Cấp 5 - AI là phương pháp cốt lõi

## 4. Chữ ký Tác giả

*Bằng việc ký dưới đây, tôi cam đoan bài suy ngẫm này trung thực và phản ánh chính xác cách AI được dùng trong project. Tôi chịu hoàn toàn trách nhiệm trí tuệ cho sản phẩm cuối.*


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
