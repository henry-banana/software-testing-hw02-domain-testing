# BUG-B01 — Coupon bị từ chối khi tổng tiền bằng đúng ngưỡng

| Field | Value |
|---|---|
| Bug ID | BUG-B01 |
| Feature | FR-09 — Áp dụng mã giảm giá |
| Severity | High — đề xuất kỹ thuật, xem Impact |
| Status | Reproduced; SUT chưa được sửa |
| Seam | API + UI |
| Oracle | FR-09 C3 |
| SUT baseline | 85af3ba875c88283615e22cb108f13e2fccaf0e9 |
| Affected TCs | [B-API-03](../tests/B-FR09-discount-coupons.md#b-api-03), [B-API-06](../tests/B-FR09-discount-coupons.md#b-api-06), [B-API-24](../tests/B-FR09-discount-coupons.md#b-api-24), [B-UI-02](../tests/B-FR09-discount-coupons.md#b-ui-02) |
| GitHub Issue | Chưa đăng; cập nhật URL/number sau giai đoạn nhóm |
| Screenshot coverage | Có ảnh UI cụ thể dưới đây |

## 1. Mô tả và điều kiện kích hoạt

Coupon bị từ chối khi tổng tiền bằng đúng ngưỡng. Nhánh accept dùng total_amount > coupon.min_order_amount, bỏ equality.

Lỗi được nhóm theo behavior; các giá trị biên/biến thể cùng nguyên nhân không tạo một bug mới cho mỗi TC FAIL.

## 2. Environment và preconditions

- Reset tám coupon; user2/VIP100 used=0, limit=2; user3 used=0. Coupon trong request phải có đúng type/value/minimum của fixture.
- Authentication request mục tiêu: `user`.

Run xác nhận: Windows, Node v24.16.0; backend copy tại `http://127.0.0.1:3100`; SUT clock cố định `2026-10-19T08:00:00.000Z`. Timestamp actual dùng UTC thật. Source/database gốc được đối chiếu SHA-256 trước/sau suite và không thay đổi. Header `Content-Type: application/json`; `Authorization: Bearer <JWT đúng role>` trừ missing/invalid/expired case. Demo login và dữ liệu nominal đầy đủ có trong [fixture của test report](../tests/B-FR09-discount-coupons.md#1-phạm-vi-quy-ước-và-fixture).

## 3. Steps to Reproduce

1. Chuẩn bị isolated fixture và lấy JWT đúng role như Preconditions; xác minh nominal trước khi thay điều kiện mục tiêu.
2. Gửi `POST /api/apply-coupon` với authentication `user` và JSON Input bên dưới.
3. Đối chiếu response và hậu điều kiện với Expected; chỉ GET/readback là quan sát, fixture SQL không được dùng làm oracle.

### Request mục tiêu đầy đủ của representative

`POST /api/apply-coupon`; authentication `user`.

```json
{
  "code": "BIGBUY",
  "total_amount": 500000,
  "user_id": 2
}
```

Tái hiện qua HTTP theo request, authentication và preconditions nêu trên. Full raw record giữ nguyên kết quả thực thi; script hỗ trợ chạy được quản lý ngoài repository nộp bài.

## 4. Expected Result

discount=50000; final=450000.

Expected bắt buộc ở mức hành vi của SRS/mapping. HTTP status hoặc câu chữ error chỉ là contract bắt buộc khi có nguồn; không tự yêu cầu một error string cụ thể nếu SRS không quy định. Với request bị reject, dữ liệu phải giữ nguyên theo hậu điều kiện.

## 5. Actual Result và hậu điều kiện

Timestamp UTC: `2026-10-19T19:50:58.904Z`. Trace sau giữ nguyên request/status/field values; danh sách dài chỉ giữ row liên quan và row_count, full record được liên kết.

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "BIGBUY",
      "total_amount": 500000,
      "user_id": 2
    },
    "status": 400,
    "body": {
      "error": "Đơn hàng chưa đủ giá trị tối thiểu 500,000 ₫ để áp dụng mã này"
    }
  }
]
```

[Full record B-API-03](../evidence/execution/B-api.md#b-api-03).

## 6. Các biến thể và traceability

| TC | Input | Status | Evidence |
|---|---|---|---|
| B-API-03 | {"code": "BIGBUY", "total_amount": 500000, "user_id": 2} | FAIL | [raw](../evidence/execution/B-api.md#b-api-03) |
| B-API-06 | {"code": "SAVE10", "total_amount": 300000, "user_id": 2} | FAIL | [raw](../evidence/execution/B-api.md#b-api-06) |
| B-API-24 | {"code": "VIP100", "total_amount": 300000, "user_id": 2} | FAIL | [raw](../evidence/execution/B-api.md#b-api-24) |
| B-UI-02 | {"code": "BIGBUY", "total": 500000} | FAIL | [UI case](../tests/B-FR09-discount-coupons.md#b-ui-02) |

## 7. Impact và severity rationale

Đơn vừa đạt ngưỡng bị từ chối mã dù điều kiện total≥minimum đã thỏa.

Severity High được đề xuất theo ảnh hưởng tới tính đúng đắn dữ liệu, quyền truy cập hoặc phép tính tiền của behavior này; chưa phải mức do giảng viên duyệt. Bug không đồng nghĩa một sự cố production đã xảy ra.

## 8. Root Cause và hướng khắc phục đề xuất

Nhánh accept dùng total_amount > coupon.min_order_amount, bỏ equality.

[Source baseline](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/backend/server.js). Source giải thích cơ chế; xác nhận runtime dựa trên evidence ở trên.

Dùng total_amount >= minimum ở nhánh accept; giữ test M−1/M/M+1.

Đây là đề xuất, chưa sửa SUT và chưa chạy retest sau fix.

## 9. Screenshots và GitHub Issue

![B-UI-02_01-input](../evidence/screenshots/B/B-UI-02_01-input.png)

![B-UI-02_02-response](../evidence/screenshots/B/B-UI-02_02-response.png)

Issue URL/number: **chờ cập nhật sau phần cá nhân**. Nội dung file này có thể dùng làm Issue body; cần đính kèm ảnh thật của đúng bug và lưu ảnh trang Issue vào `evidence/github-issues/` khi đăng. Không coi placeholder là Issue đã tồn tại.

## 10. Regression checklist

- Chạy lại representative và các lân cận/biến thể liên quan trong bảng TC.
- Kiểm valid nominal vẫn thành công, invalid không làm đổi state.
- Với auth/role: kiểm riêng none/invalid/user/admin; với API+UI: retest cả hai lớp.
- Ghi run mới sau fix riêng; giữ evidence baseline hiện tại để đối chiếu.
