# Coffee_Atlas｜GitHub 匯入與驗證紀錄

最後更新：2026-11-16

## 本次已確認的修正
1. Wiki 首頁的程式資料區塊曾出現裸露 JSON；本地修正版重新建立 script 區塊，GitHub 目前 Wiki 的 script 開閉標籤各一組。
2. Wiki 首頁 Hero 主視覺路徑曾與實際資產副檔名不一致；已統一改用 Repository 內的 `01_Wiki/assets/coffee_atlas_hero.svg`。
3. HTML 雜誌封面 CSS 背景與內頁動態圖片曾引用不存在的 PNG／WebP；已改成使用相對路徑 `../01_Wiki/assets/coffee_atlas_hero.svg`。
4. 補入並追蹤四個 SVG：coffee_atlas_hero、processing_methods、flavor_wheel、brewing_steps。
5. APA 7 參考文獻 A4 作者順序已修正為 Cordoba Castro、Ruiz Pardo、Moreno Moreno、Fernandez Alduenda。
6. 公開 Repository 的專案規格已移除學生姓名與學號。

## GitHub 遠端靜態檢查（2026-11-16）
- Wiki 與雜誌的 script 開啟／關閉標籤數量：均為 1／1。
- Wiki Hero SVG 路徑：存在。
- Wiki 三個章節圖像 SVG：存在。
- 雜誌封面 CSS 背景及內頁 img 路徑：均指向已追蹤 SVG。
- 雜誌舊的 coffee_atlas_hero.png 引用：未發現。
- 五冊 Markdown：存在。
- 來源登錄 JSON 及 APA 7 文獻清單：存在。
- Graph＋Loop Mermaid、流程說明及驗證紀錄：存在。
- A4 作者排序：已修正。
- GitHub 目前追蹤 20 個檔案。

## 尚未完成／不可標示通過的項目
- 尚未在真實 Brave／Chrome／Edge 環境逐項操作搜尋、收藏、側邊抽屜、深淺色、字級調整、複製、列印、圖片放大、滑鼠滾輪、鍵盤切頁及全螢幕。
- 尚未對所有參考文獻逐筆做出版商原頁、Crossref／DOI resolver 的完整交叉核驗。
- Word／PDF 報告與預覽 PNG 等二進位檔尚未匯入本 Repository；本 Repository 目前以網站程式、Markdown、JSON、SVG、參考資料及工作流程文件為主。

## 可重跑的靜態檢查
在專案根目錄執行：
```bash
python 06_Project_Source/validate_project.py
```
需安裝 Node.js，供 `node --check` 檢查內嵌 JavaScript。

靜態檢查不等於真實瀏覽器互動驗收。若有錯誤，應先記錄、修正，再重新執行檢查。