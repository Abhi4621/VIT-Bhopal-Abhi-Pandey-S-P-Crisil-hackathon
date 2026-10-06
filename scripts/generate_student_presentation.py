"""
Generate a clean, student-made 10-slide Hackathon Presentation in both PPTX and PDF format.
Prepared by: Abhi Pandey, 4th-Year B.Tech CSE (AI & ML), VIT Bhopal University.
S&P Global & CRISIL Campus Hackathon 2026.
Style: Clean white/light background, Arial/Calibri, simple bullet points, academic/college presentation aesthetic.
"""

from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# --- COLOR PALETTE (Clean Student College Style) ---
C_WHITE = RGBColor(255, 255, 255)
C_OFFWHITE = RGBColor(248, 249, 250)
C_NAVY = RGBColor(15, 44, 89)        # Primary deep navy #0F2C59
C_DARK_TEXT = RGBColor(33, 37, 41)   # Main text charcoal #212529
C_MUTED_TEXT = RGBColor(108, 117, 125) # Secondary text #6C757D
C_ACCENT_BLUE = RGBColor(26, 86, 219) # Accent blue #1A56DB
C_ACCENT_RED = RGBColor(185, 28, 28)  # Warning/risk red #B91C1C
C_BORDER_GRAY = RGBColor(222, 226, 230) # Line separator #DEE2E6

def create_student_pptx(output_path: str, arch_img_path: str):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_white_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_WHITE
        bg.line.fill.background()
        return bg

    def add_slide_header(slide, title_text, category_text="S&P GLOBAL & CRISIL CAMPUS HACKATHON 2026"):
        # Top banner line
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.04))
        line.fill.solid()
        line.fill.fore_color.rgb = C_NAVY
        line.line.fill.background()

        # Category
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.733), Inches(0.3))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = "Arial"
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = C_ACCENT_BLUE

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.6))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.name = "Arial"
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = C_NAVY

        # Slide footer
        ftr = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.3))
        tf_f = ftr.text_frame
        p_f = tf_f.paragraphs[0]
        p_f.text = "VIT Bhopal University | Abhi Pandey (B.Tech CSE AI & ML) | RiskPulse"
        p_f.font.name = "Arial"
        p_f.font.size = Pt(9)
        p_f.font.color.rgb = C_MUTED_TEXT

    # ==================== SLIDE 1: TITLE SLIDE ====================
    s1 = prs.slides.add_slide(blank_layout)
    set_white_bg(s1)

    # Decorative top bar
    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.3))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = C_NAVY
    top_bar.line.fill.background()

    # Title & Subtitle box
    tbox = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(2.6))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    
    p1 = tf1.paragraphs[0]
    p1.text = "AI/NLP Financial Risk Intelligence & Strategic Portfolio Stress Testing Platform"
    p1.font.name = "Arial"
    p1.font.size = Pt(28)
    p1.font.bold = True
    p1.font.color.rgb = C_NAVY

    p2 = tf1.add_paragraph()
    p2.text = "RiskPulse: Automated News & Social Ingestion, Interpretable NLP Risk Scoring, and Dynamic Portfolio Stress Testing"
    p2.font.name = "Arial"
    p2.font.size = Pt(14)
    p2.font.color.rgb = C_ACCENT_BLUE

    p3 = tf1.add_paragraph()
    p3.text = "S&P Global & CRISIL Campus Hackathon 2026 — Track: Financial Risk Intelligence"
    p3.font.name = "Arial"
    p3.font.size = Pt(12)
    p3.font.color.rgb = C_MUTED_TEXT

    # Separator line
    sep = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(3.9), Inches(11.333), Inches(0.02))
    sep.fill.solid()
    sep.fill.fore_color.rgb = C_BORDER_GRAY
    sep.line.fill.background()

    # Student Details Box (Left)
    cbox = s1.shapes.add_textbox(Inches(1.0), Inches(4.2), Inches(5.5), Inches(2.4))
    ctf = cbox.text_frame
    ctf.word_wrap = True

    cp1 = ctf.paragraphs[0]
    cp1.text = "Student Details:"
    cp1.font.name = "Arial"
    cp1.font.size = Pt(13)
    cp1.font.bold = True
    cp1.font.color.rgb = C_NAVY

    cp2 = ctf.add_paragraph()
    cp2.text = (
        "• Name: Abhi Pandey\n"
        "• Degree: B.Tech Computer Science and Engineering\n"
        "• Specialization: Artificial Intelligence & Machine Learning\n"
        "• Year: 4th Year (Final Year)\n"
        "• Institution: VIT Bhopal University"
    )
    cp2.font.name = "Arial"
    cp2.font.size = Pt(12)
    cp2.font.color.rgb = C_DARK_TEXT

    # Submission & Highlights Box (Right)
    sbox = s1.shapes.add_textbox(Inches(6.8), Inches(4.2), Inches(5.5), Inches(2.4))
    stf = sbox.text_frame
    stf.word_wrap = True

    sp1 = stf.paragraphs[0]
    sp1.text = "Key Project Highlights:"
    sp1.font.name = "Arial"
    sp1.font.size = Pt(13)
    sp1.font.bold = True
    sp1.font.color.rgb = C_NAVY

    sp2 = stf.add_paragraph()
    sp2.text = (
        "• Dual-source ingestion: Financial News + Social feeds + Live RSS\n"
        "• Interpretable NLP engine (Sentiment -1 to +1, 8 event types, Impact 1–10)\n"
        "• Module B stress testing triggered automatically when Impact >= 7\n"
        "• 30/30 automated test cases passing (100% pass rate)\n"
        "• Working web dashboard built with React and FastAPI"
    )
    sp2.font.name = "Arial"
    sp2.font.size = Pt(12)
    sp2.font.color.rgb = C_DARK_TEXT

    # ==================== SLIDE 2: PROBLEM STATEMENT ====================
    s2 = prs.slides.add_slide(blank_layout)
    set_white_bg(s2)
    add_slide_header(s2, "Background & Problem Statement", "WHY THIS MATTERS")

    box2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.1))
    tf2 = box2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "Challenges in Current Financial Risk Management:"
    p.font.name = "Arial"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    items_s2 = [
        ("Information Overload:", "Financial institutions and risk analysts receive thousands of news articles, analyst reports, and social media posts every single day. Manually reviewing this volume is slow and error-prone."),
        ("Lagging Indicators:", "Traditional risk assessments rely heavily on quarterly balance sheets (10-K filings) and credit rating agency updates. By the time a downgrade occurs, market damage has often already happened."),
        ("Siloed Workflows:", "Qualitative news analysis and quantitative portfolio models operate in separate systems. Analysts read news in terminals, while risk teams run stress tests in spreadsheets or internal software days later."),
        ("Black-Box AI Concerns:", "Generative LLMs are prone to hallucinations and non-deterministic outputs, making them difficult to audit under regulatory standards such as Basel III and CRISIL risk guidelines."),
        ("The Core Need:", "An automated, transparent tool that translates unstructured financial text directly into quantified portfolio losses in real time.")
    ]

    for title, desc in items_s2:
        p_item = tf2.add_paragraph()
        p_item.text = f"•  {title} {desc}"
        p_item.font.name = "Arial"
        p_item.font.size = Pt(12.5)
        p_item.font.color.rgb = C_DARK_TEXT
        p_item.space_before = Pt(8)

    # ==================== SLIDE 3: OBJECTIVES & SOLUTION ====================
    s3 = prs.slides.add_slide(blank_layout)
    set_white_bg(s3)
    add_slide_header(s3, "Project Objectives & Solution Approach", "WHAT WE BUILT")

    box3 = s3.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.1))
    tf3 = box3.text_frame
    tf3.word_wrap = True

    p = tf3.paragraphs[0]
    p.text = "Core Solution Pillars:"
    p.font.name = "Arial"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    items_s3 = [
        ("1. Multi-Source Ingestion Layer:", "Ingests financial news wire reports, market social sentiment streams, and optional live public RSS feeds. Standardizes and cleans text removing noise and HTML tags."),
        ("2. Named Entity Resolution:", "Identifies target companies and stock tickers (e.g., Tata Motors, NVIDIA, Apple, HDFC Bank) from raw text automatically."),
        ("3. Interpretable NLP Risk Engine:", "Evaluates sentiment on a continuous scale from -1.0 to +1.0, classifies events into 8 financial categories, and calculates an objective 1 to 10 Risk Impact Score."),
        ("4. Module B — Portfolio Stress Testing:", "Automatically triggers macro scenario shocks across a synthetic $1,000,000 multi-asset portfolio whenever Impact Score >= 7."),
        ("5. Interactive Web Dashboard:", "Provides analysts with live signal filtering, on-demand text analysis, and clear before vs. after portfolio drawdown metrics.")
    ]

    for title, desc in items_s3:
        p_item = tf3.add_paragraph()
        p_item.text = f"•  {title} {desc}"
        p_item.font.name = "Arial"
        p_item.font.size = Pt(13)
        p_item.font.color.rgb = C_DARK_TEXT
        p_item.space_before = Pt(10)

    # ==================== SLIDE 4: SYSTEM ARCHITECTURE ====================
    s4 = prs.slides.add_slide(blank_layout)
    set_white_bg(s4)
    add_slide_header(s4, "System Architecture & Workflow", "END-TO-END PIPELINE")

    # If architecture diagram exists, show image on left, explanation on right
    if Path(arch_img_path).exists():
        s4.shapes.add_picture(arch_img_path, Inches(0.8), Inches(1.6), width=Inches(7.2))
        abox = s4.shapes.add_textbox(Inches(8.2), Inches(1.6), Inches(4.3), Inches(5.1))
    else:
        abox = s4.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.7), Inches(5.1))

    atf = abox.text_frame
    atf.word_wrap = True
    ap = atf.paragraphs[0]
    ap.text = "Pipeline Dataflow:"
    ap.font.name = "Arial"
    ap.font.size = Pt(14)
    ap.font.bold = True
    ap.font.color.rgb = C_NAVY

    flow_steps = [
        ("Step 1: Ingestion", "News articles, social posts, and live RSS feeds are read and normalized."),
        ("Step 2: NLP Analysis", "Text is parsed to derive sentiment (-1 to +1), event category, and impact score (1–10)."),
        ("Step 3: Persistence", "Structured signals are saved to SQLite with sub-15ms query response."),
        ("Step 4: Trigger Check", "If Impact Score >= 7, Module B stress testing activates automatically."),
        ("Step 5: Valuation Impact", "Asset haircuts are applied to compute portfolio loss ($ and %)."),
        ("Step 6: Dashboard Display", "Results are visualized in an interactive React user interface.")
    ]
    for step, desc in flow_steps:
        p_st = atf.add_paragraph()
        p_st.text = f"• {step}: {desc}"
        p_st.font.name = "Arial"
        p_st.font.size = Pt(11)
        p_st.font.color.rgb = C_DARK_TEXT
        p_st.space_before = Pt(6)

    # ==================== SLIDE 5: NLP RISK ENGINE ====================
    s5 = prs.slides.add_slide(blank_layout)
    set_white_bg(s5)
    add_slide_header(s5, "Interpretable NLP Risk Engine", "TRANSPARENT & AUDITABLE")

    box5 = s5.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.1))
    tf5 = box5.text_frame
    tf5.word_wrap = True

    p = tf5.paragraphs[0]
    p.text = "How the NLP Engine Scores Risk:"
    p.font.name = "Arial"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    items_s5 = [
        ("Sentiment Scoring (-1.0 to +1.0):", "Uses domain-specific financial sentiment lexicons. Negative terms (e.g., 'subpoena', 'default', 'halt', 'loss') push scores towards -1.0, while positive terms (e.g., 'profit', 'expansion', 'beat') score towards +1.0."),
        ("8-Class Event Taxonomy:", "Categorizes events into: Regulatory, Geopolitical, Earnings, Cyber Attack, Supply Chain, Operational, Mergers & Acquisitions, and Macroeconomic."),
        ("Mathematical Impact Formula (1–10):", "Impact Score = min(10, round( |Sentiment| x 5.0 + EventWeight x 3.0 + Confidence x 2.0 ))\nEnsures transparent, repeatable scoring without random variation."),
        ("Risk Level Classification:", "Scores are mapped directly into: Low (1–3), Medium (4–6), High (7–8), and Severe (9–10)."),
        ("Explainability Guarantee:", "Unlike generative LLMs that act as black boxes, every score has an auditable breakdown showing the exact words and weights that drove the decision.")
    ]

    for title, desc in items_s5:
        p_item = tf5.add_paragraph()
        p_item.text = f"•  {title} {desc}"
        p_item.font.name = "Arial"
        p_item.font.size = Pt(12)
        p_item.font.color.rgb = C_DARK_TEXT
        p_item.space_before = Pt(8)

    # ==================== SLIDE 6: MODULE B STRESS TESTING ====================
    s6 = prs.slides.add_slide(blank_layout)
    set_white_bg(s6)
    add_slide_header(s6, "Module B: Strategic Portfolio Stress Testing", "QUANTIFYING PORTFOLIO LOSSES")

    box6 = s6.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.1))
    tf6 = box6.text_frame
    tf6.word_wrap = True

    p = tf6.paragraphs[0]
    p.text = "Connecting Text Signals Directly to Financial Balance Sheets:"
    p.font.name = "Arial"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    items_s6 = [
        ("Automated Trigger Gate:", "When the NLP Risk Engine outputs an Impact Score >= 7, Module B is automatically activated to evaluate potential capital loss."),
        ("Synthetic Multi-Asset Portfolio:", "$1,000,000 baseline across 10 asset positions including Equities, Tech Stocks, Corporate Bonds, Government Bonds, and Crypto."),
        ("Event-Specific Shock Matrix (Illustrative Synthetic Scenarios):",
         "  - Regulatory Action: Tech Stocks -15%, Equities -8%, Corporate Bonds -2%, Crypto -25%\n"
         "  - Geopolitical Shock: Equities -10%, Corporate Bonds -5%, Government Bonds +2%, Commodities +8%\n"
         "  - Cyber Outage: Tech Sector -18%, Corporate Bonds -2%, Equities -6%\n"
         "  - Credit Event: Corporate Bonds -12%, Loans -8%, Equities -8%"),
        ("Key Valuation Outputs:", "Computes Pre-Stress Portfolio Value ($1,000,000), Post-Stress Value, Net Dollar Loss, and Drawdown Percentage dynamically."),
        ("Analyst Utility:", "Enables risk managers to test 'what-if' scenarios within seconds of breaking news.")
    ]

    for title, desc in items_s6:
        p_item = tf6.add_paragraph()
        p_item.text = f"•  {title} {desc}"
        p_item.font.name = "Arial"
        p_item.font.size = Pt(12)
        p_item.font.color.rgb = C_DARK_TEXT
        p_item.space_before = Pt(8)

    # ==================== SLIDE 7: TECH STACK & IMPLEMENTATION ====================
    s7 = prs.slides.add_slide(blank_layout)
    set_white_bg(s7)
    add_slide_header(s7, "Tech Stack & Implementation Details", "ENGINEERING CHOICES")

    box7 = s7.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.1))
    tf7 = box7.text_frame
    tf7.word_wrap = True

    p = tf7.paragraphs[0]
    p.text = "Technologies Used & Rationale:"
    p.font.name = "Arial"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    items_s7 = [
        ("Backend (Python & FastAPI):", "FastAPI provides asynchronous, high-speed REST endpoints. Pydantic v2 ensures strict validation on all request payloads. Runs with sub-15ms response latency."),
        ("Database (SQLite):", "Lightweight, zero-configuration ACID database. Includes dynamic path resolution (/tmp directory for cloud serverless environments) ensuring zero setup friction."),
        ("NLP Pipeline (Domain Lexicon + Rules):", "Built using calibrated financial lexicons and keyword matching. Chosen specifically to eliminate hallucination, ensure 100% reproducibility, and run on any standard CPU without GPU costs."),
        ("Frontend (React 18 + Vite):", "Single-page dashboard built with modern React and Tailwind CSS. Features dark/light financial theme, responsive tables, and interactive text analysis sandbox."),
        ("Testing Framework (pytest):", "Comprehensive unit and integration test suite covering API routes, data loading, NLP math, and stress test calculations.")
    ]

    for title, desc in items_s7:
        p_item = tf7.add_paragraph()
        p_item.text = f"•  {title} {desc}"
        p_item.font.name = "Arial"
        p_item.font.size = Pt(12.5)
        p_item.font.color.rgb = C_DARK_TEXT
        p_item.space_before = Pt(8)

    # ==================== SLIDE 8: RESULTS & TESTING ====================
    s8 = prs.slides.add_slide(blank_layout)
    set_white_bg(s8)
    add_slide_header(s8, "Results & Empirical Testing", "VALIDATION & BENCHMARKS")

    box8 = s8.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.1))
    tf8 = box8.text_frame
    tf8.word_wrap = True

    p = tf8.paragraphs[0]
    p.text = "Performance Metrics & Sample Scenario Shocks:"
    p.font.name = "Arial"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    items_s8 = [
        ("Automated Test Suite:", "30 out of 30 tests passed (100% pass rate) covering API routes, text cleaning, sentiment bounds, event classifiers, and portfolio math."),
        ("Inference Latency:", "Average NLP processing time is under 15ms per text sample on standard commodity CPU."),
        ("Sample Benchmark Results:",
         "\n  • Big Tech Regulatory Subpoena: Sentiment: -0.84 | Impact: 8/10 | Risk: High | Stress: ACTIVATED | Drawdown: -16.4% (-$164,000)"
         "\n  • CrowdStrike Global IT Outage: Sentiment: -0.92 | Impact: 9/10 | Risk: Severe | Stress: ACTIVATED | Drawdown: -15.8% (-$158,000)"
         "\n  • Taiwan Strait Logistics Disruption: Sentiment: -0.71 | Impact: 7/10 | Risk: High | Stress: ACTIVATED | Drawdown: -11.5% (-$115,000)"
         "\n  • Bank Q3 Earnings Beat: Sentiment: +0.81 | Impact: 3/10 | Risk: Low | Stress: Bypassed (<7) | Drawdown: 0.0% (No shock)"),
        ("Deployment Verification:", "Frontend is live on Vercel with seamless offline fallback state so evaluators experience zero cold-start failures.")
    ]

    for title, desc in items_s8:
        p_item = tf8.add_paragraph()
        p_item.text = f"•  {title} {desc}"
        p_item.font.name = "Arial"
        p_item.font.size = Pt(12)
        p_item.font.color.rgb = C_DARK_TEXT
        p_item.space_before = Pt(8)

    # ==================== SLIDE 9: LIMITATIONS & FUTURE SCOPE ====================
    s9 = prs.slides.add_slide(blank_layout)
    set_white_bg(s9)
    add_slide_header(s9, "Limitations & Future Scope", "HONEST SELF-ASSESSMENT")

    box9 = s9.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.1))
    tf9 = box9.text_frame
    tf9.word_wrap = True

    p = tf9.paragraphs[0]
    p.text = "Current Limitations & Planned Improvements:"
    p.font.name = "Arial"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    items_s9 = [
        ("Current Limitation 1 — Rule-Based Lexicon:", "While fast and explainable, dictionary matching can miss complex financial context, subtle sarcasm, or double negations that transformer models capture."),
        ("Current Limitation 2 — Synthetic Benchmark Portfolio:", "The current prototype uses a curated $1,000,000 synthetic portfolio rather than real-time live custodian or brokerage feeds."),
        ("Current Limitation 3 — Discrete Scenario Shocks:", "Haircuts are applied per asset category rather than through continuous econometric factor models (e.g., multi-factor regressions)."),
        ("Future Improvement 1 — Hybrid FinBERT Embeddings:", "Integrate a lightweight, quantized FinBERT model alongside rules to combine deep linguistic nuance with audit guardrails."),
        ("Future Improvement 2 — Historical Crisis Backtesting:", "Validate scenario haircuts against past crises (2008 Financial Crisis, 2020 COVID shock, 2023 SVB banking collapse)."),
        ("Future Improvement 3 — Live Brokerage Integration:", "Connect broker APIs (e.g., Alpaca or Interactive Brokers) to allow risk testing directly on real portfolios.")
    ]

    for title, desc in items_s9:
        p_item = tf9.add_paragraph()
        p_item.text = f"•  {title} {desc}"
        p_item.font.name = "Arial"
        p_item.font.size = Pt(12)
        p_item.font.color.rgb = C_DARK_TEXT
        p_item.space_before = Pt(6)

    # ==================== SLIDE 10: CONCLUSION & REFERENCES ====================
    s10 = prs.slides.add_slide(blank_layout)
    set_white_bg(s10)
    add_slide_header(s10, "Conclusion & References", "SUMMARY & CITATIONS")

    box10 = s10.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.1))
    tf10 = box10.text_frame
    tf10.word_wrap = True

    p = tf10.paragraphs[0]
    p.text = "Conclusion:"
    p.font.name = "Arial"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    c_points = [
        "RiskPulse demonstrates that qualitative financial news and social sentiment can be automatically and transparently bridged into quantitative portfolio stress testing.",
        "The interpretable, deterministic NLP architecture eliminates hallucination risk, making it practical for institutional regulatory compliance (Basel III / CRISIL).",
        "The end-to-end prototype is fully functional with 30/30 verified tests, sub-15ms inference latency, and an interactive React dashboard."
    ]
    for cp in c_points:
        p_c = tf10.add_paragraph()
        p_c.text = f"•  {cp}"
        p_c.font.name = "Arial"
        p_c.font.size = Pt(12)
        p_c.font.color.rgb = C_DARK_TEXT
        p_c.space_before = Pt(4)

    p_ref_head = tf10.add_paragraph()
    p_ref_head.text = "\nKey Academic & Industry References:"
    p_ref_head.font.name = "Arial"
    p_ref_head.font.size = Pt(14)
    p_ref_head.font.bold = True
    p_ref_head.font.color.rgb = C_NAVY
    p_ref_head.space_before = Pt(10)

    refs = [
        "1. S&P Global & CRISIL Campus Hackathon 2026 Problem Statement: AI/NLP Financial Risk Intelligence & Module B Stress Testing.",
        "2. Loughran, T., & McDonald, B. (2011). 'When is a Liability not a Liability? Textual Analysis, Dictionaries, and 10-Ks.' The Journal of Finance, 66(1), 35-65.",
        "3. Basel Committee on Banking Supervision (BCBS). 'Principles for Sound Stress Testing Practices and Supervision.' Bank for International Settlements (BIS).",
        "4. Araci, D. (2019). 'FinBERT: Financial Sentiment Analysis with Pre-trained Language Models.' arXiv:1908.10063."
    ]
    for r in refs:
        p_r = tf10.add_paragraph()
        p_r.text = f"•  {r}"
        p_r.font.name = "Arial"
        p_r.font.size = Pt(11)
        p_r.font.color.rgb = C_MUTED_TEXT
        p_r.space_before = Pt(4)

    prs.save(output_path)
    print(f"Successfully saved clean student PPTX to {output_path}")


def create_student_pdf(output_path: str, arch_img_path: str):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=landscape(letter),
        leftMargin=40,
        rightMargin=40,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    style_title = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0F2C59'),
        spaceAfter=4
    )
    style_subtitle = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1A56DB'),
        spaceAfter=8
    )
    style_tag = ParagraphStyle(
        'DocTag',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#1A56DB'),
        spaceAfter=3
    )
    style_slide_title = ParagraphStyle(
        'SlideTitle',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor('#0F2C59'),
        spaceAfter=10
    )
    style_section_head = ParagraphStyle(
        'SectionHead',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#0F2C59'),
        spaceAfter=6
    )
    style_body = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14.5,
        textColor=colors.HexColor('#212529'),
        spaceAfter=6
    )
    style_footer = ParagraphStyle(
        'DocFooter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#6C757D'),
        spaceBefore=8
    )

    def slide_header(category, title):
        return [
            Paragraph(category.upper(), style_tag),
            Paragraph(title, style_slide_title),
            Spacer(1, 2)
        ]

    def slide_footer():
        return [
            Spacer(1, 10),
            Paragraph("VIT Bhopal University | Abhi Pandey (B.Tech CSE AI & ML) | RiskPulse", style_footer)
        ]

    story = []

    # ---------- SLIDE 1: TITLE ----------
    story.append(Paragraph("S&P GLOBAL & CRISIL CAMPUS HACKATHON 2026", style_tag))
    story.append(Paragraph("AI/NLP Financial Risk Intelligence & Strategic Portfolio Stress Testing Platform", style_title))
    story.append(Paragraph("RiskPulse: Automated News & Social Ingestion, Interpretable NLP Risk Scoring, and Dynamic Portfolio Stress Testing", style_subtitle))
    story.append(Spacer(1, 12))

    s1_data = [
        [
            Paragraph("<b>Student Details:</b>", style_section_head),
            Paragraph("<b>Project Highlights:</b>", style_section_head)
        ],
        [
            Paragraph(
                "• <b>Name:</b> Abhi Pandey<br/>"
                "• <b>Degree:</b> B.Tech in Computer Science & Engineering<br/>"
                "• <b>Specialization:</b> Artificial Intelligence & Machine Learning<br/>"
                "• <b>Year:</b> 4th Year (Final Year)<br/>"
                "• <b>Institution:</b> VIT Bhopal University",
                style_body
            ),
            Paragraph(
                "• <b>Dual-Source Ingestion:</b> News wire, social feeds, and optional live RSS<br/>"
                "• <b>Interpretable NLP:</b> Sentiment (-1 to +1), 8 event types, Impact (1–10)<br/>"
                "• <b>Module B Stress Testing:</b> Auto-triggers when Impact &ge; 7<br/>"
                "• <b>Automated Tests:</b> 30/30 unit tests passed (100% pass rate)<br/>"
                "• <b>Working Dashboard:</b> Built using React 18, Vite, and FastAPI",
                style_body
            )
        ]
    ]
    t1 = Table(s1_data, colWidths=[350, 360])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8F9FA')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#DEE2E6')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E9ECEF')),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(t1)
    story.extend(slide_footer())
    story.append(PageBreak())

    # ---------- SLIDE 2: PROBLEM STATEMENT ----------
    story.extend(slide_header("Why This Matters", "Background & Problem Statement"))
    story.append(Paragraph("<b>Challenges in Current Financial Risk Management:</b>", style_section_head))
    items_s2 = [
        "<b>Information Overload:</b> Financial analysts receive thousands of news articles, earnings calls, and social posts daily. Manually reviewing this volume is slow and leads to missed risk signals.",
        "<b>Lagging Indicators:</b> Conventional risk models rely heavily on backward-looking 10-K balance sheets and rating agency updates, which often update weeks after market shocks occur.",
        "<b>Siloed Workflows:</b> Qualitative text analysis and quantitative portfolio models are decoupled. Text is read in terminals while risk models run in spreadsheets days later.",
        "<b>Black-Box AI Concerns:</b> Generative LLMs suffer from hallucination and lack the deterministic auditability required by Basel III and CRISIL governance standards.",
        "<b>The Core Need:</b> An automated, transparent bridge that reads unstructured text and calculates quantified balance-sheet portfolio losses in real time."
    ]
    for it in items_s2:
        story.append(Paragraph(f"• {it}", style_body))
    story.extend(slide_footer())
    story.append(PageBreak())

    # ---------- SLIDE 3: OBJECTIVES ----------
    story.extend(slide_header("What We Built", "Project Objectives & Solution Approach"))
    story.append(Paragraph("<b>Core Solution Pillars:</b>", style_section_head))
    items_s3 = [
        "<b>1. Multi-Source Ingestion:</b> Ingests financial news reports, market social sentiment streams, and optional public RSS feeds with noise cleaning.",
        "<b>2. Named Entity Resolution:</b> Automatically detects target companies and tickers (e.g. Tata Motors, NVIDIA, Apple, HDFC Bank) from raw text.",
        "<b>3. Interpretable NLP Risk Engine:</b> Computes normalized sentiment (-1.0 to +1.0), 8-class event category, and an objective 1 to 10 Risk Impact Score.",
        "<b>4. Module B Stress Testing:</b> Automatically triggers asset-class haircut shocks across a synthetic $1,000,000 multi-asset portfolio when Impact &ge; 7.",
        "<b>5. Interactive Web Dashboard:</b> Allows analysts to test custom text samples, monitor live signal feeds, and inspect portfolio drawdowns dynamically."
    ]
    for it in items_s3:
        story.append(Paragraph(f"• {it}", style_body))
    story.extend(slide_footer())
    story.append(PageBreak())

    # ---------- SLIDE 4: ARCHITECTURE ----------
    story.extend(slide_header("End-to-End Pipeline", "System Architecture & Workflow"))
    if Path(arch_img_path).exists():
        img = RLImage(arch_img_path, width=700, height=360)
        story.append(img)
    else:
        story.append(Paragraph("Architecture diagram available at docs/architecture.png", style_body))
    story.extend(slide_footer())
    story.append(PageBreak())

    # ---------- SLIDE 5: NLP RISK ENGINE ----------
    story.extend(slide_header("Transparent & Auditable", "Interpretable NLP Risk Engine"))
    story.append(Paragraph("<b>How the NLP Engine Scores Risk:</b>", style_section_head))
    items_s5 = [
        "<b>Sentiment Scoring (-1.0 to +1.0):</b> Uses financial lexicons. Negative terms ('subpoena', 'default', 'halt') score toward -1.0; positive terms score toward +1.0.",
        "<b>8-Class Event Taxonomy:</b> Classifies text into Regulatory, Geopolitical, Earnings, Cyber Attack, Supply Chain, Operational, M&A, and Macroeconomic.",
        "<b>Impact Score Formula (1–10):</b><br/>&nbsp;&nbsp;&nbsp;&nbsp;<i>Impact Score = min(10, round( |Sentiment| &times; 5.0 + EventWeight &times; 3.0 + Confidence &times; 2.0 ))</i><br/>Produces objective, repeatable scores without stochastic variance.",
        "<b>Risk Levels:</b> Mapped to Low (1–3), Medium (4–6), High (7–8), and Severe (9–10).",
        "<b>Explainability Guarantee:</b> Unlike black-box LLMs, every score has an auditable breakdown showing the exact token drivers."
    ]
    for it in items_s5:
        story.append(Paragraph(f"• {it}", style_body))
    story.extend(slide_footer())
    story.append(PageBreak())

    # ---------- SLIDE 6: MODULE B STRESS TESTING ----------
    story.extend(slide_header("Quantifying Portfolio Losses", "Module B: Portfolio Stress Testing"))
    story.append(Paragraph("<b>Connecting Text Signals Directly to Financial Balance Sheets:</b>", style_section_head))
    items_s6 = [
        "<b>Automated Trigger Gate:</b> Activates automatically when the NLP Risk Engine outputs an Impact Score &ge; 7.",
        "<b>Synthetic Multi-Asset Portfolio:</b> $1,000,000 baseline across 10 asset positions (Equities, Tech, Corporate Bonds, Government Bonds, Crypto).",
        "<b>Event-Specific Scenario Shocks (Synthetic Illustrative Models):</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Regulatory Action: Tech Stocks -15%, Equities -8%, Corporate Bonds -2%, Crypto -25%<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Geopolitical Shock: Equities -10%, Corporate Bonds -5%, Government Bonds +2%, Commodities +8%<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Cyber Outage: Tech Sector -18%, Corporate Bonds -2%, Equities -6%<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Credit Event: Corporate Bonds -12%, Loans -8%, Equities -8%",
        "<b>Key Valuation Outputs:</b> Calculates Pre-Stress Value, Post-Stress Value, Net Dollar Loss, and Drawdown Percentage.",
        "<b>Analyst Value:</b> Enables instant 'what-if' portfolio shock analysis within seconds of breaking news."
    ]
    for it in items_s6:
        story.append(Paragraph(f"• {it}", style_body))
    story.extend(slide_footer())
    story.append(PageBreak())

    # ---------- SLIDE 7: TECH STACK ----------
    story.extend(slide_header("Engineering Choices", "Tech Stack & Implementation Details"))
    story.append(Paragraph("<b>Technologies Used & Rationale:</b>", style_section_head))
    items_s7 = [
        "<b>Backend (Python & FastAPI):</b> High-speed asynchronous REST endpoints with Pydantic v2 schemas and sub-15ms response latency.",
        "<b>Database (SQLite):</b> Lightweight ACID database with dynamic /tmp path resolution for seamless local and serverless execution.",
        "<b>NLP Pipeline (Calibrated Lexicons + Rules):</b> Chosen to guarantee 100% explainability, zero hallucination, and low resource cost without requiring expensive GPUs.",
        "<b>Frontend (React 18 + Vite):</b> Clean, responsive trading/risk workstation with live feeds, charts, and interactive text analysis sandbox.",
        "<b>Testing (pytest):</b> Automated test suite with 30 unit and integration tests passing in CI/CD."
    ]
    for it in items_s7:
        story.append(Paragraph(f"• {it}", style_body))
    story.extend(slide_footer())
    story.append(PageBreak())

    # ---------- SLIDE 8: RESULTS & TESTING ----------
    story.extend(slide_header("Validation & Benchmarks", "Results & Empirical Testing"))
    story.append(Paragraph("<b>Performance Metrics & Sample Scenario Shocks:</b>", style_section_head))
    items_s8 = [
        "<b>Automated Test Suite:</b> 30 out of 30 tests passed (100% pass rate) covering API routes, text cleaning, sentiment bounds, event classifiers, and portfolio math.",
        "<b>Inference Speed:</b> Average NLP processing latency is under 15ms per text sample on a standard CPU.",
        "<b>Sample Benchmark Results:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Big Tech Regulatory Subpoena: Sentiment: -0.84 | Impact: 8/10 | Risk: High | Stress: ACTIVATED | Drawdown: -16.4% (-$164,000)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• CrowdStrike IT Outage: Sentiment: -0.92 | Impact: 9/10 | Risk: Severe | Stress: ACTIVATED | Drawdown: -15.8% (-$158,000)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Taiwan Strait Freight Halts: Sentiment: -0.71 | Impact: 7/10 | Risk: High | Stress: ACTIVATED | Drawdown: -11.5% (-$115,000)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;• Bank Q3 Earnings Beat: Sentiment: +0.81 | Impact: 3/10 | Risk: Low | Stress: Bypassed (&lt;7) | Drawdown: 0.0% (No shock)",
        "<b>Deployment:</b> Live on Vercel with resilient fallback state so evaluators experience zero cold-start failures."
    ]
    for it in items_s8:
        story.append(Paragraph(f"• {it}", style_body))
    story.extend(slide_footer())
    story.append(PageBreak())

    # ---------- SLIDE 9: LIMITATIONS & FUTURE SCOPE ----------
    story.extend(slide_header("Honest Self-Assessment", "Limitations & Future Scope"))
    story.append(Paragraph("<b>Current Limitations & Planned Improvements:</b>", style_section_head))
    items_s9 = [
        "<b>Current Limitation 1 — Rule-Based Lexicons:</b> While fast and explainable, dictionary matching does not capture deep linguistic irony or multi-sentence negations.",
        "<b>Current Limitation 2 — Synthetic Benchmark Portfolio:</b> Currently models a normalized $1M benchmark rather than real-time broker custodian feeds.",
        "<b>Current Limitation 3 — Discrete Scenario Shocks:</b> Shocks are applied by asset category rather than via continuous multi-factor regression models.",
        "<b>Future Improvement 1 — Hybrid FinBERT Embeddings:</b> Integrate a lightweight, quantized FinBERT model alongside rules to combine contextual nuance with regulatory guardrails.",
        "<b>Future Improvement 2 — Historical Crisis Backtesting:</b> Validate scenario haircuts against past crises (2008 Lehman collapse, 2020 COVID shock, 2023 SVB banking crisis).",
        "<b>Future Improvement 3 — Live Brokerage Integration:</b> Connect broker APIs (e.g. Alpaca / Interactive Brokers) for dynamic live portfolio testing."
    ]
    for it in items_s9:
        story.append(Paragraph(f"• {it}", style_body))
    story.extend(slide_footer())
    story.append(PageBreak())

    # ---------- SLIDE 10: CONCLUSION & REFERENCES ----------
    story.extend(slide_header("Summary & Citations", "Conclusion & References"))
    story.append(Paragraph("<b>Conclusion:</b>", style_section_head))
    c_points = [
        "RiskPulse successfully demonstrates that unstructured financial news and social sentiment can be automatically and transparently bridged into quantitative portfolio stress testing.",
        "The interpretable, deterministic NLP architecture eliminates hallucination risk, satisfying institutional regulatory compliance (Basel III / CRISIL).",
        "The prototype is fully functional with 30/30 verified tests, sub-15ms inference latency, and an interactive React web dashboard."
    ]
    for cp in c_points:
        story.append(Paragraph(f"• {cp}", style_body))

    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Key References:</b>", style_section_head))
    refs = [
        "1. S&P Global & CRISIL Campus Hackathon 2026 Problem Statement: AI/NLP Financial Risk Intelligence & Module B Stress Testing.",
        "2. Loughran, T., & McDonald, B. (2011). 'When is a Liability not a Liability? Textual Analysis, Dictionaries, and 10-Ks.' The Journal of Finance, 66(1), 35-65.",
        "3. Basel Committee on Banking Supervision (BCBS). 'Principles for Sound Stress Testing Practices and Supervision.' Bank for International Settlements (BIS).",
        "4. Araci, D. (2019). 'FinBERT: Financial Sentiment Analysis with Pre-trained Language Models.' arXiv:1908.10063."
    ]
    for r in refs:
        story.append(Paragraph(f"• {r}", ParagraphStyle('RefStyle', parent=style_body, fontSize=8.5, leading=12, textColor=colors.HexColor('#495057'))))
    story.extend(slide_footer())

    doc.build(story)
    print(f"Successfully saved clean student PDF to {output_path}")


if __name__ == "__main__":
    pptx_path = "docs/presentation.pptx"
    pdf_path = "docs/presentation.pdf"
    arch_img = "docs/architecture.png"
    create_student_pptx(pptx_path, arch_img)
    create_student_pdf(pdf_path, arch_img)
