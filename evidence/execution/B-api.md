# B - Raw API execution

Started (UTC): 2026-10-19T19:50:58.485Z

Finished (UTC): 2026-10-19T19:50:59.464Z

Host timezone labels use UTC explicitly; add 07:00 for Asia/Saigon. SUT clock frozen at 2026-10-19T08:00:00.000Z; runner timestamp uses real clock.

Origin: http://127.0.0.1:3100. Byte-identical copied backend source; HTTP listen port and global Date adapter only. SQLite fixtures are test setup; assertions observe public API. Password/token fields are omitted from evidence.

Original SUT files unchanged after run: **PASS**.

## Source hashes

| File | SHA-256 before (= after when PASS) |
|---|---|
| backend/server.js | e2263811a1690a63a7dbb4446c3fd33fb87f50d073d9f8cdfab7083a52f5e8ed |
| backend/database.js | 50012f35c2cf0776dd837482d76adf701f0ee40cdcb9d80143278fccde034717 |
| backend/database.sqlite | c63f00544180ba1fbb1427a9b9dd3f1784842698809972f33ce90482e7420ba6 |
| frontend-web/src/pages/Profile.jsx | 847f893bf17b311373d6670e027d0083f79bafa50d6552771e4c20fc29bd1469 |
| frontend-web/src/pages/Checkout.jsx | c8246642b7935dc3feb93056f8b61990584a7f16f1f1759d7ecbc9172521287a |
| frontend-admin/src/App.jsx | f43a7ed720eb2608563ab5329edc2858f4aab913ecfb57784b30a467803c5b5f |
| frontend-mobile/App.js | f32d1e6288602407d82b34ec2e1b39efb652ec82d1c4173dd6a4bf477795de1b |

## Results

| ID | Status | Bug group |
|---|---|---|
| B-API-01 | PASS | - |
| B-API-02 | PASS | - |
| B-API-03 | FAIL | BUG-B01 |
| B-API-04 | PASS | - |
| B-API-05 | PASS | - |
| B-API-06 | FAIL | BUG-B01 |
| B-API-07 | FAIL | BUG-B02 |
| B-API-08 | FAIL | BUG-B02 |
| B-API-09 | PASS | - |
| B-API-10 | PASS | - |
| B-API-11 | PASS | - |
| B-API-12 | PASS | - |
| B-API-13 | FAIL | BUG-B03 |
| B-API-14 | PASS | - |
| B-API-15 | PASS | - |
| B-API-16 | PASS | - |
| B-API-17 | PASS | - |
| B-API-18 | PASS | - |
| B-API-19 | FAIL | BUG-B04 |
| B-API-20 | FAIL | BUG-B04 |
| B-API-21 | FAIL | BUG-B04 |
| B-API-22 | FAIL | BUG-B05 |
| B-API-23 | FAIL | BUG-B05 |
| B-API-24 | FAIL | BUG-B01 |
| B-API-25 | PASS | - |
| B-API-26 | FAIL | BUG-B02 |

## B-API-01

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:58.838Z

Expected: discount=50000; final=550000

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "BIGBUY",
      "total_amount": 600000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 6,
      "discount_amount": 50000,
      "final_amount": 550000,
      "message": "Áp dụng thành công! Giảm 50,000 ₫"
    }
  }
]
```

## B-API-02

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:58.875Z

Expected: Reject insufficient total

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "BIGBUY",
      "total_amount": 499999,
      "user_id": 2
    },
    "status": 400,
    "body": {
      "error": "Đơn hàng chưa đủ giá trị tối thiểu 500,000 ₫ để áp dụng mã này"
    }
  }
]
```

## B-API-03

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:58.904Z

Expected: discount=50000; final=450000

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "BIGBUY",
      "total_amount": 500000,
      "user_id": 2
    },
    "status": 400,
    "body": {
      "error": "Đơn hàng chưa đủ giá trị tối thiểu 500,000 ₫ để áp dụng mã này"
    }
  }
]
```

## B-API-04

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:58.931Z

Expected: discount=50000; final=450001

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "BIGBUY",
      "total_amount": 500001,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 30,
      "discount_amount": 50000,
      "final_amount": 450001,
      "message": "Áp dụng thành công! Giảm 50,000 ₫"
    }
  }
]
```

## B-API-05

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:58.958Z

Expected: Reject insufficient total

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "SAVE10",
      "total_amount": 299999,
      "user_id": 2
    },
    "status": 400,
    "body": {
      "error": "Đơn hàng chưa đủ giá trị tối thiểu 300,000 ₫ để áp dụng mã này"
    }
  }
]
```

## B-API-06

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:58.983Z

Expected: discount=30000; final=270000

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "SAVE10",
      "total_amount": 300000,
      "user_id": 2
    },
    "status": 400,
    "body": {
      "error": "Đơn hàng chưa đủ giá trị tối thiểu 300,000 ₫ để áp dụng mã này"
    }
  }
]
```

## B-API-07

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:59.010Z

Expected: discount=30000.1; final=270000.9 (SRS has no rounding rule)

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "SAVE10",
      "total_amount": 300001,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 53,
      "discount_amount": -2700009,
      "final_amount": 3000010,
      "message": "Áp dụng thành công! Giảm 10%"
    }
  }
]
```

## B-API-08

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:59.040Z

Expected: discount=40000; final=360000

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "SAVE10",
      "total_amount": 400000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 61,
      "discount_amount": -3600000,
      "final_amount": 4000000,
      "message": "Áp dụng thành công! Giảm 10%"
    }
  }
]
```

## B-API-09

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:59.064Z

Expected: Reject nonexistent code

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "NO_SUCH_CODE",
      "total_amount": 600000,
      "user_id": 2
    },
    "status": 404,
    "body": {
      "error": "Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa"
    }
  }
]
```

## B-API-10

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:59.090Z

Expected: Reject inactive code

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "OFF",
      "total_amount": 600000,
      "user_id": 2
    },
    "status": 404,
    "body": {
      "error": "Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa"
    }
  }
]
```

## B-API-11

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:59.111Z

Expected: Reject missing code

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "total_amount": 600000,
      "user_id": 2
    },
    "status": 400,
    "body": {
      "error": "Vui lòng nhập mã giảm giá"
    }
  }
]
```

## B-API-12

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:59.130Z

Expected: Reject expired coupon

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "TIME",
      "total_amount": 400000,
      "user_id": 2
    },
    "status": 400,
    "body": {
      "error": "Mã giảm giá đã hết hạn"
    }
  }
]
```

## B-API-13

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:59.150Z

Expected: Reject: current time must be strictly before expiry

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "TIME",
      "total_amount": 400000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 106,
      "discount_amount": 10000,
      "final_amount": 390000,
      "message": "Áp dụng thành công! Giảm 10,000 ₫"
    }
  }
]
```

## B-API-14

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:59.170Z

Expected: discount=10000; final=390000

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "TIME",
      "total_amount": 400000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 114,
      "discount_amount": 10000,
      "final_amount": 390000,
      "message": "Áp dụng thành công! Giảm 10,000 ₫"
    }
  }
]
```

## B-API-15

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:59.189Z

Expected: discount=100000; final=300000

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "VIP100",
      "total_amount": 400000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 119,
      "discount_amount": 100000,
      "final_amount": 300000,
      "message": "Áp dụng thành công! Giảm 100,000 ₫"
    }
  }
]
```

## B-API-16

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:59.208Z

Expected: discount=100000; final=300000

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "VIP100",
      "total_amount": 400000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 127,
      "discount_amount": 100000,
      "final_amount": 300000,
      "message": "Áp dụng thành công! Giảm 100,000 ₫"
    }
  }
]
```

## B-API-17

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:59.229Z

Expected: Reject exhausted coupon

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "VIP100",
      "total_amount": 400000,
      "user_id": 2
    },
    "status": 400,
    "body": {
      "error": "Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)"
    }
  }
]
```

## B-API-18

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:59.252Z

Expected: Reject exhausted coupon

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "VIP100",
      "total_amount": 400000,
      "user_id": 2
    },
    "status": 400,
    "body": {
      "error": "Bạn đã sử dụng mã này 2 lần (đã đạt giới hạn)"
    }
  }
]
```

## B-API-19

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:59.280Z

Expected: Reject invalid/missing authentication (401/403)

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "none",
    "input": {
      "code": "BIGBUY",
      "total_amount": 600000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 150,
      "discount_amount": 50000,
      "final_amount": 550000,
      "message": "Áp dụng thành công! Giảm 50,000 ₫"
    }
  }
]
```

## B-API-20

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:59.302Z

Expected: Reject invalid/missing authentication (401/403)

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "invalid",
    "input": {
      "code": "BIGBUY",
      "total_amount": 600000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 158,
      "discount_amount": 50000,
      "final_amount": 550000,
      "message": "Áp dụng thành công! Giảm 50,000 ₫"
    }
  }
]
```

## B-API-21

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:59.322Z

Expected: Reject invalid/missing authentication (401/403)

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "expired",
    "input": {
      "code": "BIGBUY",
      "total_amount": 600000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 166,
      "discount_amount": 50000,
      "final_amount": 550000,
      "message": "Áp dụng thành công! Giảm 50,000 ₫"
    }
  }
]
```

## B-API-22

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:59.342Z

Expected: Reject: user 2 already used limit; client user_id is not identity

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "VIP100",
      "total_amount": 400000,
      "user_id": 3
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 175,
      "discount_amount": 100000,
      "final_amount": 300000,
      "message": "Áp dụng thành công! Giảm 100,000 ₫"
    }
  }
]
```

## B-API-23

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:59.365Z

Expected: Reject: authenticated user 2 already used limit

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "VIP100",
      "total_amount": 400000
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 183,
      "discount_amount": 100000,
      "final_amount": 300000,
      "message": "Áp dụng thành công! Giảm 100,000 ₫"
    }
  }
]
```

## B-API-24

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:59.388Z

Expected: discount=100000; final=200000

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "VIP100",
      "total_amount": 300000,
      "user_id": 2
    },
    "status": 400,
    "body": {
      "error": "Đơn hàng chưa đủ giá trị tối thiểu 300,000 ₫ để áp dụng mã này"
    }
  }
]
```

## B-API-25

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:59.414Z

Expected: Reject; no error precedence is specified

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "none",
    "input": {
      "code": "OFF",
      "total_amount": 0
    },
    "status": 404,
    "body": {
      "error": "Mã giảm giá không tồn tại hoặc đã bị vô hiệu hóa"
    }
  }
]
```

## B-API-26

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:59.437Z

Expected: discount=400000; final=0

Requests/responses (sanitized):

```json
[
  {
    "method": "POST",
    "url": "/api/apply-coupon",
    "authentication": "user",
    "input": {
      "code": "P100",
      "total_amount": 400000,
      "user_id": 2
    },
    "status": 200,
    "body": {
      "success": true,
      "coupon_id": 211,
      "discount_amount": -39600000,
      "final_amount": 40000000,
      "message": "Áp dụng thành công! Giảm 100%"
    }
  }
]
```
