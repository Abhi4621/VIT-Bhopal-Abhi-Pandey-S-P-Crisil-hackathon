
# RiskPulse: AI-Powered Financial Risk Analysis and Portfolio Stress Testing

**Project Documentation — S&P Global & CRISIL Campus Hackathon 2026**

- **Candidate:** Abhi Pandey
- **Registration Number:** 23BAI10909
- **Institution:** VIT Bhopal University, Madhya Pradesh, India
- **Course:** B.Tech Computer Science and Engineering (AI & ML)

**GitHub Repository:** [RiskPulse](https://github.com/Abhi4621/VIT-Bhopal-Abhi-Pandey-S-P-Crisil-hackathon)

**Live Demo:** [Open RiskPulse](https://vit-bhopal-abhi-pandey-s-p-crisil-h.vercel.app/)

---

## 1. Project Overview

RiskPulse is a financial risk analysis platform designed to help users understand how financial news and major economic events may affect investments.

Financial news can influence company performance, stock prices, and market conditions. Manually reviewing news from multiple sources and estimating its possible effect on an investment portfolio can take time.

RiskPulse aims to simplify this process by analysing financial news, identifying important events, assigning risk scores, and estimating the possible impact on a sample investment portfolio.

The project combines Natural Language Processing (NLP), financial risk analysis, and an interactive dashboard.

## 2. Problem Statement

Financial markets are affected by events such as interest rate changes, company announcements, economic uncertainty, geopolitical conflicts, and supply chain disruptions.

Investors and analysts may face several challenges:

- Financial news is spread across multiple sources.
- Understanding whether news is positive or negative requires analysis.
- Identifying affected companies and sectors can be difficult.
- Estimating the possible impact on an investment portfolio requires additional calculations.
- Manual analysis can delay risk assessment.

**The main problem is how to convert financial news into useful risk information and estimate its potential impact on an investment portfolio.**

## 3. Proposed Solution

RiskPulse provides a single platform for financial news analysis and portfolio stress testing.

The system processes financial news, analyses its sentiment, identifies relevant companies or events, and generates risk information. Users can then explore how selected scenarios might affect a sample portfolio.

### Project Objectives

1. Reduce the effort required to review financial news.
2. Identify potentially important financial events.
3. Present sentiment and risk information clearly.
4. Estimate portfolio losses under selected hypothetical scenarios.
5. Display the results through an interactive dashboard.

RiskPulse is a decision-support tool. Its outputs are estimates, not guaranteed predictions of future market movements.

## 4. Key Features

### 4.1 Financial News Collection

Collects news from supported financial RSS feeds so users can review information from different sources.

### 4.2 Sentiment Analysis

Analyses financial text to estimate whether its sentiment is positive, negative, or neutral.

FinBERT can be used for domain-specific financial sentiment analysis when enabled in the implementation.

### 4.3 Financial Event Analysis

Identifies relevant financial events and associated companies or sectors where supported.

### 4.4 Risk Scoring

Assigns risk or impact scores to help users identify news items that may require further attention.

### 4.5 Portfolio Stress Testing

Estimates how a sample portfolio may change under hypothetical market scenarios.

### 4.6 Interactive Dashboard

Presents news signals, risk scores, and stress-testing results in a visual format.

> Note: Include only features that are implemented and working in the submitted version.

## 5. Technology Stack

The project uses a combination of web development, data processing, and NLP technologies.

| Technology | Purpose |
|---|---|
| Python | Backend logic and financial analysis |
| FastAPI | REST API development |
| FinBERT / PyTorch | Financial sentiment analysis, if enabled |
| React | Interactive user interface |
| Vite | Frontend development and build tooling |
| Tailwind CSS | Dashboard styling |
| SQLite | Data storage, if used by the deployed backend |
| RSS feeds | Financial news collection |
| Vercel | Deployment, according to the project configuration |

The final technology list should match the actual source code, dependencies, and deployment setup.

## 6. System Workflow

RiskPulse follows a sequence of steps to turn financial news into risk information.

1. **Collect News:** Retrieve news from supported sources.
2. **Process Text:** Clean the text and check for duplicate items.
3. **Analyse Sentiment:** Estimate the sentiment using the configured NLP method.
4. **Identify Events:** Identify relevant companies, sectors, or financial events where supported.
5. **Calculate Risk:** Generate a risk score using the implemented scoring rules.
6. **Run Stress Tests:** Apply a selected hypothetical scenario to the sample portfolio.
7. **Display Results:** Present the analysis on the dashboard.

### Workflow Diagram

```text
Financial News
      |
      v
Text Processing
      |
      v
Sentiment Analysis
      |
      v
Event Identification
      |
      v
Risk Scoring
      |
      v
Portfolio Stress Testing
      |
      v
Results Dashboard
```

## 7. Financial Risk Analysis

RiskPulse connects information extracted from financial news with quantitative portfolio analysis.

### 7.1 Sentiment Score

If the model provides positive and negative class probabilities, sentiment polarity can be calculated as:

\[
S=P(\text{Positive})-P(\text{Negative})
\]

The score ranges from -1 to +1.

- A positive score indicates positive sentiment.
- A negative score indicates negative sentiment.
- A score close to zero indicates more neutral or balanced sentiment.

This score represents the model's interpretation of the text. It does not directly predict future stock returns.

### 7.2 Risk or Impact Score

The system uses scoring rules to represent the potential importance of a financial news event.

Depending on the implementation, the score may consider sentiment, event category, and event severity.

A higher score indicates that an event may deserve more attention under the configured scoring method. It should not be interpreted as a calibrated probability of financial loss unless that calibration has been validated.

### 7.3 Portfolio Stress Testing

Stress testing estimates how a portfolio may behave under a hypothetical market event.

For example, a scenario may model a market decline or an increase in interest rates. The resulting portfolio value is compared with its initial value.

\[
\text{Portfolio Loss}=V_{\text{initial}}-V_{\text{stressed}}
\]

\[
\text{Loss Percentage}=
\frac{\text{Portfolio Loss}}{V_{\text{initial}}}\times100
\]

These calculations help users understand possible exposure under selected assumptions.

### 7.4 Value-at-Risk and Conditional Value-at-Risk

If supported by the implementation, Value-at-Risk (VaR) estimates a loss threshold at a selected confidence level.

Conditional Value-at-Risk (CVaR), also known as Expected Shortfall in common risk-management usage, estimates the average loss in the tail beyond a VaR threshold under the chosen model.

These are model-based estimates, not guarantees of the maximum possible loss.

## 8. System Architecture

RiskPulse can be described through four main components, subject to verification against the repository.

1. **News Collection Layer:** Retrieves financial news from supported feeds.
2. **Analysis Layer:** Processes text, performs sentiment analysis, and generates risk signals.
3. **Backend and Data Layer:** Exposes API endpoints and stores or retrieves information according to the configured setup.
4. **Frontend Dashboard:** Displays news, risk information, and stress-testing results.

Together, these components provide a workflow from news collection to portfolio risk analysis.

## 9. Testing and Results

Testing helps verify that the application handles inputs correctly and that its main components work as expected.

The supplied test log reports the following results:

| Test Category | Tests Passed |
|---|---:|
| API | 9 |
| Configuration | 3 |
| Database | 1 |
| News Ingestion | 5 |
| NLP | 7 |
| Portfolio | 5 |
| **Total** | **30** |

According to the supplied log, all 30 tests passed in approximately 4.44 seconds.

These figures should be included in the final submission only if the test log corresponds to the submitted code and the results can be reproduced.

### Testing Areas

- API responses and input validation
- News ingestion and duplicate handling
- Sentiment-analysis outputs
- Database operations
- Portfolio calculations and stress-test results

Passing software tests does not, by itself, prove that the system predicts real financial market movements accurately.

Any claims about model accuracy, inference speed, or API latency should be supported by reproducible experiments. Hypothetical portfolio losses must be labelled as simulated results.

## 10. Limitations

RiskPulse has several limitations:

- **News Quality:** Incomplete, delayed, or misleading articles may affect the analysis.
- **Sentiment Limitations:** Models may misunderstand complex financial language or events with mixed implications.
- **Market Uncertainty:** Financial markets respond to many factors beyond news sentiment.
- **Scenario Assumptions:** Stress-test outputs depend on selected parameters and portfolio assumptions.
- **Data Availability:** RSS feeds and cloud services may experience interruptions or restrictions.
- **Model Validation:** Further testing against historical market events is needed before using the system for real investment decisions.

## 11. Future Improvements

Potential improvements include:

1. Adding more reliable financial news and regulatory filing sources.
2. Improving company and stock ticker identification.
3. Testing sentiment predictions against labelled financial datasets.
4. Validating stress-test estimates against historical market events.
5. Adding historical risk trends and portfolio comparisons.
6. Improving explanations for generated risk scores.
7. Strengthening monitoring, error handling, and deployment reliability.

These are proposed improvements and should not be presented as completed features unless already implemented.

## 12. Conclusion

RiskPulse explores how Natural Language Processing and financial risk analysis can work together to help users understand financial news.

The project brings news collection, sentiment analysis, risk scoring, and portfolio stress testing into one workflow. Its dashboard is designed to make the results easier to review and understand.

Developed for the S&P Global & CRISIL Campus Hackathon 2026, RiskPulse demonstrates an approach to connecting unstructured financial information with quantitative risk assessment.

Future work will focus on improving data quality, strengthening validation, and comparing the system's estimates with historical market behaviour.

### Project Links

- **GitHub:** [RiskPulse Repository](https://github.com/Abhi4621/VIT-Bhopal-Abhi-Pandey-S-P-Crisil-hackathon)
- **Live Demo:** [Open RiskPulse](https://vit-bhopal-abhi-pandey-s-p-crisil-h.vercel.app/)

**Project Summary:** Collect financial news. Analyse sentiment. Estimate risk. Test portfolio scenarios. Present results clearly.

## References

1. S. Araci, "FinBERT: Financial Sentiment Analysis with Pre-trained Language Models," *arXiv preprint arXiv:1908.10063*, 2019.
2. T. Loughran and B. McDonald, "When Is a Liability Not a Liability? Textual Analysis, Dictionaries, and 10-Ks," *The Journal of Finance*, vol. 66, no. 1, 2011.
3. A. Vaswani et al., "Attention Is All You Need," *Advances in Neural Information Processing Systems*, 2017.
4. J. Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," *Proceedings of NAACL-HLT*, 2019.
5. P. Artzner et al., "Coherent Measures of Risk," *Mathematical Finance*, vol. 9, no. 3, 1999.
6. R. T. Rockafellar and S. Uryasev, "Optimization of Conditional Value-at-Risk," *Journal of Risk*, vol. 2, 2000.
7. Basel Committee on Banking Supervision, "Stress Testing Principles," Bank for International Settlements, 2018.
