# Stock Analysis Framework v2.0

A systematic approach to analyze stocks using AI agent skills with **mandatory official source verification**.

---

## ⚠️ Critical Data Requirements

### Official Source Hierarchy

| Priority | Source Type | Examples | When to Use |
|----------|-------------|----------|-------------|
| **1 (Primary)** | Company IR/Filings | Company website, HKEX, SEC | ALL key financial data |
| **2 (Primary)** | Exchange Data | HKEX, NASDAQ, NYSE | Price, volume, market data |
| **3 (Secondary)** | Financial Databases | yfinance, Bloomberg, Reuters | Cross-verification only |
| **4 (Tertiary)** | Financial Portals | Yahoo Finance, Google Finance | Supplementary only |
| **5 (Context)** | News/Analysts | Media, broker reports | Context, not data source |

### Data Verification Rules

1. **ALL key metrics** (P/E, P/B, ROE, dividend yield) must be verified against **at least 2 sources**
2. **Primary source required** for: Revenue, Net Income, Book Value, EPS
3. **yfinance data MUST be cross-verified** - known to have errors (e.g., Alibaba P/B)
4. **Flag unverified data** with ⚠️ warning in analysis
5. **Document all sources** in progress.json

---

## Phase 1: Data Collection & Verification

**Objective:** Gather all relevant data and **verify against official sources**

### Step 1.1: Collect Raw Data

| Task | Tool | Output |
|------|------|--------|
| Fetch stock price, basic metrics | yfinance | Raw financial data |
| Extract annual report info | PDF reader | Key findings |
| Get peer comparison | Web search | Peer data |

### Step 1.2: VERIFY Data (NEW - MANDATORY)

| Data Point | Primary Source | Secondary Source | Action if Mismatch |
|------------|---------------|------------------|-------------------|
| **Price** | Exchange (HKEX/NASDAQ) | yfinance | Use exchange data |
| **P/E Ratio** | Company IR | yfinance, financial portal | Verify with company filings |
| **P/B Ratio** | Company filings (book value) | yfinance | **CALCULATE: Price / BVPS** |
| **ROE** | Annual report | yfinance | Use annual report |
| **Dividend Yield** | Company announcement | Exchange data | Verify ex-dividend date |
| **Revenue** | SEC 10-K / HKEX filing | yfinance | Use filing data |
| **Net Income** | SEC 10-K / HKEX filing | yfinance | Use filing data |

### Step 1.3: Document Sources

Add to progress.json:

```json
{
  "data_sources": {
    "primary": {
      "company_ir": "https://company.com/ir",
      "exchange_filings": "HKEX 00XXX",
      "annual_report": "FY2024 Annual Report"
    },
    "secondary": {
      "yfinance": "verified against primary",
      "financial_portal": "Xueqiu"
    },
    "verification_status": {
      "price": "verified",
      "pe_ratio": "verified",
      "pb_ratio": "verified",
      "dividend_yield": "verified"
    },
    "discrepancies_found": []
  }
}
```

---

## Phase 2: Fundamental Analysis

**Objective:** Understand the business and financial health

| Step | Task | Output |
|------|------|--------|
| 2.1 | Analyze business model | Revenue breakdown |
| 2.2 | Assess competitive moat | Moat analysis |
| 2.3 | Analyze financial statements | Financial health report |
| 2.4 | Calculate intrinsic value | Valuation analysis |

**Key Metrics to Calculate (not just fetch):**

| Metric | Formula | Verify Against |
|--------|---------|----------------|
| P/B Ratio | Price / Book Value Per Share | Company filing for BVPS |
| P/E Ratio | Price / EPS | Company filing for EPS |
| ROE | Net Income / Shareholders' Equity | Annual report |
| Dividend Yield | Annual Dividend / Price | Company announcement |
| Debt/Equity | Total Debt / Total Equity | Balance sheet |

---

## Phase 3: Risk Assessment

**Objective:** Identify and evaluate all risks

| Step | Task | Output |
|------|------|--------|
| 3.1 | Review risk factors from annual report | Risk list |
| 3.2 | Apply Munger's "Invert" thinking | Failure scenarios |
| 3.3 | Assess governance and management | Governance report |

---

## Phase 4: Investment Decision

**Objective:** Synthesize findings into an investment thesis

| Step | Task | Output |
|------|------|--------|
| 4.1 | Develop bull/bear cases | Scenario analysis |
| 4.2 | Apply Buffett-Munger criteria | Scorecard |
| 4.3 | Determine entry/exit points | Trading plan |

---

## Phase 5: Documentation & Review

**Objective:** Create final deliverables with verified data

| Step | Task | Output |
|------|------|--------|
| 5.1 | Write final report | phase5_final_report.md |
| 5.2 | Include source citations | Source section |
| 5.3 | Data verification checklist | Verification status |

---

## Output Files Structure

```
/analysis/
├── phase1_data_collection.md
├── phase2_fundamental_analysis.md
├── phase3_risk_assessment.md
├── phase4_investment_decision.md
├── phase5_final_report.md
├── progress.json
└── data_verification.md (NEW)
```

---

## Progress Tracking Template (v2.0)

```json
{
  "stock": "XXXX.HK",
  "company": "Company Name",
  "start_date": "2026-02-20",
  "phases": {
    "phase1": {"status": "pending", "completed_date": null},
    "phase2": {"status": "pending", "completed_date": null},
    "phase3": {"status": "pending", "completed_date": null},
    "phase4": {"status": "pending", "completed_date": null},
    "phase5": {"status": "pending", "completed_date": null}
  },
  "data_sources": {
    "primary": {
      "company_ir": null,
      "exchange_filings": null,
      "annual_report": null
    },
    "verification_status": {
      "price": "unverified",
      "pe_ratio": "unverified",
      "pb_ratio": "unverified",
      "dividend_yield": "unverified",
      "roe": "unverified"
    },
    "discrepancies_found": []
  },
  "recommendation": null,
  "rating": null
}
```

---

## Known Data Source Issues

| Source | Known Issues | Mitigation |
|--------|--------------|------------|
| **yfinance** | P/B ratio errors (esp. HK stocks) | Always calculate manually |
| **yfinance** | Book value in wrong currency | Verify currency, check vs annual report |
| **Yahoo Finance** | Stale dividend yields | Check company announcements |
| **Web search** | Varies in accuracy | Always cross-reference |

### Case Study: Alibaba (9988.HK) P/B Error

- **yfinance reported:** P/B 0.30x, Book Value HK$504
- **Actual:** P/B ~2.5x, Book Value ~HK$60
- **Cause:** yfinance showed book value in CNY or ADR conversion
- **Lesson:** ALWAYS verify P/B by calculating: Price / Book Value Per Share

---

## Official Source Links

| Exchange | Filing Portal |
|----------|---------------|
| Hong Kong (HKEX) | https://www.hkexnews.hk |
| US (SEC) | https://www.sec.gov/edgar |
| Shanghai/Shenzhen | http://www.cninfo.com.cn |

### Company IR Pages

| Company | IR URL |
|---------|--------|
| Tencent | https://www.tencent.com/en-us/investors/ |
| Alibaba | https://www.alibabagroup.com/en/ir |
| Meituan | https://about.meituan.com/en/investor |
| Trip.com | https://investors.trip.com |
| China Mobile | HKEX 00941 filings |

---

## Buffett-Munger Checklist

### Business Quality
- [ ] Can I explain how this company makes money in 1 minute?
- [ ] Does it have a durable competitive advantage (moat)?
- [ ] Is the business simple and understandable?

### Management Quality
- [ ] Is management honest and shareholder-friendly?
- [ ] Do they have a track record of good capital allocation?
- [ ] Are their interests aligned with shareholders?

### Financial Health
- [ ] Is ROE consistently >15%? (Verify from annual report)
- [ ] Is debt manageable? (Verify from balance sheet)
- [ ] Are earnings consistent and predictable?

### Valuation
- [ ] Is there a margin of safety (>25%)?
- [ ] What is the intrinsic value? (Show calculation)
- [ ] What is the worst-case scenario?

### Data Verification
- [ ] All key metrics verified against official sources?
- [ ] P/B ratio calculated manually?
- [ ] Sources documented in progress.json?

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-19 | Initial framework |
| 2.0 | 2026-02-20 | Added mandatory data verification, official source hierarchy |

---

*Framework Version: 2.0*
*Last Updated: 2026-02-20*
