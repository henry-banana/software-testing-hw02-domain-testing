# BUG-A01 - API chấp nhận và lưu phone không hợp lệ

| Field | Value |
|---|---|
| Bug ID | BUG-A01 |
| Feature | FR-04 - Quản lý hồ sơ cá nhân |
| Severity | High - đề xuất kỹ thuật, xem Impact |
| Status | Reproduced; SUT chưa được sửa |
| Seam | API |
| Oracle | FR-04.2 |
| SUT baseline | 85af3ba875c88283615e22cb108f13e2fccaf0e9 |
| Affected TCs | [A-API-03](../tests/A-FR04-profile.md#a-api-03), [A-API-04](../tests/A-FR04-profile.md#a-api-04), [A-API-05](../tests/A-FR04-profile.md#a-api-05), [A-API-06](../tests/A-FR04-profile.md#a-api-06), [A-API-07](../tests/A-FR04-profile.md#a-api-07), [A-API-08](../tests/A-FR04-profile.md#a-api-08), [A-API-09](../tests/A-FR04-profile.md#a-api-09), [A-API-10](../tests/A-FR04-profile.md#a-api-10), [A-API-11](../tests/A-FR04-profile.md#a-api-11), [A-API-12](../tests/A-FR04-profile.md#a-api-12), [A-API-13](../tests/A-FR04-profile.md#a-api-13), [A-API-14](../tests/A-FR04-profile.md#a-api-14), [A-API-16](../tests/A-FR04-profile.md#a-api-16) |
| GitHub Issue | [#31](https://github.com/tkob-team/eshop-sut/issues/31) - OPEN |
| Screenshot coverage | Có raw API trace; còn thiếu ảnh terminal/API cho Issue |

## 1. Mô tả và điều kiện kích hoạt

API chấp nhận và lưu phone không hợp lệ. Route PUT lấy phone từ body rồi UPDATE mà không validate prefix/length/charset.

Lỗi được nhóm theo behavior; các giá trị biên/biến thể cùng nguyên nhân không tạo một bug mới cho mỗi TC FAIL.

## 2. Environment và preconditions

- Khôi phục profile user2/user3 như fixture chung; JWT user2 trừ TC auth. Giữ name/address và các field không phải mục tiêu hợp lệ.
- Authentication request mục tiêu: `user`.

Run xác nhận: Windows, Node v24.16.0; backend copy tại `http://127.0.0.1:3100`; SUT clock cố định `2026-10-19T08:00:00.000Z`. Timestamp actual dùng UTC thật. Source/database gốc được đối chiếu SHA-256 trước/sau suite và không thay đổi. Header `Content-Type: application/json`; `Authorization: Bearer <JWT đúng role>` trừ missing/invalid/expired case. Demo login và dữ liệu nominal đầy đủ có trong [fixture của test report](../tests/A-FR04-profile.md#1-phạm-vi-quy-ước-và-fixture).

## 3. Steps to Reproduce

1. Chuẩn bị isolated fixture và lấy JWT đúng role như Preconditions; xác minh nominal trước khi thay điều kiện mục tiêu.
2. Gửi `PUT /api/users/me` với authentication `user` và JSON Input bên dưới.
3. Gửi `GET /api/users/me` với authentication `user`; không có request body.
4. Đối chiếu response và hậu điều kiện với Expected; chỉ GET/readback là quan sát, fixture SQL không được dùng làm oracle.

### Request mục tiêu đầy đủ của representative

`PUT /api/users/me`; authentication `user`.

```json
{
  "name": "HW02 User",
  "shipping_address": "1 Test Street",
  "phone": "091234567"
}
```

Tái hiện qua HTTP theo request, authentication và preconditions nêu trên. Full raw record giữ nguyên kết quả thực thi; script hỗ trợ chạy được quản lý ngoài repository nộp bài.

## 4. Expected Result

Reject; stored phone stays 0912345678.

Expected bắt buộc ở mức hành vi của SRS/mapping. HTTP status hoặc câu chữ error chỉ là contract bắt buộc khi có nguồn; không tự yêu cầu một error string cụ thể nếu SRS không quy định. Với request bị reject, dữ liệu phải giữ nguyên theo hậu điều kiện.

## 5. Actual Result và hậu điều kiện

Timestamp UTC: `2026-10-19T19:50:57.797Z`. Trace sau giữ nguyên request/status/field values; danh sách dài chỉ giữ row liên quan và row_count, full record được liên kết.

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "091234567"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "091234567"
    }
  }
]
```

[Full record A-API-03](../evidence/execution/A-api.md#a-api-03).

## 6. Các biến thể và traceability

| TC | Input | Status | Evidence |
|---|---|---|---|
| A-API-03 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "091234567"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-03) |
| A-API-04 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "091234567890"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-04) |
| A-API-05 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": ""} | FAIL | [raw](../evidence/execution/A-api.md#a-api-05) |
| A-API-06 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "0"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-06) |
| A-API-07 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "09123456"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-07) |
| A-API-08 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "0912345678901"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-08) |
| A-API-09 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "1912345678"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-09) |
| A-API-10 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "19123456789"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-10) |
| A-API-11 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "091234567a"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-11) |
| A-API-12 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "09123 5678"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-12) |
| A-API-13 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "+84912345678"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-13) |
| A-API-14 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": "09123-5678"} | FAIL | [raw](../evidence/execution/A-api.md#a-api-14) |
| A-API-16 | {"name": "HW02 User", "shipping_address": "1 Test Street", "phone": null} | FAIL | [raw](../evidence/execution/A-api.md#a-api-16) |

## 7. Impact và severity rationale

Profile lưu dữ liệu không đạt định dạng; các tác động tới giao hàng chỉ là rủi ro, chưa test hệ thống SMS/OTP.

Severity High được đề xuất theo ảnh hưởng tới tính đúng đắn dữ liệu, quyền truy cập hoặc phép tính tiền của behavior này; chưa phải mức do giảng viên duyệt. Bug không đồng nghĩa một sự cố production đã xảy ra.

## 8. Root Cause và hướng khắc phục đề xuất

Route PUT lấy phone từ body rồi UPDATE mà không validate prefix/length/charset.

[Source baseline](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/backend/server.js). Source giải thích cơ chế; xác nhận runtime dựa trên evidence ở trên.

Validate phone ở backend trước UPDATE; reject phải giữ dữ liệu cũ. Không chỉ dựa frontend.

Đây là đề xuất, chưa sửa SUT và chưa chạy retest sau fix.

## 9. Screenshots và GitHub Issue

Raw HTTP record là evidence của run đã thực hiện. Chưa có screenshot API thật cho bug này; không dùng ảnh một UI khác làm chứng cứ thay thế.

Issue URL/number: [#31](https://github.com/tkob-team/eshop-sut/issues/31). Đã đăng và đọc lại bằng GitHub CLI. Ảnh bug đính kèm và ảnh trang Issue còn chờ sinh viên bổ sung; [trạng thái evidence](../evidence/github-issues/README.md). Không coi việc tạo Issue là đã có screenshot.

## 10. Regression checklist

- Chạy lại representative và các lân cận/biến thể liên quan trong bảng TC.
- Kiểm valid nominal vẫn thành công, invalid không làm đổi state.
- Với auth/role: kiểm riêng none/invalid/user/admin; với API+UI: retest cả hai lớp.
- Ghi run mới sau fix riêng; giữ evidence baseline hiện tại để đối chiếu.
