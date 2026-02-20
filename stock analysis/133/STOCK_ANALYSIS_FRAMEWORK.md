# Stock Analysis Framework

A systematic approach to analyze stocks using AI agent skills.

---

## Phase 1: Data Collection & Verification

**Objective:** Gather all relevant data and verify key facts

| Step | Skill | Task | Output |
|------|-------|------|--------|
| 1.1 | `/pdf` | Extract key information from annual reports (patents, risks, governance) | Key findings summary |
| 1.2 | `/yahoo-finance` | Fetch latest stock price, financials, dividends, key ratios | Financial data dump |
| 1.3 | `/tushare-finance` | Get market context and peer comparison data | Peer comparison table |

**Key Questions:**
- What are the key risks disclosed in annual reports?
- What is the current valuation?
- Who are the main competitors?

---

## Phase 2: Fundamental Analysis

**Objective:** Understand the business and financial health

| Step | Skill | Task | Output |
|------|-------|------|--------|
| 2.1 | `/stock-analysis` | Comprehensive fundamental analysis | Business overview |
| 2.2 | `/finance-expert` | Deep dive into financial statements | Financial health report |
| 2.3 | `/market-sizing-analysis` | Analyze market size & growth potential | Market analysis |

**Key Questions:**
- How does the company make money?
- What is the competitive moat?
- Is the balance sheet healthy?

---

## Phase 3: Risk Assessment

**Objective:** Identify and evaluate all risks

| Step | Skill | Task | Output |
|------|-------|------|--------|
| 3.1 | `/stock-research-executor` | Research governance, regulatory, and operational risks | Risk research report |
| 3.2 | `/stock-question-refiner` | Refine key risk questions | Prioritized risk list |
| 3.3 | `/scan` | Compare with competitors | Competitive analysis |

**Key Questions:**
- What could go wrong?
- How does this compare to peers?
- Are there any red flags in governance?

---

## Phase 4: Investment Decision

**Objective:** Synthesize findings into an investment thesis

| Step | Skill | Task | Output |
|------|-------|------|--------|
| 4.1 | `/analyze` | Synthesize all findings | Investment thesis |
| 4.2 | `/trading-analysis` | Determine entry/exit points, risk-reward | Trading plan |
| 4.3 | `/brief` | Create investment summary | Executive summary |

**Key Questions:**
- What is the intrinsic value?
- What is the margin of safety?
- What would trigger a buy/sell decision?

---

## Phase 5: Documentation & Review

**Objective:** Create final deliverables and validate

| Step | Skill | Task | Output |
|------|-------|------|--------|
| 5.1 | `/review` | Review and validate analysis | Review notes |
| 5.2 | `/pdf` or `/pptx` | Generate final report | Final report |

---

## Output Files Structure

```
/analysis/
├── phase1_data_collection.md
├── phase2_fundamental_analysis.md
├── phase3_risk_assessment.md
├── phase4_investment_decision.md
├── phase5_final_report.md
└── progress.json
```

---

## Progress Tracking

Use a progress file to track completion:

```json
{
  "stock": "133.HK",
  "company": "China Merchants China Direct Investments Limited",
  "start_date": "2026-02-20",
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

## Buffett-Munger Checklist

Use this checklist throughout the analysis:

### Business Quality
- [ ] Can I explain how this company makes money in 1 minute?
- [ ] Does it have a durable competitive advantage (moat)?
- [ ] Is the business simple and understandable?

### Management Quality
- [ ] Is management honest and shareholder-friendly?
- [ ] Do they have a track record of good capital allocation?
- [ ] Are their interests aligned with shareholders?

### Financial Health
- [ ] Is ROE consistently >15%?
- [ ] Is debt manageable?
- [ ] Are earnings consistent and predictable?

### Valuation
- [ ] Is there a margin of safety (>25%)?
- [ ] What is the intrinsic value?
- [ ] What is the worst-case scenario?

---

*Framework Version: 1.0*
