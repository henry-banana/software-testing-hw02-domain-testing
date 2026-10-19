# D — Domain Testing và Boundary Value Analysis

**Feature:** Mobile productDetail — Chi tiết sản phẩm và quantity<br>
**SUT:** `85af3ba875c88283615e22cb108f13e2fccaf0e9`.

## 1. Requirements và oracle

| Rule | Nội dung theo SRS | Domain |
|---|---|---|
| FR-20 | Mobile có chức năng xem sản phẩm và giỏ hàng | D-D1/D6 |
| FR-06 → Mobile mapping | Hiển thị ảnh, tên, giá, mô tả, category; quantity nguyên dương ≥1; feedback khi Add | D-D1/D3–D6 |
| FR-07 → Mobile mapping | Cùng sản phẩm thêm lại phải tăng quantity, không tạo dòng mới | D-D6 |
| Unspecified | Không có MAX quantity, JSON price type, HTTP 404 hay default reset policy bắt buộc | D-D2/D7 |

[Nguồn SRS cố định](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md). Các tên rule dạng FR-04.1 trong báo cáo là nhãn nội bộ để truy vết, không phải mã mới của SRS.

FR-20 liệt kê chức năng Mobile ở mức tổng quan. Chúng tôi áp dụng các rule hành vi xem sản phẩm/giỏ của FR-06/07 cho màn tương ứng trên Mobile, công khai mapping này cho cả quantity lẫn category. Không áp DOM `<h1>`/HTML input cho native. BUG-D02 được kết luận trong phạm vi mapping này; nếu giảng viên quy định Mobile khác, cập nhật oracle đồng bộ thay vì chỉ bỏ riêng case category.

## 2. Domain Testing — quy trình từng bước

Chúng tôi lấy SRS làm oracle, sau đó dùng source để xây dựng giả thuyết và giải thích nguyên nhân. Source không thay thế yêu cầu. Mỗi TC có ID ổn định; một TC có thể phủ cả Domain Testing và BVA nhưng chỉ được tính một lần. Chúng tôi tách API với Web/Admin/Mobile UI vì validation ở một lớp không chứng minh lớp còn lại đạt.

Với từng input/state, chúng tôi xác định miền hợp lệ, phần bù không hợp lệ, precision và các ràng buộc giữa các chiều. Các lớp trong cùng một chiều được chọn để phân biệt hành vi; bảng nhiều chiều không có nghĩa mọi hàng đều là các tập rời nhau của toàn bộ vector. Test invalid giữ các chiều khác nominal; interaction nhiều lỗi có chủ đích được ghi riêng. Chúng tôi dùng readback public HTTP sau thay đổi để kiểm tra hậu điều kiện.

BVA được áp dụng cho miền có thứ tự, kể cả độ dài chuỗi và số lượt nguyên. Điểm ON nằm trên mặt biên; giá trị ON có thể hợp lệ hoặc không tùy dấu ≥ hay >. Các điểm lân cận được ghi bằng số và trạng thái valid/invalid để tránh nhập nhằng thuật ngữ. Các label OFF/IN không thay thế tập giá trị cụ thể. Rỗng, enum, charset và identity là Domain classes; không tự đặt một maximum mà SRS không quy định.

API execution dùng backend copy, clock cố định và fixture reset mỗi TC. UI evidence là ảnh thật đã cung cấp; không suy timestamp chạy từ ngày sửa file, không dùng ảnh vẽ hoặc build output làm bằng chứng UI. PASS/FAIL chỉ kết luận theo criterion có evidence; OBSERVATION dành cho oracle chưa quy định; INCOMPLETE dành cho TC còn thiếu bước/precondition/evidence. Một TC INCOMPLETE có thể đã được thao tác một phần, nhưng không được cộng vào executed đủ bằng chứng.

Chúng tôi kiểm tra kỹ thuật theo Domain/Boundary đã nêu; chưa có bản lecture của môn trong workspace để xác nhận đã đối chiếu mọi quy ước của giảng viên. Nguồn phương pháp bổ trợ là ISTQB CTFL §4.2.1–4.2.2. Các giới hạn này được giữ rõ trong phần coverage, không tuyên bố exhaustive coverage toàn hệ thống.

### Bước 1 — Xác định inputs/outputs

Vector `(selected product, product data, quantity string, cart state, số lần Add, navigation)`. Output gồm thông báo, response và hậu điều kiện ở profile/coupon/cart tương ứng.

### Bước 2 — Thiết lập nominal fixture

Tách product data, quantity và cart/navigation. Giỏ ban đầu trống ngăn quantity cũ che mất lượng Add. Không dùng keyboard numeric như bằng chứng validation; mixed/fraction là chuỗi đầu vào độc lập.

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
| D-D1 | Product tồn tại/detail | Valid data | iPhone 1; Samsung 2 | Dữ liệu đúng; đủ ảnh/tên/giá/mô tả/category | [D-API-01](../tests/D-mobile-product-detail.md#d-api-01), [D-API-02](../tests/D-mobile-product-detail.md#d-api-02), [D-UI-09](../tests/D-mobile-product-detail.md#d-ui-09), [D-UI-10](../tests/D-mobile-product-detail.md#d-ui-10) |
| D-D2 | Product không tồn tại | Observation | id=999999 | Ghi HTTP/body; SRS không mandate 404 | [D-API-03](../tests/D-mobile-product-detail.md#d-api-03) |
| D-D3 | Quantity rỗng/không dương | Invalid | rỗng; −1; 0 | Từ chối, không thêm sản phẩm | [D-UI-01](../tests/D-mobile-product-detail.md#d-ui-01), [D-UI-02](../tests/D-mobile-product-detail.md#d-ui-02), [D-UI-03](../tests/D-mobile-product-detail.md#d-ui-03) |
| D-D4 | Quantity nguyên dương | Valid boundary | 1; 2 | Giữ đúng quantity và đơn giá×quantity | [D-UI-04](../tests/D-mobile-product-detail.md#d-ui-04), [D-UI-05](../tests/D-mobile-product-detail.md#d-ui-05) |
| D-D5 | Quantity sai kiểu chuỗi | Invalid | 1.5; abc; 1abc | Từ chối, không tự truncate/default | [D-UI-06](../tests/D-mobile-product-detail.md#d-ui-06), [D-UI-07](../tests/D-mobile-product-detail.md#d-ui-07), [D-UI-08](../tests/D-mobile-product-detail.md#d-ui-08) |
| D-D6 | Add feedback và repeat | State/action | Add một lần; hai lần cùng SP | Feedback; gộp một dòng, cộng quantity | [D-UI-11](../tests/D-mobile-product-detail.md#d-ui-11), [D-UI-12](../tests/D-mobile-product-detail.md#d-ui-12) |
| D-D7 | Switch/large input | Observation | Chuyển product; quantity rất lớn | Ghi hành vi; không tự thêm reset/MAX rule | [D-UI-13](../tests/D-mobile-product-detail.md#d-ui-13), [D-UI-14](../tests/D-mobile-product-detail.md#d-ui-14) |

## 4. Boundary Value Analysis — từng bước

1. Chọn biến có thứ tự và miền áp dụng từ rule; không lấy giới hạn tùy ý trong code.
2. Viết bất đẳng thức và xác định điểm equality hợp lệ hay không.
3. Ghi precision của fixture, lấy điểm biên và lân cận hai phía.
4. Giữ các chiều ngoài biên đang xét nominal; thêm giao biên khi có lý do.
5. Tính expected độc lập; liên kết TC và phân biệt numerical boundary với missing/type domain.
6. So actual với expected; khi rounding/MAX/reset không có rule, giữ observation hoặc giới hạn kết luận.

| Biến | Rule | Delta/precision | Điểm chọn và giải thích | Cases |
|---|---|---|---|---|
| quantity q | q ∈ ℤ, q ≥ 1 | 1 đơn vị | 0 OFF invalid; 1 ON valid; 2 valid interior; −1 invalid interior | D-UI-02–05 |
| quantity sai kiểu | Ngoài miền integer | Không có bước số học | Rỗng/1.5/abc/1abc là domain/type class | D-UI-01/06/07/08 |
| Upper quantity | SRS không quy định | Không tự đặt | Quan sát input lớn; không coi stock/2^53 là business boundary | D-UI-14 |

## 5. Kết quả thực thi

| TC | Status | Actual tóm tắt | Bug |
|---|---|---|---|
| [D-API-01](../tests/D-mobile-product-detail.md#d-api-01) | PASS | GET /api/products/1 → HTTP 200: {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"description":"Điện thoại cao cấp của Apple","imageUrl":"https://placehold.co/300x300/png?text=iPhone+15","category_id":1} | — |
| [D-API-02](../tests/D-mobile-product-detail.md#d-api-02) | PASS | GET /api/products/2 → HTTP 200: {"id":2,"name":"Samsung Galaxy S24 Ultra","price":"28000000","description":"Màn hình hiển thị xuất sắc, camera siêu zoom","imageUrl":"https://placehold.co/300x300/png?text=Samsung+S24","category_id":1} | — |
| [D-API-03](../tests/D-mobile-product-detail.md#d-api-03) | OBSERVATION | GET /api/products/999999 → HTTP 200: {} | — |
| [D-UI-01](../tests/D-mobile-product-detail.md#d-ui-01) | FAIL | Nhập quantity="" vẫn nhận alert thêm thành công; ảnh cart cho thấy sản phẩm có quantity=1. | BUG-D01 |
| [D-UI-02](../tests/D-mobile-product-detail.md#d-ui-02) | FAIL | Nhập quantity="-1" vẫn nhận alert thêm thành công; ảnh cart cho thấy sản phẩm có quantity=1. | BUG-D01 |
| [D-UI-03](../tests/D-mobile-product-detail.md#d-ui-03) | FAIL | Nhập quantity="0" vẫn nhận alert thêm thành công; ảnh cart cho thấy sản phẩm có quantity=1. | BUG-D01 |
| [D-UI-04](../tests/D-mobile-product-detail.md#d-ui-04) | PASS | Cart Samsung Galaxy S24 Ultra có quantity=1, đơn giá 28000000, thành tiền 28000000. | — |
| [D-UI-05](../tests/D-mobile-product-detail.md#d-ui-05) | PASS | Samsung quantity=2, thành tiền 56000000; khớp 28000000×2. | — |
| [D-UI-06](../tests/D-mobile-product-detail.md#d-ui-06) | FAIL | Nhập quantity="1.5" vẫn nhận alert thêm thành công; ảnh cart cho thấy sản phẩm có quantity=1. | BUG-D01 |
| [D-UI-07](../tests/D-mobile-product-detail.md#d-ui-07) | FAIL | Nhập quantity="abc" vẫn nhận alert thêm thành công; ảnh cart cho thấy sản phẩm có quantity=1. | BUG-D01 |
| [D-UI-08](../tests/D-mobile-product-detail.md#d-ui-08) | FAIL | Input 1abc vẫn nhận alert thêm thành công. Chỉ điều kiện phải từ chối đã bị vi phạm; chưa có ảnh cart để kết luận quantity lưu cho riêng lượt này. | BUG-D01 |
| [D-UI-09](../tests/D-mobile-product-detail.md#d-ui-09) | FAIL | Detail Samsung có ảnh, tên, giá, mô tả và quantity nhưng không có danh mục. Source renderProductDetail cũng không render category. | BUG-D02 |
| [D-UI-10](../tests/D-mobile-product-detail.md#d-ui-10) | PASS | Giá Samsung hiển thị 28.000.000 ₫ dù API product 2 trả price dạng chuỗi số; không có lỗi hiển thị trong ảnh. | — |
| [D-UI-11](../tests/D-mobile-product-detail.md#d-ui-11) | PASS | Sau Add, Mobile hiển thị Alert Thành công/Đã thêm vào giỏ hàng. Mục tiêu feedback đạt. | — |
| [D-UI-12](../tests/D-mobile-product-detail.md#d-ui-12) | INCOMPLETE | Cart có một dòng quantity=2 và có ảnh phản hồi, nhưng ảnh không xác nhận hai lần Add với quantity=1 từ giỏ trống. | — |
| [D-UI-13](../tests/D-mobile-product-detail.md#d-ui-13) | OBSERVATION | Ảnh MacBook có cart quantity=2 và phản hồi Add. Không có chuỗi chuyển product đủ rõ để kết luận reset quantity. | — |
| [D-UI-14](../tests/D-mobile-product-detail.md#d-ui-14) | OBSERVATION | Có input số dài, alert thành công và cart. Ô input có thể cuộn ngang; không đồng nhất literal trong ảnh với 9007199254740992 của thiết kế. | — |

## 6. Spec vs Code và bug groups

| Bug | Rule | Nguyên nhân có source support | Representative |
|---|---|---|---|
| [BUG-D01](../bugs/BUG-D01.md) | FR-20 → FR-06 quantity mapping | normalizeQuantity dùng parseInt(value,10); invalid/không dương default1, fraction/mixed text bị truncate rồi nhận như số nguyên. | D-UI-01 |
| [BUG-D02](../bugs/BUG-D02.md) | FR-20 → FR-06 detail mapping | renderProductDetail render ảnh/tên/giá/mô tả/quantity nhưng không render category; API có category_id chưa được chuyển thành nhãn. | D-UI-09 |

## 7. AI gap analysis

Các mục dưới đây là technical corrections có evidence của quá trình soạn/kiểm tra; không tự gán mọi phát hiện cho sinh viên hoặc một model bên ngoài. Bản nháp nguyên văn giữ trong AI audit snapshot.

| Gap | Nhóm nguyên nhân | Evidence/điều sai | Cách sửa |
|---|---|---|---|
| Sai nhãn BVA | Prompt/assumption | Rỗng/fraction từng bị coi như nearest integer boundary | Biên integer chỉ 0/1/2; giữ type classes riêng |
| False PASS đầy đủ detail | Giới hạn đọc evidence | D-UI-09 expected có category nhưng ảnh/source không render | FAIL theo mapping công khai; lập BUG-D02 |
| Suy diễn cart từ alert | Giới hạn công cụ | D-UI-08 có success nhưng thiếu cart | FAIL chỉ cho chấp nhận mixed input; không khẳng định cart=1 của lượt đó |
| Sequence bị suy từ ảnh cuối | Độ phức tạp trạng thái | Cart quantity2 không chứng minh hai lần Add quantity1 | D-UI-12 INCOMPLETE; switch/large giữ observation |

## 8. Coverage và giới hạn

Các domain và điểm biên đã liệt kê đều có TC-ID. Một số TC có evidence một phần nên chưa có verdict hoàn chỉnh. Không suy full requirement coverage từ số TC hoặc số ảnh; class chưa có rule rõ không biến thành bug. Các form/UI tiêu chuẩn chung ngoài mục tiêu các TC hiện tại chưa được kiểm chứng exhaustive. Lecture chưa có trong bộ nguồn; cần đối chiếu bản giảng viên trước nộp.

[Detailed test cases](../tests/D-mobile-product-detail.md) · [Raw API evidence](../evidence/execution/D-api.md) · [Bug index](../bugs/bug-reports.md).
