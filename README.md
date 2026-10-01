# RiskPulse - S&P Global & Crisil Campus Hackathon

**Candidate Name:** Abhi Pandey  
**College:** VIT Bhopal University  
**Specialization:** B.Tech CSE (AI & ML)  

---

> *"Turning financial noise into actionable risk signals."*

---

## Project Overview

**RiskPulse** is an AI/NLP-powered financial risk intelligence platform built for the S&P Global & Crisil Campus Hackathon 2026. The platform bridges the gap between unstructured textual data (news headlines, press announcements, analyst commentary, and market social streams) and quantitative financial decision support.

RiskPulse ingests multi-source unstructured financial information, standardizes it through text preprocessing and entity normalization, executes an interpretable NLP risk pipeline (Sentiment Scoring, Event Classification, Prototype Risk Impact Scoring), and connects these signals directly to an automated portfolio stress-testing engine.

---

## Problem Statement

Financial analysts, risk managers, and investment committees face an overwhelming influx of daily financial news and social chatter. Key challenges include:

1. **Information Overload:** Critical risk signals are buried inside thousands of daily unstructured articles and commentaries.
2. **Delayed Response:** Translating breaking geopolitical, macroeconomic, or credit events into quantitative risk assessments traditionally requires manual review.
3. **Decoupled Workflows:** Text analysis and portfolio risk management are often isolated silos. Analysts read news in one tool and run risk models in another, leading to delayed stress testing during market shocks.

---

## Solution

RiskPulse provides an end-to-end automated pipeline:

1. **Multi-Source Ingestion:** Ingests unstructured data from financial news reports and social sentiment feeds.
2. **NLP Risk Engine:**
   - **Sentiment Scoring:** Normalized score from `-1.0` (very negative) to `+1.0` (very positive).
   - **Event Classification:** Categorizes events into 8 distinct financial types (*Geopolitical*, *Macroeconomic*, *Credit Event*, *Merger/Acquisition*, *Product Launch*, *Regulatory*, *Earnings/Financial*, *Other*).
   - **Prototype Risk Impact Score:** Transparent 1–10 impact index reflecting event category severity, sentiment intensity, and financial risk terminology.
3. **Automated Stress Testing (Module B):** When a high-impact risk signal (Impact Score $\ge 7$) is detected, the system triggers pre-defined synthetic shock scenarios across a multi-asset portfolio (Equity, Corporate Bonds, Government Bonds, Loans, Commodities) to calculate before-and-after valuations and potential losses.
4. **Analyst Dashboard & REST API:** Real-time visibility into incoming signals, sentiment distributions, company-specific exposure, and portfolio shocks.

---

## Architecture

```text
 ┌─────────────────────────┐      ┌─────────────────────────┐
 │ Financial News Feed     │      │ Market Social Feed      │
 └────────────┬────────────┘      └────────────┬────────────┘
              │                                │
              └───────────────┬────────────────┘
                              ▼
               ┌──────────────────────────────┐
               │    Data Ingestion Layer      │
               │ (Cleaning, Validation, Entity)│
               └──────────────┬───────────────┘
                              ▼
               ┌──────────────────────────────┐
               │       NLP Risk Engine        │
               │  - Sentiment Score (-1 to 1) │
               │  - Event Classification      │
               │  - Prototype Impact Score    │
               └──────────────┬───────────────┘
                              ▼
               ┌──────────────────────────────┐
               │     Risk Signal Storage      │
               │  (Structured SQLite / JSON)  │
               └──────────────┬───────────────┘
                              │
               ┌──────────────┴───────────────┐
               ▼                              ▼
 ┌───────────────────────────┐  ┌───────────────────────────┐
 │   FastAPI REST Engine     │  │ Strategic Stress Testing  │
 │  - /analyze               │  │  - Impact >= 7 Trigger    │
 │  - /signals               │  │  - Scenario Shocks        │
 │  - /portfolio             │  │  - Valuation Delta (ΔV)   │
 └─────────────┬─────────────┘  └─────────────┬─────────────┘
               │                              │
               └──────────────┬───────────────┘
                              ▼
               ┌──────────────────────────────┐
               │  React Analytics Dashboard   │
               │ (Recharts, Signal Filters)   │
               └──────────────────────────────┘
```

---

## Tech Stack

The architecture focuses on transparent, explainable, and industry-standard tools:

- **Backend:** Python 3.10+, FastAPI (asynchronous REST API), Pydantic v2 (data validation & schemas), Pandas & NumPy (data transformations and portfolio math), SQLite (lightweight persistent store).
- **NLP & Machine Learning:** scikit-learn (vectorization and classification), rule-enhanced financial lexicons for deterministic scoring and confidence estimation.
- **Frontend:** React (Vite-powered SPA), Modern CSS, Recharts (financial data visualization).
- **Environment & Quality:** Git, GitHub, pytest.

---

## Dataset

To ensure immediate reproducibility without external paid API rate limits or keys, RiskPulse includes synthetically curated benchmark datasets:

1. **Financial News (`data/news_sample.csv`):** Structured records containing `id`, `timestamp`, `source`, `company`, `headline`, and `article_text`.
2. **Social Media (`data/social_sample.csv`):** Compact social commentary records containing `id`, `timestamp`, `source`, `company`, and `text`.
3. **Synthetic Portfolio (`data/portfolio.csv`):** Multi-asset portfolio with `asset_id`, `asset_name`, `asset_type`, `sector`, `value`, `duration`, and `credit_risk`.

> **Note on Data Authenticity:** All benchmark records are synthetic datasets created for demonstration purposes and do not represent proprietary feeds from S&P Global, CRISIL, Bloomberg, Reuters, or X/Twitter.

---

## NLP Risk Engine

The risk engine exposes an interpretable, verifiable pipeline:

```python
def analyze_text(text: str, company: str) -> dict:
    sentiment = get_sentiment(text)
    event_type, confidence = classify_event(text)
    impact_score = calculate_impact(sentiment, event_type, text)
    risk_level = map_impact_to_level(impact_score)

    return {
        "company": company,
        "sentiment_score": sentiment,
        "event_type": event_type,
        "impact_score": impact_score,
        "risk_level": risk_level,
        "confidence": confidence
    }
```

- **Sentiment Range:** Normalized continuous scale from `-1.0` (Very Negative) to `+1.0` (Very Positive) mapped to human-readable labels (`Negative`, `Neutral`, `Positive`).
- **Event Taxonomy:** 8 standard event categories ensuring direct analyst comprehension.
- **Prototype Risk Impact Score:** 1 to 10 scale categorized into *Low (1–3)*, *Moderate (4–6)*, *High (7–8)*, and *Critical (9–10)*.

---

## Portfolio Stress Testing

When a risk signal with `impact_score >= 7` is detected, RiskPulse evaluates the signal against the portfolio using Module B (Strategic Portfolio Stress Testing).

### Synthetic Scenario Shock Matrix

| Event Category | Equity Shock | Corporate Bond Shock | Govt Bond Shock | Commodity Shock |
| :--- | :---: | :---: | :---: | :---: |
| **Geopolitical** | -10% | -5% | +2% | +8% |
| **Macroeconomic** | -7% | -5% | -3% | -2% |
| **Credit Event** | -8% | -12% | +1% | 0% |
| **Regulatory** | -6% | -2% | 0% | 0% |

Metrics generated:
- **Baseline Portfolio Value ($V_0$)**
- **Stressed Portfolio Value ($V_1$)**
- **Absolute Net Impact ($\Delta V = V_1 - V_0$)**
- **Percentage Drawdown ($\% \Delta V$)**

*All shock assumptions are synthetic illustrative stress scenarios for hackathon evaluation and do not represent actual market forecasts.*

---

## API Endpoints

- `GET /health` - Health check and engine readiness.
- `POST /analyze` - Ingests single text payload and generates sentiment, classification, and impact score.
- `GET /signals` - Retrieves historical risk signals with filtering options.
- `GET /signals/{company}` - Retrieves risk signals specific to a company.
- `GET /portfolio` - Fetches synthetic portfolio holdings and asset breakdowns.
- `POST /stress-test` - Runs scenario shock simulation on current portfolio holdings.

---

## Dashboard

The user interface follows a modern, institutional financial analytics layout:
- **Top Metrics:** Total Signals Processed, High Impact Alerts ($\ge 7$), Average Market Sentiment, Portfolio Exposure.
- **Visualizations:**
  1. Risk Signals Timeline.
  2. Sentiment Distribution Histogram.
  3. Event Category Breakdown.
  4. Company Risk Concentration Table.
  5. Interactive Before vs. After Portfolio Stress Test Comparison.
- **Signal Feed:** Filterable by entity, event category, source, and severity.

---

## Results

Initial prototype benchmarks:
- **Processing Latency:** Sub-50ms inference time per text record on CPU.
- **Rule & ML Classification:** Clear explainability with zero black-box ambiguity.
- **Stress-Test Integration:** Instantaneous recalculation of asset valuations upon signal trigger.

---

## Limitations

1. **Synthetic Assumptions:** Stress-test shocks are heuristic hackathon assumptions rather than calibrated historical econometric models.
2. **Static Demonstrative Datasets:** Uses pre-bundled representative datasets rather than direct live streaming sockets.
3. **Lexicon Coverage:** Highly specialized slang or emerging non-traditional financial idioms may require expanded vocabulary coverage.

---

## Future Improvements

1. Integration of fine-tuned FinBERT / transformer embeddings for domain-specific nuance.
2. Real-time RSS and SEC EDGAR filing connectors.
3. Historical backtesting against actual market volatility events.
4. VaR (Value at Risk) and CVaR calculations for enterprise compliance.

---

## Quickstart

### Prerequisites
- Python 3.10+
- Node.js 18+ (for frontend)
- Git

### Backend Setup

```bash
# 1. Clone repository
git clone https://github.com/Abhi4621/VIT-Bhopal-Abhi-Pandey-S-P-Crisil-hackathon.git
cd VIT-Bhopal-Abhi-Pandey-S-P-Crisil-hackathon

# 2. Set up virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start backend server
uvicorn backend.main:app --reload --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## Demo Walkthrough

1. Open the RiskPulse dashboard in your browser (`http://localhost:5173`).
2. Review ingested financial news and social media records.
3. Inspect the NLP analysis showing sentiment, detected event type, and prototype impact score.
4. Select a critical event (e.g. Geopolitical shock with Impact Score 9).
5. Click **Run Stress Test** to observe the instant portfolio revaluation and asset-level drawdown calculations.

---

## Project Structure

```text
riskpulse/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── api/
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── ingestion/
│   │   ├── news_loader.py
│   │   └── social_loader.py
│   ├── nlp/
│   │   ├── sentiment.py
│   │   ├── event_classifier.py
│   │   ├── impact_score.py
│   │   └── risk_engine.py
│   ├── portfolio/
│   │   ├── portfolio.py
│   │   └── stress_test.py
│   └── database/
│       └── db.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│   └── package.json
├── data/
│   ├── news_sample.csv
│   ├── social_sample.csv
│   └── portfolio.csv
└── docs/
    └── architecture.png
```
