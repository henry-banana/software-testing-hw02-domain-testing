# Feature C - FR-17 - Quản lý mã giảm giá

### 5.1. Requirements và oracle

| Rule | Nội dung theo SRS | Domain |
|---|---|---|
| FR-17.1 | Admin có thể Thêm/Xem/Xóa; không có yêu cầu Update cụ thể | C-D1/D8-D10 |
| FR-17.2 | Required: code,type,discount_value,expired_at,min_order_amount,max_uses_per_user | C-D2 |
| FR-17.3 | code duy nhất; type chỉ percent/fixed | C-D3/D4 |
| FR-17.4 | discount_value>0; min_order_amount>=0; max_uses_per_user>=1 | C-D5-D7 |
| FR-12 / SEC-03 | Admin API phải kiểm tra role=admin trong token | C-D8-D10 |

[Nguồn SRS cố định](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md). Các nhãn rule trong bảng được dùng để truy vết giữa yêu cầu, domain và test case.

Contract API: POST `/api/admin/coupons`; GET `/api/coupons`; DELETE `/api/admin/coupons/:id`. Body snake_case, enum `percent`/`fixed`. Tên "CRUD" không tự tạo yêu cầu Update.

### 5.2. Domain Testing - quy trình từng bước

#### Bước 1 - Xác định inputs/outputs

Vector gồm `(requester role/JWT, code, type, discount_value, min_order_amount, expired_at, max_uses_per_user, operation)`. Đầu ra gồm phản hồi Create/List/Delete và trạng thái coupon đọc lại qua GET /api/coupons.

#### Bước 2 - Thiết lập nominal fixture

Payload nominal sử dụng code riêng biệt, enum hợp lệ, discount_value dương, min_order_amount không âm, expired_at và max_uses_per_user hợp lệ. Admin thực hiện các case dữ liệu; user thường và thiếu JWT được dùng cho các case quyền truy cập.

#### Bước 3 - Chia lớp hợp lệ/không hợp lệ

Các lớp bao gồm required fields, code rỗng/trùng, enum ngoài percent/fixed và miền số của ba trường giá trị. Authentication và role được phân lớp riêng cho từng operation Create/List/Delete.

#### Bước 4 - Cô lập một điều kiện sai

Từng required field được bỏ riêng trong khi năm trường còn lại hợp lệ. Các case zero, negative và enum sai giữ code unique cùng quyền Admin, giúp tránh lỗi uniqueness hoặc authorization che khuất validation mục tiêu.

#### Bước 5 - Chọn đại diện và giải thích

Giá trị -1, 0, 1 và 2 được chọn theo ràng buộc từng trường. Code trùng được kiểm tra bằng số row và dữ liệu đọc lại. Create, View và Delete được đánh giá riêng; phạm vi không bao gồm Update.

#### Bước 6 - Phân tích cross-constraint

Payload hợp lệ vẫn phải đáp ứng role của operation. Sau Create, các trường phải khớp dữ liệu gửi; sau Delete, coupon đích phải biến mất và coupon đối chứng được giữ nguyên. Một route có kiểm tra quyền không đại diện cho các route còn lại.

#### Bước 7 - Đối chiếu hypothesis bằng thực thi

Các request POST/DELETE được theo sau bởi GET /api/coupons để kiểm tra hậu điều kiện. Admin UI cung cấp bằng chứng về coupon được tạo, hiển thị và xóa. Raw records được dùng để phân biệt zero bị đổi thành 1 với negative được giữ nguyên.

#### Bước 8 - Review coverage và AI output

Contract snake_case, enum percent/fixed và endpoint readback được đối chiếu với API specification. Mapping C-API-12/13 và C-API-18/19 được kiểm tra theo input thực tế. Uniqueness đạt nên không lập Issue cho điều kiện code trùng.

### 5.3. Domain partition và traceability

| Domain ID | Chiều/lớp | Loại | Representative | Expected | TC coverage |
|---|---|---|---|---|---|
| C-D1 | Nominal coupon | Valid | fixed và percent; đầy đủ required fields | Tạo và GET lại đúng dữ liệu | [C-API-01](../tests/C-FR17-coupon-management.md#c-api-01), [C-API-02](../tests/C-FR17-coupon-management.md#c-api-02), [C-UI-02](../tests/C-FR17-coupon-management.md#c-ui-02) |
| C-D2 | Required field presence | Invalid | Thiếu từng field trong 6 field; code rỗng | Reject; số row không tăng | [C-API-03](../tests/C-FR17-coupon-management.md#c-api-03), [C-API-04](../tests/C-FR17-coupon-management.md#c-api-04), [C-API-05](../tests/C-FR17-coupon-management.md#c-api-05), [C-API-06](../tests/C-FR17-coupon-management.md#c-api-06), [C-API-07](../tests/C-FR17-coupon-management.md#c-api-07), [C-API-08](../tests/C-FR17-coupon-management.md#c-api-08), [C-API-09](../tests/C-FR17-coupon-management.md#c-api-09) |
| C-D3 | Code uniqueness | Invalid duplicate | SAVE10 đã tồn tại | Không tạo bản ghi trùng | [C-API-10](../tests/C-FR17-coupon-management.md#c-api-10), [C-UI-05](../tests/C-FR17-coupon-management.md#c-ui-05) |
| C-D4 | Type enum | Invalid | type=other | Chỉ percent/fixed được chấp nhận | [C-API-11](../tests/C-FR17-coupon-management.md#c-api-11) |
| C-D5 | discount_value > 0 | Boundary | -1/0/1 VND trong fixture | Reject/reject/accept | [C-API-12](../tests/C-FR17-coupon-management.md#c-api-12), [C-API-13](../tests/C-FR17-coupon-management.md#c-api-13), [C-API-14](../tests/C-FR17-coupon-management.md#c-api-14), [C-UI-01](../tests/C-FR17-coupon-management.md#c-ui-01) |
| C-D6 | min_order_amount >= 0 | Boundary | -1/0/1 VND | Reject/accept/accept | [C-API-15](../tests/C-FR17-coupon-management.md#c-api-15), [C-API-16](../tests/C-FR17-coupon-management.md#c-api-16), [C-API-17](../tests/C-FR17-coupon-management.md#c-api-17), [C-UI-03](../tests/C-FR17-coupon-management.md#c-ui-03) |
| C-D7 | max_uses_per_user >= 1 | Boundary | -1/0/1/2 lần | Reject/reject/accept/accept | [C-API-18](../tests/C-FR17-coupon-management.md#c-api-18), [C-API-19](../tests/C-FR17-coupon-management.md#c-api-19), [C-API-20](../tests/C-FR17-coupon-management.md#c-api-20), [C-API-21](../tests/C-FR17-coupon-management.md#c-api-21), [C-UI-04](../tests/C-FR17-coupon-management.md#c-ui-04) |
| C-D8 | Create permission | Role/auth | Admin/user/none/invalid JWT | Chỉ admin tạo được | [C-API-01](../tests/C-FR17-coupon-management.md#c-api-01), [C-API-22](../tests/C-FR17-coupon-management.md#c-api-22), [C-API-23](../tests/C-FR17-coupon-management.md#c-api-23), [C-API-24](../tests/C-FR17-coupon-management.md#c-api-24) |
| C-D9 | List permission | Role/auth | Admin/user/none | Admin allow; user/none deny | [C-API-25](../tests/C-FR17-coupon-management.md#c-api-25), [C-API-26](../tests/C-FR17-coupon-management.md#c-api-26), [C-API-27](../tests/C-FR17-coupon-management.md#c-api-27) |
| C-D10 | Delete permission | Role/auth | Admin/user/none; coupon có thật | Admin xóa đúng row; user/none không xóa | [C-API-28](../tests/C-FR17-coupon-management.md#c-api-28), [C-API-29](../tests/C-FR17-coupon-management.md#c-api-29), [C-API-30](../tests/C-FR17-coupon-management.md#c-api-30), [C-UI-06](../tests/C-FR17-coupon-management.md#c-ui-06) |

### 5.4. Boundary Value Analysis - từng bước

1. Các biến số được xác định là discount_value, min_order_amount và max_uses_per_user.
2. Ràng buộc lần lượt là v > 0, m >= 0 và k >= 1, trong đó k là số lượt nguyên.
3. Fixture tiền dùng bước 1 VND; fixture số lượt dùng bước 1 lượt. Các trường khác và quyền Admin được giữ nominal.
4. Các điểm -1/0/1 và 0/1/2 được chọn theo từng ràng buộc, kèm negative interior để kiểm tra đường xử lý giá trị âm.
5. Sau Create, dữ liệu đọc lại được đối chiếu với input để phân biệt chấp nhận dữ liệu sai và biến đổi dữ liệu ngầm.
6. expired_at bị thiếu được kiểm tra như required-field domain; quy tắc cấm tạo mã hết hạn không được bổ sung khi SRS không quy định.

| Biến | Rule | Delta/precision | Điểm chọn và giải thích | Cases |
|---|---|---|---|---|
| discount_value v | v > 0 | 1 VND trong fixture | -1 invalid; 0 ON invalid; +1 valid. Không tuyên bố 1 là số dương nhỏ nhất của miền số thực | C-API-12-14; C-UI-01 |
| min_order_amount m | m >= 0 | 1 VND | -1 invalid; 0 ON valid; +1 valid | C-API-15-17; C-UI-03 |
| max_uses_per_user k | k >= 1, k là số lượt | 1 lượt | 0 invalid; 1 ON valid; 2 valid; -1 thêm invalid interior | C-API-18-21; C-UI-04 |
| expired_at presence | Field bắt buộc | Không áp BVA ngày ở create | Thiếu field là Domain; SRS không cấm tạo mã hết hạn | C-API-07 |

### 5.5. Kết quả thực thi

| TC | Status | Actual tóm tắt | Bug |
|---|---|---|---|
| [C-API-01](../tests/C-FR17-coupon-management.md#c-api-01) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":13}<br>GET /api/coupons -> HTTP 200: array 9 rows | - |
| [C-API-02](../tests/C-FR17-coupon-management.md#c-api-02) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":22}<br>GET /api/coupons -> HTTP 200: array 9 rows | - |
| [C-API-03](../tests/C-FR17-coupon-management.md#c-api-03) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":31}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-01, FR17-02, FR17-03, FR17-04, FR17-05, FR17-06, FR17-07 |
| [C-API-04](../tests/C-FR17-coupon-management.md#c-api-04) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":40}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-01, FR17-02, FR17-03, FR17-04, FR17-05, FR17-06, FR17-07 |
| [C-API-05](../tests/C-FR17-coupon-management.md#c-api-05) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":49}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-01, FR17-02, FR17-03, FR17-04, FR17-05, FR17-06, FR17-07 |
| [C-API-06](../tests/C-FR17-coupon-management.md#c-api-06) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":58}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-01, FR17-02, FR17-03, FR17-04, FR17-05, FR17-06, FR17-07 |
| [C-API-07](../tests/C-FR17-coupon-management.md#c-api-07) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":67}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-01, FR17-02, FR17-03, FR17-04, FR17-05, FR17-06, FR17-07 |
| [C-API-08](../tests/C-FR17-coupon-management.md#c-api-08) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":76}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-01, FR17-02, FR17-03, FR17-04, FR17-05, FR17-06, FR17-07 |
| [C-API-09](../tests/C-FR17-coupon-management.md#c-api-09) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":85}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-01, FR17-02, FR17-03, FR17-04, FR17-05, FR17-06, FR17-07 |
| [C-API-10](../tests/C-FR17-coupon-management.md#c-api-10) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 500: {"error":"SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code"}<br>GET /api/coupons -> HTTP 200: array 8 rows | - |
| [C-API-11](../tests/C-FR17-coupon-management.md#c-api-11) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":102}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-08 |
| [C-API-12](../tests/C-FR17-coupon-management.md#c-api-12) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":111}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-09, FR17-10 |
| [C-API-13](../tests/C-FR17-coupon-management.md#c-api-13) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":120}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-09, FR17-10 |
| [C-API-14](../tests/C-FR17-coupon-management.md#c-api-14) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":129}<br>GET /api/coupons -> HTTP 200: array 9 rows | - |
| [C-API-15](../tests/C-FR17-coupon-management.md#c-api-15) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":138}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-11 |
| [C-API-16](../tests/C-FR17-coupon-management.md#c-api-16) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":147}<br>GET /api/coupons -> HTTP 200: array 9 rows | - |
| [C-API-17](../tests/C-FR17-coupon-management.md#c-api-17) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":156}<br>GET /api/coupons -> HTTP 200: array 9 rows | - |
| [C-API-18](../tests/C-FR17-coupon-management.md#c-api-18) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":165}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-12, FR17-13 |
| [C-API-19](../tests/C-FR17-coupon-management.md#c-api-19) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":174}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-12, FR17-13 |
| [C-API-20](../tests/C-FR17-coupon-management.md#c-api-20) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":183}<br>GET /api/coupons -> HTTP 200: array 9 rows | - |
| [C-API-21](../tests/C-FR17-coupon-management.md#c-api-21) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":192}<br>GET /api/coupons -> HTTP 200: array 9 rows | - |
| [C-API-22](../tests/C-FR17-coupon-management.md#c-api-22) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 401: {"error":"Unauthorized"}<br>GET /api/coupons -> HTTP 200: array 8 rows | - |
| [C-API-23](../tests/C-FR17-coupon-management.md#c-api-23) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 200: {"message":"Coupon created","id":209}<br>GET /api/coupons -> HTTP 200: array 9 rows | FR17-14 |
| [C-API-24](../tests/C-FR17-coupon-management.md#c-api-24) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>POST /api/admin/coupons -> HTTP 403: {"error":"Forbidden"}<br>GET /api/coupons -> HTTP 200: array 8 rows | - |
| [C-API-25](../tests/C-FR17-coupon-management.md#c-api-25) | PASS | GET /api/coupons -> HTTP 200: array 8 rows | - |
| [C-API-26](../tests/C-FR17-coupon-management.md#c-api-26) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows | FR17-15 |
| [C-API-27](../tests/C-FR17-coupon-management.md#c-api-27) | PASS | GET /api/coupons -> HTTP 401: {"error":"Unauthorized"} | - |
| [C-API-28](../tests/C-FR17-coupon-management.md#c-api-28) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>DELETE /api/admin/coupons/249 -> HTTP 200: {"message":"Coupon deleted"}<br>GET /api/coupons -> HTTP 200: array 7 rows | - |
| [C-API-29](../tests/C-FR17-coupon-management.md#c-api-29) | FAIL | GET /api/coupons -> HTTP 200: array 8 rows<br>DELETE /api/admin/coupons/257 -> HTTP 200: {"message":"Coupon deleted"}<br>GET /api/coupons -> HTTP 200: array 7 rows | FR17-16 |
| [C-API-30](../tests/C-FR17-coupon-management.md#c-api-30) | PASS | GET /api/coupons -> HTTP 200: array 8 rows<br>DELETE /api/admin/coupons/265 -> HTTP 401: {"error":"Unauthorized"}<br>GET /api/coupons -> HTTP 200: array 8 rows | - |
| [C-UI-01](../tests/C-FR17-coupon-management.md#c-ui-01) | FAIL | Coupon có discount_value=0 được tạo và xuất hiện trong danh sách. | FR17-09, FR17-10 |
| [C-UI-02](../tests/C-FR17-coupon-management.md#c-ui-02) | PASS | Sau reload, ảnh danh sách vẫn có HW02_C_UI_02: fixed, discount_value=1, min_order_amount=0, expired_at=2099-12-31, max_uses_per_user=1. Ảnh danh sách được dùng chung cho C-UI-02/C-UI-06, kết hợp xác nhận thao tác sau reload. | - |
| [C-UI-03](../tests/C-FR17-coupon-management.md#c-ui-03) | FAIL | Coupon với min_order_amount=-1 được tạo và hiển thị ngưỡng âm. | FR17-11 |
| [C-UI-04](../tests/C-FR17-coupon-management.md#c-ui-04) | PASS | Browser native validation chặn max_uses_per_user=0 ở bước submit. Đây là PASS của frontend rejection; C-API-19 vẫn FAIL ở backend. | - |
| [C-UI-05](../tests/C-FR17-coupon-management.md#c-ui-05) | PASS | Tạo trùng SAVE10 trả lỗi UNIQUE. Source/schema và C-API-10 xác nhận không có bản ghi trùng; không tự đặt HTTP 409 làm oracle. | - |
| [C-UI-06](../tests/C-FR17-coupon-management.md#c-ui-06) | PASS | Ảnh trước đó có HW02_DELETE_UI; ảnh danh sách dùng chung không còn coupon này, vẫn còn HW02_C_UI_02 và SAVE10. Xác nhận thao tác xác định ảnh chung thuộc bước sau xóa/reload của C-UI-06. | - |

### 5.6. Spec vs Code và findings

| ID | Điều kiện vi phạm | Oracle / root cause |
|---|---|---|
| [FR17-01](../bugs/FR17-01.md) | Coupon creation accepts a missing required code | FR-17 required fields; The creation route passes request values directly to SQLite without required-field checks. |
| [FR17-02](../bugs/FR17-02.md) | Coupon creation accepts a missing required type | FR-17 required fields; The creation route passes request values directly to SQLite without required-field checks. |
| [FR17-03](../bugs/FR17-03.md) | Coupon creation accepts a missing required discount_value | FR-17 required fields; The creation route passes request values directly to SQLite without required-field checks. |
| [FR17-04](../bugs/FR17-04.md) | Coupon creation accepts a missing required min_order_amount | FR-17 required fields; The creation route passes request values directly to SQLite without required-field checks. |
| [FR17-05](../bugs/FR17-05.md) | Coupon creation accepts a missing required expired_at | FR-17 required fields; The creation route passes request values directly to SQLite without required-field checks. |
| [FR17-06](../bugs/FR17-06.md) | Coupon creation accepts a missing required max_uses_per_user | FR-17 required fields; The creation route passes request values directly to SQLite without required-field checks. |
| [FR17-07](../bugs/FR17-07.md) | Coupon creation accepts an empty code | FR-17 required fields; The creation route passes request values directly to SQLite without required-field checks. |
| [FR17-08](../bugs/FR17-08.md) | Coupon creation persists a type outside percent and fixed | FR-17 enum; Neither the route nor database schema enforces the declared enum. |
| [FR17-09](../bugs/FR17-09.md) | Coupon creation accepts a negative discount_value | FR-17 discount_value > 0; There is no positive-value validation before INSERT. |
| [FR17-10](../bugs/FR17-10.md) | Coupon creation accepts discount_value equal to zero | FR-17 discount_value > 0; There is no positive-value validation before INSERT. |
| [FR17-11](../bugs/FR17-11.md) | Coupon creation accepts a negative min_order_amount | FR-17 min_order_amount >= 0; The route has no nonnegative minimum check. |
| [FR17-12](../bugs/FR17-12.md) | Coupon creation accepts a negative max_uses_per_user | FR-17 max_uses_per_user >= 1; The expression max_uses_per_user || 1 substitutes only falsy input and does not validate the range. |
| [FR17-13](../bugs/FR17-13.md) | Coupon creation silently changes a zero max_uses_per_user to one | FR-17 max_uses_per_user >= 1; The expression max_uses_per_user || 1 substitutes only falsy input and does not validate the range. |
| [FR17-14](../bugs/FR17-14.md) | A regular user can create an administrator coupon | FR-17 admin operation; SEC-03; The route verifies token presence/validity without checking role=admin. |
| [FR17-15](../bugs/FR17-15.md) | A regular user can read the administrator coupon list | FR-17 admin view; SEC-03; The management-list route lacks an admin-role check. |
| [FR17-16](../bugs/FR17-16.md) | A regular user can delete an administrator coupon | FR-17 admin delete; SEC-03; The delete route authenticates the token but never checks its role. |
| [FR17-17](../bugs/FR17-17.md) | Coupon form omits required-field markers | FR-22 required markers; FR-17 required fields; The form uses placeholders and bare controls without required-field labels/markers. |

### 5.7. AI gap analysis

Các sai lệch trong đầu ra AI và cách hiệu chỉnh được đối chiếu với rule, raw record và ảnh tương ứng. Bản nháp gốc được lưu trong AI audit snapshot.

| Gap | Nhóm nguyên nhân | Evidence/điều sai | Cách sửa |
|---|---|---|---|
| Contract bị đổi khi diễn giải | Giới hạn công cụ | Draft dùng camelCase, enum FIXED/PERCENTAGE và GET sai endpoint | Khôi phục snake_case, percent/fixed, GET /api/coupons |
| Sai TC mapping zero/negative | Giới hạn công cụ | Draft đảo C-API-12/13 và 18/19 | Đối chiếu input raw, không dựa thứ tự trong mô tả prose |
| CRUD naming và duplicate status | Prompt/assumption | Tên CRUD không có Update; duplicate500 vẫn không nhân bản | Không tạo bug missing Update hoặc unique-status409 |
| UI block và API acceptance | Độ phức tạp nhiều seam | C-UI-04 chặn 0 nhưng C-API-19 vẫn accept/default1 | UI PASS, API FAIL, không gán một verdict cho cả hai |

### 5.8. Coverage và giới hạn

Coverage gồm required fields, enum, code uniqueness, các miền số và quyền truy cập riêng cho Create/List/Delete. Các case được truy vết từ domain đến dữ liệu đọc lại và bug. C-UI-02/C-UI-06 dùng chung ảnh danh sách kết hợp xác nhận thao tác; tính dùng chung của bằng chứng được ghi rõ trong kết quả. Update không thuộc phạm vi FR-17 đã chọn.

[Detailed test cases](../tests/C-FR17-coupon-management.md), [Raw API evidence](../evidence/execution/C-api.md), [Bug index](../bugs/bug-reports.md).


### Kiểm thử contract và state bổ sung

| Domain | Chiều phân hoạch | Oracle / controls | TC-ID | Kết luận |
|---|---|---|---|---|
| C-D11 | Required form affordance | Các nhãn trường bắt buộc phải có dấu * theo FR-22; đối chiếu trong DOM thật. | C-UI-07 | FR17-17 |

Các lớp bổ sung được suy từ contract, security property và state transition; không gắn nhãn BVA cho boolean/DOM/enum. Riêng phone Mobile dùng cùng các biên độ dài 9/10/11/12, với các chiều prefix được cô lập.

| TC-ID | Seam | Status | Actual / bug |
|---|---|---|---|
| [C-UI-07](../tests/C-FR17-coupon-management.md#c-ui-07) | UI | FAIL | Required coupon fields have visible required markers / FR17-17 |

AI gap mới: validate dữ liệu và authorization chưa bao phủ đầy đủ quy định hiển thị bắt buộc của FR-22. C-UI-07 đọc DOM và ảnh form thật; đây là lỗi affordance riêng, không trùng lỗi backend chấp nhận dữ liệu sai.

[A execution](../evidence/execution/A-execution.md), [B execution](../evidence/execution/B-execution.md), [C execution](../evidence/execution/C-execution.md), [D execution](../evidence/execution/D-execution.md).
