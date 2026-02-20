# Stock Analysis Project

A systematic stock analysis framework using AI agent skills for Buffett-Munger style investment analysis.

---

## Project Structure

```
6896/
├── README.md                           # This file
├── STOCK_ANALYSIS_FRAMEWORK.md         # Reusable analysis framework
├── analysis/                           # Analysis outputs
│   ├── progress.json                   # Progress tracker (for resuming)
│   ├── phase1_data_collection.md       # Phase 1: Data & verification
│   ├── phase2_fundamental_analysis.md  # Phase 2: Business & financials
│   ├── phase3_risk_assessment.md       # Phase 3: Risk analysis
│   ├── phase4_investment_decision.md   # Phase 4: Valuation & decision
│   └── phase5_final_report.md          # Phase 5: Final summary
├── Financial Reports/                  # Source documents (PDFs)
└── [Company]_Investment_Analysis.md    # Original analysis files
```

---

## How to Analyze a New Stock

### Step 1: Create a New Project Folder

```bash
mkdir -p ~/Projects/ai/[STOCK_CODE]/analysis
mkdir -p ~/Projects/ai/[STOCK_CODE]/Financial\ Reports
```

### Step 2: Copy the Framework

```bash
cp STOCK_ANALYSIS_FRAMEWORK.md ~/Projects/ai/[STOCK_CODE]/
```

### Step 3: Download Annual Reports

Download the last 3-5 years of annual reports (PDFs) from:
- HKEX: https://www.hkexnews.hk
- SEC EDGAR: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany
- Company IR websites

Save them to `Financial Reports/` folder.

### Step 4: Initialize Progress Tracker

Create `analysis/progress.json`:

```json
{
  "stock": "[STOCK_CODE]",
  "company": "[Company Name]",
  "start_date": "[YYYY-MM-DD]",
  "phases": {
    "phase1": {"status": "pending", "completed_date": null},
    "phase2": {"status": "pending", "completed_date": null},
    "phase3": {"status": "pending", "completed_date": null},
    "phase4": {"status": "pending", "completed_date": null},
    "phase5": {"status": "pending", "completed_date": null}
  },
  "current_phase": 1,
  "current_step": "1.1"
}
```

### Step 5: Run the Analysis

Follow the 5-phase framework in `STOCK_ANALYSIS_FRAMEWORK.md`:

1. **Phase 1: Data Collection** - Gather data from annual reports, Yahoo Finance
2. **Phase 2: Fundamental Analysis** - Analyze business, financials, moat
3. **Phase 3: Risk Assessment** - Identify governance, competitive, financial risks
4. **Phase 4: Investment Decision** - Calculate intrinsic value, make recommendation
5. **Phase 5: Final Report** - Create executive summary

---

## Installed Skills

The following skills are installed and available for stock analysis:

### Stock & Finance Analysis
| Skill | Purpose |
|-------|---------|
| `stock-analysis` | Comprehensive stock analysis |
| `china-stock-analysis` | A-share market analysis |
| `stock-research-executor` | Deep research execution |
| `trading-analysis` | Trading strategy analysis |
| `yahoo-finance` | Yahoo Finance data fetcher |
| `tushare-finance` | Chinese stock data (Tushare) |
| `finance-expert` | Financial expertise |
| `market-sizing-analysis` | Market size analysis |

### Document Handling
| Skill | Purpose |
|-------|---------|
| `pdf` | PDF reading/manipulation |
| `xlsx` | Excel spreadsheet handling |
| `docx` | Word document handling |
| `pptx` | PowerPoint creation |

### Investment Decision
| Skill | Purpose |
|-------|---------|
| `analyze` | Investment analysis |
| `scan` | Stock scanning |
| `review` | Investment review |
| `brief` | Investment briefings |
| `trade` | Trading recommendations |

---

## Using the Skills

Skills are documentation guides. To use them:

1. Read the skill documentation:
   ```bash
   cat ~/.agents/skills/[skill-name]/SKILL.md
   ```

2. Follow the instructions in the skill guide

3. Example for Yahoo Finance:
   ```bash
   # Get stock quote
   python3 -c "
   import yfinance as yf
   stock = yf.Ticker('AAPL')
   print(stock.info)
   "
   ```

4. Example for PDF reading:
   ```bash
   python3 -c "
   import pdfplumber
   with pdfplumber.open('report.pdf') as pdf:
       for page in pdf.pages:
           print(page.extract_text())
   "
   ```

---

## Buffett-Munger Checklist

Use this checklist for every stock analysis:

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

## Analysis Template

### Phase 1 Output Template

```markdown
# Phase 1: Data Collection & Verification

**Stock:** [CODE] - [Company Name]
**Date:** [YYYY-MM-DD]

## 1.1 PDF Annual Report Analysis
### Source Documents
- [List PDF files analyzed]

### Key Findings
- [Business overview]
- [Financial highlights]
- [Risk factors disclosed]

## 1.2 Yahoo Finance Data
### Basic Information
[Price data, valuation metrics, financials]

## 1.3 Peer Comparison
[Competitor analysis]
```

### Phase 5 Output Template

```markdown
# Phase 5: Final Report

## Executive Summary
| Metric | Value | Assessment |
|--------|-------|------------|
| Current Price | $X.XX | |
| Intrinsic Value | $X.XX | |
| Margin of Safety | XX% | |

## Final Recommendation
# [BUY / HOLD / SELL / AVOID]

## Key Risks
1. [Risk 1]
2. [Risk 2]

## Positive Factors
1. [Factor 1]
2. [Factor 2]

## Suitable For
- [Investor type 1]
- [Investor type 2]

## Not Suitable For
- [Investor type 1]
- [Investor type 2]
```

---

## Requirements

- Node.js (v20+) - for skills.sh
- Python 3.9+ - for analysis scripts
- pdfplumber - for PDF reading
- yfinance - for Yahoo Finance data

Install requirements:
```bash
# Node.js (if not installed)
# Download from https://nodejs.org

# Python packages
pip3 install pdfplumber yfinance PyPDF2 pandas
```

---

## Example: Golden Throat (6896.HK)

This project contains a complete analysis of Golden Throat Holdings:

- **Recommendation:** AVOID
- **Rating:** 5.25/10 (SPECULATIVE)
- **Key Issue:** Management integrity concerns

See `analysis/` folder for detailed phase-by-phase analysis.

---

*Last Updated: 2026-02-19*
