# Feature B - FR-09 - Áp dụng mã giảm giá

### 4.1. Requirements và oracle

| Rule | Nội dung theo SRS | Domain |
|---|---|---|
| C1 | Code tồn tại và is_active=1 | B-D4 |
| C2 | now < expired_at | B-D5 |
| C3 | total >= min_order_amount | B-D2 |
| C4 | JWT hợp lệ | B-D7 |
| C5 | Usage của đúng user xác thực < limit | B-D6/D8 |
| Formula | percent: Txvalue/100; fixed: value; final=T-discount | B-D1/D3 |
| Intersection | Đồng thời đáp ứng mọi điều kiện; không quy định error precedence | B-D9/D10 |

[Nguồn SRS cố định](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md). Các nhãn rule trong bảng được dùng để truy vết giữa yêu cầu, domain và test case.

### 4.2. Domain Testing - quy trình từng bước

#### Bước 1 - Xác định inputs/outputs

Vector gồm `(code, active/existence, now/expiry, total/minimum, JWT identity, used/limit, type/value)`. Đầu ra gồm quyết định chấp nhận/từ chối, discount_amount, final_amount và phản hồi Checkout UI.

#### Bước 2 - Thiết lập nominal fixture

Fixed coupon được dùng để cô lập minimum, expiry và usage khỏi công thức phần trăm. Các coupon SAVE10, BIGBUY, VIP100, EXPIRED, OFF và TIME cung cấp trạng thái đối chứng; clock API được cố định theo Mục 1.2.

#### Bước 3 - Chia lớp hợp lệ/không hợp lệ

Domain được xây dựng cho điều kiện tồn tại/active, tổng tiền, hạn sử dụng, JWT, số lượt dùng, danh tính user và loại coupon. Các điều kiện được biểu diễn bằng C1-C5; công thức fixed/percent được kiểm tra độc lập.

#### Bước 4 - Cô lập một điều kiện sai

Mỗi case đơn điều kiện giữ bốn điều kiện C1-C5 còn lại hợp lệ. B-API-25 kết hợp nhiều điều kiện sai có chủ đích để quan sát validation; thứ tự ưu tiên thông báo lỗi không được bổ sung vào expected.

#### Bước 5 - Chọn đại diện và giải thích

Các đại diện gồm code hợp lệ, không tồn tại, inactive và expired; tổng tiền dưới/bằng/trên minimum; usage trước/tại/sau limit. Tổng tiền cho kết quả phần trăm nguyên được chọn để cô lập lỗi công thức khỏi vấn đề làm tròn.

#### Bước 6 - Phân tích cross-constraint

Coupon chỉ hợp lệ khi C1 AND C2 AND C3 AND C4 AND C5 cùng đúng. Usage phải gắn với user xác thực từ JWT; body user_id không được thay thế danh tính này. B-API-24 kiểm tra giao điểm total=minimum và used=limit-1.

#### Bước 7 - Đối chiếu hypothesis bằng thực thi

POST /api/apply-coupon được đối chiếu với expected tính độc lập từ SRS. Checkout UI cung cấp bằng chứng cho thông báo, số tiền và giới hạn sử dụng. Fixture usage được phân biệt với luồng tạo đơn hàng thực tế.

#### Bước 8 - Review coverage và AI output

Các sai lệch về dấu bằng, công thức phần trăm và body identity được truy vết đến bug tương ứng. Raw discount_amount/final_amount được giữ nguyên; kết luận về rounding và error precedence chỉ nằm trong phạm vi đặc tả.

### 4.3. Domain partition và traceability

| Domain ID | Chiều/lớp | Loại | Representative | Expected | TC coverage |
|---|---|---|---|---|---|
| B-D1 | Fixed nominal | Valid | BIGBUY/600000 | discount=50000; final=550000 | [B-API-01](../tests/B-FR09-discount-coupons.md#b-api-01) |
| B-D2 | Total so với minimum | Boundary | M-1/M/M+1 cho BIGBUY và SAVE10 | Reject/accept/accept | [B-API-02](../tests/B-FR09-discount-coupons.md#b-api-02), [B-API-03](../tests/B-FR09-discount-coupons.md#b-api-03), [B-API-04](../tests/B-FR09-discount-coupons.md#b-api-04), [B-API-05](../tests/B-FR09-discount-coupons.md#b-api-05), [B-API-06](../tests/B-FR09-discount-coupons.md#b-api-06), [B-API-07](../tests/B-FR09-discount-coupons.md#b-api-07), [B-UI-01](../tests/B-FR09-discount-coupons.md#b-ui-01), [B-UI-02](../tests/B-FR09-discount-coupons.md#b-ui-02), [B-UI-03](../tests/B-FR09-discount-coupons.md#b-ui-03) |
| B-D3 | Công thức percent | Valid numeric input | SAVE10/400000; P100/400000 | 40000/360000; 400000/0 | [B-API-08](../tests/B-FR09-discount-coupons.md#b-api-08), [B-API-26](../tests/B-FR09-discount-coupons.md#b-api-26), [B-UI-04](../tests/B-FR09-discount-coupons.md#b-ui-04) |
| B-D4 | Code existence/active/presence | Invalid | NO_SUCH_CODE; OFF; thiếu code | Không áp coupon | [B-API-09](../tests/B-FR09-discount-coupons.md#b-api-09), [B-API-10](../tests/B-FR09-discount-coupons.md#b-api-10), [B-API-11](../tests/B-FR09-discount-coupons.md#b-api-11) |
| B-D5 | Expiry với controlled clock | Boundary | expiry-now = -1/0/+1 ms | Reject/reject/accept | [B-API-12](../tests/B-FR09-discount-coupons.md#b-api-12), [B-API-13](../tests/B-FR09-discount-coupons.md#b-api-13), [B-API-14](../tests/B-FR09-discount-coupons.md#b-api-14), [B-UI-05](../tests/B-FR09-discount-coupons.md#b-ui-05) |
| B-D6 | Usage so với limit | Boundary | used=0/1/2/3, limit=2 | Accept/accept/reject/reject | [B-API-15](../tests/B-FR09-discount-coupons.md#b-api-15), [B-API-16](../tests/B-FR09-discount-coupons.md#b-api-16), [B-API-17](../tests/B-FR09-discount-coupons.md#b-api-17), [B-API-18](../tests/B-FR09-discount-coupons.md#b-api-18), [B-UI-06](../tests/B-FR09-discount-coupons.md#b-ui-06) |
| B-D7 | JWT | Invalid identity | Thiếu/sai/hết hạn | Từ chối trước khi áp coupon | [B-API-19](../tests/B-FR09-discount-coupons.md#b-api-19), [B-API-20](../tests/B-FR09-discount-coupons.md#b-api-20), [B-API-21](../tests/B-FR09-discount-coupons.md#b-api-21) |
| B-D8 | JWT identity vs body user_id | Cross constraint | user 2 hết lượt; body user_id=3 hoặc thiếu | Không bypass limit user đã xác thực | [B-API-22](../tests/B-FR09-discount-coupons.md#b-api-22), [B-API-23](../tests/B-FR09-discount-coupons.md#b-api-23) |
| B-D9 | Giao hai biên hợp lệ | Intersection | VIP100 total=300000, used=1 | Accept; discount=100000; final=200000 | [B-API-24](../tests/B-FR09-discount-coupons.md#b-api-24) |
| B-D10 | Nhiều điều kiện sai | Interaction | OFF; total=0; thiếu JWT | Reject; thứ tự error không quy định | [B-API-25](../tests/B-FR09-discount-coupons.md#b-api-25) |

#### Decision table C1-C5

| Rule | C1 | C2 | C3 | C4 | C5 | Expected | Representative |
|---|---|---|---|---|---|---|---|
| R0 | T | T | T | T | T | Accept + tính đúng | B-API-01 |
| R1 | F | T | T | T | T | Reject | B-API-09/10/11 |
| R2 | T | F | T | T | T | Reject | B-API-12/13 |
| R3 | T | T | F | T | T | Reject | B-API-02/05 |
| R4 | T | T | T | F | T | Reject | B-API-19-21 |
| R5 | T | T | T | T | F | Reject | B-API-17/18/22/23 |
| R6 | F | - | F | F | - | Reject, không định precedence | B-API-25 |

T/F là giá trị điều kiện thiết kế, không phải verdict thực tế. C5 phải tính theo JWT user; body user_id không được thay identity. Đây là reduced decision table theo từng điều kiện sai, không tuyên bố test mọi tổ hợp Cartesian.

### 4.4. Boundary Value Analysis - từng bước

1. Các biến có thứ tự được xác định là total, expiry-now và used.
2. Ba điều kiện biên được biểu diễn bằng total >= minimum, expiry-now > 0 và used < limit.
3. Fixture dùng bước 1 VND, 1 ms và 1 lượt; mỗi phép kiểm giữ các điều kiện C1-C5 khác nominal.
4. Các điểm trước/tại/sau ngưỡng được chọn; B-API-24 bổ sung giao điểm total=minimum, used=limit-1.
5. Expected cho coupon fixed/percent được tính độc lập, đồng thời kiểm tra discount_amount và final_amount.
6. Các sai lệch tại minimum, expiry và phép tính phần trăm được đối chiếu với raw API và Checkout UI; không bổ sung quy tắc rounding ngoài SRS.

| Biến | Rule | Delta/precision | Điểm chọn và giải thích | Cases |
|---|---|---|---|---|
| total T | T >= M | 1 VND cho fixture integer | M-1 invalid; M ON valid; M+1 valid | B-API-02-07; B-UI-01-03 |
| Δ = expiry - now | Δ > 0 | 1 ms | -1 invalid; 0 ON invalid; +1 valid | B-API-12-14 |
| used u, limit=2 | u < 2 | 1 lượt | 0 valid interior; 1 last valid; 2 ON invalid; 3 invalid interior | B-API-15-18 |
| Giao mặt biên | T=M và used=limit-1 | 1 VND / 1 lượt | VIP100/300000/used=1: valid; chỉ một giao điểm chọn có chủ đích | B-API-24 |

### 4.5. Kết quả thực thi

| TC | Status | Actual tóm tắt | Bug |
|---|---|---|---|
| [B-API-01](../tests/B-FR09-discount-coupons.md#b-api-01) | PASS | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":6,"discount_amount":50000,"final_amount":550000,"message":"Áp dụng thành công! Giảm 50,000 VND"} | - |
| [B-API-02](../tests/B-FR09-discount-coupons.md#b-api-02) | PASS | POST /api/apply-coupon -> HTTP 400: {"error":"Đơn hàng chưa đủ giá trị tối thiểu 500,000 VND để áp dụng mã này"} | - |
| [B-API-03](../tests/B-FR09-discount-coupons.md#b-api-03) | FAIL | POST /api/apply-coupon -> HTTP 400: {"error":"Đơn hàng chưa đủ giá trị tối thiểu 500,000 VND để áp dụng mã này"} | FR09-01, FR09-02, FR09-10 |
| [B-API-04](../tests/B-FR09-discount-coupons.md#b-api-04) | PASS | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":30,"discount_amount":50000,"final_amount":450001,"message":"Áp dụng thành công! Giảm 50,000 VND"} | - |
| [B-API-05](../tests/B-FR09-discount-coupons.md#b-api-05) | PASS | POST /api/apply-coupon -> HTTP 400: {"error":"Đơn hàng chưa đủ giá trị tối thiểu 300,000 VND để áp dụng mã này"} | - |
| [B-API-06](../tests/B-FR09-discount-coupons.md#b-api-06) | FAIL | POST /api/apply-coupon -> HTTP 400: {"error":"Đơn hàng chưa đủ giá trị tối thiểu 300,000 VND để áp dụng mã này"} | FR09-01, FR09-02, FR09-10 |
| [B-API-07](../tests/B-FR09-discount-coupons.md#b-api-07) | FAIL | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":53,"discount_amount":-2700009,"final_amount":3000010,"message":"Áp dụng thành công! Giảm 10%"} | FR09-03, FR09-11 |
| [B-API-08](../tests/B-FR09-discount-coupons.md#b-api-08) | FAIL | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":61,"discount_amount":-3600000,"final_amount":4000000,"message":"Áp dụng thành công! Giảm 10%"} | FR09-03, FR09-11 |
| [B-API-09](../tests/B-FR09-discount-coupons.md#b-api-09) | PASS | POST /api/apply-coupon -> HTTP 404: {"error":"Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa"} | - |
| [B-API-10](../tests/B-FR09-discount-coupons.md#b-api-10) | PASS | POST /api/apply-coupon -> HTTP 404: {"error":"Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa"} | - |
| [B-API-11](../tests/B-FR09-discount-coupons.md#b-api-11) | PASS | POST /api/apply-coupon -> HTTP 400: {"error":"Vui lòng nhập mã giảm giá"} | - |
| [B-API-12](../tests/B-FR09-discount-coupons.md#b-api-12) | PASS | POST /api/apply-coupon -> HTTP 400: {"error":"Mã giảm giá đã hết hạn"} | - |
| [B-API-13](../tests/B-FR09-discount-coupons.md#b-api-13) | FAIL | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":106,"discount_amount":10000,"final_amount":390000,"message":"Áp dụng thành công! Giảm 10,000 VND"} | FR09-04 |
| [B-API-14](../tests/B-FR09-discount-coupons.md#b-api-14) | PASS | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":114,"discount_amount":10000,"final_amount":390000,"message":"Áp dụng thành công! Giảm 10,000 VND"} | - |
| [B-API-15](../tests/B-FR09-discount-coupons.md#b-api-15) | PASS | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":119,"discount_amount":100000,"final_amount":300000,"message":"Áp dụng thành công! Giảm 100,000 VND"} | - |
| [B-API-16](../tests/B-FR09-discount-coupons.md#b-api-16) | PASS | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":127,"discount_amount":100000,"final_amount":300000,"message":"Áp dụng thành công! Giảm 100,000 VND"} | - |
| [B-API-17](../tests/B-FR09-discount-coupons.md#b-api-17) | PASS | POST /api/apply-coupon -> HTTP 400: {"error":"Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)"} | - |
| [B-API-18](../tests/B-FR09-discount-coupons.md#b-api-18) | PASS | POST /api/apply-coupon -> HTTP 400: {"error":"Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)"} | - |
| [B-API-19](../tests/B-FR09-discount-coupons.md#b-api-19) | FAIL | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":150,"discount_amount":50000,"final_amount":550000,"message":"Áp dụng thành công! Giảm 50,000 VND"} | FR09-05, FR09-06, FR09-07 |
| [B-API-20](../tests/B-FR09-discount-coupons.md#b-api-20) | FAIL | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":158,"discount_amount":50000,"final_amount":550000,"message":"Áp dụng thành công! Giảm 50,000 VND"} | FR09-05, FR09-06, FR09-07 |
| [B-API-21](../tests/B-FR09-discount-coupons.md#b-api-21) | FAIL | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":166,"discount_amount":50000,"final_amount":550000,"message":"Áp dụng thành công! Giảm 50,000 VND"} | FR09-05, FR09-06, FR09-07 |
| [B-API-22](../tests/B-FR09-discount-coupons.md#b-api-22) | FAIL | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":175,"discount_amount":100000,"final_amount":300000,"message":"Áp dụng thành công! Giảm 100,000 VND"} | FR09-08, FR09-09 |
| [B-API-23](../tests/B-FR09-discount-coupons.md#b-api-23) | FAIL | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":183,"discount_amount":100000,"final_amount":300000,"message":"Áp dụng thành công! Giảm 100,000 VND"} | FR09-08, FR09-09 |
| [B-API-24](../tests/B-FR09-discount-coupons.md#b-api-24) | FAIL | POST /api/apply-coupon -> HTTP 400: {"error":"Đơn hàng chưa đủ giá trị tối thiểu 300,000 VND để áp dụng mã này"} | FR09-01, FR09-02, FR09-10 |
| [B-API-25](../tests/B-FR09-discount-coupons.md#b-api-25) | PASS | POST /api/apply-coupon -> HTTP 404: {"error":"Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa"} | - |
| [B-API-26](../tests/B-FR09-discount-coupons.md#b-api-26) | FAIL | POST /api/apply-coupon -> HTTP 200: {"success":true,"coupon_id":211,"discount_amount":-39600000,"final_amount":40000000,"message":"Áp dụng thành công! Giảm 100%"} | FR09-03, FR09-11 |
| [B-UI-01](../tests/B-FR09-discount-coupons.md#b-ui-01) | PASS | BIGBUY với total 499999 bị từ chối vì chưa đủ ngưỡng. | - |
| [B-UI-02](../tests/B-FR09-discount-coupons.md#b-ui-02) | FAIL | BIGBUY tại total=500000 bị từ chối dù đạt ngưỡng inclusive. | FR09-01, FR09-02, FR09-10 |
| [B-UI-03](../tests/B-FR09-discount-coupons.md#b-ui-03) | PASS | Ô tổng tiền là 500001; BIGBUY giảm 50000 và thành tiền hiển thị 450001. | - |
| [B-UI-04](../tests/B-FR09-discount-coupons.md#b-ui-04) | FAIL | SAVE10/400000 hiển thị tiền giảm -3600000 và thành tiền 4000000, thay vì 40000/360000. | FR09-03, FR09-11 |
| [B-UI-05](../tests/B-FR09-discount-coupons.md#b-ui-05) | PASS | Coupon EXPIRED bị từ chối với thông báo hết hạn. | - |
| [B-UI-06](../tests/B-FR09-discount-coupons.md#b-ui-06) | PASS | Account B-UI-06, total 400000, VIP100: UI báo đã sử dụng 2 lần và đạt giới hạn; tổng giữ 400000. Precondition used=2/limit=2 được seed trực tiếp; không tuyên bố hai đơn mới. | - |

### 4.6. Spec vs Code và findings

| ID | Điều kiện vi phạm | Oracle / root cause |
|---|---|---|
| [FR09-01](../bugs/FR09-01.md) | Fixed coupon is rejected at its exact minimum total | FR-09 C3; The handler checks total_amount > coupon.min_order_amount. |
| [FR09-02](../bugs/FR09-02.md) | Percentage coupon is rejected at its exact minimum total | FR-09 C3; The handler checks total_amount > coupon.min_order_amount. |
| [FR09-03](../bugs/FR09-03.md) | A 10 percent coupon returns a negative discount and increases total | FR-09 percentage formula; The percentage branch calculates floor(total_amount * (1-discount_value)). |
| [FR09-04](../bugs/FR09-04.md) | Coupon remains valid at the exact expiration instant | FR-09 C2: now < expired_at; The handler rejects expiry < now and consequently permits equality. |
| [FR09-05](../bugs/FR09-05.md) | Coupon application succeeds without an Authorization header | FR-09 C4; SEC-02; The apply-coupon route does not use authenticateToken. |
| [FR09-06](../bugs/FR09-06.md) | Coupon application succeeds with a malformed JWT | FR-09 C4; SEC-02; The apply-coupon route does not use authenticateToken. |
| [FR09-07](../bugs/FR09-07.md) | Coupon application succeeds with an expired JWT | FR-09 C4; SEC-02; The apply-coupon route does not use authenticateToken. |
| [FR09-08](../bugs/FR09-08.md) | Substituted body user_id bypasses the authenticated coupon limit | FR-09 C5; Eligibility reads req.body.user_id instead of a verified request identity. |
| [FR09-09](../bugs/FR09-09.md) | Omitted body user_id bypasses the authenticated coupon limit | FR-09 C5; Eligibility reads req.body.user_id instead of a verified request identity. |
| [FR09-10](../bugs/FR09-10.md) | VIP100 minimum equality is rejected on the last eligible use | FR-09 C3; The handler checks total_amount > coupon.min_order_amount. |
| [FR09-11](../bugs/FR09-11.md) | A 100 percent coupon produces a negative discount instead of zero total | FR-09 percentage formula; The percentage branch calculates floor(total_amount * (1-discount_value)). |
| [FR09-12](../bugs/FR09-12.md) | Late coupon response applies a discount after the input code changes | FR-09 current coupon eligibility and UI/result consistency; handleApplyCoupon unconditionally writes its response with no request/input revision guard. |

### 4.7. AI gap analysis

Các sai lệch trong đầu ra AI và cách hiệu chỉnh được đối chiếu với rule, raw record và ảnh tương ứng. Bản nháp gốc được lưu trong AI audit snapshot.

| Gap | Nhóm nguyên nhân | Evidence/điều sai | Cách sửa |
|---|---|---|---|
| Sai literal khi viết báo cáo | Giới hạn công cụ | Draft FR09-03, FR09-11 ghi 4360000; raw/ảnh đều 4000000 | Dùng literal discount_amount=-3600000/final_amount=4000000 |
| Bỏ qua precondition usage | Độ phức tạp trạng thái | Ảnh cũ nominal không đủ; ảnh mới đúng B-UI-06 khớp fixture hai coupon_usage | Chốt PASS tại used2/limit2; khai rõ seed trực tiếp, không suy hai đơn mới |
| Nhầm arithmetic với rounding | Prompt/assumption | Case total=300001 có phần lẻ, spec im lặng về rounding | Dùng B-API-08 số nguyên làm evidence quyết định; không thêm Math.floor vào expected |
| Auth vs identity | Độ phức tạp feature | Thiếu token khác valid token nhưng body user_id giả | Tách FR09-05, FR09-06, FR09-07 và FR09-08, FR09-09; dùng VIP100 và fixture đúng |

### 4.8. Coverage và giới hạn

Coverage gồm C1-C5, công thức fixed/percent, các ngưỡng tiền, expiry, usage và một giao điểm được chọn. Bảng quyết định sử dụng từng điều kiện sai và một case nhiều lỗi; coverage không đại diện cho mọi tổ hợp Cartesian. B-UI-06 kiểm tra từ chối tại used=limit trên fixture đã thiết lập, không được dùng làm bằng chứng cho hai luồng tạo đơn hàng trước đó.

[Detailed test cases](../tests/B-FR09-discount-coupons.md), [Raw API evidence](../evidence/execution/B-api.md), [Bug index](../bugs/bug-reports.md).


### Kiểm thử contract và state bổ sung

| Domain | Chiều phân hoạch | Oracle / controls | TC-ID | Kết luận |
|---|---|---|---|---|
| B-D11 | In-flight response / input revision | Response đến muộn cho code cũ không được ghi đè trạng thái code mới; chỉ điều khiển timing, giữ nguyên body. | B-UI-07 | FR09-12 |

Các lớp bổ sung được suy từ contract, security property và state transition; không gắn nhãn BVA cho boolean/DOM/enum. Riêng phone Mobile dùng cùng các biên độ dài 9/10/11/12, với các chiều prefix được cô lập.

| TC-ID | Seam | Status | Actual / bug |
|---|---|---|---|
| [B-UI-07](../tests/B-FR09-discount-coupons.md#b-ui-07) | UI | FAIL | Coupon results are bound to the current input revision / FR09-12 |

AI gap mới: test tuần tự Apply/edit không bộc lộ thứ tự response. B-UI-07 giữ request BIGBUY đang chờ, đổi input VIP100 rồi trả response BIGBUY nguyên trạng; code hiện tại và discount trở nên không đồng nhất. Không sửa nội dung response để tạo FAIL.

[A execution](../evidence/execution/A-execution.md), [B execution](../evidence/execution/B-execution.md), [C execution](../evidence/execution/C-execution.md), [D execution](../evidence/execution/D-execution.md).
