# Feature A - FR-04 - Quản lý hồ sơ cá nhân

### 3.1. Requirements và oracle

| Rule | Nội dung theo SRS | Domain |
|---|---|---|
| FR-04.1 | Cập nhật name, phone, shipping_address của chính người dùng | A-D7/D9 |
| FR-04.2 | Phone bắt đầu 0, từ 10-11 chữ số; SRS không chốt numeral encoding | A-D1-D6 |
| FR-04.3 | Email không thay đổi qua UI | A-D11 |
| FR-04.4 / SEC-06 | Không cho client tự đổi role | A-D8 |
| SEC-02 | Profile chỉ truy cập bằng JWT hợp lệ | A-D10 |

[Nguồn SRS cố định](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md). Các nhãn rule trong bảng được dùng để truy vết giữa yêu cầu, domain và test case.

### 3.2. Domain Testing - quy trình từng bước

#### Bước 1 - Xác định inputs/outputs

Vector đầu vào gồm `(JWT, target identity, phone, name, shipping_address, role_attempt)`. Đầu ra được quan sát qua phản hồi cập nhật, hồ sơ đọc lại và thông báo trên Web /profile.

#### Bước 2 - Thiết lập nominal fixture

User 2 có phone 0912345678, role=user và dữ liệu hồ sơ hợp lệ. User 3 được dùng làm đối chứng ownership. Phone 10 và 11 chữ số được chọn làm hai đại diện hợp lệ theo SRS.

#### Bước 3 - Chia lớp hợp lệ/không hợp lệ

Phone được phân lớp theo độ dài, prefix, charset và presence; name/address được kiểm tra với Unicode. Role, body identity và JWT được phân tích thành các chiều quyền truy cập độc lập. Chữ số Unicode được tách OBSERVATION do SRS không quy định encoding.

#### Bước 4 - Cô lập một điều kiện sai

Khi thay đổi length, prefix hoặc charset, các trường còn lại được giữ hợp lệ. Trong các case role tampering và ownership, phone nominal giúp cô lập ràng buộc quyền truy cập khỏi validation dữ liệu.

#### Bước 5 - Chọn đại diện và giải thích

Các chuỗi 091234567, 0912345678, 09123456789 và 091234567890 phân biệt hai phía của miền độ dài. Prefix sai, ký tự chữ, khoảng trắng, dấu cộng và dấu gạch được kiểm tra bằng các TC riêng.

#### Bước 6 - Phân tích cross-constraint

Danh tính hồ sơ đích phải lấy từ JWT, bất kể body chứa id hoặc user_id của người khác. Cập nhật dữ liệu cá nhân phải giữ nguyên role; GET readback của cả user 2 và user 3 được dùng để đối chiếu ràng buộc này.

#### Bước 7 - Đối chiếu hypothesis bằng thực thi

PUT/GET /api/users/me kiểm tra phản hồi và dữ liệu sau cập nhật. Ảnh Web /profile kiểm tra validation phía client. Hai nguồn bằng chứng được đối chiếu riêng, qua đó phân biệt lỗi API lưu phone sai với lỗi UI chặn phone hợp lệ.

#### Bước 8 - Review coverage và AI output

Domain, giá trị biên, kết quả và bug được liên kết theo TC-ID. Nhận định ASCII được loại khỏi oracle; A-API-15 giữ OBSERVATION. A-UI-07 được đánh giá FAIL theo việc từ chối dữ liệu hợp lệ, không suy thêm lỗi persistence hoặc Unicode.

### 3.3. Domain partition và traceability

| Domain ID | Chiều/lớp | Loại | Representative | Expected | TC coverage |
|---|---|---|---|---|---|
| A-D1 | Độ dài phone hợp lệ | Valid | 0912345678; 09123456789 | Chấp nhận và lưu đúng | [A-API-01](../tests/A-FR04-profile.md#a-api-01), [A-API-02](../tests/A-FR04-profile.md#a-api-02), [A-UI-02](../tests/A-FR04-profile.md#a-ui-02), [A-UI-03](../tests/A-FR04-profile.md#a-ui-03) |
| A-D2 | Phone quá ngắn | Invalid | rỗng; 0; 09123456; 091234567 | Từ chối; giữ phone cũ | [A-API-03](../tests/A-FR04-profile.md#a-api-03), [A-API-05](../tests/A-FR04-profile.md#a-api-05), [A-API-06](../tests/A-FR04-profile.md#a-api-06), [A-API-07](../tests/A-FR04-profile.md#a-api-07), [A-UI-01](../tests/A-FR04-profile.md#a-ui-01) |
| A-D3 | Phone quá dài | Invalid | 12 và 13 chữ số | Từ chối; giữ phone cũ | [A-API-04](../tests/A-FR04-profile.md#a-api-04), [A-API-08](../tests/A-FR04-profile.md#a-api-08), [A-UI-04](../tests/A-FR04-profile.md#a-ui-04) |
| A-D4 | Prefix sai với độ dài hợp lệ | Invalid | 1912345678; 19123456789 | Từ chối; tách lỗi prefix khỏi length | [A-API-09](../tests/A-FR04-profile.md#a-api-09), [A-API-10](../tests/A-FR04-profile.md#a-api-10), [A-UI-05](../tests/A-FR04-profile.md#a-ui-05) |
| A-D5 | Charset/kiểu dữ liệu sai | Invalid | 091234567a; khoảng trắng; +84; dấu gạch; null | Từ chối và không ghi giá trị sai | [A-API-11](../tests/A-FR04-profile.md#a-api-11), [A-API-12](../tests/A-FR04-profile.md#a-api-12), [A-API-13](../tests/A-FR04-profile.md#a-api-13), [A-API-14](../tests/A-FR04-profile.md#a-api-14), [A-API-16](../tests/A-FR04-profile.md#a-api-16) |
| A-D6 | Numeral encoding chưa chốt | Observation | ０９１２３４５６７８ | Ghi nhận; không áp thêm ASCII rule từ regex | [A-API-15](../tests/A-FR04-profile.md#a-api-15) |
| A-D7 | Name/address Unicode | Valid | Người Dùng HW02; Đường Thử Nghiệm | Giữ nguyên dấu và lưu đúng | [A-API-17](../tests/A-FR04-profile.md#a-api-17), [A-UI-07](../tests/A-FR04-profile.md#a-ui-07) |
| A-D8 | Role self-edit | Invalid action | role=admin trong body user thường | Ignore/reject role; role vẫn user | [A-API-18](../tests/A-FR04-profile.md#a-api-18) |
| A-D9 | Body chỉ định người khác | Identity constraint | id=3/user_id=3, JWT user 2 | Chỉ cập nhật user 2; user 3 giữ nguyên | [A-API-19](../tests/A-FR04-profile.md#a-api-19) |
| A-D10 | Authentication | Invalid identity | JWT thiếu/sai khi PUT; thiếu khi GET | Không truy cập/sửa profile | [A-API-20](../tests/A-FR04-profile.md#a-api-20), [A-API-21](../tests/A-FR04-profile.md#a-api-21), [A-API-22](../tests/A-FR04-profile.md#a-api-22) |
| A-D11 | Email qua UI | Immutable field | other@example.invalid | Không cho chỉnh sửa email | [A-UI-06](../tests/A-FR04-profile.md#a-ui-06) |

### 3.4. Boundary Value Analysis - từng bước

1. Từ rule phone, miền độ dài hợp lệ được xác định là 10 <= L <= 11.
2. Dấu bằng tại 10 và 11 được xác định thuộc miền hợp lệ; 9 và 12 nằm ngoài miền.
3. Bước lân cận được chọn là một chữ số, với prefix 0 và charset giữ nominal.
4. Các số phone cụ thể được gắn với A-API-03/01/02/04 và A-UI-01-04.
5. Prefix, charset, presence và role được phân tích bằng Domain Testing, tách khỏi biến độ dài.
6. Phản hồi cập nhật và hồ sơ đọc lại được đối chiếu riêng với cảnh báo trên Web để phân biệt lỗi từng lớp.

| Biến | Rule | Delta/precision | Điểm chọn và giải thích | Cases |
|---|---|---|---|---|
| length(phone) | 10 <= L <= 11 | 1 chữ số | 9 invalid; 10 ON lower valid; 11 ON upper valid; 12 invalid | A-API-03/01/02/04; A-UI-01-04 |
| Prefix/role/charset | Lớp rời rạc | Không có delta số học | Dùng Domain Testing; không gọi prefix=1 là biên phone number | A-D4/D5/D8 |

### 3.5. Kết quả thực thi

| TC | Status | Actual tóm tắt | Bug |
|---|---|---|---|
| [A-API-01](../tests/A-FR04-profile.md#a-api-01) | PASS | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678"} | - |
| [A-API-02](../tests/A-FR04-profile.md#a-api-02) | PASS | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"09123456789"} | - |
| [A-API-03](../tests/A-FR04-profile.md#a-api-03) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"091234567"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-04](../tests/A-FR04-profile.md#a-api-04) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"091234567890"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-05](../tests/A-FR04-profile.md#a-api-05) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":""} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-06](../tests/A-FR04-profile.md#a-api-06) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-07](../tests/A-FR04-profile.md#a-api-07) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"09123456"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-08](../tests/A-FR04-profile.md#a-api-08) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678901"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-09](../tests/A-FR04-profile.md#a-api-09) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"1912345678"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-10](../tests/A-FR04-profile.md#a-api-10) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"19123456789"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-11](../tests/A-FR04-profile.md#a-api-11) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"091234567a"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-12](../tests/A-FR04-profile.md#a-api-12) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"09123 5678"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-13](../tests/A-FR04-profile.md#a-api-13) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"+84912345678"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-14](../tests/A-FR04-profile.md#a-api-14) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"09123-5678"} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-15](../tests/A-FR04-profile.md#a-api-15) | OBSERVATION | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"０９１２３４５６７８"} | - |
| [A-API-16](../tests/A-FR04-profile.md#a-api-16) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":null} | FR04-01, FR04-02, FR04-03, FR04-04, FR04-05, FR04-06, FR04-07, FR04-08, FR04-09, FR04-10, FR04-11, FR04-12, FR04-13 |
| [A-API-17](../tests/A-FR04-profile.md#a-api-17) | PASS | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"Người Dùng HW02","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"Đường Thử Nghiệm","phone":"0912345678"} | - |
| [A-API-18](../tests/A-FR04-profile.md#a-api-18) | FAIL | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"admin","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678"} | FR04-14 |
| [A-API-19](../tests/A-FR04-profile.md#a-api-19) | PASS | PUT /api/users/me -> HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"Owner Only","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678"}<br>GET /api/users/me -> HTTP 200: {"id":3,"name":"Other User","email":"other@hw02.invalid","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"Other Street","phone":"0987654321"} | - |
| [A-API-20](../tests/A-FR04-profile.md#a-api-20) | PASS | PUT /api/users/me -> HTTP 401: {"error":"Unauthorized"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"Test User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678"} | - |
| [A-API-21](../tests/A-FR04-profile.md#a-api-21) | PASS | PUT /api/users/me -> HTTP 403: {"error":"Forbidden"}<br>GET /api/users/me -> HTTP 200: {"id":2,"name":"Test User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678"} | - |
| [A-API-22](../tests/A-FR04-profile.md#a-api-22) | PASS | GET /api/users/me -> HTTP 401: {"error":"Unauthorized"} | - |
| [A-UI-01](../tests/A-FR04-profile.md#a-ui-01) | PASS | Phone 091234567 bị từ chối bằng cảnh báo validation. Ảnh xác nhận bước từ chối; không có GET UI readback độc lập. | - |
| [A-UI-02](../tests/A-FR04-profile.md#a-ui-02) | FAIL | Phone hợp lệ 0912345678 bị cảnh báo không hợp lệ; thao tác cập nhật bị chặn ngay ở frontend. | FR04-15, FR04-16, FR04-17 |
| [A-UI-03](../tests/A-FR04-profile.md#a-ui-03) | FAIL | Phone hợp lệ 09123456789 bị từ chối. Thông báo nói 9-10 chữ số, khác yêu cầu 10-11 chữ số bắt đầu bằng 0. | FR04-15, FR04-16, FR04-17 |
| [A-UI-04](../tests/A-FR04-profile.md#a-ui-04) | PASS | Phone 091234567890 bị frontend từ chối. Kết quả từ chối đạt mục tiêu validation của UI, không chứng minh backend có validation. | - |
| [A-UI-05](../tests/A-FR04-profile.md#a-ui-05) | FAIL | Phone 1912345678 có prefix sai nhưng UI báo cập nhật thành công. API A-API-09 xác nhận riêng việc backend có thể lưu prefix sai. | FR04-15, FR04-16, FR04-17 |
| [A-UI-06](../tests/A-FR04-profile.md#a-ui-06) | PASS | Email hiển thị ở field disabled. Source Profile.jsx dùng disabled cho input email; đây là kiểm tra thuộc tính không cho chỉnh sửa qua UI, không phải kiểm thử API đổi email. | - |
| [A-UI-07](../tests/A-FR04-profile.md#a-ui-07) | FAIL | Account A-UI-07 nhập name/address Unicode và phone hợp lệ 0912345678; UI báo phone không hợp lệ và chặn cập nhật. Persistence chưa đạt tới vì FR04-15, FR04-16, FR04-17. | FR04-15, FR04-16, FR04-17 |

### 3.6. Spec vs Code và findings

| ID | Điều kiện vi phạm | Oracle / root cause |
|---|---|---|
| [FR04-01](../bugs/FR04-01.md) | Profile API accepts and persists a 9-digit phone | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-02](../bugs/FR04-02.md) | Profile API accepts and persists a 12-digit phone | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-03](../bugs/FR04-03.md) | Profile API accepts and persists an empty phone | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-04](../bugs/FR04-04.md) | Profile API accepts and persists a one-digit phone | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-05](../bugs/FR04-05.md) | Profile API accepts and persists an 8-digit phone | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-06](../bugs/FR04-06.md) | Profile API accepts and persists a 13-digit phone | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-07](../bugs/FR04-07.md) | Profile API accepts and persists a 10-digit phone with a nonzero prefix | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-08](../bugs/FR04-08.md) | Profile API accepts and persists an 11-digit phone with a nonzero prefix | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-09](../bugs/FR04-09.md) | Profile API accepts and persists a phone containing a letter | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-10](../bugs/FR04-10.md) | Profile API accepts and persists a phone containing an embedded space | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-11](../bugs/FR04-11.md) | Profile API accepts and persists a country-code phone instead of the required 0 prefix | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-12](../bugs/FR04-12.md) | Profile API accepts and persists a hyphenated phone | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-13](../bugs/FR04-13.md) | Profile API accepts and persists a null phone | FR-04; phone starts with 0 and has 10-11 digits; The update route writes phone directly without validating its prefix, length or character set. |
| [FR04-14](../bugs/FR04-14.md) | Regular users can change their stored role to admin | FR-04; SEC-06; The route conditionally appends role to the UPDATE statement whenever the body value is truthy. |
| [FR04-15](../bugs/FR04-15.md) | Web rejects a valid 10-digit 0-prefixed phone | FR-04; Profile.jsx uses /^[1-9][0-9]{8,9}$/ instead of the specified prefix/length rule. |
| [FR04-16](../bugs/FR04-16.md) | Web rejects a valid 11-digit 0-prefixed phone | FR-04; Profile.jsx uses /^[1-9][0-9]{8,9}$/ instead of the specified prefix/length rule. |
| [FR04-17](../bugs/FR04-17.md) | Web accepts a 10-digit phone with an invalid nonzero prefix | FR-04; Profile.jsx uses /^[1-9][0-9]{8,9}$/ instead of the specified prefix/length rule. |
| [FR04-18](../bugs/FR04-18.md) | Profile response discloses the plaintext password | SEC-01 storage rule; supplementary OWASP API3 response minimization; Profile uses SELECT * and serializes the complete row; login serializes the complete user object. Plaintext password storage is separately evidenced as a contributing security weakness. |
| [FR04-19](../bugs/FR04-19.md) | Profile response discloses an active password-reset token | SEC-01 storage rule; supplementary OWASP API3 response minimization; Profile uses SELECT * and serializes the complete row; login serializes the complete user object. Plaintext password storage is separately evidenced as a contributing security weakness. |
| [FR04-20](../bugs/FR04-20.md) | Login response includes password and reset-state properties | SEC-01 storage rule; supplementary OWASP API3 response minimization; Profile uses SELECT * and serializes the complete row; login serializes the complete user object. Plaintext password storage is separately evidenced as a contributing security weakness. |
| [FR04-21](../bugs/FR04-21.md) | Mobile profile payload silently clears the shipping address | FR-04 default shipping-address update; App.js sends shippingAddress while the backend reads shipping_address; missing fields are written as null. |
| [FR04-22](../bugs/FR04-22.md) | Mobile handler rejects a valid 10-digit 0-prefixed phone | FR-04 phone rule; The Mobile handler uses /^[1-9][0-9]{8,9}$/ independently of the Web component. |
| [FR04-23](../bugs/FR04-23.md) | Mobile handler rejects a valid 11-digit 0-prefixed phone | FR-04 phone rule; The Mobile handler uses /^[1-9][0-9]{8,9}$/ independently of the Web component. |
| [FR04-24](../bugs/FR04-24.md) | Mobile handler accepts an invalid nonzero phone prefix | FR-04 phone rule; The Mobile handler uses /^[1-9][0-9]{8,9}$/ independently of the Web component. |
| [FR04-25](../bugs/FR04-25.md) | Disabled Web profile email uses text instead of email input type | FR-22 email input type; Profile.jsx explicitly declares type=text for the email input. |
| [FR04-26](../bugs/FR04-26.md) | Stored profile name executes an HTML event handler in Web greeting | SEC-04 user input must be escaped; Header renders user.name with dangerouslySetInnerHTML. |
| [FR04-27](../bugs/FR04-27.md) | SPA profile re-entry shows stale data after a successful save | FR-04 successful profile update and displayed persisted state; The save handler does not update AuthContext.user; remount initializes the form from that cached object. |

### 3.7. AI gap analysis

Các sai lệch trong đầu ra AI và cách hiệu chỉnh được đối chiếu với rule, raw record và ảnh tương ứng. Bản nháp gốc được lưu trong AI audit snapshot.

| Gap | Nhóm nguyên nhân | Evidence/điều sai | Cách sửa |
|---|---|---|---|
| Encoding bị áp thêm | Prompt/assumption | Metadata cũ ghi ASCII nhưng SRS chỉ nói chữ số | Giữ A-API-15 OBSERVATION; sửa oracle, không thêm bug Unicode |
| API và UI bị đồng nhất | Giới hạn suy luận | A-API-01/02 PASS trong khi A-UI-02/03 FAIL | Tách seam; tạo FR04-15, FR04-16, FR04-17 từ ảnh UI thật |
| Persistence bị kết luận từ alert | Độ phức tạp trạng thái | Ảnh cũ sai phone; ảnh mới với phone hợp lệ bị FR04-15, FR04-16, FR04-17 chặn | Chốt FAIL theo valid update; không suy persistence hoặc lỗi Unicode |

### 3.8. Coverage và giới hạn

Coverage gồm 11 domain groups, các độ dài phone 9/10/11/12, prefix/charset/presence, Unicode, role và ownership. A-API-15 giữ OBSERVATION do SRS không chốt numeral encoding. A-UI-07 được kết luận FAIL tại bước chấp nhận dữ liệu hợp lệ; hậu điều kiện persistence nằm ngoài bước thực thi đã đạt tới của case này.

[Detailed test cases](../tests/A-FR04-profile.md), [Raw API evidence](../evidence/execution/A-api.md), [Bug index](../bugs/bug-reports.md).


### Kiểm thử contract và state bổ sung

| Domain | Chiều phân hoạch | Oracle / controls | TC-ID | Kết luận |
|---|---|---|---|---|
| A-D12 | Response projection / credential confidentiality | Chỉ trả thuộc tính hồ sơ cần thiết; token hoạt động và password phải được loại khỏi response theo oracle bảo mật bổ sung. | A-API-23, A-API-24, A-API-29 | FR04-18, FR04-19, FR04-20 |
| A-D13 | Mobile JSON field contract | Canonical shipping_address so với shippingAddress; giữ phone và identity nominal ở seam API. | A-API-25, A-API-26 | FR04-21 |
| A-D14 | Unspecified partial/cross-feature semantics | Field vắng mặt và địa chỉ checkout chưa có oracle đầy đủ; không tự chấm FAIL. | A-API-27, A-API-28 | OBSERVATION |
| A-D15 | Mobile phone handler | 10/11 số bắt đầu 0 hợp lệ; prefix khác và 9/12 số không hợp lệ. | A-HND-01, A-HND-02, A-HND-03, A-HND-04, A-HND-05 | FR04-22, FR04-23, FR04-24 |
| A-D16 | Email semantic input type | Disabled email vẫn phải dùng type=email theo FR-22. | A-UI-08 | FR04-25 |
| A-D17 | Stored-name output encoding | Tên Unicode/plain text và HTML event canary; dữ liệu phải render như text. | A-UI-09 | FR04-26 |
| A-D18 | Profile state after navigation | Sau lưu thành công, SPA remount phải phản ánh dữ liệu đã lưu; fixture đi qua guard sai được khai riêng. | A-UI-10 | FR04-27 |

Các lớp bổ sung được suy từ contract, security property và state transition; không gắn nhãn BVA cho boolean/DOM/enum. Riêng phone Mobile dùng cùng các biên độ dài 9/10/11/12, với các chiều prefix được cô lập.

| TC-ID | Seam | Status | Actual / bug |
|---|---|---|---|
| [A-API-23](../tests/A-FR04-profile.md#a-api-23) | API | FAIL | Profile response excludes credentials and reset state / FR04-18 |
| [A-API-24](../tests/A-FR04-profile.md#a-api-24) | API | FAIL | Active recovery token is not disclosed by profile / FR04-19 |
| [A-API-25](../tests/A-FR04-profile.md#a-api-25) | API | PASS | Canonical profile payload persists address (control) / - |
| [A-API-26](../tests/A-FR04-profile.md#a-api-26) | API | FAIL | Mobile-shaped payload loses address at API boundary / FR04-21 |
| [A-API-27](../tests/A-FR04-profile.md#a-api-27) | API | OBSERVATION | O1: missing profile fields become null / - |
| [A-API-28](../tests/A-FR04-profile.md#a-api-28) | API | OBSERVATION | O2: checkout without shipping_address / - |
| [A-API-29](../tests/A-FR04-profile.md#a-api-29) | API | FAIL | Related login response excludes user secrets / FR04-20 |
| [A-HND-01](../tests/A-FR04-profile.md#a-hnd-01) | HND | FAIL | Mobile profile handler phone 0912345678 / FR04-22 |
| [A-HND-02](../tests/A-FR04-profile.md#a-hnd-02) | HND | FAIL | Mobile profile handler phone 09123456789 / FR04-23 |
| [A-HND-03](../tests/A-FR04-profile.md#a-hnd-03) | HND | FAIL | Mobile profile handler phone 1912345678 / FR04-24 |
| [A-HND-04](../tests/A-FR04-profile.md#a-hnd-04) | HND | PASS | Mobile profile handler phone 091234567 / - |
| [A-HND-05](../tests/A-FR04-profile.md#a-hnd-05) | HND | PASS | Mobile profile handler phone 091234567890 / - |
| [A-UI-08](../tests/A-FR04-profile.md#a-ui-08) | UI | FAIL | Disabled profile email uses the semantic email input type / FR04-25 |
| [A-UI-09](../tests/A-FR04-profile.md#a-ui-09) | UI | FAIL | Profile name is rendered as inert text in the greeting / FR04-26 |
| [A-UI-10](../tests/A-FR04-profile.md#a-ui-10) | UI | FAIL | SPA profile re-entry displays the successfully saved name / FR04-27 |

SEC-01 là quy tắc không lưu password plaintext; SEC-02 là authentication. Quy tắc loại password/reset_token khỏi response được dẫn thêm từ OWASP API3:2023, không gán thành câu nguyên văn trong SRS. FR04-18, FR04-19, FR04-20 đã kiểm field presence, token bằng nhau và chuỗi reset/login bằng token lộ trên fixture. FR04-21 có control snake_case PASS và camelCase FAIL. FR04-22, FR04-23, FR04-24 chỉ là handler execution. FR04-27 dùng phone 1912345678 đã được guard lỗi chấp nhận để đi tới nhánh save; đây không phải phone hợp lệ theo SRS.

FR04-14 đã xác nhận role lưu thành admin và JWT mới mang role admin. GET /api/admin/users với user token trước thay đổi cũng trả 200, nên không mô tả endpoint này như bằng chứng chuyển 403 sang 200. O1 và O2 giữ OBSERVATION; OTP 4 chữ số thuộc FR-03 được ghi liên quan, không cộng thêm feature/bug ngoài phạm vi.

[A execution](../evidence/execution/A-execution.md), [B execution](../evidence/execution/B-execution.md), [C execution](../evidence/execution/C-execution.md), [D execution](../evidence/execution/D-execution.md).
