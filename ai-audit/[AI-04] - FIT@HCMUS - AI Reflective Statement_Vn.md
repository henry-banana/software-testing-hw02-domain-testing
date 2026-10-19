# Bài Suy ngẫm về Sử dụng AI — HW02

## 1. Thông tin Project & Tác giả

Tống Dương Thái Hòa — 23120262 — Software Testing CQ2023/3; HW02-AI Domain Testing. Đoạn critique dưới đây giữ nguyên bản sinh viên đã cung cấp; không viết lại trải nghiệm cá nhân hoặc gán phát hiện mới thay sinh viên.

## 2. AI Critique — 245 từ

Trong bài HW02, AI hỗ trợ chuyển yêu cầu thành bảng domain, boundary và test cases. Tuy nhiên, đầu ra đầu tiên vẫn chứa giả định cần sửa. Ví dụ, chữ số Unicode ban đầu bị xem chắc chắn không hợp lệ, trong khi SRS chưa quy định encoding. Case này được chuyển thành observation, thay vì dùng để tăng số bug. Một giới hạn khác là AI dễ dùng nhãn BVA quá rộng. Input rỗng hoặc số thập phân không phải điểm lân cận của biên trên miền số nguyên. Thiết kế đã tách các lớp này khỏi boundary số lượng 0, 1, 2. Với coupon, ví dụ phần trăm có đáp số nguyên giúp kết luận lỗi công thức mà không phụ thuộc quy tắc làm tròn chưa được đặc tả. Nguyên nhân các thiếu sót là yêu cầu chưa đầy đủ và xu hướng bổ sung hành vi quen thuộc khi AI nhận ra tên chức năng. Tên CRUD có thể khiến AI tự yêu cầu Edit, còn kết quả API có thể bị diễn giải thành Mobile đã chạy. Báo cáo vì vậy giới hạn kết luận theo nguồn và loại bằng chứng. Nguyên tắc rút ra là giữ expected độc lập với implementation, kiểm tra hậu điều kiện và phân biệt kết quả đã chạy với phần chưa quan sát. Human review vẫn cần thiết; sinh viên phải kiểm tra UI và giải thích các quyết định trước khi nộp.

## 3. Technical addendum sau lần viết lại

Các gap mới được đối chiếu trong audit: sai contract API khi diễn giải, sai con số tiền giảm, trạng thái nominal khác exhausted usage, category Mobile bị chấm PASS thiếu căn cứ, và thiếu sequence của repeat Add. Đây là technical corrections của bản rewrite, không tự coi là nội dung sinh viên đã suy ngẫm/xác nhận. Critique245từ đáp ứng độ dài200–300; cần sinh viên đọc lại để bảo đảm vẫn phản ánh trải nghiệm thật.

## 4. Chữ ký Tác giả

| Họ tên | MSSV | Lớp | Ngày ký | Chữ ký |
|---|---|---|---|---|
| Tống Dương Thái Hòa | 23120262 | CQ2023/3 | 2026-10-19 | Tống Dương Thái Hòa |
