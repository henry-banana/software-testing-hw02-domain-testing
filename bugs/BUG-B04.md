# BUG-B04 - Apply coupon bỏ qua JWT thiếu, sai và hết hạn

| Field | Value |
|---|---|
| Bug ID | BUG-B04 |
| Feature | FR-09 - Áp dụng mã giảm giá |
| Severity | High - đề xuất kỹ thuật, xem Impact |
| Status | Reproduced; SUT chưa được sửa |
| Seam | API |
| Oracle | FR-09 C4 |
| SUT baseline | 85af3ba875c88283615e22cb108f13e2fccaf0e9 |
| Affected TCs | [B-API-19](../tests/B-FR09-discount-coupons.md#b-api-19), [B-API-20](../tests/B-FR09-discount-coupons.md#b-api-20), [B-API-21](../tests/B-FR09-discount-coupons.md#b-api-21) |
| GitHub Issue | [#37](https://github.com/tkob-team/eshop-sut/issues/37) - OPEN |
| Screenshot coverage | Có raw API trace; còn thiếu ảnh terminal/API cho Issue |

## 1. Mô tả và điều kiện kích hoạt

Apply coupon bỏ qua JWT thiếu, sai và hết hạn. POST /api/apply-coupon không gắn authenticateToken middleware.

Lỗi được nhóm theo behavior; các giá trị biên/biến thể cùng nguyên nhân không tạo một bug mới cho mỗi TC FAIL.

## 2. Environment và preconditions

- Reset tám coupon; user2/VIP100 used=0, limit=2; user3 used=0. Coupon trong request phải có đúng type/value/minimum của fixture.
- Authentication request mục tiêu: `none`.

Run xác nhận: Windows, Node v24.16.0; backend copy tại `http://127.0.0.1:3100`; SUT clock cố định `2026-10-19T08:00:00.000Z`. Timestamp actual dùng UTC thật. Source/database gốc được đối chiếu SHA-256 trước/sau suite và không thay đổi. Header `Content-Type: application/json`; `Authorization: Bearer <JWT đúng role>` trừ missing/invalid/expired case. Demo login và dữ liệu nominal đầy đủ có trong [fixture của test report](../tests/B-FR09-discount-coupons.md#1-phạm-vi-quy-ước-và-fixture).

## 3. Steps to Reproduce

1. Chuẩn bị isolated fixture và lấy JWT đúng role như Preconditions; xác minh nominal trước khi thay điều kiện mục tiêu.
2. Gửi `POST /api/apply-coupon` với authentication `none` và JSON Input bên dưới.
3. Đối chiếu response và hậu điều kiện với Expected; chỉ GET/readback là quan sát, fixture SQL không được dùng làm oracle.

### Request mục tiêu đầy đủ của representative

`POST /api/apply-coupon`; authentication `none`.

```json
{
  "code": "BIGBUY",
  "total_amount": 600000,
  "user_id": 2
}
```

Tái hiện qua HTTP theo request, authentication và preconditions nêu trên. Full raw record giữ nguyên kết quả thực thi; script hỗ trợ chạy được quản lý ngoài repository nộp bài.

## 4. Expected Result

Reject invalid/missing authentication (401/403).

Expected bắt buộc ở mức hành vi của SRS/mapping. HTTP status hoặc câu chữ error chỉ là contract bắt buộc khi có nguồn; không tự yêu cầu một error string cụ thể nếu SRS không quy định. Với request bị reject, dữ liệu phải giữ nguyên theo hậu điều kiện.

## 5. Actual Result và hậu điều kiện

Timestamp UTC: `2026-10-19T19:50:59.280Z`. Trace sau giữ nguyên request/status/field values; danh sách dài chỉ giữ row liên quan và row_count, full record được liên kết.

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "none",
    "input": {
      "code": "BIGBUY",
      "total_amount": 600000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 150,
      "discount_amount": 50000,
      "final_amount": 550000,
      "message": "Áp dụng thành công! Giảm 50,000 ₫"
    }
  }
]
```

[Full record B-API-19](../evidence/execution/B-api.md#b-api-19).

## 6. Các biến thể và traceability

| TC | Input | Status | Evidence |
|---|---|---|---|
| B-API-19 | {"code": "BIGBUY", "total_amount": 600000, "user_id": 2} | FAIL | [raw](../evidence/execution/B-api.md#b-api-19) |
| B-API-20 | {"code": "BIGBUY", "total_amount": 600000, "user_id": 2} | FAIL | [raw](../evidence/execution/B-api.md#b-api-20) |
| B-API-21 | {"code": "BIGBUY", "total_amount": 600000, "user_id": 2} | FAIL | [raw](../evidence/execution/B-api.md#b-api-21) |

## 7. Impact và severity rationale

Client không xác thực vẫn nhận phép tính giảm giá. Apply không ghi coupon_usage nên chưa chứng minh làm cạn lượt của người khác.

Severity High được đề xuất theo ảnh hưởng tới tính đúng đắn dữ liệu, quyền truy cập hoặc phép tính tiền của behavior này; chưa phải mức do giảng viên duyệt. Bug không đồng nghĩa một sự cố production đã xảy ra.

## 8. Root Cause và hướng khắc phục đề xuất

POST /api/apply-coupon không gắn authenticateToken middleware.

[Source baseline](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/backend/server.js). Source giải thích cơ chế; xác nhận runtime dựa trên evidence ở trên.

Xác thực token trước xử lý coupon; kết hợp lấy identity từ JWT.

Đây là đề xuất, chưa sửa SUT và chưa chạy retest sau fix.

## 9. Screenshots và GitHub Issue

Raw HTTP record là evidence của run đã thực hiện. Chưa có screenshot API thật cho bug này; không dùng ảnh một UI khác làm chứng cứ thay thế.

Issue URL/number: [#37](https://github.com/tkob-team/eshop-sut/issues/37). Đã đăng và đọc lại bằng GitHub CLI. Đã có ảnh phần đầu trang Issue; ảnh bug đính kèm và phần nội dung phía dưới chưa được xác minh lại; [trạng thái evidence](../evidence/github-issues/README.md). Không coi việc tạo Issue là đã có screenshot.

### Ảnh trang Issue

![BUG-B04 Issue #37 - phần đầu trang](../evidence/github-issues/BUG-B04_issue-01.png)

## 10. Regression checklist

- Chạy lại representative và các lân cận/biến thể liên quan trong bảng TC.
- Kiểm valid nominal vẫn thành công, invalid không làm đổi state.
- Với auth/role: kiểm riêng none/invalid/user/admin; với API+UI: retest cả hai lớp.
- Ghi run mới sau fix riêng; giữ evidence baseline hiện tại để đối chiếu.
