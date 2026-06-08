# Codex Skill 呼叫流程

> 目的：依照目前已安裝與常用的 skill，快速判斷任務應呼叫哪個 skill，以及多個 skill 需要串接時的順序。

## 1. 目前已安裝的個人 Skills

| Skill | 主要用途 | 典型呼叫 |
|---|---|---|
| `app-tool-development-workflow` | 規劃、開發、測試、交付與維護 app、工具、CLI、自動化、dashboard、API | `$app-tool-development-workflow` |
| `investment-technical-analysis` | 對 crypto、股票、指數、外匯、商品做技術分析並產出繁體中文交易報告 | `$investment-technical-analysis` |
| `pm-meeting-notes` | 將 PM、產品、專案、跨部門會議記錄整理成決策、action items、風險與待確認事項 | `$pm-meeting-notes` |
| `system-specification` | 建立系統規格、SRS、技術規格、架構、API、資料模型、驗收條件與 traceability matrix | `$system-specification` |
| `trade-plan-review` | 建立或審查交易計畫、交易系統、進出場、SL/TP、風險與復盤 | `$trade-plan-review` |
| `pdf` | 讀取、建立、審查 PDF，尤其是版面渲染與視覺驗證重要時 | `$pdf` |
| `playwright` | 用真實瀏覽器做導覽、表單操作、截圖、資料擷取、UI flow debug | `$playwright` |

## 2. 系統與管理 Skills

| Skill | 主要用途 | 典型呼叫 |
|---|---|---|
| `imagegen` | 產生或修改點陣圖片、插圖、素材、mockup、透明背景 cutout | `$imagegen` |
| `openai-docs` | 查 OpenAI / Codex 官方文件、模型、API 用法與升級指引 | `$openai-docs` |
| `skill-creator` | 建立或更新 Codex skill | `$skill-creator` |
| `skill-installer` | 安裝 Codex skill | `$skill-installer` |
| `plugin-creator` | 建立或更新 Codex plugin | `$plugin-creator` |

## 3. 任務類型對照表

| 任務 | 優先呼叫 | 備註 |
|---|---|---|
| 從想法建立新 app、工具、CLI、自動化流程 | `$app-tool-development-workflow` | 先產出 brief、spec、technical design、tasks、README、驗收清單 |
| 建立正式系統規格或技術文件 | `$system-specification` | 適合 SRS、API、資料模型、架構、NFR、驗收條件 |
| 整理會議記錄與待辦 | `$pm-meeting-notes` | 適合 transcript、逐字稿、粗略筆記、會議摘要 |
| 建立或審查交易計畫 | `$trade-plan-review` | 適合交易策略、進場、停損、停利、風控、復盤 |
| 對交易標的做技術分析報告 | `$investment-technical-analysis` | 適合 BTC、ETH、股票、指數、外匯、商品 |
| 處理 PDF | `$pdf` | 需要讀取內容、產 PDF、檢查版面時使用 |
| 操作網頁或驗證 UI | `$playwright` | 需要真實瀏覽器、截圖、表單、flow debug 時使用 |
| 查 OpenAI / Codex 最新官方文件 | `$openai-docs` | 只依官方文件確認 |
| 建立新 skill | `$skill-creator` | 修改或新增 skill 時使用 |
| 安裝 skill | `$skill-installer` | 從 curated list、GitHub 或本機安裝時使用 |

## 4. 常見串接流程

### 4.1 新工具 / App 開發

1. `$app-tool-development-workflow`：釐清需求、成功條件、文件組與任務。
2. `$system-specification`：將需求整理成系統規格、功能需求、NFR、API、資料模型與驗收條件。
3. 實作開發。
4. `$playwright`：若有 UI，進行瀏覽器截圖與流程驗證。
5. `$pdf`：若需要輸出 PDF 文件或報告，再進行版面驗證。

### 4.2 會議轉開發任務

1. `$pm-meeting-notes`：整理會議決策、action items、風險與 open questions。
2. `$app-tool-development-workflow`：轉成開發流程與任務拆解。
3. `$system-specification`：補齊正式規格與驗收條件。

### 4.3 交易分析與交易計畫

1. `$investment-technical-analysis`：產出標的技術分析報告。
2. `$trade-plan-review`：將分析轉成交易計畫或審查既有計畫。
3. `$pdf`：若需要輸出正式報告，再生成或檢查 PDF。

### 4.4 自動化交易 / 分析工具

1. `$trade-plan-review`：定義交易邏輯、風險、進出場條件與 no-trade 條件。
2. `$investment-technical-analysis`：定義分析輸出格式與資料需求。
3. `$app-tool-development-workflow`：規劃工具、任務、驗收與 README。
4. `$system-specification`：整理 API、資料模型、排程、錯誤處理與監控。

### 4.5 文件、報告與交付

1. 依內容選擇主 skill，例如 `$system-specification` 或 `$pm-meeting-notes`。
2. `$pdf`：需要 PDF 時負責生成、讀取或版面驗證。
3. 若文件要變成 app 或工具流程，再接 `$app-tool-development-workflow`。

## 5. 呼叫決策規則

- 任務是「我要做一個工具 / app / 自動化」：先用 `$app-tool-development-workflow`。
- 任務是「我要一份規格 / 架構 / API 文件」：用 `$system-specification`。
- 任務是「這是會議記錄，幫我整理」：用 `$pm-meeting-notes`。
- 任務是「幫我看交易計畫是否合理」：用 `$trade-plan-review`。
- 任務是「幫我分析 BTC / ETH / 股票技術面」：用 `$investment-technical-analysis`。
- 任務是「PDF 內容、排版或輸出」：用 `$pdf`。
- 任務是「需要打開網站、操作 UI、截圖」：用 `$playwright`。
- 任務是「OpenAI / Codex API 或模型最新用法」：用 `$openai-docs`。
- 任務是「新增或修改 skill」：用 `$skill-creator`。
- 任務是「安裝 skill」：用 `$skill-installer`。

## 6. 維護流程

新增或更新 skill 時：

1. 在工作區或 Codex skills 目錄中建立 / 更新 skill。
2. 確認 `SKILL.md` frontmatter 有 `name` 與 `description`。
3. 確認需要時有 `agents/openai.yaml`。
4. 若 skill 存在於工作區但要讓 Codex 直接呼叫，複製到：
   - `C:\Users\cpcp3\.codex\skills\<skill-name>`
5. 更新本文件的：
   - 已安裝 skill 清單
   - 任務類型對照表
   - 常見串接流程
6. 開新 Codex session 後確認 skill 是否出現在可用清單。

## 7. 最小驗收清單

- [ ] `C:\Users\cpcp3\.codex\skills` 中存在所有常用 skill。
- [ ] 每個 skill 目錄都有 `SKILL.md`。
- [ ] 每個 `SKILL.md` 都有 `name` 與 `description`。
- [ ] 本文件列出的呼叫名稱與 `SKILL.md` 的 `name` 一致。
- [ ] 常見任務能依本文件選到正確 skill。
