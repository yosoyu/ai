# Stock Analysis Framework

A systematic 5-phase approach to analyze stocks using AI agent skills, based on Buffett-Munger investment principles.

---

## Quick Start

1. **Create a new stock folder**: `mkdir -p /Users/colinyu/Projects/ai/{TICKER}/analysis`
2. **Copy the template**: `cp templates/progress.json /Users/colinyu/Projects/ai/{TICKER}/analysis/`
3. **Run Phase 1**: Start with data collection
4. **Progress through phases**: Complete each phase sequentially
5. **Generate final report**: Use Phase 5 to synthesize all findings

---

## 5-Phase Framework

| Phase | Objective | Skills Used | Output |
|-------|-----------|-------------|--------|
| **1. Data Collection** | Gather & verify facts | `/pdf`, `/yahoo-finance`, `/tushare-finance` | `phase1_data_collection.md` |
| **2. Fundamental Analysis** | Understand business | `/stock-analysis`, `/finance-expert` | `phase2_fundamental_analysis.md` |
| **3. Risk Assessment** | Identify all risks | `/stock-research-executor`, `/scan` | `phase3_risk_assessment.md` |
| **4. Investment Decision** | Synthesize thesis | `/analyze`, `/trading-analysis` | `phase4_investment_decision.md` |
| **5. Final Report** | Document & review | `/review`, `/pdf` | `phase5_final_report.md` |

---

## Directory Structure

```
stock-analysis-framework/
├── README.md                      # This file
├── FRAMEWORK.md                   # Detailed framework documentation
├── templates/
│   ├── progress.json              # Progress tracking template
│   ├── phase1_template.md         # Data collection template
│   ├── phase2_template.md         # Fundamental analysis template
│   ├── phase3_template.md         # Risk assessment template
│   ├── phase4_template.md         # Investment decision template
│   └── phase5_template.md         # Final report template
├── checklists/
│   ├── buffett_munger.md          # Quality investing checklist
│   ├── due_diligence.md           # Due diligence checklist
│   └── red_flags.md               # Red flags to watch for
└── skills/
    └── skill_mapping.md           # Which skills to use for each task
```

---

## Completed Analyses

| Ticker | Company | Date | Recommendation | Rating |
|--------|---------|------|----------------|--------|
| 6896.HK | Golden Throat | 2026-02-19 | AVOID | 5.25/10 |
| 683.HK | Kerry Properties | 2026-02-20 | BUY | 7.7/10 |
| 700.HK | Tencent | 2026-02-20 | BUY | 8.2/10 |
| 9988.HK | Alibaba | 2026-02-20 | BUY | 7.8/10 |
| 133.HK | China Merchants CDI | 2026-02-20 | SPEC BUY | 6.6/10 |
| 9961.HK | Trip.com | 2026-02-20 | HOLD | 6.5/10 |
| 3690.HK | Meituan | 2026-02-20 | AVOID | 5.55/10 |
| CRWV | CoreWeave | 2026-02-20 | AVOID | 4.25/10 |

---

## Key Principles

### Buffett-Munger Approach
1. **Business Quality** - Simple, understandable, durable moat
2. **Management Integrity** - Honest, shareholder-friendly, aligned interests
3. **Financial Health** - High ROE, manageable debt, consistent earnings
4. **Margin of Safety** - Buy at discount to intrinsic value

### Invert, Always Invert
- Focus on what could go wrong first
- Eliminate stocks with disqualifying red flags
- Only then evaluate upside potential

---

## Usage Example

```
# Analyze a new stock (e.g., 9999.HK)

1. Create folder structure:
   mkdir -p /Users/colinyu/Projects/ai/9999/analysis

2. Copy template:
   cp templates/progress.json /Users/colinyu/Projects/ai/9999/analysis/

3. Run Phase 1:
   Use /pdf to extract annual report
   Use /yahoo-finance to get financials

4. Continue through phases...

5. Final output:
   /Users/colinyu/Projects/ai/9999/analysis/phase5_final_report.md
```

---

*Framework Version: 1.0*
