---
title: "The Discounted Cash Flow Model: A Framework for Traders"
description: "A practical introduction to DCF valuation for both day traders and long-term investors, covering core mechanics, real-world application, and key limitations."
difficulty: Intermediate
tags: [Valuation, DCF, Trading, Fundamental Analysis]
---
# The Discounted Cash Flow Model: A Framework for Traders

## 1. What Is A DCF?
A DCF or Discounted Cash Flow Model is an intrinsic valuation method, meaning it measures the value of a company based on its fundamentals (historical financials, market outlook, management efficacy etc...) rather than looking at a stock price. A DCF in essence measures the present value of future cash flows of a company. The product of a DCF is a company's enterprise value (EV), the total value of a company. But, what does that mean? In this article we will dive into that as well as do a real life DCF with Apple, by the end you will be able to build your own basic DCF and understand how to use it both for short or long term investments.

## 2. Core Concepts
### The Time Value of Money 
The most important concept in a DCF is the Time Value of Money. The Time Value of Money is boiled down into the famous saying, "A $1 today is worth more than $1 tomorrow." But why? Let's use this example: you borrow $1000 from a close friend with no interest to be repaid in a year. You might have intended to use this money to pay rent, but if you were to put this into a government bond yielding 5%, you could return the $1000 a year later and pocket the $50 of interest you made on the 5%. In this example, $1000 today is worth the same as $1050 a year from today. Therefore, a $1 today is worth more than $1 tomorrow.

### Discount Rate (WACC)
The Discount rate is the rate at which we discount cash flows back to present value. The Discount Rate goes hand in hand with the Time Value of Money, in the example above where you borrow $1000 from your friend, we assumed that you could invest it into a government bond at 5%. This is the discount rate. We got to the conclusion that $1000 Today = $1050 in 1 year using the government bond rate (discount rate) of 5%. But, this number could be anything. We could assume you invest it into the S&P500 which returns ~7% annually. In that example our discount rate would be 7%, so $1000 today = $1070 in 1 Year.

### Enterprise Value (EV)
Enterprise Value (EV) is the intrinsic value of the entire company. The easiest way to understand this is using a house as an example. Say you buy a house for $100k, and put down $20k as a down payment and finance the other $80k with debt. The Enterprise value is $100k, the total value of the house. While the equity value would be $20k, because that's the part of the house you actually own, while the remaining $80k is debt. When the DCF is complete, the value we get is the EV (The whole house).

### Free Cash Flow (FCF) 
In a DCF it is most common to us unlevered free cash flow (UFCF). In simple terms, it is the profit that a company makes from its core operations before paying off an debt. But why specifically UFCF? In a DCF we are "solving" for enterprise value (EV), so we have to account for profit that is attributable to both debt and equity holders. The equation for UFCF is below.

$$
UFCF = EBIT \times (1 - t) + DA - CapEx - \Delta NWC
$$

**Where:**
- **EBIT** — Earnings Before Interest & Taxes (operating profit before financing costs)
- **t** — Tax rate
- **DA** — Depreciation & Amortization *(a car loses value each year = depreciation)*
- **CapEx** — Capital Expenditures *(e.g., buying an office building)*
- **ΔNWC** — Change in Net Working Capital *(Current Assets _minus_ Current Liabilities)*

### Terminal Value
The final core concept is the terminal value. In a DCF it is common to use unlevered free cash flows for 5-10 years in advance. But, in finance company's are immortal, that is we assume they will operate forever. So, if you discount 10 years of UFCF back to present value, you would have the value of owning the company over the next 10 years, but what about after that? That is where the Terminal Value comes in, there are two ways to calculate a company's value in perpetuity; The Multiples Method and The Gordon Growth Model. The Multiples Method is simple, you take the final year EBIDTA (earnings before interests, depreciation, taxes, amortization) and mulutiply it by a common industry multiple. You use this method for most companies, but especially those in high growth sectors like tech. 

$$
TV = EBITDA_n \times \text{Exit Multiple}
$$

The other method is the Gordon Growth Model, where you take the final year EBITDA, and use a long term growth rate, which is a percent greater than inflation, but less than GDP growth. Then you use the formula below, to find the value of this perpetual cash flow, which gives you it's terminal value.

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
### Step 1: Gather Historical Revenue/FCF data (10-K Filings, Financial Platforms)
All this data is publically available for every public company. To find this information search, "Company A Investor Report Quarter _" To complete a DCF you must find a company's FCF, which includes EBIT, Tax Rate, D&A, NWC, and Capital Expenditures. The first two appear on the company's income statement, while D&A and NWC appear on it's cash flow statement, and Capital Expenditures will be on the balance sheet.
### Step 2: Project FCF 5–10 years forward using a growth assumption
This is the part of the DCF that requires actual analysis. The growth rate you use largely determines what valuation you get. The market is an equilibrium, it has its own projected growth rate, and if you use the same one, you will find that your result will match that of the markets. So, this is where research and analysis comes into play, are you more bullish on this company than the market? Less bullish? Why? What aspect of the current geopolitical climent, what expectation of the company do you think is too high or low, or any other reason you have that this company will perform differently than the market expects. You must have some perceived edge over the market for the DCF to yield either a buy or sell, and this is where it comes into play.
- Step 3: Calculate WACC
- Step 4: Calculate Terminal Value
**Terminal Value (Gordon Growth Model):**

$$
TV = \frac{FCF_n \times (1 + g)}{r - g}
$$

  where $g$ = long-term growth rate

- Step 5: Discount FCF's and Terminal Value back to Present value using WACC
  - **Discount factor for a given year:**

$$
\text{Discount Factor}_t = \frac{1}{(1 + r)^t}
$$
- Step 6: Sum our discounted cash flows

## 4. Case Studies
- Walk through of a real company simple:



- **Sensitivity table idea**: grid showing valuation output across discount rate (rows, 8–12%) vs. growth rate (columns, 1–4%) combinations

## 6. Practical Applications
- Sensitivity to assumptions; doesn't account for timing; less reliable for pre-revenue/volatile names
- **Day traders**: DCF as a contextual filter — is this stock fundamentally overextended? — not a direct entry/exit signal; pair with technicals
- **Long-term traders**: DCF supports conviction-building, position sizing, and a fair value anchor during volatility

## 7. Further Reading
- Link to related internal articles 
- Point to a downloadable DCF template or platform calculator if available
