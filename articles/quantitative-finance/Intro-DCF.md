---
title: "The Discounted Cash Flow Model: A Framework for Traders"
description: "A practical introduction to DCF valuation for both day traders and long-term investors, covering core mechanics, real-world application, and key limitations."
difficulty: Intermediate
tags: [Valuation, DCF, Trading, Fundamental Analysis]
---
# The Discounted Cash Flow Model: A Framework for Traders

## 1. What Is A DCF?
A DCF, or Discounted Cash Flow Model, is an intrinsic valuation method, meaning it measures the value of a company based on its fundamentals (historical financials, market outlook, management efficacy, etc.) rather than looking at a stock price. A DCF, in essence, measures the present value of future cash flows of a company. The product of a DCF is a company's enterprise value (EV), the total value of a company. But what does that mean? In this article we will dive into that, as well as do a real-life DCF with Apple. By the end, you will be able to build your own basic DCF and understand how to use it both for short- or long-term investments.

## 2. Core Concepts
### The Time Value of Money 
The most important concept in a DCF is the Time Value of Money. The Time Value of Money is boiled down into the famous saying, "$1 today is worth more than $1 tomorrow." But why? Let's use this example: you borrow $1000 from a close friend with no interest, to be repaid in a year. You might have intended to use this money to pay rent, but if you were to put this into a government bond yielding 5%, you could return the $1000 a year later and pocket the $50 of interest you made on the 5%. In this example, $1000 today is worth the same as $1050 a year from today. Therefore, $1 today is worth more than $1 tomorrow.

### Discount Rate
The discount rate is the rate at which we discount cash flows back to present value. The discount rate goes hand in hand with the Time Value of Money. In the example above where you borrow $1000 from your friend, we assumed that you could invest it into a government bond at 5%. This is the discount rate. We got to the conclusion that $1000 today = $1050 in 1 year using the government bond rate (discount rate) of 5%. But this number could be anything. We could assume you invest it into the S&P 500, which returns ~7% annually. In that example our discount rate would be 7%, so $1000 today = $1070 in 1 year.

### Enterprise Value (EV)
Enterprise Value (EV) is the intrinsic value of the entire company. The easiest way to understand this is using a house as an example. Say you buy a house for $100k, and put down $20k as a down payment and finance the other $80k with debt. The Enterprise Value is $100k, the total value of the house. The equity value would be $20k, because that's the part of the house you actually own, while the remaining $80k is debt. When the DCF is complete, the value we get is the EV (the whole house).

### Free Cash Flow (FCF) 
In a DCF it is most common to use unlevered free cash flow (UFCF). In simple terms, it is the profit that a company makes from its core operations before paying off any debt. But why specifically UFCF? In a DCF we are "solving" for Enterprise Value (EV), so we have to account for profit that is attributable to both debt and equity holders. The equation for UFCF is below.

$$
UFCF = EBIT \times (1 - t) + DA - CapEx - \Delta NWC
$$

**Where:**
- **EBIT** — Earnings Before Interest & Taxes (operating profit before financing costs)
- **t** — Tax rate
- **DA** — Depreciation & Amortization *(a car loses value each year = depreciation)*
- **CapEx** — Capital Expenditures *(e.g., buying an office building)*
- **ΔNWC** — Change in Net Working Capital *(Current Assets minus Current Liabilities)*

### Terminal Value
The final core concept is the terminal value. In a DCF it is common to use unlevered free cash flows for 5-10 years in advance. But in finance, companies are immortal — that is, we assume they will operate forever. So, if you discount 10 years of UFCF back to present value, you would have the value of owning the company over the next 10 years, but what about after that? That is where the Terminal Value comes in. There are two ways to calculate a company's value in perpetuity: the Multiples Method and the Gordon Growth Model. The Multiples Method is simple: you take the final year EBITDA (earnings before interest, depreciation, taxes, amortization) and multiply it by a common industry multiple. You use this method for most companies, but especially those in high-growth sectors like tech. 

$$
TV = EBITDA_n \times \text{Exit Multiple}
$$

The other method is the Gordon Growth Model, where you take the final year EBITDA, and use a long-term growth rate, which is a percent greater than inflation, but less than GDP growth. Then you use the formula below, to find the value of this perpetual cash flow, which gives you its terminal value.

$$
TV = \frac{FCF_n \times (1 + g)}{r - g}
$$

**Where:**
- **TV** — Terminal Value
- **FCF_n** — Free Cash Flow in the final projected year (year *n*)
- **g** — Long-term growth rate
- **r** — Discount rate (e.g., WACC)
## 3. Mechanisms/Examples
Now, we will use what we have learned to go over the 6 steps to complete a DCF analysis. 

**Core DCF equation:**

$$
\text{DCF Value} = \sum_{t=1}^{n} \frac{FCF_t}{(1 + r)^t} + \frac{TV}{(1 + r)^n}
$$

  where $FCF_t$ = free cash flow in year $t$, $r$ = discount rate, $n$ = final projection year
### Step 1: Gather Historical Revenue/FCF Data (10-K Filings, Financial Platforms)
All this data is publicly available for every public company. To find this information, search "Company A Investor Report Quarter _." To complete a DCF, you must find a company's FCF, which includes EBIT, Tax Rate, D&A, NWC, and Capital Expenditures. The first two appear on the company's income statement, while D&A and NWC appear on its cash flow statement, and Capital Expenditures will be on the balance sheet.
### Step 2: Project FCF 5–10 Years Forward Using A Growth Assumption
This is the part of the DCF that requires actual analysis. The growth rate you use largely determines what valuation you get. The market is an equilibrium; it has its own projected growth rate, and if you use the same one, you will find that your result will match that of the market. So, this is where research and analysis come into play. Are you more bullish on this company than the market? Less bullish? Why? What aspect of the current geopolitical climate, what expectation of the company do you think is too high or low, or any other reason you have that this company will perform differently than the market expects. You must have some perceived edge over the market for the DCF to yield either a buy or sell, and this is where it comes into play.
### Step 3: Calculate Weighted Average Cost of Capital (WACC)
So far, we have calculated the future cash flows of a company, but a DCF is the *discounted* cash flows of a company. This is where WACC comes into play. WACC is the discount rate used for a DCF, but what is it conceptually? WACC is the average cost a company uses to finance its assets. An easy way to think about it is: what is the average expected return on a $1 investment in the company for both equity and debt holders. So, we must calculate how much debt and equity are used in the company's capital structure, then calculate the cost of each. For debt, it is simple: just the interest rate used for the debt and preferred stock. The cost of equity is a bit more complicated. The formula is below.   

**Weighted Average Cost of Capital (WACC):**

$$
WACC = r_d \cdot w_d + r_e \cdot w_e + r_p \cdot w_p
$$

**Where:**
- $r_d$ — Cost of debt
- $w_d$ — Weight of debt in capital structure
- $r_e$ — Cost of equity
- $w_e$ — Weight of equity in capital structure
- $r_p$ — Cost of preferred stock
- $w_p$ — Weight of preferred stock in capital structure  

**Cost of Equity (CAPM)**

$$
r_e = r_f + \beta \cdot (r_m - r_f)
$$

**Where:**
- $r_e$ — Cost of equity
- $r_f$ — Risk-free rate
- $\beta$ — Beta (stock's volatility relative to the market)
- $r_m$ — Expected market return
- $(r_m - r_f)$ — Equity risk premium

### Step 4: Calculate Terminal Value
As discussed before, there are two ways to calculate the terminal value of a company: the Multiples Method and the Gordon Growth Model. It is important to think about when to use which: if it is a stable company with predictable cash flows, use the Gordon Growth Model because it assumes steady cash flows. For any other business, use the Multiples Method. Below is the equation for the Gordon Growth Model:

**Terminal Value (Gordon Growth Model):**

$$
TV = \frac{FCF_n \times (1 + g)}{r - g}
$$

  where $g$ = long-term growth rate

### Step 5: Discount FCFs and Terminal Value Back to Present Value Using WACC
Now, we will take each of our cash flows and discount them back to present value. Then take our terminal value and discount that back to present value as well.
  - **Discount factor for a given year:**

$$
\text{Discount Factor}_t = \frac{1}{(1 + r)^t}
$$
### Step 6: Sum Our Discounted Cash Flows  
Add the discounted terminal value and the discounted cash flows, which will give you the total value of a company. Take that number and divide it by the number of shares to get the price per share.

## Enterprise Value & Price Per Share

Add the discounted terminal value and the discounted cash flows, which will give you the total value of a company. Take that number and divide it by the number of shares to get the price per share.

$$
EV = \sum_{i=1}^{n} \frac{FCF_i}{(1 + r)^i} + \frac{TV}{(1 + r)^n}
$$

$$
Price\ Per\ Share = \frac{EV}{Shares\ Outstanding}
$$

**Where:**
- $EV$ — Enterprise Value (total value of the company)
- $FCF_i$ — Free cash flow in year $i$
- $r$ — Discount rate (e.g., WACC)
- $n$ — Final projected year
- $TV$ — Terminal Value
- $Shares\ Outstanding$ — Total number of shares outstanding

## 4. Case Studies
## Simple DCF Example — SampleCo Inc.

### Key Assumptions

| Assumption | Value |
|---|---|
| Revenue, Year 0 ($mm) | 100 |
| Revenue Growth Rate | 8.0% |
| EBITDA Margin | 25.0% |
| Tax Rate | 21.0% |
| Discount Rate (WACC) | 10.0% |
| Long-Term Growth Rate (g) | 2.5% |
| Shares Outstanding (mm) | 20.0 |

### 5-Year Free Cash Flow Projection

| ($ in millions) | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| Revenue | 108 | 117 | 126 | 136 | 147 |
| EBITDA | 27 | 29 | 31 | 34 | 37 |
| Less: Taxes | (6) | (6) | (7) | (7) | (8) |
| **Unlevered FCF** | **21** | **23** | **25** | **27** | **29** |

### Discounted Cash Flows

| | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
|---|---|---|---|---|---|
| PV of FCF | 19 | 19 | 19 | 18 | 18 |

### Terminal Value (Gordon Growth Method)

$$
TV = \frac{FCF_5 \times (1 + g)}{WACC - g}
$$

| | ($mm) |
|---|---|
| Terminal Value | 397 |
| PV of Terminal Value | 246 |

### Valuation Summary

| | ($mm) |
|---|---|
| Sum of PV of FCF | 93 |
| PV of Terminal Value | 246 |
| **Enterprise Value** | **340** |
| Shares Outstanding (mm) | 20.0 |
| **Implied Price Per Share** | **$16.99** |

### Sensitivity Table: Price Per Share
*Rows = Discount Rate (WACC), Columns = Long-Term Growth Rate (g)*

| WACC \ g | 1.0% | 2.0% | 3.0% | 4.0% |
|---|---|---|---|---|
| 8.0% | 19.19 | 21.73 | 25.28 | 30.61 |
| 9.0% | 16.71 | 18.54 | 20.99 | 24.42 |
| 10.0% | 14.79 | 16.16 | 17.93 | 20.29 |
| 11.0% | 13.25 | 14.31 | 15.64 | 17.34 |
| 12.0% | 11.99 | 12.83 | 13.86 | 15.14 |

## 5. Practical Applications And Limitations
- **Day traders**: DCF should be used as a contextual filter to answer the question: is this stock fundamentally overextended? This is not a direct exit/entry signal — it should be combined with technical analysis to form a better investment thesis.
- **Long-term traders**: DCF supports conviction-building, position sizing, and a fair value anchor during volatility. It can show whether a company's current stock price is too high or too low based on your assumptions.
- There are limitations to a DCF. The most common one is that it is highly based on assumption — the growth rate, the terminal value, and even the discount rate are all based on assumptions. It is also highly unpredictable for companies that are highly volatile or don't have consistent cash flows. However, it is the most common intrinsic valuation method for companies and is a great tool for everyday traders.
