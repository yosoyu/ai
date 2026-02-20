#!/usr/bin/env python3
"""
Bridge between stock-analysis-framework and stock-analysis-site.
Reads analysis phase files and generates/updates website pages.
"""

import os
import re
import json
from pathlib import Path

# Paths
AI_DIR = Path("/Users/colinyu/Projects/ai/stock analysis")
SITE_DIR = Path("/Users/colinyu/Projects/ai/stock analysis/stock-analysis-site")
STOCKS_DIR = SITE_DIR / "stocks"

# Stock folder mapping (analysis folder -> ticker)
STOCK_FOLDERS = {
    "6896": {"ticker": "6896", "name": "Golden Throat", "yahoo_ticker": "6896.HK"},
    "683": {"ticker": "683", "name": "Kerry Properties", "yahoo_ticker": "683.HK"},
    "700": {"ticker": "700", "name": "Tencent", "yahoo_ticker": "700.HK"},
    "9988": {"ticker": "9988", "name": "Alibaba", "yahoo_ticker": "9988.HK"},
    "133": {"ticker": "133", "name": "China Merchants CDI", "yahoo_ticker": "133.HK"},
    "9961": {"ticker": "9961", "name": "Trip.com", "yahoo_ticker": "9961.HK"},
    "3690": {"ticker": "3690", "name": "Meituan", "yahoo_ticker": "3690.HK"},
    "728": {"ticker": "728", "name": "China Telecom", "yahoo_ticker": "728.HK"},
    "941": {"ticker": "941", "name": "China Mobile", "yahoo_ticker": "941.HK"},
    "COREWEAVE": {"ticker": "CRWV", "name": "CoreWeave", "yahoo_ticker": "CRWV"},
}


def parse_phase5_report(folder_path):
    """Parse phase5_final_report.md to extract key data."""
    phase5_path = folder_path / "analysis" / "phase5_final_report.md"
    if not phase5_path.exists():
        return None

    content = phase5_path.read_text()

    data = {
        "ticker": "",
        "name": "",
        "recommendation": "HOLD",
        "rating": 0,
        "price": 0,
        "currency": "HK$",
        "market_cap": "",
        "pe": None,
        "pb": None,
        "roe": "",
        "margin": "",
        "dividend": "",
        "intrinsic_value": None,
        "margin_of_safety": "",
        "target": None,
        "stop_loss": None,
        "positives": [],
        "risks": [],
        "sources": [],
        "scores": {},
    }

    # Extract stock name and ticker
    stock_match = re.search(r"\*\*Stock:\*\*\s*(\S+)\s*-\s*(.+)", content)
    if stock_match:
        data["ticker"] = stock_match.group(1).replace(".HK", "")
        data["name"] = stock_match.group(2).strip()

    # Extract recommendation
    if "✅ BUY" in content or "# ✅ BUY" in content or "RECOMMENDATION: BUY" in content:
        data["recommendation"] = "buy"
    elif "❌ AVOID" in content or "# ❌ AVOID" in content or "RECOMMENDATION: AVOID" in content:
        data["recommendation"] = "avoid"
    elif "⚠️ HOLD" in content or "SPECULATIVE BUY" in content or "RECOMMENDATION: HOLD" in content:
        data["recommendation"] = "hold"

    # Extract executive summary metrics (table format: | **Metric** | Value | ...)
    # Look for the next ## heading as the section boundary
    exec_summary = re.search(r"## Executive Summary(.+?)(?=##)", content, re.DOTALL)
    if exec_summary:
        summary_text = exec_summary.group(1)

        # Price - handles | **Current Price** | HK$20.56 | or | **Current Price** | ~HK$3.18-3.22 |
        price_match = re.search(r"\|\s*\*\*Current Price\*\*\s*\|\s*[~]?(?:HK)?\$?([\d.]+)", summary_text)
        if price_match:
            data["price"] = float(price_match.group(1))

        # P/E - handles | **P/E Ratio** | 7.76x | or | **P/E (TTM)** | 21.8x |
        pe_match = re.search(r"\|\s*\*\*P/E(?:\s*(?:Ratio|\([^)]+\)))?\*\*\s*\|\s*([\d.]+)(?:-[\d.]+)?x", summary_text)
        if pe_match:
            data["pe"] = float(pe_match.group(1))

        # P/B - handles | **P/B Ratio** | 1.72x | or | **P/B Ratio** | **0.29x** |
        pb_match = re.search(r"\|\s*\*\*P/B(?:\s*Ratio)?\*\*\s*\|\s*\*{0,2}([\d.]+)\*{0,2}x", summary_text)
        if pb_match:
            data["pb"] = float(pb_match.group(1))

        # ROE - handles | **ROE** | 21.5% |
        roe_match = re.search(r"\|\s*\*\*ROE\*\*\s*\|\s*([\d.]+)%", summary_text)
        if roe_match:
            data["roe"] = f"{float(roe_match.group(1)):.1f}%"

        # Dividend - handles | **Dividend Yield** | ~15.7% | or | **Dividend Yield** | **6.5%** |
        div_match = re.search(r"\|\s*\*\*Dividend Yield\*\*\s*\|\s*\*{0,2}[~]?([\d.]+)%", summary_text)
        if div_match:
            data["dividend"] = f"{float(div_match.group(1)):.2f}%"

        # Intrinsic Value - from table | **Intrinsic Value** | HK$4.07 |
        iv_match = re.search(r"\|\s*\*\*Intrinsic Value\*\*\s*\|\s*(?:HK)?\$?([\d.]+)", content)
        if iv_match:
            data["intrinsic_value"] = float(iv_match.group(1))

        # Margin of Safety - handles | **Discount to Book** | 71% |
        mos_match = re.search(r"\|\s*\*\*Discount to Book\*\*\s*\|\s*(\d+)%", summary_text)
        if mos_match:
            data["margin_of_safety"] = f"{float(mos_match.group(1)):.1f}%"

    # Extract rating score - handles | **Total** | | 100% | **5.25/10** |
    rating_match = re.search(r"\|\s*\*\*Total\*\*\s*\|[^|]*\|[^|]*\|\s*\*\*([\d.]+)/10\*\*", content)
    if rating_match:
        data["rating"] = float(rating_match.group(1))

    # Also try ASCII box format: RATING: 8.2 / 10
    if data["rating"] == 0:
        ascii_rating_match = re.search(r"RATING:\s*([\d.]+)\s*/\s*10", content)
        if ascii_rating_match:
            data["rating"] = float(ascii_rating_match.group(1))

    # Extract individual scores
    scores_section = re.search(r"## Investment Rating(.+?)\*\*Rating:", content, re.DOTALL)
    if scores_section:
        for match in re.finditer(r"\|\s*([\w\s]+)\s*\|\s*(\d+)/10\s*\|", scores_section.group(1)):
            category = match.group(1).strip()
            score = int(match.group(2))
            data["scores"][category] = score

    # Extract positive factors - handles ### Positive Factors followed by numbered list
    positives_section = re.search(r"### Positive Factors.*?(?=### |## |---)", content, re.DOTALL)
    if positives_section:
        for match in re.finditer(r"\d+\.\s+\*\*(.+?)\*\*\s*(.+?)(?=\n\d+\.|\n\n###|\Z)", positives_section.group(0), re.DOTALL):
            title = match.group(1).strip()
            desc = match.group(2).strip().replace("\n", " ")[:200]  # Limit description length
            data["positives"].append((title, desc))

    # Extract risk factors - handles ### Risk Factors or ### Critical Red Flags followed by numbered list
    # Look for "Risk Factors" or "Critical Red Flags" specifically
    risks_section = re.search(r"### (Risk Factors|Critical Red Flags).*?(?=### |## |---)", content, re.DOTALL)
    if risks_section:
        for match in re.finditer(r"\d+\.\s+\*\*(.+?)\*\*\s*(.+?)(?=\n\d+\.|\n\n###|\Z)", risks_section.group(0), re.DOTALL):
            title = match.group(1).strip()
            desc = match.group(2).strip().replace("\n", " ")[:200]  # Limit description length
            data["risks"].append((title, desc))

    return data


def parse_progress_json(folder_path):
    """Parse progress.json for additional data."""
    progress_path = folder_path / "analysis" / "progress.json"
    if not progress_path.exists():
        return None

    with open(progress_path) as f:
        return json.load(f)


def generate_stock_html(stock_data, folder_info):
    """Generate HTML page for a stock."""
    ticker = folder_info["ticker"]
    name = stock_data.get("name", folder_info["name"])
    yahoo_ticker = folder_info["yahoo_ticker"]

    rec_class = stock_data["recommendation"]
    rec_text = {"buy": "BUY", "avoid": "AVOID", "hold": "HOLD"}.get(rec_class, "HOLD")

    # Generate scores HTML
    scores_html = ""
    for cat, score in stock_data.get("scores", {}).items():
        scores_html += f"""
          <div class="rating-bar">
            <span class="rating-bar-label">{cat}</span>
            <div class="rating-bar-track"><div class="rating-bar-fill" style="width: {score * 10}%"></div></div>
            <span class="rating-bar-value">{score}/10</span>
          </div>"""

    # Generate positives HTML
    positives_html = ""
    for title, desc in stock_data.get("positives", [])[:4]:
        positives_html += f"""
        <li>
          <div class="finding-icon positive">✓</div>
          <div class="finding-text"><strong>{title}:</strong> {desc}</div>
        </li>"""

    # Generate risks HTML
    risks_html = ""
    for title, desc in stock_data.get("risks", [])[:4]:
        risks_html += f"""
        <li>
          <div class="finding-icon {'warning' if rec_class != 'avoid' else 'negative'}">{'!' if rec_class != 'avoid' else '✗'}</div>
          <div class="finding-text"><strong>{title}:</strong> {desc}</div>
        </li>"""

    # Format values
    price = stock_data.get("price", 0)
    currency = "$" if ticker == "CRWV" else "HK$"
    pe_display = f"{stock_data['pe']:.2f}x" if stock_data.get("pe") else "N/A"
    pb_display = f"{stock_data['pb']:.2f}x" if stock_data.get("pb") else "N/A"
    pb_class = "positive" if stock_data.get("pb") and stock_data["pb"] < 1 else ""
    roe_class = "positive" if stock_data.get("roe") and float(stock_data["roe"].replace("%", "")) > 15 else ""
    rating_class = "positive" if stock_data["rating"] >= 7 else "negative" if stock_data["rating"] < 6 else ""
    iv_display = f"{currency}{stock_data['intrinsic_value']:.0f}" if stock_data.get("intrinsic_value") else "N/A"
    iv_class = "positive" if stock_data.get("intrinsic_value") else ""
    mos_display = stock_data.get("margin_of_safety", "N/A")
    mos_class = "gold" if stock_data.get("margin_of_safety") else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{ticker}.HK {name} - Stock Analysis</title>
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
        <h1>{name}</h1>
        <span class="ticker">{ticker}{'HK' if ticker != 'CRWV' else ''}</span>
      </div>
      <div class="badge {rec_class}">{rec_text}</div>
    </div>

    <div class="rating-box">
      <div class="rating-score {rec_class}">{stock_data['rating']:.1f}</div>
      <div class="rating-breakdown">
        <div class="rating-bars">{scores_html}</div>
      </div>
    </div>

    <div class="section">
      <h2>Key Metrics</h2>
      <div class="data-grid">
        <div class="data-item">
          <div class="data-label">
            Current Price
            <a href="https://finance.yahoo.com/quote/{'0' + yahoo_ticker if ticker != 'CRWV' else yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value">{currency}{price:.2f}</div>
          <div class="data-note">From analysis report</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            P/E Ratio
            <a href="https://finance.yahoo.com/quote/{'0' + yahoo_ticker if ticker != 'CRWV' else yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value">{pe_display}</div>
          <div class="data-note">TTM</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            P/B Ratio
            <a href="https://finance.yahoo.com/quote/{'0' + yahoo_ticker if ticker != 'CRWV' else yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value {pb_class}">{pb_display}</div>
          <div class="data-note">{'Deep Value' if stock_data.get('pb') and stock_data['pb'] < 1 else ''}</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            ROE
            <a href="https://finance.yahoo.com/quote/{'0' + yahoo_ticker if ticker != 'CRWV' else yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value {roe_class}">{stock_data.get('roe', 'N/A')}</div>
          <div class="data-note">{'Excellent' if stock_data.get('roe') and float(stock_data['roe'].replace('%', '')) > 15 else ''}</div>
        </div>
        <div class="data-item">
          <div class="data-label">
            Dividend Yield
            <a href="https://finance.yahoo.com/quote/{'0' + yahoo_ticker if ticker != 'CRWV' else yahoo_ticker}" class="data-source" target="_blank">Yahoo Finance →</a>
          </div>
          <div class="data-value">{stock_data.get('dividend', '0%')}</div>
          <div class="data-note"></div>
        </div>
        <div class="data-item">
          <div class="data-label">
            Rating
          </div>
          <div class="data-value {rating_class}">{stock_data['rating']:.1f}/10</div>
          <div class="data-note">Investment rating</div>
        </div>
        <div class="data-item">
          <div class="data-label">Intrinsic Value</div>
          <div class="data-value {iv_class}">{iv_display}</div>
          <div class="data-note">From DCF/EPV analysis</div>
        </div>
        <div class="data-item">
          <div class="data-label">Margin of Safety</div>
          <div class="data-value {mos_class}">{mos_display}</div>
          <div class="data-note">Discount to fair value</div>
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
      <h2>Data Sources</h2>
      <ul class="sources-list">
        <li><a href="https://finance.yahoo.com/quote/{'0' + yahoo_ticker if ticker != 'CRWV' else yahoo_ticker}" target="_blank">Yahoo Finance</a> <span class="source-tag">Price, P/E, P/B</span></li>
        <li><a href="https://www1.hkexnews.hk" target="_blank">HKEX News</a> <span class="source-tag">Annual Reports</span></li>
        <li><a href="../analysis/phase5_final_report.md">Phase 5 Report</a> <span class="source-tag">Full Analysis</span></li>
      </ul>
    </div>

    <div class="footer">
      <p>Analysis Date: 2026-02-20 | Framework: Stock Analysis v1.0</p>
      <p style="margin-top: 8px; font-size: 11px;">Disclaimer: This analysis is for educational purposes only. Not investment advice.</p>
    </div>
  </div>
</body>
</html>"""


def generate_index_data(all_stocks):
    """Generate JavaScript data for index.html."""
    js_stocks = []
    for stock_data, folder_info in all_stocks:
        if not stock_data:
            continue

        ticker = folder_info["ticker"]
        ticker_display = ticker if ticker == "CRWV" else f"{ticker}.HK"
        currency = "$" if ticker == "CRWV" else "HK$"

        # Extract positive highlights
        pos_highlights = [p[0] for p in stock_data.get("positives", [])[:2]]
        neg_highlights = [r[0] for r in stock_data.get("risks", [])[:2]]

        # Escape single quotes in name
        stock_name = stock_data.get("name", folder_info["name"]).replace("'", "\\'")

        # Build target value
        target_val = "null"
        if stock_data.get("intrinsic_value"):
            target_val = f'"HK${int(stock_data["intrinsic_value"])}"'

        js_stock = f"""      {{
        id: '{ticker}',
        ticker: '{ticker_display}',
        name: '{stock_name}',
        price: {stock_data.get("price", 0)},
        currency: '{currency}',
        recommendation: '{stock_data["recommendation"]}',
        rating: {stock_data["rating"]},
        pe: {stock_data.get("pe") or "null"},
        pb: {stock_data.get("pb") or "null"},
        roe: '{stock_data.get("roe", "-")}',
        marginOfSafety: '{stock_data.get("margin_of_safety", "-")}',
        dividend: '{stock_data.get("dividend", "0%")}',
        target: {target_val},
        highlights: [],
        risk: '',
        riskColor: 'normal',
        positiveHighlights: {json.dumps(pos_highlights)},
        negativeHighlights: {json.dumps(neg_highlights)}
      }}"""
        js_stocks.append(js_stock)

    return ",\n".join(js_stocks)


def main():
    print("Stock Analysis Framework → Site Bridge")
    print("=" * 50)

    all_stocks = []

    for folder_name, folder_info in STOCK_FOLDERS.items():
        folder_path = AI_DIR / folder_name
        if not folder_path.exists():
            print(f"⚠️  {folder_name}: Folder not found")
            continue

        # Parse phase5 report
        stock_data = parse_phase5_report(folder_path)
        if not stock_data:
            print(f"⚠️  {folder_name}: No phase5 report found")
            continue

        # Override with folder info
        stock_data["ticker"] = folder_info["ticker"]
        stock_data["name"] = stock_data.get("name") or folder_info["name"]

        all_stocks.append((stock_data, folder_info))

        # Generate HTML page
        html = generate_stock_html(stock_data, folder_info)
        output_path = STOCKS_DIR / f"{folder_info['ticker']}.html"
        output_path.write_text(html)
        print(f"✅ {folder_info['ticker']}: Generated {stock_data['name']} (Rating: {stock_data['rating']:.1f}/10, {stock_data['recommendation'].upper()})")

    print(f"\nGenerated {len(all_stocks)} stock pages")
    print(f"Output: {STOCKS_DIR}")

    # Generate index data snippet
    js_data = generate_index_data(all_stocks)
    print(f"\n--- JavaScript Data for index.html ---")
    print(f"const stocks = [\n{js_data}\n];")


if __name__ == "__main__":
    main()
