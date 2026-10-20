# B — Domain Testing và Boundary Value Analysis

**Feature:** FR-09 — Áp dụng mã giảm giá<br>
**SUT:** `85af3ba875c88283615e22cb108f13e2fccaf0e9`.

## 1. Requirements và oracle

| Rule | Nội dung theo SRS | Domain |
|---|---|---|
| C1 | Code tồn tại và is_active=1 | B-D4 |
| C2 | now < expired_at | B-D5 |
| C3 | total ≥ min_order_amount | B-D2 |
| C4 | JWT hợp lệ | B-D7 |
| C5 | Usage của đúng user xác thực < limit | B-D6/D8 |
| Formula | percent: T×value/100; fixed: value; final=T−discount | B-D1/D3 |
| Intersection | Đồng thời đáp ứng mọi điều kiện; không quy định error precedence | B-D9/D10 |

[Nguồn SRS cố định](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/README.md). Các tên rule dạng FR-04.1 trong báo cáo là nhãn nội bộ để truy vết, không phải mã mới của SRS.

## 2. Domain Testing — quy trình từng bước

Chúng tôi lấy SRS làm oracle, sau đó dùng source để xây dựng giả thuyết và giải thích nguyên nhân. Source không thay thế yêu cầu. Mỗi TC có ID ổn định; một TC có thể phủ cả Domain Testing và BVA nhưng chỉ được tính một lần. Chúng tôi tách API với Web/Admin/Mobile UI vì validation ở một lớp không chứng minh lớp còn lại đạt.

Với từng input/state, chúng tôi xác định miền hợp lệ, phần bù không hợp lệ, precision và các ràng buộc giữa các chiều. Các lớp trong cùng một chiều được chọn để phân biệt hành vi; bảng nhiều chiều không có nghĩa mọi hàng đều là các tập rời nhau của toàn bộ vector. Test invalid giữ các chiều khác nominal; interaction nhiều lỗi có chủ đích được ghi riêng. Chúng tôi dùng readback public HTTP sau thay đổi để kiểm tra hậu điều kiện.

BVA được áp dụng cho miền có thứ tự, kể cả độ dài chuỗi và số lượt nguyên. Điểm ON nằm trên mặt biên; giá trị ON có thể hợp lệ hoặc không tùy dấu ≥ hay >. Các điểm lân cận được ghi bằng số và trạng thái valid/invalid để tránh nhập nhằng thuật ngữ. Các label OFF/IN không thay thế tập giá trị cụ thể. Rỗng, enum, charset và identity là Domain classes; không tự đặt một maximum mà SRS không quy định.

API execution dùng backend copy, clock cố định và fixture reset mỗi TC. UI evidence là ảnh thật đã cung cấp; không suy timestamp chạy từ ngày sửa file, không dùng ảnh vẽ hoặc build output làm bằng chứng UI. PASS/FAIL chỉ kết luận theo criterion có evidence; OBSERVATION dành cho oracle chưa quy định; INCOMPLETE dành cho TC còn thiếu bước/precondition/evidence. Một TC INCOMPLETE có thể đã được thao tác một phần, nhưng không được cộng vào executed đủ bằng chứng.

Chúng tôi kiểm tra kỹ thuật theo Domain/Boundary đã nêu; chưa có bản lecture của môn trong workspace để xác nhận đã đối chiếu mọi quy ước của giảng viên. Nguồn phương pháp bổ trợ là ISTQB CTFL §4.2.1–4.2.2. Các giới hạn này được giữ rõ trong phần coverage, không tuyên bố exhaustive coverage toàn hệ thống.

### Bước 1 — Xác định inputs/outputs

Vector `(code, active/existence, now/expiry, total/minimum, JWT identity, used/limit, type/value)`. Output gồm thông báo, response và hậu điều kiện ở profile/coupon/cart tương ứng.

### Bước 2 — Thiết lập nominal fixture

Dùng fixed coupon để cô lập điều kiện minimum/expiry/usage khỏi percent arithmetic. Mỗi test một điều kiện sai giữ bốn điều kiện còn lại đúng; B-API-25 cố ý nhiều lỗi và không đặt error precedence.

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
| B-D1 | Fixed nominal | Valid | BIGBUY/600000 | discount=50000; final=550000 | [B-API-01](../tests/B-FR09-discount-coupons.md#b-api-01) |
| B-D2 | Total so với minimum | Boundary | M−1/M/M+1 cho BIGBUY và SAVE10 | Reject/accept/accept | [B-API-02](../tests/B-FR09-discount-coupons.md#b-api-02), [B-API-03](../tests/B-FR09-discount-coupons.md#b-api-03), [B-API-04](../tests/B-FR09-discount-coupons.md#b-api-04), [B-API-05](../tests/B-FR09-discount-coupons.md#b-api-05), [B-API-06](../tests/B-FR09-discount-coupons.md#b-api-06), [B-API-07](../tests/B-FR09-discount-coupons.md#b-api-07), [B-UI-01](../tests/B-FR09-discount-coupons.md#b-ui-01), [B-UI-02](../tests/B-FR09-discount-coupons.md#b-ui-02), [B-UI-03](../tests/B-FR09-discount-coupons.md#b-ui-03) |
| B-D3 | Công thức percent | Valid numeric input | SAVE10/400000; P100/400000 | 40000/360000; 400000/0 | [B-API-08](../tests/B-FR09-discount-coupons.md#b-api-08), [B-API-26](../tests/B-FR09-discount-coupons.md#b-api-26), [B-UI-04](../tests/B-FR09-discount-coupons.md#b-ui-04) |
| B-D4 | Code existence/active/presence | Invalid | NO_SUCH_CODE; OFF; thiếu code | Không áp coupon | [B-API-09](../tests/B-FR09-discount-coupons.md#b-api-09), [B-API-10](../tests/B-FR09-discount-coupons.md#b-api-10), [B-API-11](../tests/B-FR09-discount-coupons.md#b-api-11) |
| B-D5 | Expiry với controlled clock | Boundary | expiry−now = −1/0/+1 ms | Reject/reject/accept | [B-API-12](../tests/B-FR09-discount-coupons.md#b-api-12), [B-API-13](../tests/B-FR09-discount-coupons.md#b-api-13), [B-API-14](../tests/B-FR09-discount-coupons.md#b-api-14), [B-UI-05](../tests/B-FR09-discount-coupons.md#b-ui-05) |
| B-D6 | Usage so với limit | Boundary | used=0/1/2/3, limit=2 | Accept/accept/reject/reject | [B-API-15](../tests/B-FR09-discount-coupons.md#b-api-15), [B-API-16](../tests/B-FR09-discount-coupons.md#b-api-16), [B-API-17](../tests/B-FR09-discount-coupons.md#b-api-17), [B-API-18](../tests/B-FR09-discount-coupons.md#b-api-18), [B-UI-06](../tests/B-FR09-discount-coupons.md#b-ui-06) |
| B-D7 | JWT | Invalid identity | Thiếu/sai/hết hạn | Từ chối trước khi áp coupon | [B-API-19](../tests/B-FR09-discount-coupons.md#b-api-19), [B-API-20](../tests/B-FR09-discount-coupons.md#b-api-20), [B-API-21](../tests/B-FR09-discount-coupons.md#b-api-21) |
| B-D8 | JWT identity vs body user_id | Cross constraint | user 2 hết lượt; body user_id=3 hoặc thiếu | Không bypass limit user đã xác thực | [B-API-22](../tests/B-FR09-discount-coupons.md#b-api-22), [B-API-23](../tests/B-FR09-discount-coupons.md#b-api-23) |
| B-D9 | Giao hai biên hợp lệ | Intersection | VIP100 total=300000, used=1 | Accept; discount=100000; final=200000 | [B-API-24](../tests/B-FR09-discount-coupons.md#b-api-24) |
| B-D10 | Nhiều điều kiện sai | Interaction | OFF; total=0; thiếu JWT | Reject; thứ tự error không quy định | [B-API-25](../tests/B-FR09-discount-coupons.md#b-api-25) |

### Decision table C1–C5

| Rule | C1 | C2 | C3 | C4 | C5 | Expected | Representative |
|---|---|---|---|---|---|---|---|
| R0 | T | T | T | T | T | Accept + tính đúng | B-API-01 |
| R1 | F | T | T | T | T | Reject | B-API-09/10/11 |
| R2 | T | F | T | T | T | Reject | B-API-12/13 |
| R3 | T | T | F | T | T | Reject | B-API-02/05 |
| R4 | T | T | T | F | T | Reject | B-API-19–21 |
| R5 | T | T | T | T | F | Reject | B-API-17/18/22/23 |
| R6 | F | — | F | F | — | Reject, không định precedence | B-API-25 |

T/F là giá trị điều kiện thiết kế, không phải verdict thực tế. C5 phải tính theo JWT user; body user_id không được thay identity. Đây là reduced decision table theo từng điều kiện sai, không tuyên bố test mọi tổ hợp Cartesian.

## 4. Boundary Value Analysis — từng bước

1. Chọn biến có thứ tự và miền áp dụng từ rule; không lấy giới hạn tùy ý trong code.
2. Viết bất đẳng thức và xác định điểm equality hợp lệ hay không.
3. Ghi precision của fixture, lấy điểm biên và lân cận hai phía.
4. Giữ các chiều ngoài biên đang xét nominal; thêm giao biên khi có lý do.
5. Tính expected độc lập; liên kết TC và phân biệt numerical boundary với missing/type domain.
6. So actual với expected; khi rounding/MAX/reset không có rule, giữ observation hoặc giới hạn kết luận.

| Biến | Rule | Delta/precision | Điểm chọn và giải thích | Cases |
|---|---|---|---|---|
| total T | T ≥ M | 1 VND cho fixture integer | M−1 invalid; M ON valid; M+1 valid | B-API-02–07; B-UI-01–03 |
| Δ = expiry − now | Δ > 0 | 1 ms | −1 invalid; 0 ON invalid; +1 valid | B-API-12–14 |
| used u, limit=2 | u < 2 | 1 lượt | 0 valid interior; 1 last valid; 2 ON invalid; 3 invalid interior | B-API-15–18 |
| Giao mặt biên | T=M và used=limit−1 | 1 VND / 1 lượt | VIP100/300000/used=1: valid; chỉ một giao điểm chọn có chủ đích | B-API-24 |

## 5. Kết quả thực thi

| TC | Status | Actual tóm tắt | Bug |
|---|---|---|---|
| [B-API-01](../tests/B-FR09-discount-coupons.md#b-api-01) | PASS | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":6,"discount_amount":50000,"final_amount":550000,"message":"Áp dụng thành công! Giảm 50,000 ₫"} | — |
| [B-API-02](../tests/B-FR09-discount-coupons.md#b-api-02) | PASS | POST /api/apply-coupon → HTTP 400: {"error":"Đơn hàng chưa đủ giá trị tối thiểu 500,000 ₫ để áp dụng mã này"} | — |
| [B-API-03](../tests/B-FR09-discount-coupons.md#b-api-03) | FAIL | POST /api/apply-coupon → HTTP 400: {"error":"Đơn hàng chưa đủ giá trị tối thiểu 500,000 ₫ để áp dụng mã này"} | BUG-B01 |
| [B-API-04](../tests/B-FR09-discount-coupons.md#b-api-04) | PASS | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":30,"discount_amount":50000,"final_amount":450001,"message":"Áp dụng thành công! Giảm 50,000 ₫"} | — |
| [B-API-05](../tests/B-FR09-discount-coupons.md#b-api-05) | PASS | POST /api/apply-coupon → HTTP 400: {"error":"Đơn hàng chưa đủ giá trị tối thiểu 300,000 ₫ để áp dụng mã này"} | — |
| [B-API-06](../tests/B-FR09-discount-coupons.md#b-api-06) | FAIL | POST /api/apply-coupon → HTTP 400: {"error":"Đơn hàng chưa đủ giá trị tối thiểu 300,000 ₫ để áp dụng mã này"} | BUG-B01 |
| [B-API-07](../tests/B-FR09-discount-coupons.md#b-api-07) | FAIL | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":53,"discount_amount":-2700009,"final_amount":3000010,"message":"Áp dụng thành công! Giảm 10%"} | BUG-B02 |
| [B-API-08](../tests/B-FR09-discount-coupons.md#b-api-08) | FAIL | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":61,"discount_amount":-3600000,"final_amount":4000000,"message":"Áp dụng thành công! Giảm 10%"} | BUG-B02 |
| [B-API-09](../tests/B-FR09-discount-coupons.md#b-api-09) | PASS | POST /api/apply-coupon → HTTP 404: {"error":"Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa"} | — |
| [B-API-10](../tests/B-FR09-discount-coupons.md#b-api-10) | PASS | POST /api/apply-coupon → HTTP 404: {"error":"Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa"} | — |
| [B-API-11](../tests/B-FR09-discount-coupons.md#b-api-11) | PASS | POST /api/apply-coupon → HTTP 400: {"error":"Vui lòng nhập mã giảm giá"} | — |
| [B-API-12](../tests/B-FR09-discount-coupons.md#b-api-12) | PASS | POST /api/apply-coupon → HTTP 400: {"error":"Mã giảm giá đã hết hạn"} | — |
| [B-API-13](../tests/B-FR09-discount-coupons.md#b-api-13) | FAIL | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":106,"discount_amount":10000,"final_amount":390000,"message":"Áp dụng thành công! Giảm 10,000 ₫"} | BUG-B03 |
| [B-API-14](../tests/B-FR09-discount-coupons.md#b-api-14) | PASS | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":114,"discount_amount":10000,"final_amount":390000,"message":"Áp dụng thành công! Giảm 10,000 ₫"} | — |
| [B-API-15](../tests/B-FR09-discount-coupons.md#b-api-15) | PASS | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":119,"discount_amount":100000,"final_amount":300000,"message":"Áp dụng thành công! Giảm 100,000 ₫"} | — |
| [B-API-16](../tests/B-FR09-discount-coupons.md#b-api-16) | PASS | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":127,"discount_amount":100000,"final_amount":300000,"message":"Áp dụng thành công! Giảm 100,000 ₫"} | — |
| [B-API-17](../tests/B-FR09-discount-coupons.md#b-api-17) | PASS | POST /api/apply-coupon → HTTP 400: {"error":"Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)"} | — |
| [B-API-18](../tests/B-FR09-discount-coupons.md#b-api-18) | PASS | POST /api/apply-coupon → HTTP 400: {"error":"Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)"} | — |
| [B-API-19](../tests/B-FR09-discount-coupons.md#b-api-19) | FAIL | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":150,"discount_amount":50000,"final_amount":550000,"message":"Áp dụng thành công! Giảm 50,000 ₫"} | BUG-B04 |
| [B-API-20](../tests/B-FR09-discount-coupons.md#b-api-20) | FAIL | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":158,"discount_amount":50000,"final_amount":550000,"message":"Áp dụng thành công! Giảm 50,000 ₫"} | BUG-B04 |
| [B-API-21](../tests/B-FR09-discount-coupons.md#b-api-21) | FAIL | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":166,"discount_amount":50000,"final_amount":550000,"message":"Áp dụng thành công! Giảm 50,000 ₫"} | BUG-B04 |
| [B-API-22](../tests/B-FR09-discount-coupons.md#b-api-22) | FAIL | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":175,"discount_amount":100000,"final_amount":300000,"message":"Áp dụng thành công! Giảm 100,000 ₫"} | BUG-B05 |
| [B-API-23](../tests/B-FR09-discount-coupons.md#b-api-23) | FAIL | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":183,"discount_amount":100000,"final_amount":300000,"message":"Áp dụng thành công! Giảm 100,000 ₫"} | BUG-B05 |
| [B-API-24](../tests/B-FR09-discount-coupons.md#b-api-24) | FAIL | POST /api/apply-coupon → HTTP 400: {"error":"Đơn hàng chưa đủ giá trị tối thiểu 300,000 ₫ để áp dụng mã này"} | BUG-B01 |
| [B-API-25](../tests/B-FR09-discount-coupons.md#b-api-25) | PASS | POST /api/apply-coupon → HTTP 404: {"error":"Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa"} | — |
| [B-API-26](../tests/B-FR09-discount-coupons.md#b-api-26) | FAIL | POST /api/apply-coupon → HTTP 200: {"success":true,"coupon_id":211,"discount_amount":-39600000,"final_amount":40000000,"message":"Áp dụng thành công! Giảm 100%"} | BUG-B02 |
| [B-UI-01](../tests/B-FR09-discount-coupons.md#b-ui-01) | PASS | BIGBUY với total 499999 bị từ chối vì chưa đủ ngưỡng. | — |
| [B-UI-02](../tests/B-FR09-discount-coupons.md#b-ui-02) | FAIL | BIGBUY tại total=500000 bị từ chối dù đạt ngưỡng inclusive. | BUG-B01 |
| [B-UI-03](../tests/B-FR09-discount-coupons.md#b-ui-03) | PASS | Ô tổng tiền là 500001; BIGBUY giảm 50000 và thành tiền hiển thị 450001. | — |
| [B-UI-04](../tests/B-FR09-discount-coupons.md#b-ui-04) | FAIL | SAVE10/400000 hiển thị tiền giảm −3600000 và thành tiền 4000000, thay vì 40000/360000. | BUG-B02 |
| [B-UI-05](../tests/B-FR09-discount-coupons.md#b-ui-05) | PASS | Coupon EXPIRED bị từ chối với thông báo hết hạn. | — |
| [B-UI-06](../tests/B-FR09-discount-coupons.md#b-ui-06) | PASS | Account B-UI-06, total 400000, VIP100: UI báo đã sử dụng 2 lần và đạt giới hạn; tổng giữ 400000. Precondition used=2/limit=2 được seed trực tiếp; không tuyên bố hai đơn mới. | — |

## 6. Spec vs Code và bug groups

| Bug | Rule | Nguyên nhân có source support | Representative |
|---|---|---|---|
| [BUG-B01](../bugs/BUG-B01.md) | FR-09 C3 | Nhánh accept dùng total_amount > coupon.min_order_amount, bỏ equality. | B-API-03 |
| [BUG-B02](../bugs/BUG-B02.md) | FR-09 Formula | Source tính Math.floor(total_amount * (1 - coupon.discount_value)) thành discount_amount; final trừ tiếp discount sai. | B-API-08 |
| [BUG-B03](../bugs/BUG-B03.md) | FR-09 C2 | Source chỉ reject khi expiry < now; equality không bị reject. | B-API-13 |
| [BUG-B04](../bugs/BUG-B04.md) | FR-09 C4 | POST /api/apply-coupon không gắn authenticateToken middleware. | B-API-19 |
| [BUG-B05](../bugs/BUG-B05.md) | FR-09 C5 / identity | Server đếm usage theo body.user_id; khi thiếu user_id thì bỏ kiểm tra usage; không dùng JWT identity. | B-API-22 |

## 7. AI gap analysis

Các mục dưới đây là technical corrections có evidence của quá trình soạn/kiểm tra; không tự gán mọi phát hiện cho sinh viên hoặc một model bên ngoài. Bản nháp nguyên văn giữ trong AI audit snapshot.

| Gap | Nhóm nguyên nhân | Evidence/điều sai | Cách sửa |
|---|---|---|---|
| Sai literal khi viết báo cáo | Giới hạn công cụ | Draft BUG-B02 ghi 4360000; raw/ảnh đều 4000000 | Dùng literal discount_amount=−3600000/final_amount=4000000 |
| Bỏ qua precondition usage | Độ phức tạp trạng thái | Ảnh cũ nominal không đủ; ảnh mới đúng B-UI-06 khớp fixture hai coupon_usage | Chốt PASS tại used2/limit2; khai rõ seed trực tiếp, không suy hai đơn mới |
| Nhầm arithmetic với rounding | Prompt/assumption | Case total=300001 có phần lẻ, spec im lặng về rounding | Dùng B-API-08 số nguyên làm evidence quyết định; không thêm Math.floor vào expected |
| Auth vs identity | Độ phức tạp feature | Thiếu token khác valid token nhưng body user_id giả | Tách BUG-B04 và BUG-B05; dùng VIP100 và fixture đúng |

## 8. Coverage và giới hạn

Các domain và điểm biên đã liệt kê đều có TC-ID. Một số TC có evidence một phần nên chưa có verdict hoàn chỉnh. Không suy full requirement coverage từ số TC hoặc số ảnh; class chưa có rule rõ không biến thành bug. Các form/UI tiêu chuẩn chung ngoài mục tiêu các TC hiện tại chưa được kiểm chứng exhaustive. Lecture chưa có trong bộ nguồn; cần đối chiếu bản giảng viên trước nộp.

[Detailed test cases](../tests/B-FR09-discount-coupons.md) · [Raw API evidence](../evidence/execution/B-api.md) · [Bug index](../bugs/bug-reports.md).
