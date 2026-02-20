# Stock Analysis Site

Web dashboard for visualizing stock analysis results.

---

## Directory Structure

```
stock-analysis-site/
├── index.html              # Main dashboard
├── sync_from_analysis.py   # Bridge script to sync from framework
├── generate_stocks.py      # Static generator (backup)
└── stocks/
    ├── stock-page.css      # Shared styles
    ├── 700.html            # Tencent
    ├── 9988.html           # Alibaba
    ├── 683.html            # Kerry Properties
    ├── 133.html            # CMCDI
    ├── 9961.html           # Trip.com
    ├── 3690.html           # Meituan
    ├── 6896.html           # Golden Throat
    └── CRWV.html           # CoreWeave
```

---

## Linking with Stock Analysis Framework

### Workflow

```
stock-analysis-framework/          stock-analysis-site/
        │                                   │
        │  1. Analyze stock                 │
        │     using templates               │
        ▼                                   │
[TICKER]/analysis/                          │
├── phase1_data_collection.md               │
├── phase2_fundamental_analysis.md          │
├── phase3_risk_assessment.md               │
├── phase4_investment_decision.md           │
├── phase5_final_report.md  ────────────────┼──▶ 2. Run sync script
└── progress.json                           │
                                            ▼
                                     stocks/[TICKER].html
                                     (auto-generated)
```

### Sync Command

```bash
# After completing analysis in framework, run:
python3 /Users/colinyu/Projects/ai/stock-analysis-site/sync_from_analysis.py
```

This will:
1. Read all phase5_final_report.md files
2. Parse key metrics (rating, price, P/E, P/B, etc.)
3. Generate HTML pages in stocks/ folder
4. Output JavaScript data for index.html

---

## Data Flow

### From Analysis to Website

| Analysis File | Website Display |
|---------------|-----------------|
| Phase 1: Price, P/E, P/B | Key Metrics section |
| Phase 2: Business model | Investment Thesis |
| Phase 3: Risks | Risk Factors |
| Phase 4: Intrinsic value | Valuation Analysis |
| Phase 5: Recommendation | Badge & Rating |

### Auto-Updated Fields

When you run `sync_from_analysis.py`:
- ✅ Rating score
- ✅ Recommendation (Buy/Hold/Avoid)
- ✅ Current price
- ✅ P/E, P/B ratios
- ✅ ROE, Dividend
- ✅ Intrinsic value
- ✅ Margin of safety
- ✅ Positive factors
- ✅ Risk factors

---

## Manual Updates

### To update a single stock:

1. Edit the analysis file:
   ```
   /Users/colinyu/Projects/ai/[TICKER]/analysis/phase5_final_report.md
   ```

2. Run sync:
   ```bash
   python3 sync_from_analysis.py
   ```

3. Refresh the website

### To add a new stock:

1. Create analysis folder:
   ```bash
   mkdir -p /Users/colinyu/Projects/ai/[TICKER]/analysis
   ```

2. Add to `sync_from_analysis.py`:
   ```python
   STOCK_FOLDERS["[TICKER]"] = {
       "ticker": "[TICKER]",
       "name": "Company Name",
       "yahoo_ticker": "[TICKER].HK"
   }
   ```

3. Run analysis using framework templates

4. Run sync script

---

## Development

### Local Preview

```bash
# Open in browser
open /Users/colinyu/Projects/ai/stock-analysis-site/index.html

# Or start a local server
cd /Users/colinyu/Projects/ai/stock-analysis-site
python3 -m http.server 8000
# Then open http://localhost:8000
```

### Regenerate All Pages

```bash
python3 sync_from_analysis.py
```

### Regenerate Static (Backup)

```bash
python3 generate_stocks.py
```

---

## Integration Points

| Component | Location | Purpose |
|-----------|----------|---------|
| Framework | `../stock-analysis-framework/` | Analysis methodology |
| Analysis Data | `../[TICKER]/analysis/` | Raw analysis files |
| Website | `./` | Visualization layer |
| Sync Script | `./sync_from_analysis.py` | Bridge between layers |

---

*Stock Analysis Site v1.0*
