# Skill Mapping

Which Claude Code skills to use for each analysis task.

---

## Phase 1: Data Collection

| Task | Skill | Usage |
|------|-------|-------|
| Extract annual reports | `/pdf` | Read and extract key info from PDF reports |
| Fetch stock price | `/yahoo-finance` | Current price, P/E, P/B, dividend, 52W range |
| Get financials | `/yahoo-finance` | Income statement, balance sheet, cash flow |
| Chinese market data | `/tushare-finance` | A-share, HK, US stocks data |
| Search for info | `WebSearch` | Find recent news, company info |

### Example Commands
```
/pdf /path/to/annual_report.pdf
/yahoo-finance quote 0700.HK
/yahoo-finance fundamentals 0700.HK
/tushare-finance (for Chinese market data)
```

---

## Phase 2: Fundamental Analysis

| Task | Skill | Usage |
|------|-------|-------|
| Comprehensive analysis | `/stock-analysis` | 8-dimension stock analysis |
| Financial deep dive | `/finance-expert` | Financial statement analysis |
| Market sizing | `/market-sizing-analysis` | TAM/SAM/SOM calculation |
| Compare stocks | `/yahoo-finance compare` | Side-by-side comparison |

### Example Commands
```
/stock-analysis AAPL
/finance-expert (describe financial questions)
/market-sizing-analysis (describe market)
/yahoo-finance compare 0700.HK,9988.HK,3690.HK
```

---

## Phase 3: Risk Assessment

| Task | Skill | Usage |
|------|-------|-------|
| Deep research | `/stock-research-executor` | Execute 7-phase research |
| Refine questions | `/stock-question-refiner` | Structure investment questions |
| Market scan | `/scan` | Find opportunities, compare peers |
| Verify citations | `/citation-validator` | Validate source accuracy |

### Example Commands
```
/stock-research-executor (structured research prompt)
/stock-question-refiner What are the key risks for 0700.HK?
/scan HK tech stocks
```

---

## Phase 4: Investment Decision

| Task | Skill | Usage |
|------|-------|-------|
| Synthesize analysis | `/analyze` | Individual stock deep analysis |
| Trading analysis | `/trading-analysis` | Entry/exit points, risk-reward |
| Daily brief | `/brief` | Investment summary |
| Backtest strategy | `/backtesting-trading-strategies` | Test trading ideas |

### Example Commands
```
/analyze 0700.HK
/trading-analysis 0700.HK
/brief (market summary)
```

---

## Phase 5: Final Report

| Task | Skill | Usage |
|------|-------|-------|
| Review analysis | `/review` | Periodic review of thesis |
| Generate PDF | `/pdf` | Create final report |
| Create presentation | `/pptx` | Investment deck |

### Example Commands
```
/review (review current holdings)
/pdf (create report document)
/pptx (create presentation)
```

---

## Utility Skills

| Task | Skill | Usage |
|------|-------|-------|
| Read website | `mcp__web_reader__webReader` | Fetch and read web content |
| Analyze image | `mcp__4_5v_mcp__analyze_image` | Analyze charts, screenshots |
| Create frontend | `/frontend-design` | Build dashboard/visualization |
| Document writing | `/doc-coauthoring` | Write structured documents |

---

## Quick Reference by Stock Type

### Hong Kong Stocks
```
/yahoo-finance quote 0700.HK
/yahoo-finance fundamentals 0700.HK
/tushare-finance (for detailed HK data)
```

### US Stocks
```
/yahoo-finance quote AAPL
/yahoo-finance fundamentals AAPL
/yahoo-finance earnings AAPL
```

### A-Share (China)
```
/tushare-finance (primary source)
```

### Crypto
```
/yahoo-finance quote BTC-USD
/stock-analysis (supports top 20 crypto)
```

---

## Workflow Example

### Full Analysis Workflow
```
1. /yahoo-finance quote 0700.HK
2. /yahoo-finance fundamentals 0700.HK
3. /pdf annual_report.pdf
4. /stock-analysis 0700.HK
5. /scan HK tech peers
6. /analyze 0700.HK
7. /trading-analysis 0700.HK
```

### Quick Check Workflow
```
1. /yahoo-finance quote 0700.HK
2. /brief
```

---

*Skill Mapping v1.0*
