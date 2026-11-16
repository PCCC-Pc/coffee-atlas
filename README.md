# Coffee Atlas｜咖啡世界圖鑑

本 Repository 是獨立的咖啡知識庫專案。包含五冊知識筆記、互動式 Wiki、30 頁 HTML 教學雜誌、參考來源、Graph＋Loop 流程及作業報告。

## 專案狀態
- Wiki：原始版本已檢查並發現 JavaScript 標籤與首頁內容輸出問題；本地修正版已完成靜態檢查。
- 靜態檢查：五冊、11 章、30 頁教學內容、15 筆來源；JSON、HTML 資源路徑與 JavaScript 語法檢查通過。
- 真實瀏覽器操作：尚未完成，請勿將其視為通過。

## 預計目錄
- `01_Wiki/`：五冊 Markdown 與 Wiki HTML。
- `02_HTML_Magazine/`：30 頁教學雜誌 HTML。
- `03_Sources/`：來源登錄及 APA 7th。
- `04_Workflow/`：Graph＋Loop 與驗證紀錄。
- `05_Report/`：Word／PDF 報告與預覽圖。
- `06_Project_Source/`：內容模型、原始程式及驗證腳本。

## 本地驗證
```bash
python 06_Project_Source/validate_project.py
```

此腳本進行靜態檢查，不取代 Chrome／Edge 的真實互動測試。