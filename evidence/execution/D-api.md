# D - Raw API execution

Started (UTC): 2026-10-19T19:51:00.621Z

Finished (UTC): 2026-10-19T19:51:01.044Z

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
| D-API-01 | PASS | - |
| D-API-02 | PASS | - |
| D-API-03 | OBSERVATION | - |

## D-API-01

Status: PASS

Timestamp (UTC): 2026-10-19T19:51:00.970Z

Expected: Product 1 name/price/description/image/category ID match fixture

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/products/1",
    "authentication": "none",
    "input": null,
    "status": 200,
    "body": {
      "id": 1,
      "name": "iPhone 15 Pro Max",
      "price": 30000000,
      "description": "Điện thoại cao cấp của Apple",
      "imageUrl": "https://placehold.co/300x300/png?text=iPhone+15",
      "category_id": 1
    }
  }
]
```

## D-API-02

Status: PASS

Timestamp (UTC): 2026-10-19T19:51:00.997Z

Expected: Product 2 data usable; price numerically 28000000 (JSON type not specified)

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/products/2",
    "authentication": "none",
    "input": null,
    "status": 200,
    "body": {
      "id": 2,
      "name": "Samsung Galaxy S24 Ultra",
      "price": "28000000",
      "description": "Màn hình hiển thị xuất sắc, camera siêu zoom",
      "imageUrl": "https://placehold.co/300x300/png?text=Samsung+S24",
      "category_id": 1
    }
  }
]
```

## D-API-03

Status: OBSERVATION

Timestamp (UTC): 2026-10-19T19:51:01.017Z

Expected: Record HTTP/body; no mandated status code in SRS

Requests/responses (sanitized):

```json
[
  {
    "method": "GET",
    "url": "/api/products/999999",
    "authentication": "none",
    "input": null,
    "status": 200,
    "body": {}
  }
]
```
