#!/usr/bin/env python3
"""Generate individual stock analysis pages with data sources."""

import os

STOCKS_DIR = "/Users/colinyu/Projects/ai/stock-analysis-site/stocks"

STOCKS = [
    {
        "id": "tencent",
        "ticker": "700",
        "name": "Tencent Holdings Limited",
        "chinese": "腾讯控股",
        "recommendation": "buy",
        "rating": 8.2,
        "scores": {"Business Quality": 9, "Competitive Moat": 9, "Growth Potential": 8, "Management": 8, "Financial Health": 8, "Valuation": 7},
        "price": 521.0,
        "prev_close": 533.0,
        "market_cap": "HK$4.70T",
        "pe": 20.7,
        "pb": 3.57,
        "roe": 19.8,
        "margin": 29.9,
        "dividend": 0.84,
        "range_low": 419,
        "range_high": 683,
        "intrinsic_value": 650,
        "margin_of_safety": 18.5,
        "target": 650,
        "stop_loss": 420,
        "positives": [
            ("Dominant Ecosystem", "WeChat/Weixin with 1.4B+ MAU creates massive network effects and switching costs.", "Company Reports"),
            ("Exceptional Profitability", "29.9% net margin and 19.8% ROE demonstrate pricing power and operational efficiency.", None),
            ("Strong Gaming Business", "Global gaming leader with Honor of Kings, PUBG Mobile, and growing pipeline.", None),
            ("Shareholder Returns", "HK$80B+ buyback program (2025) and growing dividend.", "HKEX"),
        ],
        "risks": [
            ("AI Competition", "ByteDance leading in AI apps; Tencent investing heavily to catch up."),
            ("Regulatory Environment", "Gaming regulations and antitrust concerns remain potential headwinds."),
        ],
        "sources": [
            ("Yahoo Finance - 700.HK", "https://finance.yahoo.com/quote/0700.HK", "Price, P/E, P/B, 52W Range"),
            ("HKEX News", "https://www1.hkexnews.hk/listedco/listconews/sehk/index.html", "Annual Reports, Announcements"),
            ("Tencent IR", "https://www.tencent.com/en-us/about.html", "Company Reports, Presentations"),
            ("Stock Analysis", "https://stockanalysis.com/quote/hkg/0700/", "Financial Statements"),
        ]
    },
    {
        "id": "alibaba",
        "ticker": "9988",
        "name": "Alibaba Group Holding Limited",
        "chinese": "阿里巴巴",
        "recommendation": "buy",
        "rating": 7.8,
        "scores": {"Business Quality": 8, "Competitive Moat": 7, "Growth Potential": 7, "Management": 7, "Financial Health": 8, "Valuation": 9},
        "price": 148.8,
        "prev_close": 154.7,
        "market_cap": "HK$2.84T",
        "pe": 20.08,
        "pb": 0.30,
        "roe": 11.2,
        "margin": 12.2,
        "dividend": 0.67,
        "range_low": 95.7,
        "range_high": 186.2,
        "intrinsic_value": 220,
        "margin_of_safety": 31.4,
        "target": 220,
        "stop_loss": 110,
        "positives": [
            ("Deep Value", "P/B 0.30x - trading at 70% discount to book value of HK$504.", "Yahoo Finance"),
            ("Improving Profitability", "Net profit +76% YoY (Q1 FY2026), margin recovery underway.", "HKEX"),
            ("Cloud Leadership", "Alibaba Cloud is market leader in China with AI growth potential.", None),
            ("Shareholder Returns", "Active buyback program and dividend initiated.", "HKEX"),
        ],
        "risks": [
            ("Intense Competition", "PDD taking market share, JD.com in premium, ongoing price wars."),
            ("Regulatory Overhang", "Antitrust history, ongoing scrutiny, policy uncertainty."),
            ("US-China Tensions", "Potential delisting risk (reduced), tariff concerns."),
        ],
        "sources": [
            ("Yahoo Finance - 9988.HK", "https://finance.yahoo.com/quote/9988.HK", "Price, P/E, P/B, 52W Range"),
            ("HKEX News", "https://www1.hkexnews.hk/listedco/listconews/sehk/index.html", "Annual Reports"),
            ("Alibaba IR", "https://www.alibabagroup.com/en/ir", "Company Reports"),
            ("SEC EDGAR", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=BABA", "US Filings"),
        ]
    },
    {
        "id": "kerry",
        "ticker": "683",
        "name": "Kerry Properties Limited",
        "chinese": "嘉里建设",
        "recommendation": "buy",
        "rating": 7.7,
        "scores": {"Business Quality": 7, "Competitive Moat": 7, "Management Quality": 9, "Financial Health": 6, "Valuation": 9},
        "price": 25.58,
        "prev_close": 25.16,
        "market_cap": "HK$37.1B",
        "pe": 58.1,
        "pb": 0.36,
        "roe": 0.95,
        "margin": 2.8,
        "dividend": 5.3,
        "range_low": 15.02,
        "range_high": 25.60,
        "intrinsic_value": 45.89,
        "margin_of_safety": 44.3,
        "target": 46,
        "stop_loss": 18,
        "positives": [
            ("Deep Value", "P/B 0.36x - trading at 64% discount to book value of HK$71.84.", "Yahoo Finance"),
            ("Quality Assets", "Prime HK locations (Quarry Bay, Kowloon) and Shanghai properties.", "Annual Report"),
            ("Excellent Management", "Kuok family controlled (65%) with high integrity reputation.", None),
            ("Attractive Dividend", "5.3% yield, HK$1.35/share consistently maintained.", "HKEX"),
        ],
        "risks": [
            ("Cyclical Earnings", "ROE 0.95%, profit down 75% YoY, 'revenue up, profit down' trend."),
            ("Office Oversupply", "HK vacancy ~15%, rental rates declining."),
            ("High Debt", "HK$61.8B total debt, D/E 52.3%."),
        ],
        "sources": [
            ("Yahoo Finance - 683.HK", "https://finance.yahoo.com/quote/0683.HK", "Price, P/B, 52W Range"),
            ("HKEX Annual Report", "https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0425/2025042501089.html", "Financial Statements"),
            ("Kerry Properties IR", "http://www.kerryprops.com", "Company Information"),
        ]
    },
    {
        "id": "cmcdi",
        "ticker": "133",
        "name": "China Merchants China Direct Investments",
        "chinese": "招商局中国基金",
        "recommendation": "hold",
        "recommendation_text": "SPECULATIVE BUY",
        "rating": 6.6,
        "scores": {"Business Quality": 6, "Competitive Moat": 5, "Management Quality": 5, "Financial Health": 8, "Valuation": 9},
        "price": 15.25,
        "prev_close": 15.04,
        "market_cap": "HK$2.32B",
        "pe": 1.48,
        "pb": 0.38,
        "roe": 29.0,
        "margin": None,
        "dividend": 4.15,
        "range_low": 11.9,
        "range_high": 17.02,
        "intrinsic_value": 26.14,
        "margin_of_safety": 40.4,
        "target": 26,
        "stop_loss": 10,
        "positives": [
            ("Extreme NAV Discount", "P/NAV 0.38x - trading at 62% discount to NAV of HK$40.21.", "Yahoo Finance"),
            ("Quality Holdings", "China Merchants Bank (46%), China UnionPay, iFlytek.", "Annual Report"),
            ("Governance Victory", "Shareholders voted down management contract (HK first!); fee reduced 76%.", "HKEX"),
            ("Strong ROE", "29.0% ROE in 2024, net profit up 2,002% YoY.", "Annual Report"),
        ],
        "risks": [
            ("Value Trap Risk", "Discount has persisted for years; no guarantee of narrowing."),
            ("Fee Uncertainty", "Fee reduction is interim, not yet permanent."),
            ("Illiquidity", "Low trading volume, difficult to exit large positions."),
        ],
        "sources": [
            ("Yahoo Finance - 133.HK", "https://finance.yahoo.com/quote/0133.HK", "Price, P/E, P/B, NAV"),
            ("CMCDI Company Website", "http://www.cmcdi.com.hk", "NAV Announcements"),
            ("HKEX Announcements", "https://www1.hkexnews.hk", "Fee Structure, Reports"),
        ]
    },
    {
        "id": "trip",
        "ticker": "9961",
        "name": "Trip.com Group Limited",
        "chinese": "携程集团",
        "recommendation": "hold",
        "rating": 6.5,
        "scores": {"Business Quality": 8, "Competitive Moat": 7, "Growth Potential": 7, "Management": 7, "Financial Health": 8, "Valuation": 7, "Risk Profile": 5},
        "price": 417.8,
        "prev_close": 419.8,
        "market_cap": "HK$273B",
        "pe": 14.24,
        "pb": 1.44,
        "roe": 20.2,
        "margin": 52.2,
        "dividend": 0.56,
        "range_low": 402.6,
        "range_high": 613.0,
        "intrinsic_value": 550,
        "margin_of_safety": None,
        "target": 550,
        "stop_loss": 350,
        "positives": [
            ("Exceptional Profitability", "52.2% net margin (extraordinary), 20.2% ROE.", "Annual Report"),
            ("Market Leadership", "#1 online travel platform in China across all segments.", None),
            ("Growth Drivers", "Outbound travel recovery (+12%), international business +34%.", None),
        ],
        "risks": [
            ("Antitrust Investigation", "SAMR probe launched Jan 2026; potential fine unknown.", "SAMR"),
            ("Consumer Spending", "China consumption weakness affecting travel expenditure.", None),
            ("Competition", "Fliggy (Alibaba), Qunar, Meituan travel competing.", None),
        ],
        "sources": [
            ("Yahoo Finance - 9961.HK", "https://finance.yahoo.com/quote/9961.HK", "Price, P/E, P/B"),
            ("Trip.com IR", "https://investors.trip.com", "Company Reports"),
            ("SAMR", "https://www.samr.gov.cn", "Regulatory Announcements"),
        ]
    },
    {
        "id": "meituan",
        "ticker": "3690",
        "name": "Meituan",
        "chinese": "美团",
        "recommendation": "avoid",
        "recommendation_text": "HOLD/AVOID",
        "rating": 5.55,
        "scores": {"Business Quality": 8, "Competitive Moat": 4, "Management": 8, "Financial Health": 5, "Valuation": 5, "Risk Profile": 3},
        "price": 80.6,
        "prev_close": 82.05,
        "market_cap": "HK$492B",
        "pe": 15.18,
        "pb": 2.49,
        "roe": -1.2,
        "margin": None,
        "dividend": 0,
        "range_low": 80.1,
        "range_high": 189.6,
        "intrinsic_value": None,
        "margin_of_safety": None,
        "target": None,
        "stop_loss": None,
        "positives": [
            ("Strong Cash Position", "HK$141B cash and equivalents, can survive prolonged competition.", "Annual Report"),
            ("Still #1 Position", "50%+ market share, 3.36M active riders, network effects intact.", None),
            ("Quality Management", "Wang Xing - serial entrepreneur with proven track record.", None),
        ],
        "risks": [
            ("Massive Profit Warning", "2024: +RMB 35.8B profit → 2025E: -RMB 240B loss (RMB 276B swing).", "Company Guidance"),
            ("Existential Competition", "Market share 85%→55% in 2 years; Alibaba (饿了么) at 42%.", "Industry Reports"),
            ("Broken Unit Economics", "Marketing spend +91% YoY, per-order economics negative.", None),
        ],
        "sources": [
            ("Yahoo Finance - 3690.HK", "https://finance.yahoo.com/quote/3690.HK", "Price, P/S, Market Cap"),
            ("Meituan IR", "https://ir.meituan.com", "Financial Reports"),
            ("HKEX News", "https://www1.hkexnews.hk", "Announcements"),
        ]
    },
    {
        "id": "golden",
        "ticker": "6896",
        "name": "Golden Throat Holdings Group",
        "chinese": "金嗓子",
        "recommendation": "avoid",
        "rating": 5.25,
        "scores": {"Business Quality": 6, "Competitive Moat": 5, "Management Quality": 2, "Financial Health": 7, "Valuation": 7},
        "price": 3.18,
        "prev_close": 3.14,
        "market_cap": "HK$2.35B",
        "pe": 7.76,
        "pb": 1.72,
        "roe": 21.5,
        "margin": 27,
        "dividend": 15.7,
        "range_low": 3.03,
        "range_high": 5.65,
        "intrinsic_value": 4.07,
        "margin_of_safety": 26,
        "target": None,
        "stop_loss": None,
        "positives": [
            ("Strong Profitability", "27% net margin, 21.5% ROE, 75% gross margin.", "Annual Report"),
            ("Market Leadership", "#1 in China throat lozenge market (17% share).", None),
            ("Financial Health", "HK$1.06B cash, current ratio 1.87.", None),
        ],
        "risks": [
            ("Management Integrity FAILS", "2021 failed privatization at lowball price; founder listed as '老赖'.", "HKEX/Court Records"),
            ("Unsustainable Dividend", "126% payout ratio - paying MORE than earnings.", "Annual Report"),
            ("Information Opacity", "Annual report doesn't disclose core patent expiration dates.", None),
        ],
        "sources": [
            ("Yahoo Finance - 6896.HK", "https://finance.yahoo.com/quote/6896.HK", "Price, P/E, P/B"),
            ("HKEX Annual Report", "https://www1.hkexnews.hk/listedco/listconews/sehk/2025/0425/2025042501089.pdf", "Financial Statements"),
            ("CNIPA Patent Database", "https://pss-system.cponline.cnipa.gov.cn", "Patent Verification"),
            ("NMPA TCM Protection", "https://www.nmpa.gov.cn", "Regulatory Status"),
        ]
    },
    {
        "id": "coreweave",
        "ticker": "CRWV",
        "name": "CoreWeave, Inc.",
        "chinese": None,
        "recommendation": "avoid",
        "rating": 4.25,
        "scores": {"Business Quality": 5, "Growth Potential": 9, "Competitive Moat": 3, "Management": 5, "Financial Health": 2, "Valuation": 4, "Risk Profile": 2},
        "price": 97.14,
        "prev_close": 95.45,
        "market_cap": "$50.6B",
        "pe": None,
        "pb": 12.46,
        "roe": -29.2,
        "margin": -17.8,
        "dividend": 0,
        "range_low": 33.515,
        "range_high": 187.0,
        "intrinsic_value": None,
        "margin_of_safety": None,
        "target": None,
        "stop_loss": None,
        "positives": [
            ("Explosive Growth", "Revenue +276% YoY, TTM revenue $4.31B.", "SEC Filing"),
            ("Contract Backlog", "$30B+ total commitments (OpenAI $22.4B, NVIDIA $6.3B).", None),
            ("Strong Partnerships", "NVIDIA 6% stake ($4.2B invested), Microsoft largest customer.", None),
        ],
        "risks": [
            ("Unprofitable", "Net income -$825M (TTM), net margin -17.8%, no clear path to profit.", "SEC Filing"),
            ("Extreme Debt", "Total debt $18.8B, D/E 485%, interest expense up 300%.", None),
            ("Liquidity Crisis", "Cash $1.94B, FCF burn -$6.95B/year = 3-4 month runway.", None),
            ("Customer Concentration", "Microsoft 62-77% of revenue; single customer loss = collapse.", None),
        ],
        "sources": [
            ("Yahoo Finance - CRWV", "https://finance.yahoo.com/quote/CRWV", "Price, Market Cap"),
            ("SEC EDGAR", "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=CRWV", "S-1, 10-K Filings"),
            ("CoreWeave IR", "https://investors.coreweave.com", "Investor Presentations"),
        ]
    }
]


def generate_stock_page(stock):
    """Generate HTML for a single stock page."""
    rec_class = "buy" if stock["recommendation"] == "buy" else "avoid" if stock["recommendation"] == "avoid" else "hold"
    rec_text = stock.get("recommendation_text", stock["recommendation"].upper())

    scores_html = ""
    for name, score in stock["scores"].items():
        scores_html += f"""
          <div class="rating-bar">
            <span class="rating-bar-label">{name}</span>
            <div class="rating-bar-track"><div class="rating-bar-fill" style="width: {score * 10}%"></div></div>
            <span class="rating-bar-value">{score}/10</span>
          </div>"""

    positives_html = ""
    for item in stock.get("positives", []):
        source_link = f' Source: <a href="#" target="_blank">{item[2]}</a>' if len(item) > 2 and item[2] else ""
        positives_html += f"""
        <li>
          <div class="finding-icon positive">✓</div>
          <div class="finding-text"><strong>{item[0]}:</strong> {item[1]}{source_link}</div>
        </li>"""

    risks_html = ""
    for risk in stock.get("risks", []):
        risks_html += f"""
        <li>
          <div class="finding-icon {'warning' if stock['recommendation'] != 'avoid' else 'negative'}">{'!' if stock['recommendation'] != 'avoid' else '✗'}</div>
          <div class="finding-text"><strong>{risk[0]}:</strong> {risk[1]}</div>
        </li>"""

    sources_html = ""
    for source in stock.get("sources", []):
        sources_html += f"""
        <li><a href="{source[1]}" target="_blank">{source[0]}</a> <span class="source-tag">{source[2]}</span></li>"""

    margin_note = f"{stock['margin_of_safety']}% discount to fair value" if stock.get("margin_of_safety") else "N/A"
    target_val = f"HK${stock['target']}" if stock.get("target") and stock["ticker"] not in ["CRWV"] else f"${stock['target']}" if stock.get("target") else "N/A"
    stop_val = f"HK${stock['stop_loss']}" if stock.get("stop_loss") and stock["ticker"] not in ["CRWV"] else f"${stock['stop_loss']}" if stock.get("stop_loss") else "N/A"

    pe_display = f"{stock['pe']:.2f}x" if stock.get("pe") else "N/A (unprofitable)"
    margin_display = f"{stock['margin']}%" if stock.get("margin") else "N/A"
    roe_class = "positive" if stock.get("roe") and stock["roe"] > 15 else "negative" if stock.get("roe") and stock["roe"] < 0 else ""

    yahoo_ticker = f"0{stock['ticker']}.HK" if stock["ticker"] not in ["CRWV"] else "CRWV"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{stock['ticker']}.HK {stock['name']} - Stock Analysis</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="stock-page.css">
</head>
<body>
  <div class="container">
    <a href="../index.html" class="back-link">← Back to Dashboard</a>

    <div class="header">
      <div class="stock-title">
        <h1>{stock['name']}</h1>
        <span class="ticker">{stock['ticker']}.HK{' | ' + stock['chinese'] if stock.get('chinese') else ''}</span>
      </div>
      <div class="badge {rec_class}">{rec_text}</div>
    </div>

    <div class="rating-box">
      <div class="rating-score {rec_class}">{stock['rating']}</div>
      <div class="rating-breakdown">
        <div class="rating-bars">{scores_html}</div>
      </div>
    </div>

    <div class="section">
      <h2>Key Metrics (Live Data)</h2>
      <div class="data-grid">
        <div class="data-item">
          <div class="data-label">
            Current Price
            <a href="https://finance.yahoo.com/quote/{yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value">{'HK$' if stock['ticker'] != 'CRWV' else '$'}{stock['price']:.2f}</div>
          <div class="data-note">Previous Close: {'HK$' if stock['ticker'] != 'CRWV' else '$'}{stock['prev_close']:.2f}</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            Market Cap
            <a href="https://finance.yahoo.com/quote/{yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value">{stock['market_cap']}</div>
          <div class="data-note">{'Mega Cap' if 'T' in stock['market_cap'] else 'Large Cap' if 'B' in stock['market_cap'] else 'Mid Cap'}</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            P/E Ratio (TTM)
            <a href="https://finance.yahoo.com/quote/{yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value">{pe_display}</div>
          <div class="data-note">{'Reasonable' if stock.get('pe') and stock['pe'] < 25 else 'Expensive' if stock.get('pe') and stock['pe'] > 40 else ''}</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            P/B Ratio
            <a href="https://finance.yahoo.com/quote/{yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value {'positive' if stock['pb'] < 1 else ''}">{stock['pb']:.2f}x</div>
          <div class="data-note">{'Deep Value (<1x)' if stock['pb'] < 1 else ''}</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            ROE
            <a href="https://finance.yahoo.com/quote/{yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value {roe_class}">{stock['roe']:.1f}%</div>
          <div class="data-note">{'Excellent (>15%)' if stock.get('roe') and stock['roe'] > 15 else 'Negative' if stock.get('roe') and stock['roe'] < 0 else ''}</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            Profit Margin
            <a href="#" class="data-source" target="_blank">Annual Report →</a>
          </div>
          <div class="data-value {'positive' if stock.get('margin') and stock['margin'] > 20 else 'negative' if stock.get('margin') and stock['margin'] < 0 else ''}">{margin_display}</div>
          <div class="data-note">{'Strong' if stock.get('margin') and stock['margin'] > 20 else ''}</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            Dividend Yield
            <a href="https://finance.yahoo.com/quote/{yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value{' negative' if stock.get('dividend') and stock['dividend'] > 10 else ' gold' if stock.get('dividend') and stock['dividend'] > 3 else ''}">{stock['dividend']:.2f}%{'*' if stock.get('dividend') and stock['dividend'] > 10 else ''}</div>
          <div class="data-note">{'* Potentially unsustainable' if stock.get('dividend') and stock['dividend'] > 10 else ''}</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            52-Week Range
            <a href="https://finance.yahoo.com/quote/{yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value">{'HK$' if stock['ticker'] != 'CRWV' else '$'}{stock['range_low']:.2f} - {stock['range_high']:.2f}</div>
          <div class="data-note">Current: {100 * (stock['price'] - stock['range_low']) / (stock['range_high'] - stock['range_low']):.0f}% of range</div>
        </div>
      </div>
    </div>

    <div class="section">
      <h2>Investment Thesis</h2>
      <ul class="findings-list">
        {positives_html}
        {risks_html}
      </ul>
    </div>

    <div class="section">
      <h2>Valuation & Action</h2>
      <div class="data-grid">
        <div class="data-item">
          <div class="data-label">Intrinsic Value</div>
          <div class="data-value{' positive' if stock.get('intrinsic_value') else ''}">{'HK$' + str(stock['intrinsic_value']) if stock.get('intrinsic_value') and stock['ticker'] != 'CRWV' else '$' + str(stock['intrinsic_value']) if stock.get('intrinsic_value') else 'N/A'}</div>
          <div class="data-note">{'Based on DCF / NAV analysis' if stock.get('intrinsic_value') else 'Too uncertain'}</div>
        </div>
        <div class="data-item">
          <div class="data-label">Margin of Safety</div>
          <div class="data-value{' gold' if stock.get('margin_of_safety') and stock['margin_of_safety'] > 20 else ''}">{f"{stock['margin_of_safety']}%" if stock.get('margin_of_safety') else 'N/A'}</div>
          <div class="data-note">{margin_note}</div>
        </div>
        <div class="data-item">
          <div class="data-label">Target Price</div>
          <div class="data-value{' positive' if stock.get('target') else ''}">{target_val}</div>
          <div class="data-note">{'Upside potential' if stock.get('target') else 'No clear target'}</div>
        </div>
        <div class="data-item">
          <div class="data-label">Stop Loss</div>
          <div class="data-value{' negative' if stock.get('stop_loss') else ''}">{stop_val}</div>
          <div class="data-note">{'Risk management' if stock.get('stop_loss') else 'Not applicable'}</div>
        </div>
      </div>
    </div>

    <div class="section">
      <h2>Data Sources</h2>
      <ul class="sources-list">
        {sources_html}
      </ul>
    </div>

    <div class="footer">
      <p>Analysis Date: 2026-02-20 | Framework: Stock Analysis v1.0</p>
      <p style="margin-top: 8px; font-size: 11px;">Disclaimer: This analysis is for educational purposes only. Not investment advice.</p>
    </div>
  </div>
</body>
</html>"""


def generate_css():
    """Generate shared CSS for stock pages."""
    return """:root {
  --bg-primary: #030712;
  --bg-secondary: #0f172a;
  --bg-card: #1e293b;
  --bg-elevated: #334155;
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  --accent-buy: #10b981;
  --accent-avoid: #ef4444;
  --accent-gold: #f59e0b;
  --accent-blue: #3b82f6;
  --border-color: #334155;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'IBM Plex Sans', sans-serif; background: var(--bg-primary); color: var(--text-primary); min-height: 100vh; }
.container { max-width: 1200px; margin: 0 auto; padding: 24px; }
.back-link { display: inline-flex; align-items: center; gap: 8px; color: var(--accent-blue); text-decoration: none; font-family: 'JetBrains Mono', monospace; font-size: 13px; margin-bottom: 24px; }
.back-link:hover { text-decoration: underline; }
.header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 32px; flex-wrap: wrap; gap: 16px; }
.stock-title h1 { font-family: 'JetBrains Mono', monospace; font-size: 28px; margin-bottom: 8px; }
.stock-title .ticker { background: var(--bg-card); padding: 4px 12px; border-radius: 6px; font-family: 'JetBrains Mono', monospace; font-size: 14px; color: var(--text-muted); }
.badge { padding: 10px 20px; border-radius: 8px; font-family: 'JetBrains Mono', monospace; font-size: 14px; font-weight: 600; }
.badge.buy { background: rgba(16, 185, 129, 0.15); color: var(--accent-buy); border: 2px solid var(--accent-buy); }
.badge.avoid { background: rgba(239, 68, 68, 0.15); color: var(--accent-avoid); border: 2px solid var(--accent-avoid); }
.badge.hold { background: rgba(245, 158, 11, 0.15); color: var(--accent-gold); border: 2px solid var(--accent-gold); }
.rating-box { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 12px; padding: 20px; margin-bottom: 24px; display: flex; align-items: center; gap: 24px; }
.rating-score { width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'JetBrains Mono', monospace; font-size: 28px; font-weight: 700; }
.rating-score.buy { background: rgba(16, 185, 129, 0.2); color: var(--accent-buy); border: 3px solid var(--accent-buy); }
.rating-score.avoid { background: rgba(239, 68, 68, 0.2); color: var(--accent-avoid); border: 3px solid var(--accent-avoid); }
.rating-score.hold { background: rgba(245, 158, 11, 0.2); color: var(--accent-gold); border: 3px solid var(--accent-gold); }
.rating-breakdown { flex: 1; }
.rating-bars { display: flex; flex-direction: column; gap: 8px; }
.rating-bar { display: flex; align-items: center; gap: 12px; }
.rating-bar-label { font-size: 12px; color: var(--text-secondary); width: 140px; }
.rating-bar-track { flex: 1; height: 8px; background: var(--bg-elevated); border-radius: 4px; overflow: hidden; }
.rating-bar-fill { height: 100%; border-radius: 4px; background: var(--accent-buy); }
.rating-bar-value { font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--text-muted); width: 40px; }
.section { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 12px; padding: 24px; margin-bottom: 24px; }
.section h2 { font-family: 'JetBrains Mono', monospace; font-size: 16px; margin-bottom: 16px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 1px; }
.data-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
.data-item { background: var(--bg-card); padding: 16px; border-radius: 8px; }
.data-label { font-size: 12px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center; }
.data-source { font-size: 10px; color: var(--accent-blue); text-decoration: none; }
.data-source:hover { text-decoration: underline; }
.data-value { font-family: 'JetBrains Mono', monospace; font-size: 24px; font-weight: 600; }
.data-value.positive { color: var(--accent-buy); }
.data-value.negative { color: var(--accent-avoid); }
.data-value.gold { color: var(--accent-gold); }
.data-note { font-size: 11px; color: var(--text-muted); margin-top: 8px; }
.findings-list { list-style: none; }
.findings-list li { padding: 12px 0; border-bottom: 1px solid var(--border-color); display: flex; gap: 12px; }
.findings-list li:last-child { border-bottom: none; }
.finding-icon { width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; flex-shrink: 0; }
.finding-icon.positive { background: rgba(16, 185, 129, 0.2); color: var(--accent-buy); }
.finding-icon.negative { background: rgba(239, 68, 68, 0.2); color: var(--accent-avoid); }
.finding-icon.warning { background: rgba(245, 158, 11, 0.2); color: var(--accent-gold); }
.finding-text { font-size: 14px; line-height: 1.5; color: var(--text-secondary); }
.finding-text strong { color: var(--text-primary); }
.finding-text a { color: var(--accent-blue); }
.sources-list { list-style: none; }
.sources-list li { padding: 8px 0; border-bottom: 1px solid var(--border-color); font-size: 13px; }
.sources-list li:last-child { border-bottom: none; }
.sources-list a { color: var(--accent-blue); text-decoration: none; }
.sources-list a:hover { text-decoration: underline; }
.source-tag { font-size: 10px; background: var(--bg-elevated); padding: 2px 6px; border-radius: 4px; margin-left: 8px; color: var(--text-muted); }
.footer { margin-top: 48px; padding: 24px 0; border-top: 1px solid var(--border-color); text-align: center; color: var(--text-muted); font-size: 12px; }
@media (max-width: 768px) { .data-grid { grid-template-columns: 1fr; } .header { flex-direction: column; } .rating-box { flex-direction: column; } }
"""


def main():
    # Generate CSS
    with open(os.path.join(STOCKS_DIR, "stock-page.css"), "w") as f:
        f.write(generate_css())
    print("Generated stock-page.css")

    # Generate stock pages
    for stock in STOCKS:
        filename = f"{stock['ticker']}.html"
        filepath = os.path.join(STOCKS_DIR, filename)
        with open(filepath, "w") as f:
            f.write(generate_stock_page(stock))
        print(f"Generated {filename}")

    print(f"\nGenerated {len(STOCKS)} stock pages in {STOCKS_DIR}")


if __name__ == "__main__":
    main()
