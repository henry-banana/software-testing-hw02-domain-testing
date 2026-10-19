# A — Raw API execution

Started (UTC): 2026-10-19T19:50:52.465Z

Finished (UTC): 2026-10-19T19:50:58.413Z

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
| A-API-01 | PASS | — |
| A-API-02 | PASS | — |
| A-API-03 | FAIL | BUG-A01 |
| A-API-04 | FAIL | BUG-A01 |
| A-API-05 | FAIL | BUG-A01 |
| A-API-06 | FAIL | BUG-A01 |
| A-API-07 | FAIL | BUG-A01 |
| A-API-08 | FAIL | BUG-A01 |
| A-API-09 | FAIL | BUG-A01 |
| A-API-10 | FAIL | BUG-A01 |
| A-API-11 | FAIL | BUG-A01 |
| A-API-12 | FAIL | BUG-A01 |
| A-API-13 | FAIL | BUG-A01 |
| A-API-14 | FAIL | BUG-A01 |
| A-API-15 | OBSERVATION | — |
| A-API-16 | FAIL | BUG-A01 |
| A-API-17 | PASS | — |
| A-API-18 | FAIL | BUG-A02 |
| A-API-19 | PASS | — |
| A-API-20 | PASS | — |
| A-API-21 | PASS | — |
| A-API-22 | PASS | — |

## A-API-01

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:57.739Z

Expected: Accept and persist the exact valid phone

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "0912345678"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "0912345678"
    }
  }
]
```

## A-API-02

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:57.771Z

Expected: Accept and persist the exact valid phone

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "09123456789"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "09123456789"
    }
  }
]
```

## A-API-03

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:57.797Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "091234567"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "091234567"
    }
  }
]
```

## A-API-04

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:57.825Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "091234567890"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "091234567890"
    }
  }
]
```

## A-API-05

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:57.860Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": ""
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": ""
    }
  }
]
```

## A-API-06

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:57.895Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "0"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "0"
    }
  }
]
```

## A-API-07

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:57.922Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "09123456"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "09123456"
    }
  }
]
```

## A-API-08

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:57.955Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "0912345678901"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "0912345678901"
    }
  }
]
```

## A-API-09

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:57.984Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "1912345678"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "1912345678"
    }
  }
]
```

## A-API-10

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:58.013Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "19123456789"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "19123456789"
    }
  }
]
```

## A-API-11

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:58.041Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "091234567a"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "091234567a"
    }
  }
]
```

## A-API-12

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:58.073Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "09123 5678"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "09123 5678"
    }
  }
]
```

## A-API-13

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:58.103Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "+84912345678"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "+84912345678"
    }
  }
]
```

## A-API-14

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:58.132Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "09123-5678"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "09123-5678"
    }
  }
]
```

## A-API-15

Status: OBSERVATION

Timestamp (UTC): 2026-10-19T19:50:58.161Z

Expected: Record Unicode numeral acceptance; SRS does not explicitly specify numeral encoding

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": "０９１２３４５６７８"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "０９１２３４５６７８"
    }
  }
]
```

## A-API-16

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:58.195Z

Expected: Reject; stored phone stays 0912345678

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "shipping_address": "1 Test Street",
      "phone": null
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": null
    }
  }
]
```

## A-API-17

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:58.231Z

Expected: Persist Unicode name and address exactly

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "Người Dùng HW02",
      "phone": "0912345678",
      "shipping_address": "Đường Thử Nghiệm"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "Người Dùng HW02",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "Đường Thử Nghiệm",
      "phone": "0912345678"
    }
  }
]
```

## A-API-18

Status: FAIL

Timestamp (UTC): 2026-10-19T19:50:58.262Z

Expected: Reject or ignore role; GET /users/me remains role=user

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "HW02 User",
      "phone": "0912345678",
      "shipping_address": "1 Test Street",
      "role": "admin"
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "HW02 User",
      "email": "test@eshop.com",
      "role": "admin",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "0912345678"
    }
  }
]
```

## A-API-19

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:58.297Z

Expected: Update authenticated user 2; user 3 unchanged

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "user",
    "input": {
      "name": "Owner Only",
      "phone": "0912345678",
      "shipping_address": "1 Test Street",
      "id": 3,
      "user_id": 3
    },
    "status": 200,
    "body": {
      "message": "Profile updated"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "Owner Only",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "0912345678"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "other",
    "input": null,
    "status": 200,
    "body": {
      "id": 3,
      "name": "Other User",
      "email": "other@hw02.invalid",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "Other Street",
      "phone": "0987654321"
    }
  }
]
```

## A-API-20

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:58.332Z

Expected: Reject unauthenticated update (401/403); profile unchanged

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "none",
    "input": {
      "phone": "0912345678"
    },
    "status": 401,
    "body": {
      "error": "Unauthorized"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "Test User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "0912345678"
    }
  }
]
```

## A-API-21

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:58.357Z

Expected: Reject unauthenticated update (401/403); profile unchanged

Requests/responses (sanitized):

```json
[
  {
    "method": "PUT",
    "url": "/api/users/me",
    "authentication": "invalid",
    "input": {
      "phone": "0912345678"
    },
    "status": 403,
    "body": {
      "error": "Forbidden"
    }
  },
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "user",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "Test User",
      "email": "test@eshop.com",
      "role": "user",
      "login_attempts": 0,
      "locked_until": null,
      "shipping_address": "1 Test Street",
      "phone": "0912345678"
    }
  }
]
```

## A-API-22

Status: PASS

Timestamp (UTC): 2026-10-19T19:50:58.383Z

Expected: GET profile without JWT returns 401/403

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/users/me",
    "authentication": "none",
    "input": null,
    "status": 401,
    "body": {
      "error": "Unauthorized"
    }
  }
]
```
