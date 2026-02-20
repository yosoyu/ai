# Stock Analysis Framework - Detailed Guide

---

## Phase 1: Data Collection & Verification

**Objective:** Gather all relevant data and verify key facts

### Steps

| Step | Skill | Task | Output |
|------|-------|------|--------|
| 1.1 | `/pdf` | Extract key information from annual reports | Key findings summary |
| 1.2 | `/yahoo-finance` | Fetch latest stock price, financials, dividends | Financial data |
| 1.3 | `/tushare-finance` | Get market context and peer comparison | Peer comparison |

### Key Questions
- What are the key risks disclosed in annual reports?
- What is the current valuation (P/E, P/B, EV/EBITDA)?
- Who are the main competitors?
- What is the 52-week price range?
- What is the dividend history?

### Data Sources
- **HKEX News**: https://www1.hkexnews.hk
- **Yahoo Finance**: https://finance.yahoo.com
- **SEC EDGAR** (US stocks): https://www.sec.gov
- **CNIPA** (Chinese patents): https://pss-system.cponline.cnipa.gov.cn
- **NMPA** (Chinese pharma): https://www.nmpa.gov.cn

---

## Phase 2: Fundamental Analysis

**Objective:** Understand the business and financial health

### Steps

| Step | Skill | Task | Output |
|------|-------|------|--------|
| 2.1 | `/stock-analysis` | Comprehensive fundamental analysis | Business overview |
| 2.2 | `/finance-expert` | Deep dive into financial statements | Financial health report |
| 2.3 | `/market-sizing-analysis` | Analyze market size & growth | Market analysis |

### Key Questions
- How does the company make money? (Business model)
- What is the competitive moat? (Brand, scale, network effects, switching costs)
- Is the balance sheet healthy? (Debt levels, cash position)
- What is the ROE trend? (5-year history)
- What are the growth drivers?

### Financial Metrics to Analyze
- **Profitability**: Gross margin, operating margin, net margin, ROE, ROA
- **Liquidity**: Current ratio, quick ratio, cash position
- **Leverage**: Debt/Equity, interest coverage
- **Efficiency**: Asset turnover, inventory turnover
- **Growth**: Revenue CAGR, earnings CAGR

---

## Phase 3: Risk Assessment

**Objective:** Identify and evaluate all risks

### Steps

| Step | Skill | Task | Output |
|------|-------|------|--------|
| 3.1 | `/stock-research-executor` | Research governance, regulatory, operational risks | Risk research |
| 3.2 | `/stock-question-refiner` | Refine key risk questions | Prioritized risk list |
| 3.3 | `/scan` | Compare with competitors | Competitive analysis |

### Key Questions
- What could go wrong? (Invert, always invert)
- Are there governance red flags? (Related party transactions, privatization attempts)
- What is the regulatory environment?
- How does this compare to peers?
- What is the customer/supplier concentration?

### Risk Categories
1. **Governance Risk** - Management integrity, shareholder friendliness
2. **Business Risk** - Competition, disruption, obsolescence
3. **Financial Risk** - Debt, liquidity, cash flow
4. **Regulatory Risk** - Government policy, legal issues
5. **Concentration Risk** - Customer, supplier, product

---

## Phase 4: Investment Decision

**Objective:** Synthesize findings into an investment thesis

### Steps

| Step | Skill | Task | Output |
|------|-------|------|--------|
| 4.1 | `/analyze` | Synthesize all findings | Investment thesis |
| 4.2 | `/trading-analysis` | Determine entry/exit points | Trading plan |
| 4.3 | `/brief` | Create investment summary | Executive summary |

### Key Questions
- What is the intrinsic value? (DCF, NAV, sum-of-parts)
- What is the margin of safety?
- What would trigger a buy/sell decision?
- What is the expected return? (1-year, 3-year, 5-year)
- Who should/shouldn't invest?

### Valuation Methods
1. **DCF** - Discounted cash flow (for growth companies)
2. **NAV** - Net asset value (for property, investment companies)
3. **P/E Comparison** - Relative to history and peers
4. **Sum-of-Parts** - For conglomerates
5. **Liquidation Value** - For distressed companies

### Investment Rating Scale
| Rating | Recommendation | Description |
|--------|----------------|-------------|
| 8.0+ | Strong BUY | Wonderful company at fair price |
| 7.0-7.9 | BUY | Quality at reasonable price |
| 6.0-6.9 | SPECULATIVE BUY | Requires active monitoring |
| 5.0-5.9 | HOLD | Wait for better price or clarity |
| <5.0 | AVOID | Disqualifying factors present |

---

## Phase 5: Final Report

**Objective:** Create final deliverables and validate

### Steps

| Step | Skill | Task | Output |
|------|-------|------|--------|
| 5.1 | `/review` | Review and validate analysis | Review notes |
| 5.2 | `/pdf` or `/pptx` | Generate final report | Final report |

### Report Components
1. **Executive Summary** - Key metrics, recommendation, rating
2. **Investment Thesis** - Bull case and bear case
3. **Valuation Analysis** - Intrinsic value, margin of safety, scenarios
4. **Risk Assessment** - All risks with severity and probability
5. **Action Items** - Entry points, stop loss, take profit levels
6. **Who Should Invest** - Suitable vs not suitable investors
7. **Data Sources** - All sources used with links

---

## Progress Tracking

Use `progress.json` to track completion:

```json
{
  "stock": "XXXX.HK",
  "company": "Company Name",
  "start_date": "YYYY-MM-DD",
  "phases": {
    "phase1": {"status": "pending", "completed_date": null},
    "phase2": {"status": "pending", "completed_date": null},
    "phase3": {"status": "pending", "completed_date": null},
    "phase4": {"status": "pending", "completed_date": null},
    "phase5": {"status": "pending", "completed_date": null}
  },
  "current_phase": 1
}
```

---

*Framework Version: 1.0*
