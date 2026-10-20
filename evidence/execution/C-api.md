# C - Raw API execution

Started (UTC): 2026-10-19T20:08:00.378Z

Finished (UTC): 2026-10-19T20:08:01.519Z

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
| C-API-01 | PASS | - |
| C-API-02 | PASS | - |
| C-API-03 | FAIL | BUG-C01 |
| C-API-04 | FAIL | BUG-C01 |
| C-API-05 | FAIL | BUG-C01 |
| C-API-06 | FAIL | BUG-C01 |
| C-API-07 | FAIL | BUG-C01 |
| C-API-08 | FAIL | BUG-C01 |
| C-API-09 | FAIL | BUG-C01 |
| C-API-10 | PASS | - |
| C-API-11 | FAIL | BUG-C03 |
| C-API-12 | FAIL | BUG-C04 |
| C-API-13 | FAIL | BUG-C04 |
| C-API-14 | PASS | - |
| C-API-15 | FAIL | BUG-C05 |
| C-API-16 | PASS | - |
| C-API-17 | PASS | - |
| C-API-18 | FAIL | BUG-C06 |
| C-API-19 | FAIL | BUG-C06 |
| C-API-20 | PASS | - |
| C-API-21 | PASS | - |
| C-API-22 | PASS | - |
| C-API-23 | FAIL | BUG-C07 |
| C-API-24 | PASS | - |
| C-API-25 | PASS | - |
| C-API-26 | FAIL | BUG-C08 |
| C-API-27 | PASS | - |
| C-API-28 | PASS | - |
| C-API-29 | FAIL | BUG-C09 |
| C-API-30 | PASS | - |

## C-API-01

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:00.809Z

Expected: Admin creates coupon and list contains exact supplied values

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 5,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 6,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 7,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 8,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 9,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 10,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 11,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 12,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 13
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 5,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 6,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 7,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 8,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 9,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 10,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 11,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 12,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 13,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-02

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:00.838Z

Expected: Admin creates coupon and list contains exact supplied values

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 14,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 15,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 16,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 17,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 18,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 19,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 20,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 21,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "percent",
      "discount_value": 10,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 22
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 14,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 15,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 16,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 17,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 18,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 19,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 20,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 21,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 22,
        "code": "HW02_NEW",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-03

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:00.863Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 23,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 24,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 25,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 26,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 27,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 28,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 29,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 30,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 31
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 23,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 24,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 25,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 26,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 27,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 28,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 29,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 30,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 31,
        "code": null,
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-04

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:00.886Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 32,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 33,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 34,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 35,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 36,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 37,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 38,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 39,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 40
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 32,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 33,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 34,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 35,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 36,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 37,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 38,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 39,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 40,
        "code": "HW02_NEW",
        "type": null,
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-05

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:00.910Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 41,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 42,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 43,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 44,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 45,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 46,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 47,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 48,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 49
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 41,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 42,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 43,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 44,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 45,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 46,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 47,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 48,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 49,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": null,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-06

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:00.935Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 50,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 51,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 52,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 53,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 54,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 55,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 56,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 57,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 58
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 50,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 51,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 52,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 53,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 54,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 55,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 56,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 57,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 58,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": null,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-07

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:00.958Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 59,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 60,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 61,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 62,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 63,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 64,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 65,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 66,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 67
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 59,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 60,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 61,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 62,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 63,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 64,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 65,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 66,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 67,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": null,
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-08

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:00.983Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 68,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 69,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 70,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 71,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 72,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 73,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 74,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 75,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31"
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 76
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 68,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 69,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 70,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 71,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 72,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 73,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 74,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 75,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 76,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-09

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:01.006Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 77,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 78,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 79,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 80,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 81,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 82,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 83,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 84,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 85
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 77,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 78,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 79,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 80,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 81,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 82,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 83,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 84,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 85,
        "code": "",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-10

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.031Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 86,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 87,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 88,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 89,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 90,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 91,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 92,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 93,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "SAVE10",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 500,
    "body": {
      "error": "SQLITE_CONSTRAINT: UNIQUE constraint failed: coupons.code"
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 86,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 87,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 88,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 89,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 90,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 91,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 92,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 93,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-11

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:01.055Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 94,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 95,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 96,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 97,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 98,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 99,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 100,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 101,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "other",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 102
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 94,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 95,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 96,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 97,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 98,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 99,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 100,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 101,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 102,
        "code": "HW02_NEW",
        "type": "other",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-12

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:01.079Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 103,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 104,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 105,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 106,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 107,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 108,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 109,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 110,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": -1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 111
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 103,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 104,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 105,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 106,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 107,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 108,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 109,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 110,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 111,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": -1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-13

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:01.105Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 112,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 113,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 114,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 115,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 116,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 117,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 118,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 119,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 0,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 120
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 112,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 113,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 114,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 115,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 116,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 117,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 118,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 119,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 120,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 0,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-14

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.128Z

Expected: Admin creates coupon and list contains exact supplied values

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 121,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 122,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 123,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 124,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 125,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 126,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 127,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 128,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 129
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 121,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 122,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 123,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 124,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 125,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 126,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 127,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 128,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 129,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-15

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:01.153Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 130,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 131,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 132,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 133,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 134,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 135,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 136,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 137,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": -1,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 138
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 130,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 131,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 132,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 133,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 134,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 135,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 136,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 137,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 138,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": -1,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-16

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.177Z

Expected: Admin creates coupon and list contains exact supplied values

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 139,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 140,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 141,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 142,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 143,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 144,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 145,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 146,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 147
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 139,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 140,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 141,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 142,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 143,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 144,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 145,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 146,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 147,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-17

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.202Z

Expected: Admin creates coupon and list contains exact supplied values

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 148,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 149,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 150,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 151,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 152,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 153,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 154,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 155,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 1,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 156
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 148,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 149,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 150,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 151,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 152,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 153,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 154,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 155,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 156,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 1,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-18

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:01.226Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 157,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 158,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 159,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 160,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 161,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 162,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 163,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 164,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": -1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 165
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 157,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 158,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 159,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 160,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 161,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 162,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 163,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 164,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 165,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": -1
      }
    ]
  }
]
```

## C-API-19

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:01.248Z

Expected: Reject invalid coupon; list has no newly created record

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 166,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 167,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 168,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 169,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 170,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 171,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 172,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 173,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 0
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 174
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 166,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 167,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 168,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 169,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 170,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 171,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 172,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 173,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 174,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-20

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.270Z

Expected: Admin creates coupon and list contains exact supplied values

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 175,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 176,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 177,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 178,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 179,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 180,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 181,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 182,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 183
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 175,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 176,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 177,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 178,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 179,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 180,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 181,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 182,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 183,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-21

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.294Z

Expected: Admin creates coupon and list contains exact supplied values

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 184,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 185,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 186,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 187,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 188,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 189,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 190,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 191,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "admin",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 2
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 192
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 184,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 185,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 186,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 187,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 188,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 189,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 190,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 191,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 192,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      }
    ]
  }
]
```

## C-API-22

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.319Z

Expected: Reject missing/invalid JWT (401/403); valid coupon data must not be inserted

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 193,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 194,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 195,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 196,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 197,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 198,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 199,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 200,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "none",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 401,
    "body": {
      "error": "Unauthorized"
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 193,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 194,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 195,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 196,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 197,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 198,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 199,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 200,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-23

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:01.343Z

Expected: Reject non-admin create (401/403); valid coupon data must not be inserted

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 201,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 202,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 203,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 204,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 205,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 206,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 207,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 208,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "user",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 200,
    "body": {
      "message": "Coupon created",
      "id": 209
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 201,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 202,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 203,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 204,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 205,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 206,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 207,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 208,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 209,
        "code": "HW02_NEW",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-24

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.367Z

Expected: Reject missing/invalid JWT (401/403); valid coupon data must not be inserted

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 210,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 211,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 212,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 213,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 214,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 215,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 216,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 217,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "POST",
    "url": "/api/admin/coupons",
    "authentication": "invalid",
    "input": {
      "code": "HW02_NEW",
      "type": "fixed",
      "discount_value": 1,
      "min_order_amount": 0,
      "expired_at": "2099-12-31",
      "max_uses_per_user": 1
    },
    "status": 403,
    "body": {
      "error": "Forbidden"
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 210,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 211,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 212,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 213,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 214,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 215,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 216,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 217,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-25

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.387Z

Expected: Return coupon list

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 218,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 219,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 220,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 221,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 222,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 223,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 224,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 225,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-26

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:01.407Z

Expected: Reject non-admin access (401/403)

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 226,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 227,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 228,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 229,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 230,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 231,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 232,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 233,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-27

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.424Z

Expected: Reject non-admin access (401/403)

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "none",
    "input": null,
    "status": 401,
    "body": {
      "error": "Unauthorized"
    }
  }
]
```

## C-API-28

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.443Z

Expected: Coupon removed; other coupons unchanged

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 242,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 243,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 244,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 245,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 246,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 247,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 248,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 249,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "DELETE",
    "url": "/api/admin/coupons/249",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": {
      "message": "Coupon deleted"
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 242,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 243,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 244,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 245,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 246,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 247,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 248,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-29

Status: FAIL

Timestamp (UTC): 2026-10-19T20:08:01.466Z

Expected: Reject non-admin delete; coupon remains

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 250,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 251,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 252,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 253,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 254,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 255,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 256,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 257,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "DELETE",
    "url": "/api/admin/coupons/257",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "message": "Coupon deleted"
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 250,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 251,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 252,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 253,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 254,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 255,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 256,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```

## C-API-30

Status: PASS

Timestamp (UTC): 2026-10-19T20:08:01.490Z

Expected: Reject non-admin delete; coupon remains

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 258,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 259,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 260,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 261,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 262,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 263,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 264,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 265,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  },
  {
    "method": "DELETE",
    "url": "/api/admin/coupons/265",
    "authentication": "none",
    "input": null,
    "status": 401,
    "body": {
      "error": "Unauthorized"
    }
  },
  {
    "method": "GET",
    "url": "/api/coupons",
    "authentication": "admin",
    "input": null,
    "status": 200,
    "body": [
      {
        "id": 258,
        "code": "SAVE10",
        "type": "percent",
        "discount_value": 10,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 259,
        "code": "BIGBUY",
        "type": "fixed",
        "discount_value": 50000,
        "min_order_amount": 500000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 260,
        "code": "VIP100",
        "type": "fixed",
        "discount_value": 100000,
        "min_order_amount": 300000,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 2
      },
      {
        "id": 261,
        "code": "EXPIRED",
        "type": "percent",
        "discount_value": 20,
        "min_order_amount": 100000,
        "expired_at": "2020-01-01",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 262,
        "code": "OFF",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 0,
        "max_uses_per_user": 1
      },
      {
        "id": 263,
        "code": "TIME",
        "type": "fixed",
        "discount_value": 10000,
        "min_order_amount": 0,
        "expired_at": "2026-10-19T08:00:01.000Z",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 264,
        "code": "P100",
        "type": "percent",
        "discount_value": 100,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      },
      {
        "id": 265,
        "code": "DELETE_ME",
        "type": "fixed",
        "discount_value": 1,
        "min_order_amount": 0,
        "expired_at": "2099-12-31",
        "is_active": 1,
        "max_uses_per_user": 1
      }
    ]
  }
]
```
