# Data Verification Report

**Date:** 2026-02-20
**Purpose:** Cross-verify all stock analysis data against official sources

---

## Summary of Data Sources Used

| Source Type | Examples | Reliability |
|-------------|----------|-------------|
| **Official** | Company IR, HKEX filings, SEC filings | ⭐⭐⭐⭐⭐ Primary |
| **Exchange Data** | HKEX, NASDAQ | ⭐⭐⭐⭐⭐ Primary |
| **Financial Databases** | yfinance, Bloomberg, Reuters | ⭐⭐⭐⭐ Secondary |
| **Financial Portals** | Yahoo Finance, Google Finance | ⭐⭐⭐ Secondary |
| **Chinese Portals** | Xueqiu (雪球), 东方财富 | ⭐⭐⭐ Secondary |
| **Analyst Reports** | Brokerage research | ⭐⭐⭐ Tertiary |
| **News Articles** | Media coverage | ⭐⭐ Tertiary |
| **Web Search** | General search results | ⭐⭐ Tertiary |

---

## Stock-by-Stock Verification

### 1. Tencent (700.HK)

| Metric | Analysis Value | Official/Verified | Status |
|--------|---------------|-------------------|--------|
| Price | HK$533 | HK$530-533 | ✅ Match |
| P/E | 21.8x | 21-25x | ✅ Match |
| P/B | 3.63x | ~3.6x | ✅ Match |
| ROE | 19.8% | ~20% | ✅ Match |
| Net Margin | 29.9% | ~30% | ✅ Match |
| Dividend Yield | 0.84% | ~0.8% | ✅ Match |

**Official Sources:** [Tencent Investor Relations](https://www.tencent.com/en-us/investors/), HKEX filings

**Status:** ✅ VERIFIED

---

### 2. Alibaba (9988.HK)

| Metric | Original Analysis | Corrected | Verified | Status |
|--------|------------------|-----------|----------|--------|
| P/B | 0.30x ❌ | 2.5x | 2.5-2.7x | ✅ Corrected |
| Book Value | HK$504 ❌ | HK$60 | HK$54-60 | ✅ Corrected |
| P/E | 20.4x | 20.3x | 20-21x | ✅ Match |
| ROE | 11.2% | 11.2% | 11% | ✅ Match |

**Issue:** yfinance showed incorrect book value (503.66) - likely CNY or ADR conversion error

**Correction Applied:** Yes

**Status:** ✅ CORRECTED

---

### 3. Kerry Properties (683.HK)

| Metric | Analysis Value | Verified Value | Status |
|--------|---------------|----------------|--------|
| Price | HK$25.58 | HK$20.56 | ⚠️ Outdated |
| P/B | 0.36x | **0.29x** | ⚠️ Update needed |
| P/E | 58x | 46-47x | ⚠️ Update needed |
| Dividend Yield | 5.3% | 6.5% | ⚠️ Update needed |
| Book Value | HK$71.84 | HK$118.17B total | Need verification |

**Recommendation:** Update with latest verified data

**Status:** ⚠️ NEEDS UPDATE

---

### 4. China Mobile (941.HK)

| Metric | Analysis Value | Verified Value | Status |
|--------|---------------|----------------|--------|
| Price | HK$78.4 | HK$78-82 | ✅ Match |
| P/E | 10.6x | 10.8-14.8x | ✅ Match (range) |
| P/B | 1.07x | ~1.1x | ✅ Match |
| Dividend Yield | **6.7%** | **4.9-5.5%** | ⚠️ Discrepancy |
| ROE | 10.5% | ~10% | ✅ Match |

**Issue:** Dividend yield appears overstated. Need to verify calculation.

**Official Sources:** [HKEX 00941 filings](https://www.hkexnews.hk)

**Status:** ⚠️ NEEDS VERIFICATION

---

### 5. China Telecom (728.HK)

| Metric | Analysis Value | Verified Value | Status |
|--------|---------------|----------------|--------|
| Price | HK$4.93 | HK$5.38-5.43 | ⚠️ Outdated |
| P/B | 0.87x | **0.98-1.2x** | ⚠️ Update needed |
| P/E | 11.7x | 11-15x | ✅ Match |
| Dividend Yield | 6.1% | 5.5-6.3% | ✅ Match (range) |

**Status:** ⚠️ NEEDS UPDATE

---

### 6. Trip.com (9961.HK)

| Metric | Analysis Value | Verified Value | Status |
|--------|---------------|----------------|--------|
| Price | HK$419.8 | HK$419-554 | ✅ Match (range) |
| P/E | 14.3x | **16.9-20.4x** | ⚠️ Update needed |
| P/B | 1.44x | 1.98-2.24x | ⚠️ Update needed |
| ROE | 20.2% | ~4% (5yr avg) | ⚠️ Significant discrepancy |
| Net Margin | 52% | 31-52% | ✅ Match (range) |

**Issue:** ROE figure significantly different from verified sources

**Official Sources:** [Trip.com Investor Relations](http://investors.trip.com)

**Status:** ⚠️ NEEDS VERIFICATION

---

### 7. Meituan (3690.HK)

| Metric | Analysis Value | Verified Value | Status |
|--------|---------------|----------------|--------|
| Profit Warning | +RMB 36B → -RMB 240B | ✅ Confirmed via HKEX | ✅ Verified |
| Price | HK$82 | HK$91-98 | ⚠️ Outdated |
| Competition | Price wars, market share loss | ✅ Confirmed | ✅ Verified |

**Official Sources:** [HKEX 03690 Profit Warning Filing](https://www.hkexnews.hk) - Feb 13, 2025

**Status:** ✅ VERIFIED (key thesis correct)

---

### 8. Golden Throat (6896.HK)

| Metric | Analysis Value | Verification Status |
|--------|---------------|---------------------|
| P/E | 7.76x | Not independently verified |
| ROE | 21.5% | Not independently verified |
| Dividend Payout | 126% | Not independently verified |

**Note:** Limited English-language verification sources available

**Recommendation:** Verify via HKEX Chinese filings

**Status:** ⚠️ NEEDS VERIFICATION

---

### 9. CoreWeave (CRWV)

| Metric | Analysis Value | Verified Value | Status |
|--------|---------------|----------------|--------|
| Debt/Equity | 485% | 485.03% | ✅ Match |
| Revenue Growth | +276% | +420% (Q1 2025) | ⚠️ Conservative in analysis |
| Profitability | Unprofitable | ✅ Confirmed | ✅ Verified |
| P/B | 9.62x | 9.62-9.89x | ✅ Match |

**Official Sources:** SEC EDGAR filings

**Status:** ✅ VERIFIED

---

### 10. China Merchants China Direct (133.HK)

| Metric | Analysis Value | Verification Status |
|--------|---------------|---------------------|
| NAV Discount | 55% | Not independently verified |
| P/NAV | 0.45x | Not independently verified |

**Status:** ⚠️ NEEDS VERIFICATION

---

## Critical Issues Found

| Stock | Issue | Severity | Action Required |
|-------|-------|----------|-----------------|
| **9988.HK** | yfinance P/B error (0.3x vs 2.5x) | 🔴 Critical | ✅ Corrected |
| **683.HK** | Data may be outdated | 🟡 Medium | Update needed |
| **941.HK** | Dividend yield discrepancy | 🟡 Medium | Verify calculation |
| **9961.HK** | ROE significant discrepancy | 🟡 Medium | Verify source |
| **728.HK** | Price/P/B outdated | 🟡 Medium | Update needed |

---

## Recommendations

### 1. Update Framework to Require Official Source Verification

Add mandatory data source verification step:

```markdown
## Phase 1.5: Data Verification (NEW)

**Objective:** Verify all key data against official sources

| Step | Task | Official Source |
|------|------|-----------------|
| 1.5.1 | Verify price/market data | HKEX/NASDAQ official |
| 1.5.2 | Verify P/E, P/B ratios | Company IR, HKEX filings |
| 1.5.3 | Verify dividend yields | Company announcements |
| 1.5.4 | Cross-check yfinance data | Minimum 2 independent sources |
```

### 2. Establish Data Source Hierarchy

1. **Primary (Required):** Company IR, Exchange filings (HKEX, SEC)
2. **Secondary (Cross-check):** yfinance, Bloomberg, Reuters
3. **Tertiary (Context):** News, analyst reports, web search

### 3. Add Warning for Non-Verified Data

Flag any data that cannot be verified against at least 2 sources.

---

## Data Source Links

| Company | Official IR / Filings |
|---------|----------------------|
| Tencent (700) | https://www.tencent.com/en-us/investors/ |
| Alibaba (9988) | https://www.alibabagroup.com/en/ir |
| China Mobile (941) | HKEX 00941 filings |
| China Telecom (728) | HKEX 00728 filings |
| Trip.com (9961) | https://investors.trip.com |
| Meituan (3690) | https://about.meituan.com/en/investor |
| Kerry Properties (683) | https://www.kerryproperties.com.hk |
| CoreWeave (CRWV) | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=CRWV |

---

*Report Generated: 2026-02-20*
