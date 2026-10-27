# CadLISP 工具索引

AutoCAD 製圖工具集，共 **22 個獨立工具、25 個公開指令**。每個工具各有原始碼、繁體中文 README、MIT LICENSE、已知問題及自己的版本紀錄。

依需求選取工具並下載該儲存庫的 ZIP，以 APPLOAD 單獨載入。指令名稱與檔名可能不同，請以各工具 README 為準。

程式與文件採 **MIT**，署名 `Copyright (c) 2026 whos-dwg`。各工具目前完成來源與文件靜態核對，**AutoCAD 實機回歸尚待完成**。INCBLOCK、CV2D、SMARTIMPORT 有已列出的原碼問題，使用前先閱讀其已知問題。

[尺寸與註解](#尺寸與註解) · [幾何處理](#幾何處理) · [配置與圖層](#配置與圖層) · [屬性與編號](#屬性與編號) · [匯入與詳圖](#匯入與詳圖)

## 尺寸與註解

| 工具 | 指令 | 下載 | 狀態 |
| --- | --- | --- | --- |
| [FCL 與 FFL 標高標記](https://github.com/whos-dwg/CadLISP-CLL) | `CLL` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-CLL/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [純數字標高標記](https://github.com/whos-dwg/CadLISP-CLN) | `CLN` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-CLN/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [線性尺寸接續標註](https://github.com/whos-dwg/CadLISP-DLX) | `DLX` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-DLX/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [尺寸等分文字](https://github.com/whos-dwg/CadLISP-EQNUM) | `EQNUM` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-EQNUM/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [夾點連續尺寸](https://github.com/whos-dwg/CadLISP-GPDIM) | `GPDIM` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-GPDIM/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [填充線面積欄位與分色](https://github.com/whos-dwg/CadLISP-H2A) | `H2A` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-H2A/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [連續多重引線與對齊](https://github.com/whos-dwg/CadLISP-MML) | `MML` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-MML/archive/refs/heads/main.zip) | 實機回歸待完成 |

## 幾何處理

| 工具 | 指令 | 下載 | 狀態 |
| --- | --- | --- | --- |
| [聚合線轉換與標高歸零](https://github.com/whos-dwg/CadLISP-CV2D) | `CV2D` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-CV2D/archive/refs/heads/main.zip) | 需先修正原碼問題 |
| [兩曲線間插值](https://github.com/whos-dwg/CadLISP-LOFTLINES) | `LOFTLINES` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-LOFTLINES/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [多點與交點切割](https://github.com/whos-dwg/CadLISP-MBP-MBI) | `MBP` / `MBI` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-MBP-MBI/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [多群組外輪廓](https://github.com/whos-dwg/CadLISP-Outline) | `OUTLINE` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-Outline/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [單條聚合線簡化](https://github.com/whos-dwg/CadLISP-PLS) | `PLS` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-PLS/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [批次聚合線簡化](https://github.com/whos-dwg/CadLISP-PLSM) | `PLSM` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-PLSM/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [SPLINE 批次轉聚合線](https://github.com/whos-dwg/CadLISP-S2P) | `S2P` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-S2P/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [同層同長度斜線選取](https://github.com/whos-dwg/CadLISP-SXX) | `SXX` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-SXX/archive/refs/heads/main.zip) | 實機回歸待完成 |

## 配置與圖層

| 工具 | 指令 | 下載 | 狀態 |
| --- | --- | --- | --- |
| [跨視埠比例複製註解](https://github.com/whos-dwg/CadLISP-CHSC) | `CHSC` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-CHSC/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [依命令自動分層](https://github.com/whos-dwg/CadLISP-LayerDirector) | `LDON` / `LDOFF` / `LDM` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-LayerDirector/archive/refs/heads/main.zip) | 實機回歸待完成 |
| [配置頁籤批次編號](https://github.com/whos-dwg/CadLISP-LAYSEQ) | `LAYSEQ` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-LAYSEQ/archive/refs/heads/main.zip) | 實機回歸待完成 |

## 屬性與編號

| 工具 | 指令 | 下載 | 狀態 |
| --- | --- | --- | --- |
| [圖塊屬性尾碼遞增](https://github.com/whos-dwg/CadLISP-IncBlock) | `INCBLOCK` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-IncBlock/archive/refs/heads/main.zip) | 需先修正原碼問題 |
| [視埠比例寫入與檢核](https://github.com/whos-dwg/CadLISP-VP2BlkScale) | `VP2BLKSCALE` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-VP2BlkScale/archive/refs/heads/main.zip) | 實機回歸待完成 |

## 匯入與詳圖

| 工具 | 指令 | 下載 | 狀態 |
| --- | --- | --- | --- |
| [PDF 底圖與填滿匯入](https://github.com/whos-dwg/CadLISP-SmartImport) | `SMARTIMPORT` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-SmartImport/archive/refs/heads/main.zip) | 需先修正原碼問題 |
| [放大圖框與索引](https://github.com/whos-dwg/CadLISP-TBX) | `TBX` | [下載 ZIP](https://github.com/whos-dwg/CadLISP-TBX/archive/refs/heads/main.zip) | 實機回歸待完成 |

## 開始使用

1. 進入需要的工具儲存庫，閱讀相依圖塊、屬性 Tag、單位及操作空間要求。
2. 下載 ZIP 並完整解壓縮；先開啟測試圖面。
3. 依既有 AutoCAD 安全政策設定受信任位置，使用 APPLOAD 載入 lsp/ 中的程式。
4. 輸入工具 README 所列指令，檢查結果再加入日常製圖環境。

MBP／MBI 由同一支程式提供，因此放在同一儲存庫。其他工具各自維護版本、Issues 與下載內容，不必一起升版。建議各工具設定共同 Topic `cadlisp-tools`，方便搜尋。

## 回報問題

在對應工具儲存庫的 Issues 回報，提供 AutoCAD 完整版本、介面語言、命令列錯誤與去識別的最小重現圖面。不要上傳未公開的客戶圖面。

## 來源與授權

維護者已確認這 22 支為自行從零撰寫，或以 AI 協作從零開發。AutoLabel 與 AQE 未收錄於這批工具。程式與新撰文件採 [MIT 授權](LICENSE)；既有 GIF 的媒體範圍列於各工具 assets/NOTICE.md。

README 編排參考 [awesome-readme](https://github.com/matiassingers/awesome-readme)，使用清楚的用途、快速開始、功能索引、操作示範與來源資訊。
