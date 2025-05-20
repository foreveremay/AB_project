# AB 合約後端 API

這是 AB 合約工具的後端服務，採用 FastAPI + MongoDB 設計，支援 Railway、Render 等平台部署。

## 快速部署（推薦 Railway）

1. 點擊 Railway 預設按鈕或手動新增專案
2. 設定環境變數：`MONGO_URI`
3. 自動部署 `main.py`

## API 路由

| 方法 | 路徑 | 說明 |
|------|------|------|
| POST | /api/contracts | 儲存合約 |
| GET  | /api/contracts/search | 查詢合約 |
| DELETE | /api/contracts/{id} | 刪除合約 |

## 開發環境

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## .env

```
MONGO_URI=mongodb://localhost:27017
```
