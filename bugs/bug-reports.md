# Bug Report — Tổng hợp lỗi

**Sinh viên:** Tống Dương Thái Hòa — 23120262.

18 behavior groups: 15 API và 3 UI-only (A03/D01/D02). Các bug B01/B02/C04/C05 có cả API và ảnh UI, chỉ tính một lần. BUG-C02 được giữ trống có chủ đích: duplicate uniqueness đã đạt, không tạo bug chỉ vì status500.

| Bug | Feature | Tóm tắt | Severity | Failing TCs | Screenshot |
|---|---|---|---|---|---|
| [BUG-A01](BUG-A01.md) | A | API chấp nhận và lưu phone không hợp lệ | High | 13 | API screenshot còn thiếu |
| [BUG-A02](BUG-A02.md) | A | User tự ghi role=admin qua cập nhật hồ sơ | Critical | 1 | API screenshot còn thiếu |
| [BUG-A03](BUG-A03.md) | A | Frontend từ chối phone hợp lệ và chấp nhận prefix sai | High | 4 | Có UI evidence |
| [BUG-B01](BUG-B01.md) | B | Coupon bị từ chối khi tổng tiền bằng đúng ngưỡng | High | 4 | Có UI evidence |
| [BUG-B02](BUG-B02.md) | B | Coupon percent trả tiền giảm âm và tăng thành tiền | Critical | 4 | Có UI evidence |
| [BUG-B03](BUG-B03.md) | B | Coupon còn được dùng tại đúng thời điểm hết hạn | Medium | 1 | API screenshot còn thiếu |
| [BUG-B04](BUG-B04.md) | B | Apply coupon bỏ qua JWT thiếu, sai và hết hạn | High | 3 | API screenshot còn thiếu |
| [BUG-B05](BUG-B05.md) | B | Body user_id cho phép bypass lượt dùng của user xác thực | High | 2 | API screenshot còn thiếu |
| [BUG-C01](BUG-C01.md) | C | Thiếu required fields hoặc code rỗng vẫn tạo coupon | High | 7 | API screenshot còn thiếu |
| [BUG-C03](BUG-C03.md) | C | Type ngoài enum percent/fixed vẫn được lưu | Medium | 1 | API screenshot còn thiếu |
| [BUG-C04](BUG-C04.md) | C | discount_value bằng 0 hoặc âm vẫn tạo coupon | High | 3 | Có UI evidence |
| [BUG-C05](BUG-C05.md) | C | min_order_amount âm vẫn được lưu | Medium | 2 | Có UI evidence |
| [BUG-C06](BUG-C06.md) | C | Usage limit âm được lưu, zero bị đổi ngầm thành 1 | Medium | 2 | API screenshot còn thiếu |
| [BUG-C07](BUG-C07.md) | C | User thường tạo được coupon của Admin | High | 1 | API screenshot còn thiếu |
| [BUG-C08](BUG-C08.md) | C | User thường đọc được danh sách coupon quản trị | Medium | 1 | API screenshot còn thiếu |
| [BUG-C09](BUG-C09.md) | C | User thường xóa được coupon của Admin | High | 1 | API screenshot còn thiếu |
| [BUG-D01](BUG-D01.md) | D | Mobile chấp nhận quantity không hợp lệ khi Add | High | 6 | Có UI evidence |
| [BUG-D02](BUG-D02.md) | D | Mobile productDetail thiếu hiển thị danh mục | Medium | 1 | Có UI evidence |

## Quy tắc kiểm đếm

Một TC có thể nằm trong Domain+BVA nhưng chỉ tính một lần. Một bug có nhiều TC FAIL, nên số failed TC không bằng số bugs. Không tính observations hoặc thiếu ảnh là bug mới. D02 dựa mapping Mobile FR-20→FR-06 đã công bố.

## GitHub Issues

Chưa có URL/ảnh Issue thật trong bộ nguồn hiện tại. Giai đoạn đăng Issue của nhóm thực hiện cuối; mọi bug Markdown đã có payload, expected/actual, evidence và severity rationale để dùng làm body.
