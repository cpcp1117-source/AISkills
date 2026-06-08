---
name: investment-technical-analysis
description: "Analyze tradable assets such as crypto, stocks, indices, forex, or commodities with technical analysis and produce a standardized Traditional Chinese trading report. Use when Codex needs to evaluate current trend, support/resistance, RSI, EMA, MACD, Bollinger Bands, SMC structure, volume, entry/exit zones, long/short scenarios, invalidation levels, and probability estimates for an investment or trading target."
---

# Investment Technical Analysis

## Workflow

1. Identify the target asset, data timestamp, current price, exchange or market, quote currency, available price data, and requested timeframe.
2. If the user does not provide timeframe, use a medium-to-long swing trading view with `1H / 4H / 1D`.
3. If current price, candles, timeframe, or exchange are missing, first use available tools to fetch current data. If data cannot be fetched, ask for the missing data instead of inventing levels.
4. Decide the quick card first: direction, action, current location, main scenario, invalidation, and whether a trade is allowed.
5. Use indicators as evidence in this order: price structure and support/resistance > EMA / SMC > volume > RSI / MACD / BOLL.
6. Read `references/report-template.md` and output a concise decision-first report in that format.
7. Write in Traditional Chinese unless the user asks for another language.

## Decision Rules

- Start with the useful decision, not the indicator list. The first 5-10 lines must answer: bias, action, current location, main scenario, invalidation, and entry status.
- Classify status as one of: `偏多`, `偏空`, `震盪`, `等待突破`, `等待回踩`.
- Classify action as one of: `可做多`, `可做空`, `等回踩`, `等反彈`, `不進場`.
- Use exact levels or ranges. Prefer ranges for zones, such as `77K-77.5K`, when liquidity or reaction areas are not a single price.
- List at most 3 upside levels and 3 downside levels unless the user asks for a full map.
- Provide one primary direction by default. For the opposite direction, give only the trigger condition unless it is also immediately actionable.
- Include trade probability only when a concrete setup exists with entry, take profit, stop loss or invalidation, and acceptable risk/reward.
- If conditions are weak, write `判斷不進場` and explain the missing trigger.
- If data quality is poor or current data is unavailable, write `資料不足，不能給明確進場` and ask for the minimum missing data.

## Evidence Rules

- Use support/resistance and market structure as the primary source of direction.
- Use EMA and SMC to confirm trend, pullback zones, invalidation, liquidity, BOS, CHoCH, order blocks, fair value gaps, premium/discount, and equal highs/lows.
- Use volume to confirm or warn: breakout volume, absorption, divergence, low-volume grind, or climax rejection.
- Use RSI, MACD, and BOLL only as secondary evidence. Do not create a trade direction from these indicators alone.
- Avoid financial certainty. Probability estimates are technical-condition estimates, never guaranteed outcomes.

## Output Guidance

- Start directly with the report card. Do not explain the process unless the user asks.
- Keep the tone similar to trader notes: concise, concrete, and decision-oriented.
- Use the user's asset naming style when possible, such as `BTC`, `ETH`, `TSLA`, or `台積電`.
- Always show data timestamp, current price, and timeframe near the top.
- For daily automation, produce one compact card per asset. BTC and ETH should be separate cards.
- If data is incomplete but enough for a conditional view, clearly label assumptions.
- If current market data is unavailable, do not invent live prices. Ask for the current price or candle data needed to produce levels.

## Discord Delivery

- For Discord delivery, first produce the full report text, then send that exact text with `scripts/send_discord_webhook.py`.
- Read the Discord webhook URL from the `DISCORD_WEBHOOK_URL` environment variable. Never write the webhook URL into prompts, skill files, reports, or git-tracked files.
- Use a temporary UTF-8 text file as input, especially for Traditional Chinese reports on Windows PowerShell:
  - `python scripts/send_discord_webhook.py --file report.txt`
- Avoid piping Chinese text from PowerShell into native Python because the pipe can use a legacy code page and turn non-ASCII text into `????`.
- If the webhook is missing or sending fails, report the failure reason and preserve the report content. Do not say the Discord send succeeded unless the script succeeds.
