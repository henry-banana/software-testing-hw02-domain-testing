# Feature D - Mobile productDetail - Chi tiết sản phẩm và quantity

### 6.1. Requirements và oracle

| Rule | Nội dung theo SRS | Domain |
|---|---|---|
| FR-20 | Mobile có chức năng xem sản phẩm và giỏ hàng | D-D1/D6 |
| FR-06 -> Mobile mapping | Hiển thị ảnh, tên, giá, mô tả, category; quantity nguyên dương >=1; feedback khi Add | D-D1/D3-D6 |
| FR-07 -> Mobile mapping | Cùng sản phẩm thêm lại phải tăng quantity, không tạo dòng mới | D-D6 |
| Unspecified | Không có MAX quantity, JSON price type, HTTP 404 hay default reset policy bắt buộc | D-D2/D7 |

[Nguồn SRS cố định](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md). Các nhãn rule trong bảng được dùng để truy vết giữa yêu cầu, domain và test case.

FR-20 mô tả chức năng Mobile ở mức tổng quan. Các rule xem sản phẩm và giỏ hàng của FR-06/07 được ánh xạ sang màn tương ứng, áp dụng nhất quán cho quantity và category. Ràng buộc DOM `<h1>`/HTML input không được áp dụng cho native. Kết luận FR20-07 được giới hạn trong phạm vi mapping hành vi đã nêu.

### 6.2. Domain Testing - quy trình từng bước

#### Bước 1 - Xác định inputs/outputs

Vector gồm `(selected product, product data, quantity string, cart state, số lần Add, navigation)`. Đầu ra gồm chi tiết sản phẩm, phản hồi Add, quantity trong giỏ và thành tiền tương ứng.

#### Bước 2 - Thiết lập nominal fixture

Sản phẩm có dữ liệu xác định và quantity=1 được dùng làm đối chứng. Giỏ trống được thiết lập cho các case quantity; case thêm lặp dùng cùng một sản phẩm để kiểm tra gộp dòng.

#### Bước 3 - Chia lớp hợp lệ/không hợp lệ

Quantity được chia thành số nguyên dương, zero, số âm, rỗng, thập phân và chuỗi lẫn ký tự. Product data, cart merge và navigation được phân tích riêng. Quantity lớn và chính sách reset được ghi nhận OBSERVATION khi SRS không quy định.

#### Bước 4 - Cô lập một điều kiện sai

Sản phẩm và trạng thái giỏ được giữ cố định khi thay quantity. Keyboard numeric được xem là cơ chế nhập liệu, không phải bằng chứng validation; chuỗi 1.5, abc và 1abc được đánh giá theo dữ liệu thực tế.

#### Bước 5 - Chọn đại diện và giải thích

Các giá trị -1, 0, 1 và 2 phân biệt miền số nguyên dương. Rỗng, 1.5, abc và 1abc đại diện cho các lớp sai kiểu/định dạng. Input lớn được dùng làm phép quan sát, không được gán một upper business boundary tùy ý.

#### Bước 6 - Phân tích cross-constraint

Quantity phải là số nguyên dương, đồng thời ảnh hưởng đúng đến lượng trong giỏ và tổng tiền. Thêm lặp cùng sản phẩm phải tăng quantity trên một dòng; dữ liệu category được đánh giá theo mapping FR-06 sang Mobile.

#### Bước 7 - Đối chiếu hypothesis bằng thực thi

Ảnh native được dùng để kiểm tra input, phản hồi Add, chi tiết sản phẩm và trạng thái giỏ. API GET /api/products/:id hỗ trợ đối chiếu dữ liệu sản phẩm, không thay thế bằng chứng thao tác trên Mobile.

#### Bước 8 - Review coverage và AI output

Domain/type classes được tách khỏi BVA số nguyên. Với D-UI-08, FAIL chỉ kết luận việc chấp nhận mixed input. Với D-UI-12, ảnh giỏ thể hiện hậu điều kiện và xác nhận thao tác ghi nhận chuỗi Add; hai loại bằng chứng được phân biệt rõ.

### 6.3. Domain partition và traceability

| Domain ID | Chiều/lớp | Loại | Representative | Expected | TC coverage |
|---|---|---|---|---|---|
| D-D1 | Product tồn tại/detail | Valid data | iPhone 1; Samsung 2 | Dữ liệu đúng; đủ ảnh/tên/giá/mô tả/category | [D-API-01](../tests/D-FR20-mobile-product-detail.md#d-api-01), [D-API-02](../tests/D-FR20-mobile-product-detail.md#d-api-02), [D-UI-09](../tests/D-FR20-mobile-product-detail.md#d-ui-09), [D-UI-10](../tests/D-FR20-mobile-product-detail.md#d-ui-10) |
| D-D2 | Product không tồn tại | Observation | id=999999 | Ghi HTTP/body; SRS không mandate 404 | [D-API-03](../tests/D-FR20-mobile-product-detail.md#d-api-03) |
| D-D3 | Quantity rỗng/không dương | Invalid | rỗng; -1; 0 | Từ chối, không thêm sản phẩm | [D-UI-01](../tests/D-FR20-mobile-product-detail.md#d-ui-01), [D-UI-02](../tests/D-FR20-mobile-product-detail.md#d-ui-02), [D-UI-03](../tests/D-FR20-mobile-product-detail.md#d-ui-03) |
| D-D4 | Quantity nguyên dương | Valid boundary | 1; 2 | Giữ đúng quantity và đơn giáxquantity | [D-UI-04](../tests/D-FR20-mobile-product-detail.md#d-ui-04), [D-UI-05](../tests/D-FR20-mobile-product-detail.md#d-ui-05) |
| D-D5 | Quantity sai kiểu chuỗi | Invalid | 1.5; abc; 1abc | Từ chối, không tự truncate/default | [D-UI-06](../tests/D-FR20-mobile-product-detail.md#d-ui-06), [D-UI-07](../tests/D-FR20-mobile-product-detail.md#d-ui-07), [D-UI-08](../tests/D-FR20-mobile-product-detail.md#d-ui-08) |
| D-D6 | Add feedback và repeat | State/action | Add một lần; hai lần cùng SP | Feedback; gộp một dòng, cộng quantity | [D-UI-11](../tests/D-FR20-mobile-product-detail.md#d-ui-11), [D-UI-12](../tests/D-FR20-mobile-product-detail.md#d-ui-12) |
| D-D7 | Switch/large input | Observation | Chuyển product; quantity rất lớn | Ghi hành vi; không tự thêm reset/MAX rule | [D-UI-13](../tests/D-FR20-mobile-product-detail.md#d-ui-13), [D-UI-14](../tests/D-FR20-mobile-product-detail.md#d-ui-14) |

### 6.4. Boundary Value Analysis - từng bước

1. Từ yêu cầu quantity nguyên dương, miền hợp lệ được xác định là q nguyên và q >= 1.
2. Điểm biên 1 thuộc miền hợp lệ; 0 thuộc miền không hợp lệ.
3. Bước lân cận được chọn là 1 đơn vị, tạo tập 0/1/2; -1 bổ sung đại diện invalid interior.
4. Product và cart fixture được giữ cố định khi thay quantity; phản hồi Add và hậu điều kiện trong giỏ được đối chiếu theo từng case.
5. Rỗng, 1.5, abc và 1abc được xếp vào domain/type classes, không dùng thay cho điểm lân cận số nguyên.
6. Input lớn được ghi nhận theo hành vi quan sát; upper quantity, stock hoặc giới hạn biểu diễn số không được chuyển thành business boundary khi thiếu rule.

| Biến | Rule | Delta/precision | Điểm chọn và giải thích | Cases |
|---|---|---|---|---|
| quantity q | q in ℤ, q >= 1 | 1 đơn vị | 0 OFF invalid; 1 ON valid; 2 valid interior; -1 invalid interior | D-UI-02-05 |
| quantity sai kiểu | Ngoài miền integer | Không có bước số học | Rỗng/1.5/abc/1abc là domain/type class | D-UI-01/06/07/08 |
| Upper quantity | SRS không quy định | Không tự đặt | Quan sát input lớn; không coi stock/2^53 là business boundary | D-UI-14 |

### 6.5. Kết quả thực thi

| TC | Status | Actual tóm tắt | Bug |
|---|---|---|---|
| [D-API-01](../tests/D-FR20-mobile-product-detail.md#d-api-01) | PASS | GET /api/products/1 -> HTTP 200: {"id":1,"name":"iPhone 15 Pro Max","price":30000000,"description":"Điện thoại cao cấp của Apple","imageUrl":"https://placehold.co/300x300/png?text=iPhone+15","category_id":1} | - |
| [D-API-02](../tests/D-FR20-mobile-product-detail.md#d-api-02) | PASS | GET /api/products/2 -> HTTP 200: {"id":2,"name":"Samsung Galaxy S24 Ultra","price":"28000000","description":"Màn hình hiển thị xuất sắc, camera siêu zoom","imageUrl":"https://placehold.co/300x300/png?text=Samsung+S24","category_id":1} | - |
| [D-API-03](../tests/D-FR20-mobile-product-detail.md#d-api-03) | OBSERVATION | GET /api/products/999999 -> HTTP 200: {} | - |
| [D-UI-01](../tests/D-FR20-mobile-product-detail.md#d-ui-01) | FAIL | Nhập quantity="" vẫn nhận alert thêm thành công; ảnh cart cho thấy sản phẩm có quantity=1. | FR20-01, FR20-02, FR20-03, FR20-04, FR20-05, FR20-06 |
| [D-UI-02](../tests/D-FR20-mobile-product-detail.md#d-ui-02) | FAIL | Nhập quantity="-1" vẫn nhận alert thêm thành công; ảnh cart cho thấy sản phẩm có quantity=1. | FR20-01, FR20-02, FR20-03, FR20-04, FR20-05, FR20-06 |
| [D-UI-03](../tests/D-FR20-mobile-product-detail.md#d-ui-03) | FAIL | Nhập quantity="0" vẫn nhận alert thêm thành công; ảnh cart cho thấy sản phẩm có quantity=1. | FR20-01, FR20-02, FR20-03, FR20-04, FR20-05, FR20-06 |
| [D-UI-04](../tests/D-FR20-mobile-product-detail.md#d-ui-04) | PASS | Cart Samsung Galaxy S24 Ultra có quantity=1, đơn giá 28000000, thành tiền 28000000. | - |
| [D-UI-05](../tests/D-FR20-mobile-product-detail.md#d-ui-05) | PASS | Samsung quantity=2, thành tiền 56000000; khớp 28000000x2. | - |
| [D-UI-06](../tests/D-FR20-mobile-product-detail.md#d-ui-06) | FAIL | Nhập quantity="1.5" vẫn nhận alert thêm thành công; ảnh cart cho thấy sản phẩm có quantity=1. | FR20-01, FR20-02, FR20-03, FR20-04, FR20-05, FR20-06 |
| [D-UI-07](../tests/D-FR20-mobile-product-detail.md#d-ui-07) | FAIL | Nhập quantity="abc" vẫn nhận alert thêm thành công; ảnh cart cho thấy sản phẩm có quantity=1. | FR20-01, FR20-02, FR20-03, FR20-04, FR20-05, FR20-06 |
| [D-UI-08](../tests/D-FR20-mobile-product-detail.md#d-ui-08) | FAIL | Input 1abc vẫn nhận alert thêm thành công. Chỉ điều kiện phải từ chối đã bị vi phạm; chưa có ảnh cart để kết luận quantity lưu cho riêng lượt này. | FR20-01, FR20-02, FR20-03, FR20-04, FR20-05, FR20-06 |
| [D-UI-09](../tests/D-FR20-mobile-product-detail.md#d-ui-09) | FAIL | Detail Samsung có ảnh, tên, giá, mô tả và quantity nhưng không có danh mục. Source renderProductDetail cũng không render category. | FR20-07 |
| [D-UI-10](../tests/D-FR20-mobile-product-detail.md#d-ui-10) | PASS | Giá Samsung hiển thị 28.000.000 VND dù API product 2 trả price dạng chuỗi số; không có lỗi hiển thị trong ảnh. | - |
| [D-UI-11](../tests/D-FR20-mobile-product-detail.md#d-ui-11) | PASS | Sau Add, Mobile hiển thị Alert Thành công/Đã thêm vào giỏ hàng. Mục tiêu feedback đạt. | - |
| [D-UI-12](../tests/D-FR20-mobile-product-detail.md#d-ui-12) | PASS | Cart có đúng một dòng iPhone 15 Pro Max, quantity=2, đơn giá30000000 và thành tiền60000000. Ảnh được đối chiếu với D-UI-12 qua xác nhận thao tác. Ảnh thể hiện hậu điều kiện cuối; chuỗi hai lần Add được ghi nhận qua xác nhận thao tác riêng. | - |
| [D-UI-13](../tests/D-FR20-mobile-product-detail.md#d-ui-13) | OBSERVATION | Ảnh MacBook có cart quantity=2 và phản hồi Add. Không có chuỗi chuyển product đủ rõ để kết luận reset quantity. | - |
| [D-UI-14](../tests/D-FR20-mobile-product-detail.md#d-ui-14) | OBSERVATION | Có input số dài, alert thành công và cart. Ô input có thể cuộn ngang; không đồng nhất literal trong ảnh với 9007199254740992 của thiết kế. | - |

### 6.6. Spec vs Code và findings

| ID | Điều kiện vi phạm | Oracle / root cause |
|---|---|---|
| [FR20-01](../bugs/FR20-01.md) | Mobile Add to Cart accepts an empty quantity | FR-20 mapped to FR-06 positive integer quantity; The Mobile handler coerces the quantity with parsing/fallback instead of validating the full input. |
| [FR20-02](../bugs/FR20-02.md) | Mobile Add to Cart accepts a negative quantity | FR-20 mapped to FR-06 positive integer quantity; The Mobile handler coerces the quantity with parsing/fallback instead of validating the full input. |
| [FR20-03](../bugs/FR20-03.md) | Mobile Add to Cart accepts zero quantity | FR-20 mapped to FR-06 positive integer quantity; The Mobile handler coerces the quantity with parsing/fallback instead of validating the full input. |
| [FR20-04](../bugs/FR20-04.md) | Mobile Add to Cart accepts a fractional quantity | FR-20 mapped to FR-06 positive integer quantity; The Mobile handler coerces the quantity with parsing/fallback instead of validating the full input. |
| [FR20-05](../bugs/FR20-05.md) | Mobile Add to Cart accepts an alphabetic quantity | FR-20 mapped to FR-06 positive integer quantity; The Mobile handler coerces the quantity with parsing/fallback instead of validating the full input. |
| [FR20-06](../bugs/FR20-06.md) | Mobile Add to Cart accepts a mixed digit-and-letter quantity | FR-20 mapped to FR-06 positive integer quantity; The Mobile handler coerces the quantity with parsing/fallback instead of validating the full input. |
| [FR20-07](../bugs/FR20-07.md) | Mobile product detail omits the product category | FR-20 mapped to FR-06 detail fields; renderProductDetail has no category-label rendering. |
| [FR20-08](../bugs/FR20-08.md) | Mobile positive Add to Cart action is green instead of blue | FR-21 positive action colors; The positive action is assigned the greenButton style rather than the blue primary-action style. |

### 6.7. AI gap analysis

Các sai lệch trong đầu ra AI và cách hiệu chỉnh được đối chiếu với rule, raw record và ảnh tương ứng. Bản nháp gốc được lưu trong AI audit snapshot.

| Gap | Nhóm nguyên nhân | Evidence/điều sai | Cách sửa |
|---|---|---|---|
| Sai nhãn BVA | Prompt/assumption | Rỗng/fraction từng bị coi như nearest integer boundary | Biên integer chỉ 0/1/2; giữ type classes riêng |
| False PASS đầy đủ detail | Giới hạn đọc evidence | D-UI-09 expected có category nhưng ảnh/source không render | FAIL theo mapping công khai; lập FR20-07 |
| Suy diễn cart từ alert | Giới hạn công cụ | D-UI-08 có success nhưng thiếu cart | FAIL chỉ cho chấp nhận mixed input; không khẳng định cart=1 của lượt đó |
| Sequence bị suy từ ảnh cuối | Độ phức tạp trạng thái | Cart quantity2 không chứng minh hai lần Add quantity1 | D-UI-12 được đánh giá PASS từ ảnh hậu điều kiện kết hợp xác nhận thao tác; switch/large giữ OBSERVATION |

### 6.8. Coverage và giới hạn

Coverage gồm chi tiết sản phẩm, quantity nguyên dương, các lớp sai kiểu, phản hồi Add và cart merge. D-UI-10 là phép đối chiếu sản phẩm khác với cùng domain thiếu category của D-UI-09. D-UI-13/14 giữ OBSERVATION cho navigation/reset và input lớn do SRS không định nghĩa chính sách tương ứng. Ảnh trạng thái cuối và xác nhận chuỗi thao tác được sử dụng theo phạm vi chứng minh riêng.

[Detailed test cases](../tests/D-FR20-mobile-product-detail.md), [Raw API evidence](../evidence/execution/D-api.md), [Bug index](../bugs/bug-reports.md).


### Kiểm thử contract và state bổ sung

| Domain | Chiều phân hoạch | Oracle / controls | TC-ID | Kết luận |
|---|---|---|---|---|
| D-D8 | Positive-action visual contract | Nút Thêm vào giỏ hàng là positive action, FR-21 quy định màu xanh dương; ảnh native cho thấy xanh lá. | D-UI-15 | FR20-08 |

Các lớp bổ sung được suy từ contract, security property và state transition; không gắn nhãn BVA cho boolean/DOM/enum. Riêng phone Mobile dùng cùng các biên độ dài 9/10/11/12, với các chiều prefix được cô lập.

| TC-ID | Seam | Status | Actual / bug |
|---|---|---|---|
| [D-UI-15](../tests/D-FR20-mobile-product-detail.md#d-ui-15) | UI | FAIL | Product-detail positive action follows the blue-button rule / FR20-08 |

AI gap mới: các ca quantity/detail trước đó bỏ qua màu positive action trong FR-21. D-UI-15 đối chiếu nút xanh lá trong ảnh native gốc cùng styles.greenButton=#16a34a. Không có thiết bị kết nối trong đợt mở rộng, nên không tuyên bố đã thực hiện native run mới.

[A execution](../evidence/execution/A-execution.md), [B execution](../evidence/execution/B-execution.md), [C execution](../evidence/execution/C-execution.md), [D execution](../evidence/execution/D-execution.md).
