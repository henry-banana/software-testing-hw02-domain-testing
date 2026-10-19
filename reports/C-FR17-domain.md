# C — Domain Testing và Boundary Value Analysis

**Feature:** FR-17 — Quản lý mã giảm giá  
**SUT:** `85af3ba875c88283615e22cb108f13e2fccaf0e9`.

## 1. Requirements và oracle

| Rule | Nội dung theo SRS | Domain |
|---|---|---|
| FR-17.1 | Admin có thể Thêm/Xem/Xóa; không có yêu cầu Update cụ thể | C-D1/D8–D10 |
| FR-17.2 | Required: code,type,discount_value,expired_at,min_order_amount,max_uses_per_user | C-D2 |
| FR-17.3 | code duy nhất; type chỉ percent/fixed | C-D3/D4 |
| FR-17.4 | discount_value>0; min_order_amount≥0; max_uses_per_user≥1 | C-D5–D7 |
| FR-12 / SEC-03 | Admin API phải kiểm tra role=admin trong token | C-D8–D10 |

[Nguồn SRS cố định](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md). Các tên rule dạng FR-04.1 trong báo cáo là nhãn nội bộ để truy vết, không phải mã mới của SRS.

Contract API: POST `/api/admin/coupons`; GET `/api/coupons`; DELETE `/api/admin/coupons/:id`. Body snake_case, enum `percent`/`fixed`. Tên “CRUD” không tự tạo yêu cầu Update.

## 2. Domain Testing — quy trình từng bước

Chúng tôi lấy SRS làm oracle, sau đó dùng source để xây dựng giả thuyết và giải thích nguyên nhân. Source không thay thế yêu cầu. Mỗi TC có ID ổn định; một TC có thể phủ cả Domain Testing và BVA nhưng chỉ được tính một lần. Chúng tôi tách API với Web/Admin/Mobile UI vì validation ở một lớp không chứng minh lớp còn lại đạt.

Với từng input/state, chúng tôi xác định miền hợp lệ, phần bù không hợp lệ, precision và các ràng buộc giữa các chiều. Các lớp trong cùng một chiều được chọn để phân biệt hành vi; bảng nhiều chiều không có nghĩa mọi hàng đều là các tập rời nhau của toàn bộ vector. Test invalid giữ các chiều khác nominal; interaction nhiều lỗi có chủ đích được ghi riêng. Chúng tôi dùng readback public HTTP sau thay đổi để kiểm tra hậu điều kiện.

BVA được áp dụng cho miền có thứ tự, kể cả độ dài chuỗi và số lượt nguyên. Điểm ON nằm trên mặt biên; giá trị ON có thể hợp lệ hoặc không tùy dấu ≥ hay >. Các điểm lân cận được ghi bằng số và trạng thái valid/invalid để tránh nhập nhằng thuật ngữ. Các label OFF/IN không thay thế tập giá trị cụ thể. Rỗng, enum, charset và identity là Domain classes; không tự đặt một maximum mà SRS không quy định.

API execution dùng backend copy, clock cố định và fixture reset mỗi TC. UI evidence là ảnh thật đã cung cấp; không suy timestamp chạy từ ngày sửa file, không dùng ảnh vẽ hoặc build output làm bằng chứng UI. PASS/FAIL chỉ kết luận theo criterion có evidence; OBSERVATION dành cho oracle chưa quy định; INCOMPLETE dành cho TC còn thiếu bước/precondition/evidence. Một TC INCOMPLETE có thể đã được thao tác một phần, nhưng không được cộng vào executed đủ bằng chứng.

Chúng tôi kiểm tra kỹ thuật theo Domain/Boundary đã nêu; chưa có bản lecture của môn trong workspace để xác nhận đã đối chiếu mọi quy ước của giảng viên. Nguồn phương pháp bổ trợ là ISTQB CTFL §4.2.1–4.2.2. Các giới hạn này được giữ rõ trong phần coverage, không tuyên bố exhaustive coverage toàn hệ thống.

### Bước 1 — Xác định inputs/outputs

Vector `(requester role/JWT, code, type, discount_value, min_order_amount, expired_at, max_uses_per_user, operation)`. Output gồm thông báo, response và hậu điều kiện ở profile/coupon/cart tương ứng.

### Bước 2 — Thiết lập nominal fixture

Bỏ từng required field, giữ năm field còn lại đúng. Code unique được kiểm bằng row count; auth và role kiểm riêng cho Create/List/Delete vì một route đạt không chứng minh route khác đạt.

### Bước 3 — Chia lớp hợp lệ/không hợp lệ

Mỗi domain ID dưới đây mô tả một điều kiện hoặc chiều. Ghi representative, expected và TC phủ; phần không có oracle được tách observation.

### Bước 4 — Cô lập một điều kiện sai

Giữ fixture, auth và dữ liệu ngoài mục tiêu hợp lệ; ghi interaction nhiều lỗi riêng. Không dùng success response làm bằng chứng persistence nếu chưa readback.

### Bước 5 — Chọn đại diện và giải thích

Dùng giá trị dễ kiểm bằng tay; thêm các lân cận và identity/state classes. Một đại diện không chứng minh mọi phần tử của lớp đều đã chạy.

### Bước 6 — Phân tích cross-constraint

A: target=JWT user và role unchanged; B: C1∧C2∧C3∧C4∧C5; C: dữ liệu đúng vẫn cần role đúng; D: quantity ảnh hưởng cart và tổng tiền. Chỉ các ví dụ liên quan feature này được áp dụng.

### Bước 7 — Đối chiếu hypothesis bằng thực thi

Source đưa ra giả thuyết; API/ảnh UI kiểm hành vi công khai. Các bug hypothesis không được tính confirmed chỉ từ static suspicion.

### Bước 8 — Review coverage và AI output

Kiểm domain→TC→actual→bug; sửa metadata/expected sai. Giữ các vùng oracle chưa rõ và evidence thiếu ở trạng thái riêng.

## 3. Domain partition và traceability

| Domain ID | Chiều/lớp | Loại | Representative | Expected | TC coverage |
|---|---|---|---|---|---|
| C-D1 | Nominal coupon | Valid | fixed và percent; đầy đủ required fields | Tạo và GET lại đúng dữ liệu | [C-API-01](../tests/C-FR17-coupon-management.md#c-api-01), [C-API-02](../tests/C-FR17-coupon-management.md#c-api-02), [C-UI-02](../tests/C-FR17-coupon-management.md#c-ui-02) |
| C-D2 | Required field presence | Invalid | Thiếu từng field trong 6 field; code rỗng | Reject; số row không tăng | [C-API-03](../tests/C-FR17-coupon-management.md#c-api-03), [C-API-04](../tests/C-FR17-coupon-management.md#c-api-04), [C-API-05](../tests/C-FR17-coupon-management.md#c-api-05), [C-API-06](../tests/C-FR17-coupon-management.md#c-api-06), [C-API-07](../tests/C-FR17-coupon-management.md#c-api-07), [C-API-08](../tests/C-FR17-coupon-management.md#c-api-08), [C-API-09](../tests/C-FR17-coupon-management.md#c-api-09) |
| C-D3 | Code uniqueness | Invalid duplicate | SAVE10 đã tồn tại | Không tạo bản ghi trùng | [C-API-10](../tests/C-FR17-coupon-management.md#c-api-10), [C-UI-05](../tests/C-FR17-coupon-management.md#c-ui-05) |
| C-D4 | Type enum | Invalid | type=other | Chỉ percent/fixed được chấp nhận | [C-API-11](../tests/C-FR17-coupon-management.md#c-api-11) |
| C-D5 | discount_value > 0 | Boundary | −1/0/1 VND trong fixture | Reject/reject/accept | [C-API-12](../tests/C-FR17-coupon-management.md#c-api-12), [C-API-13](../tests/C-FR17-coupon-management.md#c-api-13), [C-API-14](../tests/C-FR17-coupon-management.md#c-api-14), [C-UI-01](../tests/C-FR17-coupon-management.md#c-ui-01) |
| C-D6 | min_order_amount ≥ 0 | Boundary | −1/0/1 VND | Reject/accept/accept | [C-API-15](../tests/C-FR17-coupon-management.md#c-api-15), [C-API-16](../tests/C-FR17-coupon-management.md#c-api-16), [C-API-17](../tests/C-FR17-coupon-management.md#c-api-17), [C-UI-03](../tests/C-FR17-coupon-management.md#c-ui-03) |
| C-D7 | max_uses_per_user ≥ 1 | Boundary | −1/0/1/2 lần | Reject/reject/accept/accept | [C-API-18](../tests/C-FR17-coupon-management.md#c-api-18), [C-API-19](../tests/C-FR17-coupon-management.md#c-api-19), [C-API-20](../tests/C-FR17-coupon-management.md#c-api-20), [C-API-21](../tests/C-FR17-coupon-management.md#c-api-21), [C-UI-04](../tests/C-FR17-coupon-management.md#c-ui-04) |
| C-D8 | Create permission | Role/auth | Admin/user/none/invalid JWT | Chỉ admin tạo được | [C-API-01](../tests/C-FR17-coupon-management.md#c-api-01), [C-API-22](../tests/C-FR17-coupon-management.md#c-api-22), [C-API-23](../tests/C-FR17-coupon-management.md#c-api-23), [C-API-24](../tests/C-FR17-coupon-management.md#c-api-24) |
| C-D9 | List permission | Role/auth | Admin/user/none | Admin allow; user/none deny | [C-API-25](../tests/C-FR17-coupon-management.md#c-api-25), [C-API-26](../tests/C-FR17-coupon-management.md#c-api-26), [C-API-27](../tests/C-FR17-coupon-management.md#c-api-27) |
| C-D10 | Delete permission | Role/auth | Admin/user/none; coupon có thật | Admin xóa đúng row; user/none không xóa | [C-API-28](../tests/C-FR17-coupon-management.md#c-api-28), [C-API-29](../tests/C-FR17-coupon-management.md#c-api-29), [C-API-30](../tests/C-FR17-coupon-management.md#c-api-30), [C-UI-06](../tests/C-FR17-coupon-management.md#c-ui-06) |

## 4. Boundary Value Analysis — từng bước

1. Chọn biến có thứ tự và miền áp dụng từ rule; không lấy giới hạn tùy ý trong code.
2. Viết bất đẳng thức và xác định điểm equality hợp lệ hay không.
3. Ghi precision của fixture, lấy điểm biên và lân cận hai phía.
4. Giữ các chiều ngoài biên đang xét nominal; thêm giao biên khi có lý do.
5. Tính expected độc lập; liên kết TC và phân biệt numerical boundary với missing/type domain.
6. So actual với expected; khi rounding/MAX/reset không có rule, giữ observation hoặc giới hạn kết luận.

| Biến | Rule | Delta/precision | Điểm chọn và giải thích | Cases |
|---|---|---|---|---|
| discount_value v | v > 0 | 1 VND trong fixture | −1 invalid; 0 ON invalid; +1 valid. Không tuyên bố 1 là số dương nhỏ nhất của miền số thực | C-API-12–14; C-UI-01 |
| min_order_amount m | m ≥ 0 | 1 VND | −1 invalid; 0 ON valid; +1 valid | C-API-15–17; C-UI-03 |
| max_uses_per_user k | k ≥ 1, k là số lượt | 1 lượt | 0 invalid; 1 ON valid; 2 valid; −1 thêm invalid interior | C-API-18–21; C-UI-04 |
| expired_at presence | Field bắt buộc | Không áp BVA ngày ở create | Thiếu field là Domain; SRS không cấm tạo mã hết hạn | C-API-07 |

## 5. Kết quả thực thi

| TC | Status | Actual tóm tắt | Bug |
|---|---|---|---|
| [C-API-01](../tests/C-FR17-coupon-management.md#c-api-01) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":13}<br>GET /api/coupons → HTTP 200: array 9 rows | — |
| [C-API-02](../tests/C-FR17-coupon-management.md#c-api-02) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":22}<br>GET /api/coupons → HTTP 200: array 9 rows | — |
| [C-API-03](../tests/C-FR17-coupon-management.md#c-api-03) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":31}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C01 |
| [C-API-04](../tests/C-FR17-coupon-management.md#c-api-04) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":40}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C01 |
| [C-API-05](../tests/C-FR17-coupon-management.md#c-api-05) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":49}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C01 |
| [C-API-06](../tests/C-FR17-coupon-management.md#c-api-06) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":58}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C01 |
| [C-API-07](../tests/C-FR17-coupon-management.md#c-api-07) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":67}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C01 |
| [C-API-08](../tests/C-FR17-coupon-management.md#c-api-08) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":76}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C01 |
| [C-API-09](../tests/C-FR17-coupon-management.md#c-api-09) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":85}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C01 |
| [C-API-10](../tests/C-FR17-coupon-management.md#c-api-10) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 500: {"error":"SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code"}<br>GET /api/coupons → HTTP 200: array 8 rows | — |
| [C-API-11](../tests/C-FR17-coupon-management.md#c-api-11) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":102}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C03 |
| [C-API-12](../tests/C-FR17-coupon-management.md#c-api-12) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":111}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C04 |
| [C-API-13](../tests/C-FR17-coupon-management.md#c-api-13) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":120}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C04 |
| [C-API-14](../tests/C-FR17-coupon-management.md#c-api-14) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":129}<br>GET /api/coupons → HTTP 200: array 9 rows | — |
| [C-API-15](../tests/C-FR17-coupon-management.md#c-api-15) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":138}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C05 |
| [C-API-16](../tests/C-FR17-coupon-management.md#c-api-16) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":147}<br>GET /api/coupons → HTTP 200: array 9 rows | — |
| [C-API-17](../tests/C-FR17-coupon-management.md#c-api-17) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":156}<br>GET /api/coupons → HTTP 200: array 9 rows | — |
| [C-API-18](../tests/C-FR17-coupon-management.md#c-api-18) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":165}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C06 |
| [C-API-19](../tests/C-FR17-coupon-management.md#c-api-19) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":174}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C06 |
| [C-API-20](../tests/C-FR17-coupon-management.md#c-api-20) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":183}<br>GET /api/coupons → HTTP 200: array 9 rows | — |
| [C-API-21](../tests/C-FR17-coupon-management.md#c-api-21) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":192}<br>GET /api/coupons → HTTP 200: array 9 rows | — |
| [C-API-22](../tests/C-FR17-coupon-management.md#c-api-22) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 401: {"error":"Unauthorized"}<br>GET /api/coupons → HTTP 200: array 8 rows | — |
| [C-API-23](../tests/C-FR17-coupon-management.md#c-api-23) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 200: {"message":"Coupon created","id":209}<br>GET /api/coupons → HTTP 200: array 9 rows | BUG-C07 |
| [C-API-24](../tests/C-FR17-coupon-management.md#c-api-24) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>POST /api/admin/coupons → HTTP 403: {"error":"Forbidden"}<br>GET /api/coupons → HTTP 200: array 8 rows | — |
| [C-API-25](../tests/C-FR17-coupon-management.md#c-api-25) | PASS | GET /api/coupons → HTTP 200: array 8 rows | — |
| [C-API-26](../tests/C-FR17-coupon-management.md#c-api-26) | FAIL | GET /api/coupons → HTTP 200: array 8 rows | BUG-C08 |
| [C-API-27](../tests/C-FR17-coupon-management.md#c-api-27) | PASS | GET /api/coupons → HTTP 401: {"error":"Unauthorized"} | — |
| [C-API-28](../tests/C-FR17-coupon-management.md#c-api-28) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>DELETE /api/admin/coupons/249 → HTTP 200: {"message":"Coupon deleted"}<br>GET /api/coupons → HTTP 200: array 7 rows | — |
| [C-API-29](../tests/C-FR17-coupon-management.md#c-api-29) | FAIL | GET /api/coupons → HTTP 200: array 8 rows<br>DELETE /api/admin/coupons/257 → HTTP 200: {"message":"Coupon deleted"}<br>GET /api/coupons → HTTP 200: array 7 rows | BUG-C09 |
| [C-API-30](../tests/C-FR17-coupon-management.md#c-api-30) | PASS | GET /api/coupons → HTTP 200: array 8 rows<br>DELETE /api/admin/coupons/265 → HTTP 401: {"error":"Unauthorized"}<br>GET /api/coupons → HTTP 200: array 8 rows | — |
| [C-UI-01](../tests/C-FR17-coupon-management.md#c-ui-01) | FAIL | Coupon có discount_value=0 được tạo và xuất hiện trong danh sách. | BUG-C04 |
| [C-UI-02](../tests/C-FR17-coupon-management.md#c-ui-02) | INCOMPLETE | Coupon với dữ liệu nominal được tạo; hàng mới hiển thị các giá trị đã nhập. | — |
| [C-UI-03](../tests/C-FR17-coupon-management.md#c-ui-03) | FAIL | Coupon với min_order_amount=−1 được tạo và hiển thị ngưỡng âm. | BUG-C05 |
| [C-UI-04](../tests/C-FR17-coupon-management.md#c-ui-04) | PASS | Browser native validation chặn max_uses_per_user=0 ở bước submit. Đây là PASS của frontend rejection; C-API-19 vẫn FAIL ở backend. | — |
| [C-UI-05](../tests/C-FR17-coupon-management.md#c-ui-05) | PASS | Tạo trùng SAVE10 trả lỗi UNIQUE. Source/schema và C-API-10 xác nhận không có bản ghi trùng; không tự đặt HTTP 409 làm oracle. | — |
| [C-UI-06](../tests/C-FR17-coupon-management.md#c-ui-06) | INCOMPLETE | Có ảnh nhập và tạo coupon HW02_DELETE_UI; chưa có evidence thao tác xóa và danh sách sau reload. | — |

## 6. Spec vs Code và bug groups

| Bug | Rule | Nguyên nhân có source support | Representative |
|---|---|---|---|
| [BUG-C01](../bugs/BUG-C01.md) | FR-17 required fields | Route INSERT không kiểm tra presence; schema cho phép NULL/default ở các field này. | C-API-03 |
| [BUG-C03](../bugs/BUG-C03.md) | FR-17 type enum | Route không whitelist type trước INSERT; DB không enforce enum. | C-API-11 |
| [BUG-C04](../bugs/BUG-C04.md) | FR-17 discount_value>0 | Route không kiểm tra giá trị dương; C-API-12 là −1, C-API-13 là 0. | C-API-13 |
| [BUG-C05](../bugs/BUG-C05.md) | FR-17 min_order_amount≥0 | Route không kiểm tra ngưỡng không âm trước INSERT. | C-API-15 |
| [BUG-C06](../bugs/BUG-C06.md) | FR-17 max_uses_per_user≥1 | Source dùng max_uses_per_user &#124;&#124; 1: 0 trở thành1, −1 truthy nên giữ nguyên. Không phải Math.max. | C-API-19 |
| [BUG-C07](../bugs/BUG-C07.md) | FR-12 / SEC-03 / FR-17 | Route POST có authenticateToken nhưng không kiểm tra req.user.role===admin. | C-API-23 |
| [BUG-C08](../bugs/BUG-C08.md) | FR-12 / SEC-03 / FR-17 | GET /api/coupons chỉ xác thực token; không kiểm tra role. Đây là endpoint Admin UI dùng xem danh sách. | C-API-26 |
| [BUG-C09](../bugs/BUG-C09.md) | FR-12 / SEC-03 / FR-17 | DELETE /api/admin/coupons/:id chỉ authenticateToken, thiếu role guard. | C-API-29 |

## 7. AI gap analysis

Các mục dưới đây là technical corrections có evidence của quá trình soạn/kiểm tra; không tự gán mọi phát hiện cho sinh viên hoặc một model bên ngoài. Bản nháp nguyên văn giữ trong AI audit snapshot.

| Gap | Nhóm nguyên nhân | Evidence/điều sai | Cách sửa |
|---|---|---|---|
| Contract bị đổi khi diễn giải | Giới hạn công cụ | Draft dùng camelCase, enum FIXED/PERCENTAGE và GET sai endpoint | Khôi phục snake_case, percent/fixed, GET /api/coupons |
| Sai TC mapping zero/negative | Giới hạn công cụ | Draft đảo C-API-12/13 và 18/19 | Đối chiếu input raw, không dựa thứ tự trong mô tả prose |
| CRUD naming và duplicate status | Prompt/assumption | Tên CRUD không có Update; duplicate500 vẫn không nhân bản | Không tạo bug missing Update hoặc unique-status409 |
| UI block và API acceptance | Độ phức tạp nhiều seam | C-UI-04 chặn 0 nhưng C-API-19 vẫn accept/default1 | UI PASS, API FAIL, không gán một verdict cho cả hai |

## 8. Coverage và giới hạn

Các domain và điểm biên đã liệt kê đều có TC-ID. Một số TC có evidence một phần nên chưa có verdict hoàn chỉnh. Không suy full requirement coverage từ số TC hoặc số ảnh; class chưa có rule rõ không biến thành bug. Các form/UI tiêu chuẩn chung ngoài mục tiêu các TC hiện tại chưa được kiểm chứng exhaustive. Lecture chưa có trong bộ nguồn; cần đối chiếu bản giảng viên trước nộp.

[Detailed test cases](../tests/C-FR17-coupon-management.md) · [Raw API evidence](../evidence/execution/C-api.md) · [Bug index](../bugs/bug-reports.md).
