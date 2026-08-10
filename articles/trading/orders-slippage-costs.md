# Orders, Slippage, and Transaction Costs

Many “great” strategies disappear after realistic execution. This article explains the basics so your backtests and live trading match.

## Key Terms

- **Spread**: difference between best bid and best ask. Crossing the spread costs money.
- **Slippage**: getting a worse price than expected (fast markets, low liquidity, large orders).
- **Market impact**: your own orders moving the market price against you.
- **Liquidity**: how easily you can trade size without moving price.

## Order Types (Basics)

### Market Order

- **Pros**: fast execution, higher fill probability.
- **Cons**: you pay the spread and can get large slippage in volatile markets.

### Limit Order

- **Pros**: you control price, can reduce spread cost.
- **Cons**: you may not fill; queue priority matters.

### Stop / Stop-Limit

- Used for exits or risk control. Stops can trigger during fast moves and fill worse than you expect.

## Why Slippage Happens

- Spread widens during volatility and around news.
- Order book depth is limited; large orders “walk the book”.
- Latency and routing: by the time your order reaches the venue, price moved.

## How to Model Costs (Start Simple)

For a first pass:

- Add a fixed spread cost (e.g., 1–5 bps for liquid equities).
- Add a fee per trade.
- Add a slippage term proportional to volatility and position size:
  - larger size + higher vol = larger slippage.

## Practical Guidance

- Prefer lower turnover if your edge is small.
- If you must trade frequently, use stricter entry filters and realistic fill models.
- Always measure performance *after costs* and report turnover and average trade size.
