# RL Trading Agents (Foundations)

Reinforcement learning (RL) trains an **agent** to take actions in an environment to maximize a reward. In trading, RL is attractive because it directly optimizes decisions (buy/sell/hold, sizing), but it is easy to build unrealistic environments and get misleading results.

## Key Terms

- **Agent**: the decision-maker.
- **Environment**: the market simulation the agent interacts with.
- **State**: what the agent observes (prices, indicators, inventory, risk).
- **Action**: what the agent can do (position size, enter/exit, do nothing).
- **Reward**: the score the agent tries to maximize (PnL minus costs/penalties).
- **Episode**: one run (e.g., one year of trading or one trade lifecycle).

## A Minimal Trading RL Setup

### State (keep it simple)

- Recent returns (e.g., last 20 days)
- Volatility estimate
- Current position (flat/long/short) and exposure

### Actions (avoid complexity at first)

- `{-1, 0, +1}` for short/flat/long, or a small set of position sizes.

### Reward (be careful)

- Daily reward: `PnL - costs - risk_penalty`
- Add penalties for:
  - high turnover
  - high leverage
  - large drawdowns

## What Can Go Wrong

- **Look-ahead leakage**: you accidentally feed future prices in the state.
- **Unrealistic fills**: trades execute at mid-price with no spread or slippage.
- **Overfitting to one period**: the agent learns “2021 crypto” and fails elsewhere.
- **Reward hacking**: agent exploits loopholes (e.g., taking infinite leverage if not capped).

## How to Evaluate RL Fairly

- Compare to simple baselines:
  - buy-and-hold
  - moving-average filter
  - volatility targeting
- Use walk-forward evaluation.
- Report:
  - net returns after costs
  - drawdowns
  - turnover
  - exposure time (how often it trades)

## First-Phase Advice (Maintainable)

Start with an environment you can fully explain and test. If you can’t describe why the reward is correct and why the fills are realistic, the RL results won’t survive contact with live markets.
