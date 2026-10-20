# Bug Report - Tổng hợp lỗi

**Sinh viên:** Tống Dương Thái Hòa - 23120262.

18 behavior groups: 15 API và 3 UI-only (A03/D01/D02). Các bug B01/B02/C04/C05 có cả API và ảnh UI, chỉ tính một lần. BUG-C02 được giữ trống có chủ đích: duplicate uniqueness đã đạt, không tạo bug chỉ vì status500.

| Bug | Feature | Tóm tắt | Severity | Failing TCs | Screenshot | GitHub Issue |
|---|---|---|---|---|---|---|
| [BUG-A01](BUG-A01.md) | A | API chấp nhận và lưu phone không hợp lệ | High | 13 | API screenshot còn thiếu | [#31](https://github.com/tkob-team/eshop-sut/issues/31) |
| [BUG-A02](BUG-A02.md) | A | User tự ghi role=admin qua cập nhật hồ sơ | Critical | 1 | API screenshot còn thiếu | [#32](https://github.com/tkob-team/eshop-sut/issues/32) |
| [BUG-A03](BUG-A03.md) | A | Frontend từ chối phone hợp lệ và chấp nhận prefix sai | High | 4 | Có UI evidence | [#33](https://github.com/tkob-team/eshop-sut/issues/33) |
| [BUG-B01](BUG-B01.md) | B | Coupon bị từ chối khi tổng tiền bằng đúng ngưỡng | High | 4 | Có UI evidence | [#34](https://github.com/tkob-team/eshop-sut/issues/34) |
| [BUG-B02](BUG-B02.md) | B | Coupon percent trả tiền giảm âm và tăng thành tiền | Critical | 4 | Có UI evidence | [#35](https://github.com/tkob-team/eshop-sut/issues/35) |
| [BUG-B03](BUG-B03.md) | B | Coupon còn được dùng tại đúng thời điểm hết hạn | Medium | 1 | API screenshot còn thiếu | [#36](https://github.com/tkob-team/eshop-sut/issues/36) |
| [BUG-B04](BUG-B04.md) | B | Apply coupon bỏ qua JWT thiếu, sai và hết hạn | High | 3 | API screenshot còn thiếu | [#37](https://github.com/tkob-team/eshop-sut/issues/37) |
| [BUG-B05](BUG-B05.md) | B | Body user_id cho phép bypass lượt dùng của user xác thực | High | 2 | API screenshot còn thiếu | [#38](https://github.com/tkob-team/eshop-sut/issues/38) |
| [BUG-C01](BUG-C01.md) | C | Thiếu required fields hoặc code rỗng vẫn tạo coupon | High | 7 | API screenshot còn thiếu | [#39](https://github.com/tkob-team/eshop-sut/issues/39) |
| [BUG-C03](BUG-C03.md) | C | Type ngoài enum percent/fixed vẫn được lưu | Medium | 1 | API screenshot còn thiếu | [#40](https://github.com/tkob-team/eshop-sut/issues/40) |
| [BUG-C04](BUG-C04.md) | C | discount_value bằng 0 hoặc âm vẫn tạo coupon | High | 3 | Có UI evidence | [#41](https://github.com/tkob-team/eshop-sut/issues/41) |
| [BUG-C05](BUG-C05.md) | C | min_order_amount âm vẫn được lưu | Medium | 2 | Có UI evidence | [#42](https://github.com/tkob-team/eshop-sut/issues/42) |
| [BUG-C06](BUG-C06.md) | C | Usage limit âm được lưu, zero bị đổi ngầm thành 1 | Medium | 2 | API screenshot còn thiếu | [#43](https://github.com/tkob-team/eshop-sut/issues/43) |
| [BUG-C07](BUG-C07.md) | C | User thường tạo được coupon của Admin | High | 1 | API screenshot còn thiếu | [#44](https://github.com/tkob-team/eshop-sut/issues/44) |
| [BUG-C08](BUG-C08.md) | C | User thường đọc được danh sách coupon quản trị | Medium | 1 | API screenshot còn thiếu | [#45](https://github.com/tkob-team/eshop-sut/issues/45) |
| [BUG-C09](BUG-C09.md) | C | User thường xóa được coupon của Admin | High | 1 | API screenshot còn thiếu | [#46](https://github.com/tkob-team/eshop-sut/issues/46) |
| [BUG-D01](BUG-D01.md) | D | Mobile chấp nhận quantity không hợp lệ khi Add | High | 6 | Có UI evidence | [#47](https://github.com/tkob-team/eshop-sut/issues/47) |
| [BUG-D02](BUG-D02.md) | D | Mobile productDetail thiếu hiển thị danh mục | Medium | 1 | Có UI evidence | [#48](https://github.com/tkob-team/eshop-sut/issues/48) |

## Quy tắc kiểm đếm

Một TC có thể nằm trong Domain+BVA nhưng chỉ tính một lần. Một bug có nhiều TC FAIL, nên số failed TC không bằng số bugs. Không tính observations hoặc thiếu ảnh là bug mới. D02 dựa mapping Mobile FR-20->FR-06 đã công bố.

## GitHub Issues

Đã đăng18Issues cá nhân (#31-#48) và kiểm tra body/author/assignee/label bằng API. Ảnh bug đính kèm và ảnh trang Issue do sinh viên bổ sung sau; xem [Issue Evidence](../evidence/github-issues/README.md).
