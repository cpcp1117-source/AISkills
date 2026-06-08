# Technical Analysis Report Template

Use this decision-first template for investment technical analysis reports. Match the user's requested language, defaulting to Traditional Chinese.

```text
{M/D} {標的}｜{視角，例如：中長線 1H / 4H / 1D}
資料時間：{資料時間與時區}
目前價格：{價格}

快速結論：
方向：{偏多 / 偏空 / 震盪 / 等待突破 / 等待回踩}
操作：{可做多 / 可做空 / 等回踩 / 等反彈 / 不進場}
目前位置：{價格}，靠近{壓力 / 支撐 / 中性區}
主劇本：{守住/跌破/突破} {關鍵區間} 則看 {目標區}
失效條件：{跌破/突破} {失效價位或區間}

關鍵價位：
上方關注：{壓力1}、{壓力2}、{壓力3}
下方關注：{支撐1}、{支撐2}、{支撐3}

技術依據：
結構：{趨勢 / 區間 / SMC 結構重點}
均線：{EMA 狀態與關鍵共振}
動能：{RSI / MACD / BOLL 重點，只列影響判斷者}
量能：{成交量確認或警訊}

交易方向與勝率預估：
做多：{進場 / 止盈 / 止損 / 勝率，或判斷不進場與原因}
做空：{進場 / 止盈 / 止損 / 勝率，或觸發條件 / 判斷不進場與原因}
```

## Conditional Wording

- If a trade is not attractive, use: `{方向} : 判斷不進場，原因：{缺少觸發/風險報酬不足/位置不佳/指標未共振}`.
- If only a conditional setup exists, use: `{方向} : 等待 {條件} 後再評估，預估勝率 {百分比}`.
- If data is insufficient, use: `資料不足，不能給明確進場；需要 {目前價格/K線/時間週期/交易所}`.
- If live data is unavailable, ask for the current price or candle data instead of filling template levels with guesses.

## Automation Constraints

- For BTC/ETH daily automation, produce one card per asset.
- Keep each card compact enough that the first 5-10 lines show direction, action, current location, main scenario, and invalidation.
- Show no more than 3 upside and 3 downside levels per asset.
- Give one primary direction by default; the opposite direction should be a trigger condition unless immediately actionable.
