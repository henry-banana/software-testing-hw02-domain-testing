# Bug reports by functional requirement

Mã FR04, FR09, FR17 và FR20 theo feature được chọn. Mỗi số thứ tự mô tả một điều kiện lỗi cụ thể; testcase chỉ lặp đúng hành vi sẽ dẫn về cùng Issue. Các điều kiện khác nhau có thể chung một nguyên nhân trong source. Nhãn bug trên GitHub thay cho tiền tố BUG trong tên.

| ID | Mô tả | Severity | Test cases | GitHub Issue |
|---|---|---|---|---|
| [FR04-01](FR04-01.md) | Profile API accepts and persists a 9-digit phone | High | A-API-03 | [#97](https://github.com/tkob-team/eshop-sut/issues/97) |
| [FR04-02](FR04-02.md) | Profile API accepts and persists a 12-digit phone | High | A-API-04 | [#98](https://github.com/tkob-team/eshop-sut/issues/98) |
| [FR04-03](FR04-03.md) | Profile API accepts and persists an empty phone | High | A-API-05 | [#99](https://github.com/tkob-team/eshop-sut/issues/99) |
| [FR04-04](FR04-04.md) | Profile API accepts and persists a one-digit phone | High | A-API-06 | [#100](https://github.com/tkob-team/eshop-sut/issues/100) |
| [FR04-05](FR04-05.md) | Profile API accepts and persists an 8-digit phone | High | A-API-07 | [#101](https://github.com/tkob-team/eshop-sut/issues/101) |
| [FR04-06](FR04-06.md) | Profile API accepts and persists a 13-digit phone | High | A-API-08 | [#102](https://github.com/tkob-team/eshop-sut/issues/102) |
| [FR04-07](FR04-07.md) | Profile API accepts and persists a 10-digit phone with a nonzero prefix | High | A-API-09 | [#103](https://github.com/tkob-team/eshop-sut/issues/103) |
| [FR04-08](FR04-08.md) | Profile API accepts and persists an 11-digit phone with a nonzero prefix | High | A-API-10 | [#104](https://github.com/tkob-team/eshop-sut/issues/104) |
| [FR04-09](FR04-09.md) | Profile API accepts and persists a phone containing a letter | High | A-API-11 | [#105](https://github.com/tkob-team/eshop-sut/issues/105) |
| [FR04-10](FR04-10.md) | Profile API accepts and persists a phone containing an embedded space | High | A-API-12 | [#106](https://github.com/tkob-team/eshop-sut/issues/106) |
| [FR04-11](FR04-11.md) | Profile API accepts and persists a country-code phone instead of the required 0 prefix | High | A-API-13 | [#107](https://github.com/tkob-team/eshop-sut/issues/107) |
| [FR04-12](FR04-12.md) | Profile API accepts and persists a hyphenated phone | High | A-API-14 | [#108](https://github.com/tkob-team/eshop-sut/issues/108) |
| [FR04-13](FR04-13.md) | Profile API accepts and persists a null phone | High | A-API-16 | [#109](https://github.com/tkob-team/eshop-sut/issues/109) |
| [FR04-14](FR04-14.md) | Regular users can change their stored role to admin | Critical | A-API-18 | [#110](https://github.com/tkob-team/eshop-sut/issues/110) |
| [FR04-15](FR04-15.md) | Web rejects a valid 10-digit 0-prefixed phone | High | A-UI-02, A-UI-07 | [#111](https://github.com/tkob-team/eshop-sut/issues/111) |
| [FR04-16](FR04-16.md) | Web rejects a valid 11-digit 0-prefixed phone | High | A-UI-03 | [#112](https://github.com/tkob-team/eshop-sut/issues/112) |
| [FR04-17](FR04-17.md) | Web accepts a 10-digit phone with an invalid nonzero prefix | High | A-UI-05 | [#113](https://github.com/tkob-team/eshop-sut/issues/113) |
| [FR04-18](FR04-18.md) | Profile response discloses the plaintext password | Critical | A-API-23 | [#114](https://github.com/tkob-team/eshop-sut/issues/114) |
| [FR04-19](FR04-19.md) | Profile response discloses an active password-reset token | Critical | A-API-24 | [#115](https://github.com/tkob-team/eshop-sut/issues/115) |
| [FR04-20](FR04-20.md) | Login response includes password and reset-state properties | Critical | A-API-29 | [#116](https://github.com/tkob-team/eshop-sut/issues/116) |
| [FR04-21](FR04-21.md) | Mobile profile payload silently clears the shipping address | High | A-API-26 | [#117](https://github.com/tkob-team/eshop-sut/issues/117) |
| [FR04-22](FR04-22.md) | Mobile handler rejects a valid 10-digit 0-prefixed phone | High | A-HND-01 | [#118](https://github.com/tkob-team/eshop-sut/issues/118) |
| [FR04-23](FR04-23.md) | Mobile handler rejects a valid 11-digit 0-prefixed phone | High | A-HND-02 | [#119](https://github.com/tkob-team/eshop-sut/issues/119) |
| [FR04-24](FR04-24.md) | Mobile handler accepts an invalid nonzero phone prefix | High | A-HND-03 | [#120](https://github.com/tkob-team/eshop-sut/issues/120) |
| [FR04-25](FR04-25.md) | Disabled Web profile email uses text instead of email input type | Low | A-UI-08 | [#121](https://github.com/tkob-team/eshop-sut/issues/121) |
| [FR04-26](FR04-26.md) | Stored profile name executes an HTML event handler in Web greeting | High | A-UI-09 | [#122](https://github.com/tkob-team/eshop-sut/issues/122) |
| [FR04-27](FR04-27.md) | SPA profile re-entry shows stale data after a successful save | Medium | A-UI-10 | [#123](https://github.com/tkob-team/eshop-sut/issues/123) |
| [FR09-01](FR09-01.md) | Fixed coupon is rejected at its exact minimum total | High | B-API-03, B-UI-02 | [#124](https://github.com/tkob-team/eshop-sut/issues/124) |
| [FR09-02](FR09-02.md) | Percentage coupon is rejected at its exact minimum total | High | B-API-06 | [#125](https://github.com/tkob-team/eshop-sut/issues/125) |
| [FR09-03](FR09-03.md) | A 10 percent coupon returns a negative discount and increases total | Critical | B-API-08, B-API-07, B-UI-04 | [#126](https://github.com/tkob-team/eshop-sut/issues/126) |
| [FR09-04](FR09-04.md) | Coupon remains valid at the exact expiration instant | Medium | B-API-13 | [#127](https://github.com/tkob-team/eshop-sut/issues/127) |
| [FR09-05](FR09-05.md) | Coupon application succeeds without an Authorization header | High | B-API-19 | [#128](https://github.com/tkob-team/eshop-sut/issues/128) |
| [FR09-06](FR09-06.md) | Coupon application succeeds with a malformed JWT | High | B-API-20 | [#129](https://github.com/tkob-team/eshop-sut/issues/129) |
| [FR09-07](FR09-07.md) | Coupon application succeeds with an expired JWT | High | B-API-21 | [#130](https://github.com/tkob-team/eshop-sut/issues/130) |
| [FR09-08](FR09-08.md) | Substituted body user_id bypasses the authenticated coupon limit | High | B-API-22 | [#131](https://github.com/tkob-team/eshop-sut/issues/131) |
| [FR09-09](FR09-09.md) | Omitted body user_id bypasses the authenticated coupon limit | High | B-API-23 | [#132](https://github.com/tkob-team/eshop-sut/issues/132) |
| [FR09-10](FR09-10.md) | VIP100 minimum equality is rejected on the last eligible use | High | B-API-24 | [#133](https://github.com/tkob-team/eshop-sut/issues/133) |
| [FR09-11](FR09-11.md) | A 100 percent coupon produces a negative discount instead of zero total | Critical | B-API-26 | [#134](https://github.com/tkob-team/eshop-sut/issues/134) |
| [FR09-12](FR09-12.md) | Late coupon response applies a discount after the input code changes | Medium | B-UI-07 | [#135](https://github.com/tkob-team/eshop-sut/issues/135) |
| [FR17-01](FR17-01.md) | Coupon creation accepts a missing required code | High | C-API-03 | [#136](https://github.com/tkob-team/eshop-sut/issues/136) |
| [FR17-02](FR17-02.md) | Coupon creation accepts a missing required type | High | C-API-04 | [#137](https://github.com/tkob-team/eshop-sut/issues/137) |
| [FR17-03](FR17-03.md) | Coupon creation accepts a missing required discount_value | High | C-API-05 | [#138](https://github.com/tkob-team/eshop-sut/issues/138) |
| [FR17-04](FR17-04.md) | Coupon creation accepts a missing required min_order_amount | High | C-API-06 | [#139](https://github.com/tkob-team/eshop-sut/issues/139) |
| [FR17-05](FR17-05.md) | Coupon creation accepts a missing required expired_at | High | C-API-07 | [#140](https://github.com/tkob-team/eshop-sut/issues/140) |
| [FR17-06](FR17-06.md) | Coupon creation accepts a missing required max_uses_per_user | High | C-API-08 | [#141](https://github.com/tkob-team/eshop-sut/issues/141) |
| [FR17-07](FR17-07.md) | Coupon creation accepts an empty code | High | C-API-09 | [#142](https://github.com/tkob-team/eshop-sut/issues/142) |
| [FR17-08](FR17-08.md) | Coupon creation persists a type outside percent and fixed | Medium | C-API-11 | [#143](https://github.com/tkob-team/eshop-sut/issues/143) |
| [FR17-09](FR17-09.md) | Coupon creation accepts a negative discount_value | High | C-API-12 | [#144](https://github.com/tkob-team/eshop-sut/issues/144) |
| [FR17-10](FR17-10.md) | Coupon creation accepts discount_value equal to zero | High | C-API-13, C-UI-01 | [#145](https://github.com/tkob-team/eshop-sut/issues/145) |
| [FR17-11](FR17-11.md) | Coupon creation accepts a negative min_order_amount | Medium | C-API-15, C-UI-03 | [#146](https://github.com/tkob-team/eshop-sut/issues/146) |
| [FR17-12](FR17-12.md) | Coupon creation accepts a negative max_uses_per_user | Medium | C-API-18 | [#147](https://github.com/tkob-team/eshop-sut/issues/147) |
| [FR17-13](FR17-13.md) | Coupon creation silently changes a zero max_uses_per_user to one | Medium | C-API-19 | [#148](https://github.com/tkob-team/eshop-sut/issues/148) |
| [FR17-14](FR17-14.md) | A regular user can create an administrator coupon | High | C-API-23 | [#149](https://github.com/tkob-team/eshop-sut/issues/149) |
| [FR17-15](FR17-15.md) | A regular user can read the administrator coupon list | Medium | C-API-26 | [#150](https://github.com/tkob-team/eshop-sut/issues/150) |
| [FR17-16](FR17-16.md) | A regular user can delete an administrator coupon | High | C-API-29 | [#151](https://github.com/tkob-team/eshop-sut/issues/151) |
| [FR17-17](FR17-17.md) | Coupon form omits required-field markers | Low | C-UI-07 | [#152](https://github.com/tkob-team/eshop-sut/issues/152) |
| [FR20-01](FR20-01.md) | Mobile Add to Cart accepts an empty quantity | High | D-UI-01 | [#153](https://github.com/tkob-team/eshop-sut/issues/153) |
| [FR20-02](FR20-02.md) | Mobile Add to Cart accepts a negative quantity | High | D-UI-02 | [#154](https://github.com/tkob-team/eshop-sut/issues/154) |
| [FR20-03](FR20-03.md) | Mobile Add to Cart accepts zero quantity | High | D-UI-03 | [#155](https://github.com/tkob-team/eshop-sut/issues/155) |
| [FR20-04](FR20-04.md) | Mobile Add to Cart accepts a fractional quantity | High | D-UI-06 | [#156](https://github.com/tkob-team/eshop-sut/issues/156) |
| [FR20-05](FR20-05.md) | Mobile Add to Cart accepts an alphabetic quantity | High | D-UI-07 | [#157](https://github.com/tkob-team/eshop-sut/issues/157) |
| [FR20-06](FR20-06.md) | Mobile Add to Cart accepts a mixed digit-and-letter quantity | High | D-UI-08 | [#158](https://github.com/tkob-team/eshop-sut/issues/158) |
| [FR20-07](FR20-07.md) | Mobile product detail omits the product category | Medium | D-UI-09 | [#159](https://github.com/tkob-team/eshop-sut/issues/159) |
| [FR20-08](FR20-08.md) | Mobile positive Add to Cart action is green instead of blue | Low | D-UI-15 | [#160](https://github.com/tkob-team/eshop-sut/issues/160) |
