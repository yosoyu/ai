# Phase 3: Risk Assessment

**Stock:** CRWV - CoreWeave, Inc.
**Date:** 2026-02-20
**Status:** ✅ COMPLETED

---

## 3.1 Financial Risk (CRITICAL)

### Debt Burden

| Metric | Value | Risk Level |
|--------|-------|------------|
| Total Debt | $18.8B | 🔴 Critical |
| Debt/Equity | 485% | 🔴 Extreme |
| Interest Expense (Q2'25) | $267M | Up 300% YoY |
| Annualized Interest | ~$1.1B | - |

### Liquidity Risk

| Metric | Value | Assessment |
|--------|-------|------------|
| Cash | $1.94B | - |
| FCF Burn | -$6.95B/yr | 🔴 Massive |
| **Cash Runway** | **~3-4 months** | 🔴 Critical |
| Current Ratio | 0.49 | Below 1 = danger |

### Debt Financing Structure

**Innovative but Risky:**
- Uses GPU rental income as collateral
- Asset-backed financing based on future cash flows
- If demand drops, may need to rent at losses to service debt

**Risk:** If GPU demand falls, rental income drops, debt becomes unserviceable.

---

## 3.2 Customer Concentration Risk (CRITICAL)

### Revenue Concentration

| Customer | Revenue Share | Risk |
|----------|---------------|------|
| **Microsoft** | 62-77% | 🔴 Extreme |
| **Top 2 Customers** | ~77% | 🔴 Extreme |
| OpenAI | Major (growing) | ⚠️ High |

### Customer Concentration Risks

1. **Pricing Power Loss**
   - Microsoft can demand lower prices
   - No leverage in negotiations

2. **Contract Renewal Risk**
   - What if Microsoft doesn't renew?
   - Building own infrastructure is an option

3. **Single Point of Failure**
   - Loss of Microsoft = revenue collapse

### Microsoft's Alternatives

| Option | Likelihood | Impact |
|--------|------------|--------|
| Renew with CoreWeave | Medium | Neutral |
| Build own GPU clusters | Increasing | Devastating |
| Switch to competitors | Medium | Severe |

---

## 3.3 Supplier Dependency Risk (CRITICAL)

### NVIDIA Dependency

| Aspect | Status |
|--------|--------|
| GPU Supplier | **NVIDIA only** |
| Alternative Options | None (proprietary) |
| Negotiating Power | None |
| Relationship | Partner + Investor + Customer |

### Three-Way NVIDIA Relationship

```
NVIDIA
  ├── Supplier (100% of GPUs)
  ├── Shareholder (6% stake, $4.2B invested)
  └── Customer (~15% of CoreWeave revenue)
```

**Risks:**
1. **Pricing Power:** NVIDIA sets prices, CoreWeave pays
2. **Allocation:** NVIDIA may favor other partners
3. **Sell-Off:** NVIDIA could sell shares, hurting stock
4. **Competition:** NVIDIA invests in CoreWeave competitors

---

## 3.4 Competitive Risk (HIGH)

### Competitive Landscape

| Competitor | Threat | Status |
|------------|--------|--------|
| **AWS** | 🔴 Critical | Expanding AI offerings |
| **Azure** | 🔴 Critical | Already a customer, may insource |
| **Google Cloud** | 🔴 High | TPU + NVIDIA options |
| **Nebius (NBIS)** | 🟡 Medium | $19.4B Microsoft deal |
| **Crusoe** | 🟡 Medium | OpenAI Stargate partner |
| **Lambda Labs** | 🟡 Medium | Growing competitor |

### Competitive Threats

1. **Hyperscaler In-Sourcing**
   - Microsoft/Azure may build own GPU clusters
   - As GPU supply improves, less need for CoreWeave

2. **Price Competition**
   - AWS/Azure can subsidize with other services
   - CoreWeave has no other revenue sources

3. **Technology Commodity**
   - GPU compute is becoming commoditized
   - No proprietary advantage

---

## 3.5 Demand Risk (MEDIUM-HIGH)

### AI Demand Sustainability

| Factor | Trend | Impact |
|--------|-------|--------|
| AI Model Training | Still growing | Positive |
| Inference Demand | Growing | Positive |
| GPU Supply | Improving | Negative (for pricing) |
| Competition | Intensifying | Negative |

### Demand Scenarios

| Scenario | Likelihood | Revenue Impact |
|----------|------------|----------------|
| **Boom** | 30% | +50%+ growth |
| **Normal** | 40% | +20-30% growth |
| **Slowdown** | 20% | Flat to +10% |
| **Crash** | 10% | Revenue decline |

### Key Risk: Training vs Inference

- **Training:** Needs premium GPUs (H100) - CoreWeave's focus
- **Inference:** Can use cheaper chips (L40S, MI300X)
- **Risk:** As models mature, demand shifts to inference
- **Impact:** Lower-margin business, more competition

---

## 3.6 Asset Depreciation Risk

### GPU Obsolescence

| Risk | Details |
|------|---------|
| **New GPU Generations** | NVIDIA releases annually |
| **Current Fleet** | Mostly H100s |
| **Next Gen** | Blackwell coming |
| **Depreciation** | 1-year accounting, 6-year useful life |

**Accounting Mismatch:**
- GPUs depreciated over 1 year (accelerated)
- Actual useful life ~6 years
- Creates artificial losses in early years

**Real Risk:**
- Rapid GPU obsolescence
- Must constantly refresh fleet
- Capital intensive with no profit

---

## 3.7 Market & Valuation Risk

### Valuation Concerns

| Metric | CoreWeave | AWS Proxy | Premium |
|--------|-----------|-----------|---------|
| P/S | 11.76x | ~5x | 2.4x |
| EV/Revenue | 15.2x | ~5x | 3x |
| Profitability | Negative | Positive | N/A |

### HSBC Bearish View (July 2025)

- Price target implied **76% downside**
- Key concerns:
  - No competitive advantage
  - Over-reliance on Microsoft
  - NVIDIA dependency

### Stock Volatility

| Metric | Value |
|--------|-------|
| 52-Week High | $187 |
| 52-Week Low | $33.52 |
| Current Price | $97.14 |
| **Volatility** | **Extreme** |

---

## Risk Summary Matrix

| Risk Category | Severity | Probability | Impact Score |
|---------------|----------|-------------|--------------|
| **Debt/Liquidity** | 🔴 Critical | 80% | 10/10 |
| **Customer Concentration** | 🔴 Critical | 70% | 9/10 |
| **Supplier Dependency** | 🔴 Critical | 60% | 9/10 |
| **Competition** | 🔴 High | 90% | 8/10 |
| **Profitability** | 🔴 Critical | 100% | 10/10 |
| **Demand Sustainability** | 🟡 Medium | 40% | 6/10 |
| **Asset Obsolescence** | 🟡 Medium | 50% | 5/10 |
| **Valuation** | 🟡 Medium | 70% | 6/10 |

**Overall Risk Level: EXTREME**

---

## Invert, Always Invert (Munger)

### How This Investment Could "Die":

1. **Liquidity Crisis** → Cash runs out → Bankruptcy or dilutive raise
2. **Microsoft Leaves** → Revenue collapses 70% → Debt unserviceable
3. **NVIDIA Cuts Supply** → No GPUs → Business stops
4. **Price War** → Margins compress → Can't service debt
5. **AI Slowdown** → Demand drops → Overcapacity losses

### What Could Go Right:

1. **Profitability Achieved** → Debt becomes manageable
2. **Microsoft Renews** → Revenue visibility improves
3. **AI Boom Continues** → Demand exceeds all expectations
4. **NVIDIA Continues Support** → Supply secured
5. **Market Share Gains** → Becomes dominant player

---

## Key Questions for Due Diligence

| Question | Priority | Status |
|----------|----------|--------|
| When will FCF turn positive? | 🔴 Critical | Unknown |
| Can debt be serviced? | 🔴 Critical | Uncertain |
| Will Microsoft renew? | 🔴 Critical | Unknown |
| What is normalized margin? | 🔴 High | Unclear |
| Is $97 fair value? | 🔴 Critical | Debatable |

---

*Phase 3 Completed: 2026-02-20*
