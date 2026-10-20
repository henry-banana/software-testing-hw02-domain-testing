# BUG-D02 - Mobile productDetail thiếu hiển thị danh mục

| Field | Value |
|---|---|
| Bug ID | BUG-D02 |
| Feature | Mobile productDetail - Chi tiết sản phẩm và quantity |
| Severity | Medium - đề xuất kỹ thuật, xem Impact |
| Status | Reproduced; SUT chưa được sửa |
| Seam | Mobile UI |
| Oracle | FR-20 -> FR-06 detail mapping |
| SUT baseline | 85af3ba875c88283615e22cb108f13e2fccaf0e9 |
| Affected TCs | [D-UI-09](../tests/D-mobile-product-detail.md#d-ui-09) |
| GitHub Issue | [#48](https://github.com/tkob-team/eshop-sut/issues/48) - OPEN |
| Screenshot coverage | Có ảnh UI cụ thể dưới đây |

## 1. Mô tả và điều kiện kích hoạt

Mobile productDetail thiếu hiển thị danh mục. renderProductDetail render ảnh/tên/giá/mô tả/quantity nhưng không render category; API có category_id chưa được chuyển thành nhãn.

Lỗi được nhóm theo behavior; các giá trị biên/biến thể cùng nguyên nhân không tạo một bug mới cho mỗi TC FAIL.

## 2. Environment và preconditions

Ảnh thực tế từ Expo Go/Android; account D-UI-01, không suy phiên bản Android/Expo khi chưa có log. Dùng baseline và mapping đã ghi. Giữ nguyên bytes ảnh; không có video/HTTP trace UI tự động của lượt chụp.

## 3. Steps to Reproduce

1. Mở Expo Go/Android, ghi account thực tế; xóa giỏ trước TC làm thay đổi giỏ. Mở detail đúng product ID; ghi đơn giá.
2. Đối chiếu lần lượt ảnh, tên, giá, mô tả và category theo checklist FR-06 mapping.
3. Cuộn toàn vùng detail để không nhầm thông tin nằm ngoài viewport; lưu ảnh đầy đủ.

### Input thiết kế

```json
{
  "product": 1
}
```

**Variant thực tế:** Samsung thay iPhone. Kết luận dùng mapping chức năng Mobile FR-20 -> FR-06 được trình bày trong báo cáo; không áp các ràng buộc HTML của Web cho React Native.

## 4. Expected Result

Image/name/price/description/category visible and correct; mapped FR-06.

Expected bắt buộc ở mức hành vi của SRS/mapping. HTTP status hoặc câu chữ error chỉ là contract bắt buộc khi có nguồn; không tự yêu cầu một error string cụ thể nếu SRS không quy định. Với request bị reject, dữ liệu phải giữ nguyên theo hậu điều kiện.

## 5. Actual Result và hậu điều kiện

Detail Samsung có ảnh, tên, giá, mô tả và quantity nhưng không có danh mục. Source renderProductDetail cũng không render category.

## 6. Các biến thể và traceability

| TC | Input | Status | Evidence |
|---|---|---|---|
| D-UI-09 | {"product": 1} | FAIL | [UI case](../tests/D-mobile-product-detail.md#d-ui-09) |

## 7. Impact và severity rationale

Không đạt checklist đầy đủ thông tin của FR-06 khi áp cho Mobile theo mapping đã công bố. Không phải lỗi kiểu dữ liệu price.

Severity Medium được đề xuất theo ảnh hưởng tới tính đúng đắn dữ liệu, quyền truy cập hoặc phép tính tiền của behavior này; chưa phải mức do giảng viên duyệt. Bug không đồng nghĩa một sự cố production đã xảy ra.

## 8. Root Cause và hướng khắc phục đề xuất

renderProductDetail render ảnh/tên/giá/mô tả/quantity nhưng không render category; API có category_id chưa được chuyển thành nhãn.

[Source baseline](https://github.com/ttbhanh/eshop-sut/blob/85af3ba875c88283615e22cb108f13e2fccaf0e9/frontend-mobile/App.js). Source giải thích cơ chế; xác nhận runtime dựa trên evidence ở trên.

Tra cứu/render category label đúng sản phẩm; regression kiểm tra đủ năm thành phần detail trên Mobile.

Đây là đề xuất, chưa sửa SUT và chưa chạy retest sau fix.

## 9. Screenshots và GitHub Issue

![D-UI-10_product-2_detail](../evidence/screenshots/D/D-UI-10_product-2_detail.jpg)

Issue URL/number: [#48](https://github.com/tkob-team/eshop-sut/issues/48). Đã đăng và đọc lại bằng GitHub CLI. Ảnh bug đính kèm và ảnh trang Issue còn chờ sinh viên bổ sung; [trạng thái evidence](../evidence/github-issues/README.md). Không coi việc tạo Issue là đã có screenshot.

## 10. Regression checklist

- Chạy lại representative và các lân cận/biến thể liên quan trong bảng TC.
- Kiểm valid nominal vẫn thành công, invalid không làm đổi state.
- Với auth/role: kiểm riêng none/invalid/user/admin; với API+UI: retest cả hai lớp.
- Ghi run mới sau fix riêng; giữ evidence baseline hiện tại để đối chiếu.
