# COFFEE ATLAS｜咖啡世界圖鑑

此 Repository 用於獨立的 Coffee_Atlas 課程專案。內容包含五冊 Markdown 咖啡研究筆記、互動式 Wiki、30 頁教學內容（另含封面與目錄）的 HTML 雜誌、15 筆資料來源、Graph＋Loop 工作流程及作業報告。

## 專案目錄
- `01_Wiki/`：Markdown 知識庫、章節資料與 HTML 閱讀介面。
- `02_HTML_Magazine/`：HTML 咖啡雜誌與簡報資料。
- `03_Sources/`：來源登錄與 APA 7th 參考文獻。
- `04_Workflow/`：Graph＋Loop 流程圖、說明及驗證紀錄。
- `05_Report/`：課程作業成果報告。
- `06_Project_Source/`：原始程式與驗證腳本。

## 使用
Wiki：開啟 `01_Wiki/index.html`。
雜誌：開啟 `02_HTML_Magazine/index.html`。
執行靜態檢查：`python 06_Project_Source/validate_project.py`（需要 Node.js）。

## 內容規格
5 冊、11 個 Wiki 主題、30 頁教學內容（共 32 頁含封面與目錄）、15 筆來源（8 篇學術研究、5 筆官方／研究機構、2 筆產業資料）。來源欄位使用 `doi_or_url`，以區別 DOI 與一般網頁網址。

## 測試範圍與限制
本專案已做 JSON、來源 ID 對應、HTML 本地資源路徑、script 標籤配對及 Node JavaScript 語法靜態檢查。此處不代表完成實際瀏覽器互動測試；localStorage、剪貼簿、滾輪翻頁、全螢幕及不同螢幕尺寸仍需人工驗收。請參閱 `AUDIT_REPORT.md`。
