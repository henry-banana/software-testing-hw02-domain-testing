# Evidence Register

## 1. Raw execution

| Feature | Record |
|---|---|
| A | [A-api.md](execution/A-api.md) |
| B | [B-api.md](execution/B-api.md) |
| C | [C-api.md](execution/C-api.md) |
| D | [D-api.md](execution/D-api.md) |

Raw reports ghi thời gian UTC thật, clock SUT mô phỏng, HTTP request/response, status và source hashes. 81 TC được kiểm chứng lại qua isolated backend; source/database gốc giữ nguyên hash sau từng suite.

## 2. UI screenshot provenance

71 ảnh sử dụng giữ nguyên SHA-256 từ bộ ảnh được cung cấp; tên mới gắn TC/variant. Một ảnh PNG 5x63px bị loại khỏi submission vì không đọc được nội dung. Nhiều ảnh hoặc dùng lại một ảnh không tạo TC mới.

| File hiện tại | Tên nguồn | SHA-256 | TC dùng evidence |
|---|---|---|---|
| [A-UI-01_02-response.png](screenshots/A/A-UI-01_02-response.png) | Screenshot 2026-10-19 152354.png | 4d29082727b23b3014594e36a61cdf7cf2084801891a3f8649bd07e68c516088 | A-UI-01 |
| [A-UI-02_01-input.png](screenshots/A/A-UI-02_01-input.png) | Screenshot 2026-10-19 152330.png | 75d2178fcd4be4cd993bd976677c303e59c899f7cef4e3646c6ed1584c0210ca | A-UI-02 |
| [A-UI-02_02-response.png](screenshots/A/A-UI-02_02-response.png) | Screenshot 2026-10-19 152336.png | 134799c87af06ffb113176c9c6c7302a9f136fdcf5f36c22b755cb7d4cdf67c6 | A-UI-02 |
| [A-UI-02_run-02_response.png](screenshots/A/A-UI-02_run-02_response.png) | Screenshot 2026-10-19 152644.png | 593569cd3173776aaa41dd795297f122d9bc449382dd46f1b2eb91d3840d7536 | A-UI-02 |
| [A-UI-02_variant-0987654321_response.png](screenshots/A/A-UI-02_variant-0987654321_response.png) | Screenshot 2026-10-19 152549.png | a16933b4acc66d24bc0301c34ec2f53ae99134459c7fa4c0aae02ff08402b944 | A-UI-02 |
| [A-UI-03_01-input.png](screenshots/A/A-UI-03_01-input.png) | Screenshot 2026-10-19 152700.png | 9046733d1ddce094375974cd327b772f26c7eb5dadcf688c47dfafdbd9a9a7c2 | A-UI-03 |
| [A-UI-03_02-response.png](screenshots/A/A-UI-03_02-response.png) | Screenshot 2026-10-19 152705.png | d12846a567f6d906db4f595a5afe548a16e1875845c2752b57df8c7ef5c4b6b6 | A-UI-03 |
| [A-UI-04_01-input.png](screenshots/A/A-UI-04_01-input.png) | Screenshot 2026-10-19 152749.png | afd03cda73ea3530737d8215de6c2d70c625f0d0a42e552dd17c9576542586b2 | A-UI-04 |
| [A-UI-04_02-response.png](screenshots/A/A-UI-04_02-response.png) | Screenshot 2026-10-19 152754.png | 584e9cd7de47bc50baf77337c661f94e9ebb34f222931824767433ea6aa7ef50 | A-UI-04 |
| [A-UI-05_01-input.png](screenshots/A/A-UI-05_01-input.png) | Screenshot 2026-10-19 152809.png | dfde6b6fe128c8fffd510cfca91c08e37301c2c435c5f92a1657e316db222558 | A-UI-05 |
| [A-UI-05_02-response.png](screenshots/A/A-UI-05_02-response.png) | Screenshot 2026-10-19 152812.png | 9003f301a27faca15c7d307359bfb555233b4bac0b1710c120ec881b5432ac7f | A-UI-05 |
| [A-UI-06_01-email-field.png](screenshots/A/A-UI-06_01-email-field.png) | Screenshot 2026-10-19 152856.png | efff33ff165baa8039c74d212c803ce4362d90db6cc21516bab48825c4ba9118 | A-UI-06 |
| [A-UI-07_variant-01_response.png](screenshots/A/A-UI-07_variant-01_response.png) | Screenshot 2026-10-19 152925.png | b128e711f2b9e86b7415e4d9fe297ea91be6f558cc3f69a68e8ef0593c83f647 | A-UI-07 |
| [B-total-edit_500002_input.png](screenshots/B/B-total-edit_500002_input.png) | Screenshot 2026-10-19 153238.png | aaa3617c8c0eda1ce74d9dbe2dbf56cd8f73f1cd9b498f6b6945956b63a73b3b | Ảnh bổ trợ, không cộng TC |
| [B-UI-01_00-added.png](screenshots/B/B-UI-01_00-added.png) | Screenshot 2026-10-19 153030.png | 6163bd495f85b77f999f980449ed13f7213ca9654026cc3500bc93ee52160ca0 | B-UI-01 |
| [B-UI-01_00-cart.png](screenshots/B/B-UI-01_00-cart.png) | Screenshot 2026-10-19 153033.png | c483c4850a3c0c4f89ff1b9777698ab62f0e2691944b4a5449c741bc7d6dc161 | B-UI-01 |
| [B-UI-01_00-product.png](screenshots/B/B-UI-01_00-product.png) | Screenshot 2026-10-19 153020.png | 9978fd853a36e08a64f26d4a6f41477e95ca68213d62f6a046f5759179409c54 | B-UI-01 |
| [B-UI-01_01-input.png](screenshots/B/B-UI-01_01-input.png) | Screenshot 2026-10-19 153058.png | 0be9a4c6aa0323948cbba200ddacba6db0590f1580b5c28af45a2b065edcca3b | B-UI-01 |
| [B-UI-01_02-response.png](screenshots/B/B-UI-01_02-response.png) | Screenshot 2026-10-19 153107.png | 9f0731e40c5cb993b2a00cf999b33fdedef76b4ba8e0dd29846e48146ce30f8b | B-UI-01 |
| [B-UI-02_01-input.png](screenshots/B/B-UI-02_01-input.png) | Screenshot 2026-10-19 153143.png | 06870b18aa170fdf9afa5467aa62ad4765cb9523fcf2debee135f7f044e0b362 | B-UI-02 |
| [B-UI-02_02-response.png](screenshots/B/B-UI-02_02-response.png) | Screenshot 2026-10-19 153148.png | 40c52dd956396dce467dd88eeecaf8dda5be1cbb92f276c5f82c30f67908fc4f | B-UI-02 |
| [B-UI-03_variant-01_input.png](screenshots/B/B-UI-03_variant-01_input.png) | Screenshot 2026-10-19 153224.png | dae1ad89e91622338941c7f0937f99f5b273b79817c5b81beb7f2986a51b264b | B-UI-03 |
| [B-UI-03_variant-01_response.png](screenshots/B/B-UI-03_variant-01_response.png) | Screenshot 2026-10-19 153227.png | 4edbf134674e5ee9e6cf4334284612152d5fb6da1ad1514b348198e229863c1b | B-UI-03 |
| [B-UI-04_01-input.png](screenshots/B/B-UI-04_01-input.png) | Screenshot 2026-10-19 153308.png | 4374bc347121da066a98dcf7871047b668dfa33d02d393d5bc187605b98f1fac | B-UI-04 |
| [B-UI-04_02-response.png](screenshots/B/B-UI-04_02-response.png) | Screenshot 2026-10-19 153313.png | cf25c13a54645a9ce7c09f9b68c305d404bc53d4f9b053bc1e3fe8e43d316e5b | B-UI-04 |
| [B-UI-05_02-response.png](screenshots/B/B-UI-05_02-response.png) | Screenshot 2026-10-19 153354.png | 4be014fd043f61b57c25579381dff1de6d2ca3f6c14c92f2fcf73e6fd4773734 | B-UI-05 |
| [B-VIP100_nominal_response.png](screenshots/B/B-VIP100_nominal_response.png) | Screenshot 2026-10-19 153403.png | eea973808e7d5990196afd5386ac082f1f536d0f039337921451dcad386a7793 | B-UI-06 |
| [C-UI-01_01-input.png](screenshots/C/C-UI-01_01-input.png) | Screenshot 2026-10-19 153531.png | 854b35043c4a28c0fe31b25fd718a0c61567fd2b85dc9ee63b39ecd2e94455df | C-UI-01 |
| [C-UI-01_02-created.png](screenshots/C/C-UI-01_02-created.png) | Screenshot 2026-10-19 153542.png | ba86c45fca5f487f40d28bb8fac47a1814acc96a5272081e5c67aeb47bf0ae32 | C-UI-01 |
| [C-UI-02_01-input.png](screenshots/C/C-UI-02_01-input.png) | Screenshot 2026-10-19 153646.png | 241b56e1735ef21b7a376590af21c1f12d13d097147699539f952420739dd4b7 | C-UI-02 |
| [C-UI-02_02-created.png](screenshots/C/C-UI-02_02-created.png) | Screenshot 2026-10-19 153651.png | b908d5358ace52aa05835a3ea700a67bb65f35dd13553f9af77ab149faf3ac16 | C-UI-02 |
| [C-UI-03_01-input.png](screenshots/C/C-UI-03_01-input.png) | Screenshot 2026-10-19 153714.png | c9becdc2df7209c2b3e25066adb4c0fc1f0ff8b61dbcfdb75cfb291db0a8e4d6 | C-UI-03 |
| [C-shared_coupon-list.png](screenshots/C/C-shared_coupon-list.png) | Screenshot 2026-10-19 153726.png | 579e2d285b9d4743bf5df1e87d5fda26cbfefcf1976fa65b39fb3b1aa6f0068c | C-UI-02, C-UI-03, C-UI-06 |
| [C-UI-04_01-input.png](screenshots/C/C-UI-04_01-input.png) | Screenshot 2026-10-19 153755.png | 381440aed704cc3845b9ab60fd232f1fde2d184d11d6329426108454f7b28b96 | C-UI-04 |
| [C-UI-04_02-browser-validation.png](screenshots/C/C-UI-04_02-browser-validation.png) | Screenshot 2026-10-19 153759.png | 7bc5c7c54a6c3b6db9f5847669c6aea08cf732582be85971305a4687ee2918f9 | C-UI-04 |
| [C-UI-05_01-input.png](screenshots/C/C-UI-05_01-input.png) | Screenshot 2026-10-19 153821.png | 86bcc67de6f727337f7998dea790b9f77079033681c865e34854a54358de0ff3 | C-UI-05 |
| [C-UI-05_02-response.png](screenshots/C/C-UI-05_02-response.png) | Screenshot 2026-10-19 153824.png | e1a45147cc97168d3ee8d41e337eda71c4bbaa7add5bf99edef75c317328c5fa | C-UI-05 |
| [C-UI-06_01-create-input.png](screenshots/C/C-UI-06_01-create-input.png) | Screenshot 2026-10-19 153847.png | 1918c884f1edd7cb0f61bdc1b9c31e7cdcc63d669521465a018fcb65e3a16316 | C-UI-06 |
| [C-UI-06_02-created.png](screenshots/C/C-UI-06_02-created.png) | Screenshot 2026-10-19 153850.png | f739a1d48f6cb6b6b2c10cb00d68af5fee10bc4a1d1926763b1e96409df8da6e | C-UI-06 |
| [D-extra_product-3_cart.jpg](screenshots/D/D-extra_product-3_cart.jpg) | Screenshot_2026-10-19-15-59-25-116_host.exp.exponent.jpg | a6f81e56f3d4460cc719d44d18c50e2236ea11ef785a03ef1f40622cc8a4771e | D-UI-13 |
| [D-extra_product-3_response.jpg](screenshots/D/D-extra_product-3_response.jpg) | Screenshot_2026-10-19-15-59-18-754_host.exp.exponent.jpg | e610b2b8fc13f496671abfcea94f5ee45499905e4960b4bc050e1abb6c536d0d | D-UI-13 |
| [D-UI-01_01-input.jpg](screenshots/D/D-UI-01_01-input.jpg) | Screenshot_2026-10-19-15-53-02-485_host.exp.exponent.jpg | 2d6538cdf773a4bdc55045a36cd02cff873e6ecdb7315e38954eaa22c7351aef | D-UI-01 |
| [D-UI-01_02-response.jpg](screenshots/D/D-UI-01_02-response.jpg) | Screenshot_2026-10-19-15-53-10-782_host.exp.exponent.jpg | 3498c45787501a7121c8b8e8eaa007c336c5ec15e28ee4f73543ef8e15ae2ffb | D-UI-01 |
| [D-UI-01_03-cart.jpg](screenshots/D/D-UI-01_03-cart.jpg) | Screenshot_2026-10-19-15-53-25-949_host.exp.exponent.jpg | 3494f6561f7020ffb02d8252c70cc383b0912d1a029e9272a32eee336b36c90b | D-UI-01 |
| [D-UI-02_01-input.jpg](screenshots/D/D-UI-02_01-input.jpg) | Screenshot_2026-10-19-15-53-45-577_host.exp.exponent.jpg | 36d29b0d200600754bfbf90b756592ff4cb46376a4ec8369e7a2ef07d89d9d2d | D-UI-02 |
| [D-UI-02_02-response.jpg](screenshots/D/D-UI-02_02-response.jpg) | Screenshot_2026-10-19-15-53-49-775_host.exp.exponent.jpg | 50bdbefb22f3a92163d96ed4e805376b23ac2c50595d3120f28b3a7678a1d6cc | D-UI-02 |
| [D-UI-02_03-cart.jpg](screenshots/D/D-UI-02_03-cart.jpg) | Screenshot_2026-10-19-15-54-04-428_host.exp.exponent.jpg | 5935006ed72e6f02a8e66d77fb5e5343f07a9a5ca9e958f12c91dcfbd9021d00 | D-UI-02 |
| [D-UI-03_01-input.jpg](screenshots/D/D-UI-03_01-input.jpg) | Screenshot_2026-10-19-15-54-35-004_host.exp.exponent.jpg | a6c4b58be255a0e3bf9b8901dda0ed7fc71b9f248a7a99651ee55891f6d58adc | D-UI-03 |
| [D-UI-03_02-response.jpg](screenshots/D/D-UI-03_02-response.jpg) | Screenshot_2026-10-19-15-54-40-396_host.exp.exponent.jpg | 88a2473d020ffe26fe234ccaa47d4d99118c271906d38d3da096112ec10ccc59 | D-UI-03 |
| [D-UI-03_03-cart.jpg](screenshots/D/D-UI-03_03-cart.jpg) | Screenshot_2026-10-19-15-54-48-168_host.exp.exponent.jpg | 5c001d43ec8b60c9bdfb74e448461e3ed70bc0278219e2a414df3432d0e8c391 | D-UI-03 |
| [D-UI-04_product-2_cart.jpg](screenshots/D/D-UI-04_product-2_cart.jpg) | Screenshot_2026-10-19-15-55-15-640_host.exp.exponent.jpg | cb3b7849a12f05e3fd07676493cad64a521c23333958249051d9d291c0473b96 | D-UI-04 |
| [D-UI-05_product-2_cart.jpg](screenshots/D/D-UI-05_product-2_cart.jpg) | Screenshot_2026-10-19-15-56-00-696_host.exp.exponent.jpg | e17b3e16e849fee429dbb111af37b722d93343b44637bb0837cf0bbd730378f8 | D-UI-05, D-UI-11 |
| [D-UI-05_product-2_input.jpg](screenshots/D/D-UI-05_product-2_input.jpg) | Screenshot_2026-10-19-15-55-48-911_host.exp.exponent.jpg | ed11e173b27d1fe7ead800fed9c26bb09260b33667e224001b955ce394647c89 | D-UI-05 |
| [D-UI-05_product-2_response.jpg](screenshots/D/D-UI-05_product-2_response.jpg) | Screenshot_2026-10-19-15-55-53-675_host.exp.exponent.jpg | 14d6b032279013e7ab66d210885a705a6edcdbe3f78b2e762e994746c3265489 | D-UI-05, D-UI-11 |
| [D-UI-06_01-input.jpg](screenshots/D/D-UI-06_01-input.jpg) | Screenshot_2026-10-19-15-56-11-682_host.exp.exponent.jpg | af77e954bccda0341e0a028297612382fb5697eb4349e64578d90a3e1fc0057c | D-UI-06 |
| [D-UI-06_02-response.jpg](screenshots/D/D-UI-06_02-response.jpg) | Screenshot_2026-10-19-15-56-15-694_host.exp.exponent.jpg | 53fc751cc506120d1e223883ebb24c1ae29e297161484c5d015ba5ac0581bae7 | D-UI-06 |
| [D-UI-06_03-cart.jpg](screenshots/D/D-UI-06_03-cart.jpg) | Screenshot_2026-10-19-15-56-21-750_host.exp.exponent.jpg | 8d21550401e1cba2b4bf1bac9941446236e61294335048c34ab10bdac02d918d | D-UI-06 |
| [D-UI-07_01-input.jpg](screenshots/D/D-UI-07_01-input.jpg) | Screenshot_2026-10-19-15-56-50-174_host.exp.exponent.jpg | 6c0142e1ab98cd3a500f0c25512dec36a3ee778d96356fb78ab2a91f3f7667b9 | D-UI-07 |
| [D-UI-07_02-response.jpg](screenshots/D/D-UI-07_02-response.jpg) | Screenshot_2026-10-19-15-56-52-234_host.exp.exponent.jpg | 1371aac851a1686ffff1f5b8d8a36fa4b1aacdb58cbc64e123af348fea9cd11e | D-UI-07 |
| [D-UI-07_03-cart.jpg](screenshots/D/D-UI-07_03-cart.jpg) | Screenshot_2026-10-19-15-56-59-011_host.exp.exponent.jpg | 423177b43ebf1b293fd40b65563a4779713d0544290f6b3764c764f94c65817e | D-UI-07 |
| [D-UI-08_01-input.jpg](screenshots/D/D-UI-08_01-input.jpg) | Screenshot_2026-10-19-15-57-20-725_host.exp.exponent.jpg | 6c5d8d9e9380e7a751e8603470ea929a4e42740d0e95e91ebecc6dcb8cd683df | D-UI-08 |
| [D-UI-08_02-response.jpg](screenshots/D/D-UI-08_02-response.jpg) | Screenshot_2026-10-19-15-57-24-923_host.exp.exponent.jpg | 1107ef17d8641d171f59b894ae88fc63a4af6fe5cc64fad8ecd4d6098f1a67a8 | D-UI-08 |
| [D-UI-10_product-2_detail.jpg](screenshots/D/D-UI-10_product-2_detail.jpg) | Screenshot_2026-10-19-15-55-27-567_host.exp.exponent.jpg | 893dcd1b1a44abd6d536b716c6172ca5c2248e455b83c95a53bcca9537d6cb7e | D-UI-09, D-UI-10 |
| [D-UI-12_final-cart.jpg](screenshots/D/D-UI-12_final-cart.jpg) | Screenshot_2026-10-19-16-00-02-871_host.exp.exponent.jpg | 4ce0f45a6aec6a872606238f576cd36fd235e1ce3c514413209ca62d55fd7e8f | D-UI-12 |
| [D-UI-12_candidate_response.jpg](screenshots/D/D-UI-12_candidate_response.jpg) | Screenshot_2026-10-19-15-59-56-567_host.exp.exponent.jpg | 1f005b911566e623bda61886a1cde132d666d23efafa56b9e915d092bef90ccc | D-UI-12 |
| [D-UI-14_variant-cart.jpg](screenshots/D/D-UI-14_variant-cart.jpg) | Screenshot_2026-10-19-16-00-40-975_host.exp.exponent.jpg | 216375f3c2b533affdd77635ac712e9e50104d9693e80eea84d5d00c3835bd6c | D-UI-14 |
| [D-UI-14_variant-input.jpg](screenshots/D/D-UI-14_variant-input.jpg) | Screenshot_2026-10-19-16-00-29-868_host.exp.exponent.jpg | a8d07271a6f869924f39b844713ab1fd4edb114c44f77bca3718c0e5f9fed735 | D-UI-14 |
| [D-UI-14_variant-response.jpg](screenshots/D/D-UI-14_variant-response.jpg) | Screenshot_2026-10-19-16-00-34-090_host.exp.exponent.jpg | e5745cc93240260473f9404d904ca2abf2d57cd60f2ab3dc51f502908104c5aa | D-UI-14 |
| [A-UI-07_01-valid-input.png](screenshots/A/A-UI-07_01-valid-input.png) | codex-clipboard-5db8bff6-8dbc-497e-9f91-ebdfc1c26244.png | 0c70e541472142584c211f4cc78a6362c7e58fe1628bc9e12f9cf81ad6c2706e | A-UI-07 |
| [A-UI-07_02-validation-error.png](screenshots/A/A-UI-07_02-validation-error.png) | codex-clipboard-d0bf2597-89a0-4ea9-9b32-d3f672bcc6c4.png | 99c90d4d44b2613a79968d476a1e09f0928e8f9f50845b36dd309b03d8bbacc4 | A-UI-07 |
| [B-UI-06_01-limit-rejected.png](screenshots/B/B-UI-06_01-limit-rejected.png) | codex-clipboard-0d378fb8-0d60-494a-978e-cd4e980704fe.png | 7bd40d70e92c6c107bc210f04c7071e661921c88807e70892e69ac7b7e38a608 | B-UI-06 |

## 3. GitHub Issue evidence

Đã đăng18Issues cá nhân: [Issue Evidence](github-issues/README.md), gồm URL/number và trạng thái ảnh. [Readback record](github-issues/issue-publication.json) được đối chiếu body bằng CLI; không có ảnh trang Issue tự sinh. Sinh viên sẽ đính kèm ảnh trực tiếp lên Issues và lưu ảnh trang Issue vào evidence/github-issues/.

Bản hiển thị prompt/output đã chuẩn hóa dấu câu; [source-records.json](ai-originals/source-records.json) giữ nội dung gốc vàSHA256, bao gồm rawAPI trước đổi dấu tiêu đề. PayloadJSON/rawactual không bị sửa bởi chuẩn hóa trình bày.
