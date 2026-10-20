# Biểu mẫu Khai báo Sử dụng AI — HW02

## 1. Thông tin Môn học & Sinh viên

Tống Dương Thái Hòa — 23120262 — Software Testing CQ2023/3. Môn CSC13003; bài HW02-AI Domain Testing on EShop. AI policy Open; Bloom-AI G9.2 Apply/G9.3 Analyse.

## 2. Công cụ, nhiệm vụ và đóng góp

| Công cụ | Nguồn xác định | Đóng góp được ghi nhận |
|---|---|---|
| OpenAI Codex | Transcript nguyên văn có timestamp trong Appendix A | Planning, phân tích SRS, Domain/BVA, cases, harness, API execution, evidence review, bug reports và viết lại Markdown |
| Antigravity IDE / Claude Sonnet | Khai báo trong bản sinh viên cung cấp trước lượt viết lại | Công cụ bổ sung do sinh viên khai; không gán transcript Codex cho Claude khi chưa có log tương ứng |

## 3. Prompt, output và phần AI sinh

[Prompt/output log](../Appendix_A_Prompt_Log.md) ghi ngày giờ thật theo nguồn; AI-02 giữ original output snapshot. AI đã soạn report, reports/tests/bugs, scripts và skill. 81 API TC được chạy bằng HTTP thật trên backend copy; source/database gốc được đối chiếu hash. 33 UI TC dùng ảnh thật sinh viên cung cấp; verdict mới giữ rõ 2 TC INCOMPLETE (A-UI-07/B-UI-06); ba case C/D được sinh viên xác nhận bằng ảnh.

## 4. Kiểm tra và sửa đầu ra

SRS baseline85af3ba là oracle; raw HTTP/ảnh thật là actual. Các corrections gồm enum/field/endpoint contract, literal tiền giảm, TC/domain mapping, false PASS category, usage precondition và evidence thiếu. Expected không lấy từ implementation; source chỉ giải thích cơ chế. Không dùng subagent hoặc Computer Use trong các phiên Codex được ghi.

## 5. Trách nhiệm và human review

Thao tác UI, ảnh, quay video và quyết định nộp bài do sinh viên thực hiện. Bản trước có xác nhận do sinh viên cung cấp. Vì tài liệu vừa được viết lại, sinh viên cần đọc lại bản hiện tại, xác nhận critique đúng trải nghiệm và thay video URL trước khi nộp. Không tự gán mọi correction kỹ thuật cho sinh viên phát hiện.

## 6. Cam đoan và chữ ký đã cung cấp

Khối dưới giữ nguyên từ bản sinh viên cung cấp trước lượt rewrite, không phải chữ ký mới hoặc xác nhận đã đọc bản rewrite. Sinh viên cập nhật khi kiểm tra bản cuối.

## Chữ ký

| Họ tên | MSSV | Lớp | Ngày ký | Chữ ký |
|---|---|---|---|---|
| Tống Dương Thái Hòa | 23120262 | CQ2023/3 | 2026-10-19 | Tống Dương Thái Hòa |
