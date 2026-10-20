# A - Raw API execution

Started (UTC): 2026-10-20T07:29:11.325Z

Finished (UTC): 2026-10-20T07:29:12.428Z

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
| A-API-01 | PASS | - |
| A-API-02 | PASS | - |
| A-API-03 | FAIL | the related failure |
| A-API-04 | FAIL | the related failure |
| A-API-05 | FAIL | the related failure |
| A-API-06 | FAIL | the related failure |
| A-API-07 | FAIL | the related failure |
| A-API-08 | FAIL | the related failure |
| A-API-09 | FAIL | the related failure |
| A-API-10 | FAIL | the related failure |
| A-API-11 | FAIL | the related failure |
| A-API-12 | FAIL | the related failure |
| A-API-13 | FAIL | the related failure |
| A-API-14 | FAIL | the related failure |
| A-API-15 | OBSERVATION | - |
| A-API-16 | FAIL | the related failure |
| A-API-17 | PASS | - |
| A-API-18 | FAIL | the related failure |
| A-API-19 | PASS | - |
| A-API-20 | PASS | - |
| A-API-21 | PASS | - |
| A-API-22 | PASS | - |

## A-API-01

Status: PASS

Timestamp (UTC): 2026-10-20T07:29:11.786Z

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

Timestamp (UTC): 2026-10-20T07:29:11.819Z

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

Timestamp (UTC): 2026-10-20T07:29:11.852Z

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

Timestamp (UTC): 2026-10-20T07:29:11.882Z

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

Timestamp (UTC): 2026-10-20T07:29:11.910Z

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

Timestamp (UTC): 2026-10-20T07:29:11.936Z

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

Timestamp (UTC): 2026-10-20T07:29:11.965Z

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

Timestamp (UTC): 2026-10-20T07:29:11.995Z

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

Timestamp (UTC): 2026-10-20T07:29:12.021Z

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

Timestamp (UTC): 2026-10-20T07:29:12.049Z

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

Timestamp (UTC): 2026-10-20T07:29:12.076Z

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

Timestamp (UTC): 2026-10-20T07:29:12.103Z

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

Timestamp (UTC): 2026-10-20T07:29:12.129Z

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

Timestamp (UTC): 2026-10-20T07:29:12.155Z

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

Timestamp (UTC): 2026-10-20T07:29:12.182Z

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

Timestamp (UTC): 2026-10-20T07:29:12.217Z

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

Timestamp (UTC): 2026-10-20T07:29:12.257Z

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

Timestamp (UTC): 2026-10-20T07:29:12.288Z

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

Timestamp (UTC): 2026-10-20T07:29:12.324Z

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

Timestamp (UTC): 2026-10-20T07:29:12.355Z

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

Timestamp (UTC): 2026-10-20T07:29:12.377Z

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

Timestamp (UTC): 2026-10-20T07:29:12.397Z

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


## Additional interface execution

Browser captures show real SUT DOM. Source-handler execution uses the exact Mobile handler with injected Alert/HTTP adapters and is not a native UI run. D-UI-15 reviews the original native capture for an additional visual criterion. Original source/database hashes remain unchanged.

## A-API-23

Status: FAIL

```json
{
  "at": "2026-10-20T07:21:52.318Z",
  "trace": [
    {
      "method": "GET",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
      "input": null,
      "status": 200,
      "body": {
        "id": 2,
        "name": "Test User",
        "email": "test@eshop.com",
        "password": "<REDACTED>",
        "role": "user",
        "login_attempts": 0,
        "locked_until": null,
        "reset_token": null,
        "shipping_address": "1 Test Street",
        "phone": "0912345678"
      }
    }
  ],
  "observed": {
    "profileStatus": 200,
    "passwordFieldPresent": true,
    "passwordMatchesFixture": true,
    "resetTokenFieldPresent": true,
    "storageMatchesPlaintextFixture": true
  }
}
```

## A-API-24

Status: FAIL

```json
{
  "at": "2026-10-20T07:21:52.330Z",
  "trace": [
    {
      "method": "POST",
      "url": "/api/forgot-password",
      "authentication": "none",
      "input": {
        "email": "test@eshop.com"
      },
      "status": 200,
      "body": {
        "message": "Mã đặt lại mật khẩu đã được tạo",
        "resetToken": "<REDACTED>"
      }
    },
    {
      "method": "GET",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
      "input": null,
      "status": 200,
      "body": {
        "id": 2,
        "name": "Test User",
        "email": "test@eshop.com",
        "password": "<REDACTED>",
        "role": "user",
        "login_attempts": 0,
        "locked_until": null,
        "reset_token": "<REDACTED>",
        "shipping_address": "1 Test Street",
        "phone": "0912345678"
      }
    },
    {
      "method": "POST",
      "url": "/api/reset-password",
      "authentication": "none",
      "input": {
        "email": "test@eshop.com",
        "resetToken": "<REDACTED>",
        "newPassword": "<REDACTED>"
      },
      "status": 200,
      "body": {
        "message": "Password reset successfully"
      }
    },
    {
      "method": "POST",
      "url": "/api/login",
      "authentication": "none",
      "input": {
        "email": "test@eshop.com",
        "password": "<REDACTED>"
      },
      "status": 200,
      "body": {
        "message": "Login successful",
        "token": "<REDACTED>",
        "user": {
          "id": 2,
          "name": "Test User",
          "email": "test@eshop.com",
          "password": "<REDACTED>",
          "role": "user",
          "login_attempts": 0,
          "locked_until": null,
          "reset_token": null,
          "shipping_address": "1 Test Street",
          "phone": "0912345678"
        }
      }
    }
  ],
  "observed": {
    "forgotStatus": 200,
    "tokenPresent": true,
    "tokenLength": 4,
    "profileTokenMatchesGenerated": true,
    "resetWithProfileTokenStatus": 200,
    "loginWithNewPasswordStatus": 200
  }
}
```

## A-API-25

Status: PASS

```json
{
  "at": "2026-10-20T07:21:52.354Z",
  "trace": [
    {
      "method": "PUT",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
      "input": {
        "name": "Mobile User",
        "phone": "0912345678",
        "shipping_address": "Mobile Address"
      },
      "status": 200,
      "body": {
        "message": "Profile updated"
      }
    },
    {
      "method": "GET",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
      "input": null,
      "status": 200,
      "body": {
        "id": 2,
        "name": "Mobile User",
        "email": "test@eshop.com",
        "password": "<REDACTED>",
        "role": "user",
        "login_attempts": 0,
        "locked_until": null,
        "reset_token": null,
        "shipping_address": "Mobile Address",
        "phone": "0912345678"
      }
    }
  ]
}
```

## A-API-26

Status: FAIL

```json
{
  "at": "2026-10-20T07:21:52.367Z",
  "trace": [
    {
      "method": "PUT",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
      "input": {
        "name": "Mobile User",
        "phone": "0912345678",
        "shippingAddress": "Mobile Address"
      },
      "status": 200,
      "body": {
        "message": "Profile updated"
      }
    },
    {
      "method": "GET",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
      "input": null,
      "status": 200,
      "body": {
        "id": 2,
        "name": "Mobile User",
        "email": "test@eshop.com",
        "password": "<REDACTED>",
        "role": "user",
        "login_attempts": 0,
        "locked_until": null,
        "reset_token": null,
        "shipping_address": null,
        "phone": "0912345678"
      }
    }
  ],
  "observed": {
    "accepted": true,
    "persistedAddress": null,
    "masking": "The real Mobile handler rejects this valid 0-prefixed phone before HTTP; see A-HND-01/02."
  }
}
```

## A-API-27

Status: OBSERVATION

```json
{
  "at": "2026-10-20T07:21:52.381Z",
  "trace": [
    {
      "method": "PUT",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
      "input": {
        "name": "Only Name"
      },
      "status": 200,
      "body": {
        "message": "Profile updated"
      }
    },
    {
      "method": "GET",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
      "input": null,
      "status": 200,
      "body": {
        "id": 2,
        "name": "Only Name",
        "email": "test@eshop.com",
        "password": "<REDACTED>",
        "role": "user",
        "login_attempts": 0,
        "locked_until": null,
        "reset_token": null,
        "shipping_address": null,
        "phone": null
      }
    }
  ],
  "observed": {
    "status": 200,
    "phone": null,
    "address": null
  }
}
```

## A-API-28

Status: OBSERVATION

```json
{
  "at": "2026-10-20T07:21:52.394Z",
  "trace": [
    {
      "method": "POST",
      "url": "/api/checkout",
      "authentication": "isolated JWT (redacted)",
      "input": {
        "items": [
          {
            "id": 1,
            "quantity": 1
          }
        ],
        "total_amount": 30000000,
        "coupon_id": null
      },
      "status": 200,
      "body": {
        "message": "Checkout successful",
        "orderId": 1
      }
    },
    {
      "method": "GET",
      "url": "/api/orders/my-orders",
      "authentication": "isolated JWT (redacted)",
      "input": null,
      "status": 200,
      "body": [
        {
          "id": 1,
          "user_id": 2,
          "total_amount": 30000000,
          "status": "pending",
          "shipping_address": null,
          "created_at": "2026-10-20 07:21:52"
        }
      ]
    }
  ],
  "observed": {
    "checkoutStatus": 200,
    "orderShippingAddress": null
  }
}
```

## A-API-29

Status: FAIL

```json
{
  "at": "2026-10-20T07:21:52.404Z",
  "trace": [
    {
      "method": "POST",
      "url": "/api/login",
      "authentication": "none",
      "input": {
        "email": "test@eshop.com",
        "password": "<REDACTED>"
      },
      "status": 200,
      "body": {
        "message": "Login successful",
        "token": "<REDACTED>",
        "user": {
          "id": 2,
          "name": "Test User",
          "email": "test@eshop.com",
          "password": "<REDACTED>",
          "role": "user",
          "login_attempts": 0,
          "locked_until": null,
          "reset_token": null,
          "shipping_address": "1 Test Street",
          "phone": "0912345678"
        }
      }
    }
  ],
  "observed": {
    "passwordMatchesFixture": true,
    "nestedKeys": [
      "id",
      "name",
      "email",
      "password",
      "role",
      "login_attempts",
      "locked_until",
      "reset_token",
      "shipping_address",
      "phone"
    ]
  }
}
```

## A-HND-01

Status: FAIL

```json
{
  "at": "2026-10-20T07:21:52.507Z",
  "trace": [],
  "observed": {
    "phone": "0912345678",
    "shouldAccept": true,
    "httpCalls": 0,
    "alerts": [
      [
        "Lỗi",
        "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."
      ]
    ],
    "localUser": null,
    "persistedAddress": null,
    "sourceBodySha256": "a6975cfae3415194652d76547f7feedacf830c906bad0f21e6c4f9ba696eec74",
    "evidenceScope": "Exact source handler executed with injected Alert/setUser and loopback HTTP. No React render, device, UI screenshot or native interaction."
  }
}
```

## A-HND-02

Status: FAIL

```json
{
  "at": "2026-10-20T07:21:52.510Z",
  "trace": [],
  "observed": {
    "phone": "09123456789",
    "shouldAccept": true,
    "httpCalls": 0,
    "alerts": [
      [
        "Lỗi",
        "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."
      ]
    ],
    "localUser": null,
    "persistedAddress": null,
    "sourceBodySha256": "a6975cfae3415194652d76547f7feedacf830c906bad0f21e6c4f9ba696eec74",
    "evidenceScope": "Exact source handler executed with injected Alert/setUser and loopback HTTP. No React render, device, UI screenshot or native interaction."
  }
}
```

## A-HND-03

Status: FAIL

```json
{
  "at": "2026-10-20T07:21:52.512Z",
  "trace": [
    {
      "method": "PUT",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
      "input": {
        "name": "Mobile User",
        "phone": "1912345678",
        "shippingAddress": "Mobile Address"
      },
      "status": 200,
      "body": {
        "message": "Profile updated"
      }
    },
    {
      "method": "GET",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
      "input": null,
      "status": 200,
      "body": {
        "id": 2,
        "name": "Mobile User",
        "email": "test@eshop.com",
        "password": "<REDACTED>",
        "role": "user",
        "login_attempts": 0,
        "locked_until": null,
        "reset_token": null,
        "shipping_address": null,
        "phone": "1912345678"
      }
    }
  ],
  "observed": {
    "phone": "1912345678",
    "shouldAccept": false,
    "httpCalls": 1,
    "alerts": [
      [
        "Thành công",
        "Cập nhật thành công!"
      ]
    ],
    "localUser": {
      "id": 2,
      "name": "Mobile User",
      "shipping_address": "Mobile Address",
      "phone": "1912345678"
    },
    "persistedAddress": null,
    "sourceBodySha256": "a6975cfae3415194652d76547f7feedacf830c906bad0f21e6c4f9ba696eec74",
    "evidenceScope": "Exact source handler executed with injected Alert/setUser and loopback HTTP. No React render, device, UI screenshot or native interaction."
  }
}
```

## A-HND-04

Status: PASS

```json
{
  "at": "2026-10-20T07:21:52.525Z",
  "trace": [],
  "observed": {
    "phone": "091234567",
    "shouldAccept": false,
    "httpCalls": 0,
    "alerts": [
      [
        "Lỗi",
        "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."
      ]
    ],
    "localUser": null,
    "persistedAddress": null,
    "sourceBodySha256": "a6975cfae3415194652d76547f7feedacf830c906bad0f21e6c4f9ba696eec74",
    "evidenceScope": "Exact source handler executed with injected Alert/setUser and loopback HTTP. No React render, device, UI screenshot or native interaction."
  }
}
```

## A-HND-05

Status: PASS

```json
{
  "at": "2026-10-20T07:21:52.527Z",
  "trace": [],
  "observed": {
    "phone": "091234567890",
    "shouldAccept": false,
    "httpCalls": 0,
    "alerts": [
      [
        "Lỗi",
        "Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."
      ]
    ],
    "localUser": null,
    "persistedAddress": null,
    "sourceBodySha256": "a6975cfae3415194652d76547f7feedacf830c906bad0f21e6c4f9ba696eec74",
    "evidenceScope": "Exact source handler executed with injected Alert/setUser and loopback HTTP. No React render, device, UI screenshot or native interaction."
  }
}
```

## A-UI-08

Status: FAIL

```json
{
  "at": "2026-10-20T07:43:51.616313+00:00",
  "observed": {
    "type": "text",
    "disabled": true,
    "outerHTML": "<input disabled=\"\" class=\"w-full border p-2 rounded bg-gray-100\" type=\"text\" value=\"test@eshop.com\">"
  },
  "expected": "FR-22: email fields use type=email, including a disabled field.",
  "precondition": ""
}
```



## A-UI-09

Status: FAIL

```json
{
  "at": "2026-10-20T07:43:52.151983+00:00",
  "observed": {
    "stored_name": "<img src=x onerror=\"document.documentElement.dataset.profileCanary='executed';this.outerHTML='<b>PROFILE_CANARY_EXECUTED</b>'\">",
    "canary_executed": true,
    "persisted_via": "Authenticated PUT /api/users/me",
    "update_response": {
      "message": "Profile updated"
    },
    "greeting": "EShop\nGiỏ hàng\nChào, PROFILE_CANARY_EXECUTED\nThoát",
    "scope": "Harmless DOM canary only; no token theft tested."
  },
  "expected": "SEC-04: user-controlled name is escaped; an HTML event handler cannot execute.",
  "precondition": ""
}
```



## A-UI-10

Status: FAIL

```json
{
  "at": "2026-10-20T07:43:53.025509+00:00",
  "observed": {
    "save_dialogs": [
      "Cập nhật thành công!"
    ],
    "persisted_name": "Saved Profile Canary",
    "shown_after_navigation": "Test User",
    "hard_reload_would_refetch": true,
    "phone": "1912345678"
  },
  "expected": "After a successful profile save, returning via SPA navigation displays the persisted fields.",
  "precondition": "Controlled interaction: the pre-existing phone 1912345678 is accepted by the faulty UI guard. Normal valid 0-prefixed saves are masked by the related failure; no claim that this fixture is SRS-valid."
}
```





## Role escalation control

```json
{
  "id": "A-API-18",
  "at": "2026-10-20T07:21:52.409Z",
  "kind": "revalidation attempt, not a new designed case",
  "status": "FAIL",
  "bug": "the related failure",
  "observed": {
    "roleBefore": "user",
    "roleAfter": "admin",
    "newJwtRole": "admin",
    "adminUsersBefore": 200,
    "adminUsersAfter": 200
  },
  "trace": [
    {
      "method": "GET",
      "url": "/api/admin/users",
      "authentication": "isolated JWT (redacted)",
      "input": null,
      "status": 200,
      "body": [
        {
          "id": 1,
          "name": "Admin User",
          "email": "admin@eshop.com",
          "role": "admin",
          "login_attempts": 0,
          "locked_until": null,
          "shipping_address": null
        },
        {
          "id": 2,
          "name": "Test User",
          "email": "test@eshop.com",
          "role": "user",
          "login_attempts": 0,
          "locked_until": null,
          "shipping_address": "1 Test Street"
        }
      ]
    },
    {
      "method": "PUT",
      "url": "/api/users/me",
      "authentication": "isolated JWT (redacted)",
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
      "authentication": "isolated JWT (redacted)",
      "input": null,
      "status": 200,
      "body": {
        "id": 2,
        "name": "HW02 User",
        "email": "test@eshop.com",
        "password": "<REDACTED>",
        "role": "admin",
        "login_attempts": 0,
        "locked_until": null,
        "reset_token": null,
        "shipping_address": "1 Test Street",
        "phone": "0912345678"
      }
    },
    {
      "method": "POST",
      "url": "/api/login",
      "authentication": "none",
      "input": {
        "email": "test@eshop.com",
        "password": "<REDACTED>"
      },
      "status": 200,
      "body": {
        "message": "Login successful",
        "token": "<REDACTED>",
        "user": {
          "id": 2,
          "name": "HW02 User",
          "email": "test@eshop.com",
          "password": "<REDACTED>",
          "role": "admin",
          "login_attempts": 0,
          "locked_until": null,
          "reset_token": null,
          "shipping_address": "1 Test Street",
          "phone": "0912345678"
        }
      }
    },
    {
      "method": "GET",
      "url": "/api/admin/users",
      "authentication": "isolated JWT (redacted)",
      "input": null,
      "status": 200,
      "body": [
        {
          "id": 1,
          "name": "Admin User",
          "email": "admin@eshop.com",
          "role": "admin",
          "login_attempts": 0,
          "locked_until": null,
          "shipping_address": null
        },
        {
          "id": 2,
          "name": "HW02 User",
          "email": "test@eshop.com",
          "role": "admin",
          "login_attempts": 0,
          "locked_until": null,
          "shipping_address": "1 Test Street"
        }
      ]
    }
  ]
}
```

The admin-users endpoint already returns 200 before role modification; no 403-to-200 transition is claimed.
