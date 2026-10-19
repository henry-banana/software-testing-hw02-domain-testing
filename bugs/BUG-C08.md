# BUG-C08 — User thường đọc được danh sách coupon quản trị

| Field | Value |
|---|---|
| Bug ID | BUG-C08 |
| Feature | FR-17 — Quản lý mã giảm giá |
| Severity | Medium — đề xuất kỹ thuật, xem Impact |
| Status | Reproduced; SUT chưa được sửa |
| Seam | API |
| Oracle | FR-12 / SEC-03 / FR-17 |
| SUT baseline | 85af3ba875c88283615e22cb108f13e2fccaf0e9 |
| Affected TCs | [C-API-26](../tests/C-FR17-coupon-management.md#c-api-26) |
| GitHub Issue | Chưa đăng; cập nhật URL/number sau giai đoạn nhóm |
| Screenshot coverage | Có raw API trace; còn thiếu ảnh terminal/API cho Issue |

## 1. Mô tả và điều kiện kích hoạt

User thường đọc được danh sách coupon quản trị. GET /api/coupons chỉ xác thực token; không kiểm tra role. Đây là endpoint Admin UI dùng xem danh sách.

Lỗi được nhóm theo behavior; các giá trị biên/biến thể cùng nguyên nhân không tạo một bug mới cho mỗi TC FAIL.

## 2. Environment và preconditions

- Reset coupon list có SAVE10 và DELETE_ME. Admin token dùng cho GET trước/sau; token của request mục tiêu theo bảng dưới. Chỉ thay field/role được nêu.
- Authentication request mục tiêu: `user`.

Run xác nhận: Windows, Node v24.16.0; backend copy tại `http://127.0.0.1:3100`; SUT clock cố định `2026-10-19T08:00:00.000Z`. Timestamp actual dùng UTC thật. Source/database gốc được đối chiếu SHA-256 trước/sau suite và không thay đổi. Header `Content-Type: application/json`; `Authorization: Bearer <JWT đúng role>` trừ missing/invalid/expired case. Demo login và dữ liệu nominal đầy đủ có trong [fixture của test report](../tests/C-FR17-coupon-management.md#1-phạm-vi-quy-ước-và-fixture).

## 3. Steps to Reproduce

1. Chuẩn bị isolated fixture và lấy JWT đúng role như Preconditions; xác minh nominal trước khi thay điều kiện mục tiêu.
2. Gửi `GET /api/coupons` với authentication `user`; không có request body.
3. Đối chiếu response và hậu điều kiện với Expected; chỉ GET/readback là quan sát, fixture SQL không được dùng làm oracle.

### Request mục tiêu đầy đủ của representative

`GET /api/coupons`; authentication `user`.

Không gửi request body. Target ID lấy từ GET list fixture trước thao tác.

Chạy tự động từ repository: `node scripts/run-api.cjs C`. Runner reset fixture từng TC, sở hữu server riêng, dừng server khi kết thúc; chọn record `C-API-26` trong raw output. Hướng dẫn setup chung nằm ở README.

## 4. Expected Result

Reject non-admin access (401/403).

Expected bắt buộc ở mức hành vi của SRS/mapping. HTTP status hoặc câu chữ error chỉ là contract bắt buộc khi có nguồn; không tự yêu cầu một error string cụ thể nếu SRS không quy định. Với request bị reject, dữ liệu phải giữ nguyên theo hậu điều kiện.

## 5. Actual Result và hậu điều kiện

Timestamp UTC: `2026-10-19T20:08:01.407Z`. Trace sau giữ nguyên request/status/field values; danh sách dài chỉ giữ row liên quan và row_count, full record được liên kết.

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "row_count": 8,
      "relevant_rows": [
        {
          "id": 226,
          "code": "SAVE10",
          "type": "percent",
          "discount_value": 10,
          "min_order_amount": 300000,
          "expired_at": "2099-12-31",
          "is_active": 1,
          "max_uses_per_user": 1
        },
        {
          "id": 233,
          "code": "DELETE_ME",
          "type": "fixed",
          "discount_value": 1,
          "min_order_amount": 0,
          "expired_at": "2099-12-31",
          "is_active": 1,
          "max_uses_per_user": 1
        }
      ]
    }
  }
]
```

[Full record C-API-26](../evidence/execution/C-api.md#c-api-26).

## 6. Các biến thể và traceability

| TC | Input | Status | Evidence |
|---|---|---|---|
| C-API-26 | {} | FAIL | [raw](../evidence/execution/C-api.md#c-api-26) |

## 7. Impact và severity rationale

User thường nhận toàn bộ danh sách coupon trong API tested. Không suy diễn API này phải ở đường dẫn /api/admin/coupons.

Severity Medium được đề xuất theo ảnh hưởng tới tính đúng đắn dữ liệu, quyền truy cập hoặc phép tính tiền của behavior này; chưa phải mức do giảng viên duyệt. Bug không đồng nghĩa một sự cố production đã xảy ra.

## 8. Root Cause và hướng khắc phục đề xuất

GET /api/coupons chỉ xác thực token; không kiểm tra role. Đây là endpoint Admin UI dùng xem danh sách.

[Source baseline](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/backend/server.js). Source giải thích cơ chế; xác nhận runtime dựa trên evidence ở trên.

Enforce role hoặc tách public projection khỏi admin list theo thiết kế/SRS.

Đây là đề xuất, chưa sửa SUT và chưa chạy retest sau fix.

## 9. Screenshots và GitHub Issue

Raw HTTP record là evidence của run đã thực hiện. Chưa có screenshot API thật cho bug này; không dùng ảnh một UI khác làm chứng cứ thay thế.

Issue URL/number: **chờ cập nhật sau phần cá nhân**. Nội dung file này có thể dùng làm Issue body; cần đính kèm ảnh thật của đúng bug và lưu ảnh trang Issue vào `evidence/github-issues/` khi đăng. Không coi placeholder là Issue đã tồn tại.

## 10. Regression checklist

- Chạy lại representative và các lân cận/biến thể liên quan trong bảng TC.
- Kiểm valid nominal vẫn thành công, invalid không làm đổi state.
- Với auth/role: kiểm riêng none/invalid/user/admin; với API+UI: retest cả hai lớp.
- Ghi run mới sau fix riêng; giữ evidence baseline hiện tại để đối chiếu.
