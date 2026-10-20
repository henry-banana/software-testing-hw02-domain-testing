# A — Domain Testing và Boundary Value Analysis

**Feature:** FR-04 — Quản lý hồ sơ cá nhân<br>
**SUT:** `85af3ba875c88283615e22cb108f13e2fccaf0e9`.

## 1. Requirements và oracle

| Rule | Nội dung theo SRS | Domain |
|---|---|---|
| FR-04.1 | Cập nhật name, phone, shipping_address của chính người dùng | A-D7/D9 |
| FR-04.2 | Phone bắt đầu 0, từ 10–11 chữ số; SRS không chốt numeral encoding | A-D1–D6 |
| FR-04.3 | Email không thay đổi qua UI | A-D11 |
| FR-04.4 / SEC-06 | Không cho client tự đổi role | A-D8 |
| SEC-02 | Profile chỉ truy cập bằng JWT hợp lệ | A-D10 |

[Nguồn SRS cố định](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md). Các tên rule dạng FR-04.1 trong báo cáo là nhãn nội bộ để truy vết, không phải mã mới của SRS.

## 2. Domain Testing — quy trình từng bước

Chúng tôi lấy SRS làm oracle, sau đó dùng source để xây dựng giả thuyết và giải thích nguyên nhân. Source không thay thế yêu cầu. Mỗi TC có ID ổn định; một TC có thể phủ cả Domain Testing và BVA nhưng chỉ được tính một lần. Chúng tôi tách API với Web/Admin/Mobile UI vì validation ở một lớp không chứng minh lớp còn lại đạt.

Với từng input/state, chúng tôi xác định miền hợp lệ, phần bù không hợp lệ, precision và các ràng buộc giữa các chiều. Các lớp trong cùng một chiều được chọn để phân biệt hành vi; bảng nhiều chiều không có nghĩa mọi hàng đều là các tập rời nhau của toàn bộ vector. Test invalid giữ các chiều khác nominal; interaction nhiều lỗi có chủ đích được ghi riêng. Chúng tôi dùng readback public HTTP sau thay đổi để kiểm tra hậu điều kiện.

BVA được áp dụng cho miền có thứ tự, kể cả độ dài chuỗi và số lượt nguyên. Điểm ON nằm trên mặt biên; giá trị ON có thể hợp lệ hoặc không tùy dấu ≥ hay >. Các điểm lân cận được ghi bằng số và trạng thái valid/invalid để tránh nhập nhằng thuật ngữ. Các label OFF/IN không thay thế tập giá trị cụ thể. Rỗng, enum, charset và identity là Domain classes; không tự đặt một maximum mà SRS không quy định.

API execution dùng backend copy, clock cố định và fixture reset mỗi TC. UI evidence là ảnh thật đã cung cấp; không suy timestamp chạy từ ngày sửa file, không dùng ảnh vẽ hoặc build output làm bằng chứng UI. PASS/FAIL chỉ kết luận theo criterion có evidence; OBSERVATION dành cho oracle chưa quy định; INCOMPLETE dành cho TC còn thiếu bước/precondition/evidence. Một TC INCOMPLETE có thể đã được thao tác một phần, nhưng không được cộng vào executed đủ bằng chứng.

Chúng tôi kiểm tra kỹ thuật theo Domain/Boundary đã nêu; chưa có bản lecture của môn trong workspace để xác nhận đã đối chiếu mọi quy ước của giảng viên. Nguồn phương pháp bổ trợ là ISTQB CTFL §4.2.1–4.2.2. Các giới hạn này được giữ rõ trong phần coverage, không tuyên bố exhaustive coverage toàn hệ thống.

### Bước 1 — Xác định inputs/outputs

Vector `(JWT, target identity, phone, name, shipping_address, role_attempt)`. Output gồm thông báo, response và hậu điều kiện ở profile/coupon/cart tương ứng.

### Bước 2 — Thiết lập nominal fixture

Chọn hai số phone đúng rule và thay riêng length, prefix hoặc charset. User2/user3 tách biệt để kiểm tra ownership; role tampering không bị lỗi phone che khuất.

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

## 4. Boundary Value Analysis — từng bước

1. Chọn biến có thứ tự và miền áp dụng từ rule; không lấy giới hạn tùy ý trong code.
2. Viết bất đẳng thức và xác định điểm equality hợp lệ hay không.
3. Ghi precision của fixture, lấy điểm biên và lân cận hai phía.
4. Giữ các chiều ngoài biên đang xét nominal; thêm giao biên khi có lý do.
5. Tính expected độc lập; liên kết TC và phân biệt numerical boundary với missing/type domain.
6. So actual với expected; khi rounding/MAX/reset không có rule, giữ observation hoặc giới hạn kết luận.

| Biến | Rule | Delta/precision | Điểm chọn và giải thích | Cases |
|---|---|---|---|---|
| length(phone) | 10 ≤ L ≤ 11 | 1 chữ số | 9 invalid; 10 ON lower valid; 11 ON upper valid; 12 invalid | A-API-03/01/02/04; A-UI-01–04 |
| Prefix/role/charset | Lớp rời rạc | Không có delta số học | Dùng Domain Testing; không gọi prefix=1 là biên phone number | A-D4/D5/D8 |

## 5. Kết quả thực thi

| TC | Status | Actual tóm tắt | Bug |
|---|---|---|---|
| [A-API-01](../tests/A-FR04-profile.md#a-api-01) | PASS | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678"} | — |
| [A-API-02](../tests/A-FR04-profile.md#a-api-02) | PASS | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"09123456789"} | — |
| [A-API-03](../tests/A-FR04-profile.md#a-api-03) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"091234567"} | BUG-A01 |
| [A-API-04](../tests/A-FR04-profile.md#a-api-04) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"091234567890"} | BUG-A01 |
| [A-API-05](../tests/A-FR04-profile.md#a-api-05) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":""} | BUG-A01 |
| [A-API-06](../tests/A-FR04-profile.md#a-api-06) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0"} | BUG-A01 |
| [A-API-07](../tests/A-FR04-profile.md#a-api-07) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"09123456"} | BUG-A01 |
| [A-API-08](../tests/A-FR04-profile.md#a-api-08) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678901"} | BUG-A01 |
| [A-API-09](../tests/A-FR04-profile.md#a-api-09) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"1912345678"} | BUG-A01 |
| [A-API-10](../tests/A-FR04-profile.md#a-api-10) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"19123456789"} | BUG-A01 |
| [A-API-11](../tests/A-FR04-profile.md#a-api-11) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"091234567a"} | BUG-A01 |
| [A-API-12](../tests/A-FR04-profile.md#a-api-12) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"09123 5678"} | BUG-A01 |
| [A-API-13](../tests/A-FR04-profile.md#a-api-13) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"+84912345678"} | BUG-A01 |
| [A-API-14](../tests/A-FR04-profile.md#a-api-14) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"09123-5678"} | BUG-A01 |
| [A-API-15](../tests/A-FR04-profile.md#a-api-15) | OBSERVATION | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"０９１２３４５６７８"} | — |
| [A-API-16](../tests/A-FR04-profile.md#a-api-16) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":null} | BUG-A01 |
| [A-API-17](../tests/A-FR04-profile.md#a-api-17) | PASS | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"Người Dùng HW02","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"Đường Thử Nghiệm","phone":"0912345678"} | — |
| [A-API-18](../tests/A-FR04-profile.md#a-api-18) | FAIL | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"HW02 User","email":"test@eshop.com","role":"admin","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678"} | BUG-A02 |
| [A-API-19](../tests/A-FR04-profile.md#a-api-19) | PASS | PUT /api/users/me → HTTP 200: {"message":"Profile updated"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"Owner Only","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678"}<br>GET /api/users/me → HTTP 200: {"id":3,"name":"Other User","email":"other@hw02.invalid","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"Other Street","phone":"0987654321"} | — |
| [A-API-20](../tests/A-FR04-profile.md#a-api-20) | PASS | PUT /api/users/me → HTTP 401: {"error":"Unauthorized"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"Test User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678"} | — |
| [A-API-21](../tests/A-FR04-profile.md#a-api-21) | PASS | PUT /api/users/me → HTTP 403: {"error":"Forbidden"}<br>GET /api/users/me → HTTP 200: {"id":2,"name":"Test User","email":"test@eshop.com","role":"user","login_attempts":0,"locked_until":null,"shipping_address":"1 Test Street","phone":"0912345678"} | — |
| [A-API-22](../tests/A-FR04-profile.md#a-api-22) | PASS | GET /api/users/me → HTTP 401: {"error":"Unauthorized"} | — |
| [A-UI-01](../tests/A-FR04-profile.md#a-ui-01) | PASS | Phone 091234567 bị từ chối bằng cảnh báo validation. Ảnh xác nhận bước từ chối; không có GET UI readback độc lập. | — |
| [A-UI-02](../tests/A-FR04-profile.md#a-ui-02) | FAIL | Phone hợp lệ 0912345678 bị cảnh báo không hợp lệ; thao tác cập nhật bị chặn ngay ở frontend. | BUG-A03 |
| [A-UI-03](../tests/A-FR04-profile.md#a-ui-03) | FAIL | Phone hợp lệ 09123456789 bị từ chối. Thông báo nói 9–10 chữ số, khác yêu cầu 10–11 chữ số bắt đầu bằng 0. | BUG-A03 |
| [A-UI-04](../tests/A-FR04-profile.md#a-ui-04) | PASS | Phone 091234567890 bị frontend từ chối. Kết quả từ chối đạt mục tiêu validation của UI, không chứng minh backend có validation. | — |
| [A-UI-05](../tests/A-FR04-profile.md#a-ui-05) | FAIL | Phone 1912345678 có prefix sai nhưng UI báo cập nhật thành công. API A-API-09 xác nhận riêng việc backend có thể lưu prefix sai. | BUG-A03 |
| [A-UI-06](../tests/A-FR04-profile.md#a-ui-06) | PASS | Email hiển thị ở field disabled. Source Profile.jsx dùng disabled cho input email; đây là kiểm tra thuộc tính không cho chỉnh sửa qua UI, không phải kiểm thử API đổi email. | — |
| [A-UI-07](../tests/A-FR04-profile.md#a-ui-07) | FAIL | Account A-UI-07 nhập name/address Unicode và phone hợp lệ 0912345678; UI báo phone không hợp lệ và chặn cập nhật. Persistence chưa đạt tới vì BUG-A03. | BUG-A03 |

## 6. Spec vs Code và bug groups

| Bug | Rule | Nguyên nhân có source support | Representative |
|---|---|---|---|
| [BUG-A01](../bugs/BUG-A01.md) | FR-04.2 | Route PUT lấy phone từ body rồi UPDATE mà không validate prefix/length/charset. | A-API-03 |
| [BUG-A02](../bugs/BUG-A02.md) | FR-04.4 / SEC-06 | Route destructure role, nếu truthy thì thêm role=? vào UPDATE; đây là nhánh explicit, không phải Object.assign/spread. | A-API-18 |
| [BUG-A03](../bugs/BUG-A03.md) | FR-04.2 | Profile.jsx dùng /^[1-9][0-9]{8,9}$/ và thông báo 9–10 chữ số; khác starts0/10–11digits. | A-UI-02 |

## 7. AI gap analysis

Các mục dưới đây là technical corrections có evidence của quá trình soạn/kiểm tra; không tự gán mọi phát hiện cho sinh viên hoặc một model bên ngoài. Bản nháp nguyên văn giữ trong AI audit snapshot.

| Gap | Nhóm nguyên nhân | Evidence/điều sai | Cách sửa |
|---|---|---|---|
| Encoding bị áp thêm | Prompt/assumption | Metadata cũ ghi ASCII nhưng SRS chỉ nói chữ số | Giữ A-API-15 OBSERVATION; sửa oracle, không thêm bug Unicode |
| API và UI bị đồng nhất | Giới hạn suy luận | A-API-01/02 PASS trong khi A-UI-02/03 FAIL | Tách seam; tạo BUG-A03 từ ảnh UI thật |
| Persistence bị kết luận từ alert | Độ phức tạp trạng thái | Ảnh cũ sai phone; ảnh mới với phone hợp lệ bị BUG-A03 chặn | Chốt FAIL theo valid update; không suy persistence hoặc lỗi Unicode |

## 8. Coverage và giới hạn

Các domain và điểm biên đã liệt kê đều có TC-ID. Một số TC có evidence một phần nên chưa có verdict hoàn chỉnh. Không suy full requirement coverage từ số TC hoặc số ảnh; class chưa có rule rõ không biến thành bug. Các form/UI tiêu chuẩn chung ngoài mục tiêu các TC hiện tại chưa được kiểm chứng exhaustive. Lecture chưa có trong bộ nguồn; cần đối chiếu bản giảng viên trước nộp.

[Detailed test cases](../tests/A-FR04-profile.md) · [Raw API evidence](../evidence/execution/A-api.md) · [Bug index](../bugs/bug-reports.md).
