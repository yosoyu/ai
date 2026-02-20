# New Stock Analysis Checklist

## Pre-Analysis Setup

- [ ] Create project folder: `mkdir -p ~/Projects/ai/[STOCK_CODE]/{analysis,"Financial Reports"}`
- [ ] Copy framework: `cp ~/Projects/ai/6896/STOCK_ANALYSIS_FRAMEWORK.md ~/Projects/ai/[STOCK_CODE]/`
- [ ] Copy template: `cp ~/Projects/ai/6896/TEMPLATE_progress.json ~/Projects/ai/[STOCK_CODE]/analysis/progress.json`
- [ ] Edit progress.json with stock details
- [ ] Download annual reports (3-5 years) to `Financial Reports/`

---

## Phase 1: Data Collection

### 1.1 Annual Report Analysis
```bash
# Extract text from PDFs
python3 -c "
import pdfplumber
import os

pdf_dir = '[PATH_TO_REPORTS]'
for f in os.listdir(pdf_dir):
    if f.endswith('.pdf'):
        with pdfplumber.open(os.path.join(pdf_dir, f)) as pdf:
            for page in pdf.pages[:30]:
                print(page.extract_text())
"
```

- [ ] Extract business overview
- [ ] Extract financial highlights (3-5 years)
- [ ] Identify risk factors disclosed
- [ ] Look for patent/IP information
- [ ] Check governance disclosures

### 1.2 Yahoo Finance Data
```bash
python3 -c "
import yfinance as yf
stock = yf.Ticker('[STOCK_CODE]')
print(stock.info)
"
```

- [ ] Get current price and valuation metrics
- [ ] Get profitability ratios (ROE, margins)
- [ ] Get financial health metrics (debt, cash)
- [ ] Get dividend information
- [ ] Get price history

### 1.3 Peer Comparison
- [ ] Identify main competitors
- [ ] Compare market share
- [ ] Compare valuation metrics

**Output:** `analysis/phase1_data_collection.md`

---

## Phase 2: Fundamental Analysis

### 2.1 Business Analysis
- [ ] Describe business model
- [ ] Analyze revenue streams
- [ ] Assess market position

### 2.2 Financial Analysis
- [ ] Analyze income statement (5 years)
- [ ] Analyze balance sheet
- [ ] Analyze cash flow
- [ ] Calculate key ratios

### 2.3 Moat Analysis
- [ ] Assess competitive advantages
- [ ] Rate moat strength
- [ ] Evaluate moat durability

### 2.4 Management Analysis
- [ ] Review ownership structure
- [ ] Assess management track record
- [ ] Check for governance red flags

### 2.5 Valuation
- [ ] Calculate owner earnings
- [ ] Calculate intrinsic value (multiple methods)
- [ ] Determine margin of safety

**Output:** `analysis/phase2_fundamental_analysis.md`

---

## Phase 3: Risk Assessment

### 3.1 Governance Risks
- [ ] Check for privatization attempts
- [ ] Review related party transactions
- [ ] Assess shareholder friendliness

### 3.2 Business Risks
- [ ] Analyze patent/IP risks
- [ ] Assess competitive threats
- [ ] Evaluate regulatory risks

### 3.3 Financial Risks
- [ ] Assess dividend sustainability
- [ ] Review debt levels
- [ ] Check liquidity

**Output:** `analysis/phase3_risk_assessment.md`

---

## Phase 4: Investment Decision

### 4.1 Investment Thesis
- [ ] Document bull case
- [ ] Document bear case

### 4.2 Valuation Summary
- [ ] Summarize intrinsic value
- [ ] Compare to current price

### 4.3 Recommendation
- [ ] Apply Buffett-Munger criteria
- [ ] Determine rating
- [ ] Make recommendation

**Output:** `analysis/phase4_investment_decision.md`

---

## Phase 5: Final Report

- [ ] Write executive summary
- [ ] Document key findings
- [ ] State final recommendation
- [ ] Identify suitable investors
- [ ] Create monitoring checklist

**Output:** `analysis/phase5_final_report.md`

---

## Post-Analysis

- [ ] Update progress.json with completion
- [ ] Review all phases for consistency
- [ ] Save all files
- [ ] Create backup

---

## Quick Commands

### Check Progress
```bash
cat ~/Projects/ai/[STOCK_CODE]/analysis/progress.json
```

### Resume Analysis
Tell Claude Code:
> "Resume analysis of [STOCK_CODE] from the progress.json file"

### Start New Analysis
Tell Claude Code:
> "Use the stock analysis framework to analyze [STOCK_CODE]"
```
