# B-UI-06 - Exhausted usage fixture

**Readback recorded UTC:** 2026-10-20T04:22:38.564688+00:00. Đây là thời điểm đọc trạng thái fixture, không phải timestamp chụp UI.

Chúng tôi đọc database runtime Web riêng bằng SQLite `mode=ro`; không chạy lại seed, không thay đổi dữ liệu hoặc dừng server đang dùng. Account và coupon khớp ảnh UI B-UI-06. Hai dòng `coupon_usage` được helper tạo trực tiếp để kiểm điều kiện `used=limit=2`; không tuyên bố sinh viên đã hoàn tất hai đơn mới. Readback sau khi nhận ảnh bổ sung xác nhận trạng thái hiện tại; không phải query được chụp đồng thời với thao tác UI.

```sql
SELECT u.email, c.code, c.max_uses_per_user, COUNT(cu.id) AS used_count
FROM users u JOIN coupon_usage cu ON cu.user_id=u.id
JOIN coupons c ON c.id=cu.coupon_id
WHERE u.email='b_ui_06@hw02.invalid' AND c.code='VIP100'
GROUP BY u.id, c.id;
```

```json
[
  {
    "email": "b_ui_06@hw02.invalid",
    "code": "VIP100",
    "max_uses_per_user": 2,
    "used_count": 2
  }
]
```

UI sau khi bấm Áp dụng hiển thị `Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)` với account B-UI-06, VIP100 và total 400000; [ảnh gốc](../screenshots/B/B-UI-06_01-limit-rejected.png) và [test case](../../tests/B-FR09-discount-coupons.md#b-ui-06). Kết luận PASS giới hạn ở hành vi từ chối tại trạng thái exhausted; quy trình tạo usage qua checkout không được kiểm end-to-end trong case này.
