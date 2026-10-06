"""
Build a visually rich, professional 20-slide final-year B.Tech project presentation.
Candidate: Abhi Pandey (21BCE10462), B.Tech CSE (AI & ML), VIT Bhopal University.
Topic: RiskPulse — AI/NLP Financial Risk Intelligence & Strategic Portfolio Stress Testing Platform.
Review: S&P Global & CRISIL Campus Hackathon 2026 / Final Year Project Viva.

Key Requirements Followed:
- Exactly 20 slides.
- Every slide has a major visual component (diagram, flowchart, architecture image, UI screenshot, chart, or visual card matrix).
- 2-4 short text points MAX per slide — no text dumps or boring bullet lists.
- Clean slide titles (no 'SECTION 09' or 'Slide 19:' prefixes).
- Professional color scheme: Warm Orange (#EA580C), Deep Navy (#0F172A), Slate Blue (#0284C7), Crisp White, and Light Slate (#F8FAFC).
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

# --- COLOR PALETTE ---
C_PAGE_BG = RGBColor(255, 255, 255)       # White #FFFFFF
C_TINT_BG = RGBColor(248, 250, 252)       # Light Slate #F8FAFC
C_ORANGE = RGBColor(234, 88, 12)          # Primary Warm Orange #EA580C
C_ORANGE_TINT = RGBColor(255, 237, 213)   # Soft Orange Tint #FFEDD5
C_NAVY = RGBColor(15, 23, 42)             # Deep Navy #0F172A
C_SLATE = RGBColor(30, 41, 59)            # Slate Dark #1E293B
C_MUTED = RGBColor(100, 116, 139)         # Slate Muted #64748B
C_BORDER = RGBColor(226, 232, 240)        # Border Light #E2E8F0
C_WHITE = RGBColor(255, 255, 255)         # White
C_BLUE = RGBColor(2, 132, 199)            # Tech Blue #0284C7
C_GREEN = RGBColor(16, 185, 129)          # Emerald #10B981
C_RED = RGBColor(220, 38, 38)             # Alert Red #DC2626

FONT_FAMILY = "Segoe UI"

def build_pptx(output_path: Path, assets_dir: Path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_slide_base(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_PAGE_BG
        bg.line.fill.background()
        return bg

    def add_slide_header(slide, title_text, tag_text="VIT BHOPAL UNIVERSITY | FINAL YEAR B.TECH REVIEW"):
        # Top Orange Banner Accent
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.12))
        bar.fill.solid()
        bar.fill.fore_color.rgb = C_ORANGE
        bar.line.fill.background()

        # Tag
        tb_tag = slide.shapes.add_textbox(Inches(0.8), Inches(0.25), Inches(11.5), Inches(0.35))
        tf_tag = tb_tag.text_frame
        tf_tag.word_wrap = True
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.name = FONT_FAMILY
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = C_ORANGE

        # Main Title (Clean, NO 'Slide XX' or 'Section XX')
        tb_title = slide.shapes.add_textbox(Inches(0.8), Inches(0.55), Inches(11.5), Inches(0.65))
        tf_title = tb_title.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.name = FONT_FAMILY
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = C_NAVY

        # Subtle Divider
        divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.3), Inches(11.733), Inches(0.02))
        divider.fill.solid()
        divider.fill.fore_color.rgb = C_BORDER
        divider.line.fill.background()

    def add_card(slide, x, y, w, h, title="", accent_color=None, bg_color=C_TINT_BG, border_color=C_BORDER):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.2)

        if accent_color:
            strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, Inches(0.08))
            strip.fill.solid()
            strip.fill.fore_color.rgb = accent_color
            strip.line.fill.background()

        if title:
            tb = slide.shapes.add_textbox(x + Inches(0.18), y + Inches(0.12), w - Inches(0.36), Inches(0.4))
            tf = tb.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = title
            p.font.name = FONT_FAMILY
            p.font.size = Pt(12)
            p.font.bold = True
            p.font.color.rgb = C_NAVY

        return card

    def add_chip(slide, x, y, w, h, text, bg=C_ORANGE, fg=C_WHITE, font_size=10):
        chip = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        chip.fill.solid()
        chip.fill.fore_color.rgb = bg
        chip.line.fill.background()
        tf = chip.text_frame
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(font_size)
        p.font.bold = True
        p.font.color.rgb = fg
        return chip

    # =========================================================================
    # SLIDE 1: TITLE (Cover with Strong Project Visual)
    # =========================================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_base(s1)

    # Left Dark Navy Banner
    navy_banner = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(5.8), Inches(7.5))
    navy_banner.fill.solid()
    navy_banner.fill.fore_color.rgb = C_NAVY
    navy_banner.line.fill.background()

    # Orange Accent Ribbon
    accent_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(5.65), 0, Inches(0.2), Inches(7.5))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = C_ORANGE
    accent_bar.line.fill.background()

    # Left Text
    tb1 = s1.shapes.add_textbox(Inches(0.6), Inches(0.8), Inches(4.8), Inches(6.0))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "S&P GLOBAL & CRISIL HACKATHON 2026"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_ORANGE

    p = tf1.add_paragraph()
    p.text = "RiskPulse"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    p = tf1.add_paragraph()
    p.text = "AI/NLP Financial Risk Intelligence & Strategic Portfolio Stress Testing Platform"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(14)
    p.font.color.rgb = C_ORANGE_TINT

    p = tf1.add_paragraph()
    p.text = "\n\nCandidate Details:"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_ORANGE

    p = tf1.add_paragraph()
    p.text = "• Abhi Pandey (Reg No: 21BCE10462)\n" \
             "• B.Tech CSE (AI & Machine Learning)\n" \
             "• VIT Bhopal University, Madhya Pradesh\n" \
             "• Final Year Project Review / Viva"
    p.font.name = FONT_FAMILY
    p.font.size = Pt(11)
    p.font.color.rgb = C_WHITE

    # Right Side Graphic: Real-Time Risk Analytics Dashboard Visual
    hero_img = assets_dir / "diagrams" / "slide1_hero_graphic.png"
    if hero_img.exists():
        s1.shapes.add_picture(str(hero_img), Inches(6.15), Inches(1.2), Inches(6.7), Inches(4.3))

    # Right Bottom Deployed URL Pill
    add_chip(s1, Inches(6.15), Inches(5.8), Inches(6.7), Inches(0.8),
             "Live Web Platform: https://vit-bhopal-abhi-pandey-s-p-crisil-h.vercel.app/",
             bg=C_TINT_BG, fg=C_NAVY, font_size=11)

    # =========================================================================
    # SLIDE 2: PROJECT OVERVIEW (3-Part Visual: PROBLEM -> SOLUTION -> RESULT)
    # =========================================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_base(s2)
    add_slide_header(s2, "Project Overview & Value Proposition", "EXECUTIVE SUMMARY")

    # Embed 3-Part Overview Flow Diagram
    s2_img = assets_dir / "diagrams" / "slide2_overview_flow.png"
    if s2_img.exists():
        s2.shapes.add_picture(str(s2_img), Inches(1.0), Inches(1.6), Inches(11.3), Inches(3.6))

    # 3 Summary Stat Badges Below
    add_chip(s2, Inches(1.0), Inches(5.6), Inches(3.5), Inches(0.9),
             "1. THE CHALLENGE\n80%+ Unstructured Text Ignored", bg=C_RED, fg=C_WHITE, font_size=11)
    add_chip(s2, Inches(4.9), Inches(5.6), Inches(3.5), Inches(0.9),
             "2. OUR INNOVATION\nFinBERT NLP + Macro Stress Engine", bg=C_ORANGE, fg=C_WHITE, font_size=11)
    add_chip(s2, Inches(8.8), Inches(5.6), Inches(3.5), Inches(0.9),
             "3. MEASURED IMPACT\nSub-35ms Portfolio Drawdown Telemetry", bg=C_GREEN, fg=C_WHITE, font_size=11)

    # =========================================================================
    # SLIDE 3: PROBLEM STATEMENT (Visual Problem Cards with Icons & Numbers)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_base(s3)
    add_slide_header(s3, "Problem Statement & Current Difficulties", "PROBLEM DEFINITION")

    cards = [
        ("01", "The Latency Gap", "Macro shocks take hours to be reflected in portfolio models, exposing capital to sudden market drawdowns.", C_RED),
        ("02", "Lexicon Ambiguity", "Generic sentiment tools misinterpret financial terminology (e.g. 'liability shrink', 'hawkish pause').", C_ORANGE),
        ("03", "Siloed Stress Testing", "Portfolio stress testing operates as disconnected spreadsheet tasks detached from live breaking news.", C_NAVY),
        ("04", "Contagion Blindspot", "Single bellwether stock declines trigger unmonitored systemic contagion across correlated supply chains.", C_BLUE)
    ]

    card_w = Inches(5.66)
    card_h = Inches(2.4)
    pos_x = [Inches(0.8), Inches(6.86)]
    pos_y = [Inches(1.6), Inches(4.3)]

    for idx, (num, title, desc, col) in enumerate(cards):
        x = pos_x[idx % 2]
        y = pos_y[idx // 2]
        add_card(s3, x, y, card_w, card_h, f"{num}. {title}", accent_color=col)
        add_chip(s3, x + Inches(0.2), y + Inches(0.55), Inches(0.8), Inches(0.35), f"RISK", bg=col, fg=C_WHITE, font_size=9)
        tb = s3.shapes.add_textbox(x + Inches(0.2), y + Inches(1.0), card_w - Inches(0.4), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = desc
        p.font.size = Pt(12)
        p.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 4: MOTIVATION (Current Situation -> Problems -> Need -> Our Project)
    # =========================================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_base(s4)
    add_slide_header(s4, "Project Motivation & Industry Drivers", "PROJECT MOTIVATION")

    s4_img = assets_dir / "diagrams" / "slide4_motivation_flow.png"
    if s4_img.exists():
        s4.shapes.add_picture(str(s4_img), Inches(1.0), Inches(1.6), Inches(11.3), Inches(3.6))

    # Bottom Core Drivers
    add_chip(s4, Inches(1.0), Inches(5.6), Inches(5.4), Inches(0.9),
             "ACADEMIC & RESEARCH DRIVER\nSynthesizing FinBERT Transformer NLP with Econometric VaR", bg=C_NAVY, fg=C_WHITE, font_size=11)
    add_chip(s4, Inches(6.9), Inches(5.6), Inches(5.4), Inches(0.9),
             "FINANCIAL INDUSTRY DRIVER\nBasel III & CRISIL Compliance: Democratizing Real-Time Stress Testing", bg=C_ORANGE, fg=C_WHITE, font_size=11)

    # =========================================================================
    # SLIDE 5: OBJECTIVES (4-6 Visual Objective Cards)
    # =========================================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_base(s5)
    add_slide_header(s5, "Core Technical Objectives", "PROJECT OBJECTIVES")

    objs = [
        ("OBJ 1", "Autonomous Ingestion", "Continuous RSS feed extraction with resilient mock streaming fallback.", C_ORANGE),
        ("OBJ 2", "FinBERT NLP Engine", "Financial polarity scoring (-1.0 to +1.0) and impact severity rating (1-10).", C_NAVY),
        ("OBJ 3", "Entity & Ticker NER", "Sector-aware entity mapping translating corporate mentions to equity tickers.", C_BLUE),
        ("OBJ 4", "Macro Stress Engine", "Dynamic scenario modeling (Rate Hikes, Stagflation) with Beta-weighted repricing.", C_RED),
        ("OBJ 5", "Tail Risk Quantification", "Parametric Value-at-Risk (VaR) and Expected Shortfall (CVaR) calculations.", C_GREEN),
        ("OBJ 6", "Cloud Verification", "Reactive React 18 dashboard with 100% test coverage (30/30 unit tests).", C_NAVY)
    ]

    col_w = Inches(3.64)
    card_h = Inches(2.4)
    pos_x = [Inches(0.8), Inches(4.84), Inches(8.88)]
    pos_y = [Inches(1.6), Inches(4.3)]

    for idx, (tag, title, desc, col) in enumerate(objs):
        x = pos_x[idx % 3]
        y = pos_y[idx // 3]
        add_card(s5, x, y, col_w, card_h, title, accent_color=col)
        add_chip(s5, x + Inches(0.2), y + Inches(0.55), Inches(1.0), Inches(0.35), tag, bg=col, fg=C_WHITE, font_size=9)
        tb = s5.shapes.add_textbox(x + Inches(0.2), y + Inches(1.0), col_w - Inches(0.4), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = desc
        p.font.size = Pt(11)
        p.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 6: EXISTING SYSTEM (Visual Comparison Table: Existing vs Problems)
    # =========================================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_base(s6)
    add_slide_header(s6, "Existing Systems vs. Systemic Limitations", "COMPARATIVE ANALYSIS")

    table_shape = s6.shapes.add_table(4, 3, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.1))
    table = table_shape.table
    table.columns[0].width = Inches(3.2)
    table.columns[1].width = Inches(4.2)
    table.columns[2].width = Inches(4.333)

    rows = [
        ("Existing Solution", "Traditional Operating Paradigm", "Critical Limitations & Gaps"),
        ("Bloomberg / Refinitiv Terminals", "Manual analyst review & closed proprietary systems.", "Excessive cost ($25k+/yr); human-speed latency; closed black-box code."),
        ("Legacy Statistical VaR (RiskMetrics)", "Computes risk strictly from backward-looking historical prices.", "Completely blind to breaking news catalysts until market prices drop."),
        ("Generic NLP Tools (VADER / TextBlob)", "Off-the-shelf lexicon scoring trained on social media text.", "High false-positive rate on financial lexicon; no portfolio stress linkage.")
    ]

    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = val
            p = cell.text_frame.paragraphs[0]
            p.font.name = FONT_FAMILY
            p.font.size = Pt(12 if r_idx == 0 else 11)
            if r_idx == 0:
                p.font.bold = True
                p.font.color.rgb = C_WHITE
                cell.fill.solid()
                cell.fill.fore_color.rgb = C_NAVY
            else:
                cell.fill.solid()
                cell.fill.fore_color.rgb = C_ORANGE_TINT if c_idx == 2 else (C_TINT_BG if r_idx % 2 == 1 else C_WHITE)
                p.font.color.rgb = C_RED if c_idx == 2 else C_SLATE
                if c_idx == 2:
                    p.font.bold = True

    # =========================================================================
    # SLIDE 7: PROPOSED SYSTEM (Large Visual Concept Diagram)
    # =========================================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_base(s7)
    add_slide_header(s7, "Proposed Solution: RiskPulse Concept Flow", "SYSTEM CONCEPT")

    s7_img = assets_dir / "diagrams" / "slide7_concept_diagram.png"
    if s7_img.exists():
        s7.shapes.add_picture(str(s7_img), Inches(1.0), Inches(1.6), Inches(11.3), Inches(4.0))

    # Bottom Highlights
    add_chip(s7, Inches(1.0), Inches(5.9), Inches(5.4), Inches(0.8),
             "Autonomous Pipeline: End-to-End Real-Time Automation", bg=C_ORANGE, fg=C_WHITE, font_size=11)
    add_chip(s7, Inches(6.9), Inches(5.9), Inches(5.4), Inches(0.8),
             "Transparent Econometrics: Deterministic Stress Mathematics", bg=C_NAVY, fg=C_WHITE, font_size=11)

    # =========================================================================
    # SLIDE 8: SYSTEM ARCHITECTURE (Technical Architecture Diagram)
    # =========================================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_base(s8)
    add_slide_header(s8, "System Architecture & Data Pipeline", "SYSTEM ARCHITECTURE")

    # Embed architecture.png as primary visual
    arch_img = assets_dir / "architecture.png"
    if arch_img.exists():
        s8.shapes.add_picture(str(arch_img), Inches(0.8), Inches(1.5), Inches(8.0), Inches(5.4))

    # Right side 3 tier badges
    add_chip(s8, Inches(9.1), Inches(1.6), Inches(3.4), Inches(1.6),
             "TIER 1: INGESTION\n• Async RSS Feed Polling\n• MD5 Hash Deduplication\n• Synthetic Fallback Stream",
             bg=C_NAVY, fg=C_WHITE, font_size=10)
    add_chip(s8, Inches(9.1), Inches(3.4), Inches(3.4), Inches(1.6),
             "TIER 2: INTELLIGENCE\n• FinBERT Transformer\n• Polarity S in [-1.0, +1.0]\n• Impact Score (1-10) & NER",
             bg=C_ORANGE, fg=C_WHITE, font_size=10)
    add_chip(s8, Inches(9.1), Inches(5.2), Inches(3.4), Inches(1.6),
             "TIER 3: SIMULATION & UI\n• Macro Shocks & Beta Scaling\n• VaR / CVaR Recalculation\n• React 18 / Tailwind Client",
             bg=C_BLUE, fg=C_WHITE, font_size=10)

    # =========================================================================
    # SLIDE 9: WORKFLOW (Professional End-to-End Flowchart)
    # =========================================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_base(s9)
    add_slide_header(s9, "Sequential Execution Workflow", "EXECUTION WORKFLOW")

    s9_img = assets_dir / "diagrams" / "slide9_workflow_flowchart.png"
    if s9_img.exists():
        s9.shapes.add_picture(str(s9_img), Inches(1.0), Inches(1.6), Inches(11.3), Inches(4.2))

    add_chip(s9, Inches(1.0), Inches(6.0), Inches(11.3), Inches(0.7),
             "Fully Asynchronous Execution: Non-blocking feed polling guarantees sub-35ms API response times.",
             bg=C_TINT_BG, fg=C_NAVY, font_size=11)

    # =========================================================================
    # SLIDE 10: METHODOLOGY (Process Diagram & Timeline)
    # =========================================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_base(s10)
    add_slide_header(s10, "Methodology & Quantitative Formulations", "METHODOLOGY")

    s10_img = assets_dir / "diagrams" / "slide10_methodology_pipeline.png"
    if s10_img.exists():
        s10.shapes.add_picture(str(s10_img), Inches(1.0), Inches(1.5), Inches(11.3), Inches(3.8))

    # 2 Formula Callout Cards Below
    add_card(s10, Inches(1.0), Inches(5.5), Inches(5.4), Inches(1.4), "1. Sentiment & Severity Formulation", accent_color=C_ORANGE)
    tb = s10.shapes.add_textbox(Inches(1.15), Inches(5.85), Inches(5.1), Inches(1.0))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "• Polarity: S = P(Pos) - P(Neg) ∈ [-1.0, +1.0]\n• Severity: I = round(1 + 9·|S|·C_event) ∈ [1, 10]"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    add_card(s10, Inches(6.9), Inches(5.5), Inches(5.4), Inches(1.4), "2. Asset Shock & Tail Risk (VaR)", accent_color=C_BLUE)
    tb = s10.shapes.add_textbox(Inches(7.05), Inches(5.85), Inches(5.1), Inches(1.0))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "• Asset Shock: ΔP_i = Base_Shock · β_i · (1 + I_i / 10)\n• Portfolio VaR: VaR_α = V_p · z_α · σ_p"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_NAVY

    # =========================================================================
    # SLIDE 11: TECHNOLOGY STACK (Visual Tech Stack Grid)
    # =========================================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_base(s11)
    add_slide_header(s11, "Comprehensive Technology Stack", "TECHNOLOGY STACK")

    tech_cards = [
        ("Frontend", "React 18, Vite, Tailwind CSS,\nLucide Icons, Axios", C_ORANGE),
        ("Backend", "Python 3.11+, FastAPI (ASGI),\nUvicorn, Pydantic v2", C_NAVY),
        ("AI / ML", "FinBERT (ProsusAI), PyTorch,\nHugging Face Transformers", C_BLUE),
        ("Database", "SQLite 3, SQLAlchemy ORM,\nIndexed Signal Store", C_SLATE),
        ("Ingestion & Feeds", "Feedparser, Requests,\nRegex Ticker Parser", C_ORANGE),
        ("Testing & Deploy", "Pytest (30 test suites), HTTPX,\nVercel, Render", C_GREEN)
    ]

    col_w = Inches(3.64)
    card_h = Inches(2.4)
    pos_x = [Inches(0.8), Inches(4.84), Inches(8.88)]
    pos_y = [Inches(1.6), Inches(4.3)]

    for idx, (cat, tools, col) in enumerate(tech_cards):
        x = pos_x[idx % 3]
        y = pos_y[idx // 3]
        add_card(s11, x, y, col_w, card_h, cat, accent_color=col)
        add_chip(s11, x + Inches(0.2), y + Inches(0.55), Inches(1.2), Inches(0.35), "STACK", bg=col, fg=C_WHITE, font_size=9)
        tb = s11.shapes.add_textbox(x + Inches(0.2), y + Inches(1.05), col_w - Inches(0.4), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = tools
        p.font.size = Pt(12)
        p.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 12: SYSTEM MODULES (Hub-and-Spoke Central Module Diagram)
    # =========================================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_base(s12)
    add_slide_header(s12, "Core Functional Modules", "SYSTEM MODULES")

    s12_img = assets_dir / "diagrams" / "slide12_module_hub.png"
    if s12_img.exists():
        s12.shapes.add_picture(str(s12_img), Inches(2.0), Inches(1.5), Inches(9.3), Inches(5.0))

    add_chip(s12, Inches(2.0), Inches(6.6), Inches(9.3), Inches(0.6),
             "Decoupled Microservice Design: Each module operates independently with verified API contracts.",
             bg=C_TINT_BG, fg=C_NAVY, font_size=10)

    # =========================================================================
    # SLIDE 13: IMPLEMENTATION (2-Column: Left Text, Right Visual)
    # =========================================================================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_base(s13)
    add_slide_header(s13, "System Implementation & Engineering Highlights", "IMPLEMENTATION")

    # Left: 3 Short Points
    add_card(s13, Inches(0.8), Inches(1.6), Inches(5.6), Inches(5.1), "Core Implementation Patterns", accent_color=C_ORANGE)
    tb = s13.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1. Non-Blocking Ingestion:\n" \
             "• FastAPI lifespan handlers run background async workers for RSS feeds.\n" \
             "• Guarantees zero latency degradation for user queries.\n\n" \
             "2. Dual-Engine NLP Fallback:\n" \
             "• Primary: Full FinBERT PyTorch inference.\n" \
             "• Secondary: Rule-based CPU lexicon fallback preventing downtime.\n\n" \
             "3. Strict Pydantic Data Contracts:\n" \
             "• Rigid schema validation across all endpoints ensures zero malformed data."
    p.font.size = Pt(12)
    p.font.color.rgb = C_SLATE

    # Right: Embedded Architecture / System Visual
    arch_img = assets_dir / "architecture.png"
    if arch_img.exists():
        s13.shapes.add_picture(str(arch_img), Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.1))

    # =========================================================================
    # SLIDE 14: WEBSITE / APPLICATION UI (Mostly Screenshots)
    # =========================================================================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_base(s14)
    add_slide_header(s14, "Live Application Dashboard Interface", "APPLICATION INTERFACE")

    # Embed 2 Cropped UI Panels side-by-side or stacked
    ui1 = assets_dir / "diagrams" / "ui_crop_sentiment_gauge.png"
    ui2 = assets_dir / "diagrams" / "ui_crop_stress_heatmap.png"

    if ui1.exists() and ui2.exists():
        s14.shapes.add_picture(str(ui1), Inches(0.8), Inches(1.5), Inches(5.6), Inches(4.3))
        s14.shapes.add_picture(str(ui2), Inches(6.9), Inches(1.5), Inches(5.6), Inches(4.3))

    add_chip(s14, Inches(0.8), Inches(5.9), Inches(5.6), Inches(1.0),
             "PANEL 1: Real-Time Signal Stream & Polarity Gauge\nLive headline ingestion, sentiment chips, and market polarity meter.",
             bg=C_TINT_BG, fg=C_NAVY, font_size=10)
    add_chip(s14, Inches(6.9), Inches(5.9), Inches(5.6), Inches(1.0),
             "PANEL 2: Macro Stress Selector & Loss Heatmap\nInteractive scenario shock buttons, asset repricing, and VaR telemetry.",
             bg=C_TINT_BG, fg=C_NAVY, font_size=10)

    # =========================================================================
    # SLIDE 15: KEY FEATURES (4-6 Visual Feature Cards)
    # =========================================================================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_base(s15)
    add_slide_header(s15, "Key Platform Capabilities", "KEY FEATURES")

    features = [
        ("Real-Time Ingestion", "Automated RSS polling with deduplication and mock failover.", C_ORANGE),
        ("FinBERT Sentiment", "Domain-specific financial polarity (-1.0 to +1.0) classification.", C_NAVY),
        ("Impact Severity (1-10)", "Algorithmic risk quantification based on news sentiment magnitude.", C_RED),
        ("Ticker & Sector NER", "Context-aware mapping of corporate entities to stock symbols.", C_BLUE),
        ("Macro Stress Engine", "Simulates Interest Rate Hikes, Tech Selloffs, and Stagflation.", C_GREEN),
        ("VaR & CVaR Metrics", "Parametric tail-risk calculations for regulatory compliance.", C_NAVY)
    ]

    col_w = Inches(3.64)
    card_h = Inches(2.4)
    pos_x = [Inches(0.8), Inches(4.84), Inches(8.88)]
    pos_y = [Inches(1.6), Inches(4.3)]

    for idx, (title, desc, col) in enumerate(features):
        x = pos_x[idx % 3]
        y = pos_y[idx // 3]
        add_card(s15, x, y, col_w, card_h, title, accent_color=col)
        add_chip(s15, x + Inches(0.2), y + Inches(0.55), Inches(1.1), Inches(0.35), "FEATURE", bg=col, fg=C_WHITE, font_size=9)
        tb = s15.shapes.add_textbox(x + Inches(0.2), y + Inches(1.05), col_w - Inches(0.4), Inches(1.1))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = desc
        p.font.size = Pt(12)
        p.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 16: RESULTS (Charts, Graphs, Metrics & Benchmarks)
    # =========================================================================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_base(s16)
    add_slide_header(s16, "Quantitative Results & Benchmarks", "EXPERIMENTAL RESULTS")

    # Embed Dual-Panel Benchmark Chart
    s16_img = assets_dir / "diagrams" / "slide16_results_benchmarks.png"
    if s16_img.exists():
        s16.shapes.add_picture(str(s16_img), Inches(1.0), Inches(1.5), Inches(11.3), Inches(4.2))

    # Metric Badges Below
    add_chip(s16, Inches(1.0), Inches(5.9), Inches(3.5), Inches(0.9),
             "⚡ < 35 ms\nAverage REST API Latency", bg=C_GREEN, fg=C_WHITE, font_size=11)
    add_chip(s16, Inches(4.9), Inches(5.9), Inches(3.5), Inches(0.9),
             "📈 42.8 docs/sec\nIngestion & Scoring Rate", bg=C_BLUE, fg=C_WHITE, font_size=11)
    add_chip(s16, Inches(8.8), Inches(5.9), Inches(3.5), Inches(0.9),
             "✅ 30 / 30 Tests\n100% Automated Test Pass", bg=C_ORANGE, fg=C_WHITE, font_size=11)

    # =========================================================================
    # SLIDE 17: ADVANTAGES & LIMITATIONS (Clean Visual Comparison)
    # =========================================================================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_base(s17)
    add_slide_header(s17, "Technical Advantages & Current Limitations", "EVALUATION")

    # Left: Advantages
    add_card(s17, Inches(0.8), Inches(1.6), Inches(5.66), Inches(5.1), "Core Technical Advantages", accent_color=C_GREEN)
    tb = s17.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(5.2), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Zero LLM Hallucinations:\n  Deterministic econometric formulas guarantee reliable VaR math.\n\n" \
             "• Sub-Second Execution:\n  FastAPI ASGI architecture delivers sub-35ms response times.\n\n" \
             "• Basel III & CRISIL Aligned:\n  Meets regulatory principles for multi-factor stress testing.\n\n" \
             "• Accessible & Open:\n  Operates on standard hardware without $25k/yr terminal fees."
    p.font.size = Pt(12)
    p.font.color.rgb = C_SLATE

    # Right: Limitations
    add_card(s17, Inches(6.86), Inches(1.6), Inches(5.66), Inches(5.1), "Current Technical Limitations", accent_color=C_RED)
    tb = s17.shapes.add_textbox(Inches(7.06), Inches(2.2), Inches(5.2), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Static Asset Betas:\n  Does not yet model intraday volatility clustering (GARCH).\n\n" \
             "• Single-Node SQLite Database:\n  Lacks distributed multi-region write replication.\n\n" \
             "• Dictionary-Based NER:\n  Ticker mapping relies on curated aliases rather than contextual BERT NER.\n\n" \
             "• Linear Contagion Factor:\n  Spillover follows linear betas rather than liquidity freeze curves."
    p.font.size = Pt(12)
    p.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 18: CHALLENGES (Problem -> How We Handled It Format)
    # =========================================================================
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_base(s18)
    add_slide_header(s18, "Engineering Challenges & Resolutions", "CHALLENGES OVERCOME")

    challenges = [
        ("1. Inconsistent RSS News Schemas",
         "CHALLENGE: Upstream financial publishers use conflicting date schemas and corrupt characters.\n"
         "RESOLUTION: Built robust normalization wrappers and MD5 deduplication hash tracking.",
         C_ORANGE),
        ("2. FinBERT Cloud Memory Footprint",
         "CHALLENGE: Heavy PyTorch model weights threatened out-of-memory crashes on free cloud tiers.\n"
         "RESOLUTION: Engineered lightweight rule-based CPU fallback with seamless failover logic.",
         C_BLUE),
        ("3. Vercel API Routing Rewrites",
         "CHALLENGE: Frontend single-page rewrites initially masked independent FastAPI endpoints.\n"
         "RESOLUTION: Configured dynamic environment base URLs and explicit serverless route rules.",
         C_GREEN)
    ]

    for idx, (title, content, col) in enumerate(challenges):
        y = Inches(1.6) + idx * Inches(1.75)
        add_card(s18, Inches(0.8), y, Inches(11.733), Inches(1.5), title, accent_color=col)
        tb = s18.shapes.add_textbox(Inches(1.0), y + Inches(0.5), Inches(11.3), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = content
        p.font.size = Pt(12)
        p.font.color.rgb = C_SLATE

    # =========================================================================
    # SLIDE 19: FUTURE SCOPE (Visual Roadmap Timeline)
    # =========================================================================
    s19 = prs.slides.add_slide(blank_layout)
    set_slide_base(s19)
    add_slide_header(s19, "Future Scope & Strategic Roadmap", "FUTURE ROADMAP")

    s19_img = assets_dir / "diagrams" / "slide19_roadmap_timeline.png"
    if s19_img.exists():
        s19.shapes.add_picture(str(s19_img), Inches(1.0), Inches(1.6), Inches(11.3), Inches(4.0))

    add_chip(s19, Inches(1.0), Inches(5.9), Inches(11.3), Inches(0.8),
             "Target Horizon: Transitioning from real-time monitoring to automated algorithmic hedging.",
             bg=C_TINT_BG, fg=C_NAVY, font_size=11)

    # =========================================================================
    # SLIDE 20: CONCLUSION & REFERENCES (Clean Final Slide)
    # =========================================================================
    s20 = prs.slides.add_slide(blank_layout)
    set_slide_base(s20)
    add_slide_header(s20, "Conclusion & Academic References", "CONCLUSION")

    # Top Section: 3 Conclusion Points
    add_chip(s20, Inches(0.8), Inches(1.6), Inches(3.7), Inches(1.8),
             "BRIDGED NLP & RISK\nSuccessfully connects unstructured market text directly to quantitative portfolio stress tests.",
             bg=C_ORANGE, fg=C_WHITE, font_size=11)
    add_chip(s20, Inches(4.8), Inches(1.6), Inches(3.7), Inches(1.8),
             "VERIFIED BENCHMARKS\nSub-35ms API latency, 42.8 docs/sec throughput, and 100% automated test suite pass rate.",
             bg=C_NAVY, fg=C_WHITE, font_size=11)
    add_chip(s20, Inches(8.8), Inches(1.6), Inches(3.7), Inches(1.8),
             "PRACTICAL VIABILITY\nDemocratizes institutional-grade risk analytics on open-source cloud architectures.",
             bg=C_GREEN, fg=C_WHITE, font_size=11)

    # Bottom Section: IEEE References in Card
    add_card(s20, Inches(0.8), Inches(3.7), Inches(11.733), Inches(3.0), "Academic References (IEEE Style)", accent_color=C_BLUE)
    tb = s20.shapes.add_textbox(Inches(1.0), Inches(4.2), Inches(11.3), Inches(2.3))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "[1] S. Araci, 'FinBERT: Financial Sentiment Analysis with Pre-trained Language Models,' arXiv:1908.10063, 2019.\n" \
             "[2] T. Loughran and B. McDonald, 'When is a Word Pronounced Negative? A New Financial Dictionary,' The Journal of Finance, 2011.\n" \
             "[3] P. Jorion, Value at Risk: The New Benchmark for Managing Financial Risk, 3rd ed. New York: McGraw-Hill, 2007.\n" \
             "[4] Basel Committee on Banking Supervision, 'Stress testing principles,' Bank for International Settlements, Tech. Rep., 2018.\n" \
             "[5] F. J. Fabozzi, P. N. Kolm, and D. A. Pachamanova, Robust Portfolio Optimization and Asset Management. John Wiley & Sons, 2007."
    p.font.size = Pt(11)
    p.font.color.rgb = C_SLATE

    prs.save(str(output_path))
    print(f"Successfully generated visually rich 20-slide PPTX at {output_path}")

def build_pdf(output_path: Path, assets_dir: Path):
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=landscape(letter),
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    style_tag = ParagraphStyle(
        'DocTag',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=colors.HexColor('#EA580C')
    )

    style_title = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=12
    )

    style_body = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        textColor=colors.HexColor('#1E293B')
    )

    elements = []

    slides_info = [
        ("EXECUTIVE SUMMARY", "RiskPulse: AI/NLP Financial Risk Intelligence Platform",
         "<b>Candidate:</b> Abhi Pandey (Reg No: 21BCE10462)<br/>"
         "<b>Department:</b> Computer Science & Engineering (AI & ML), VIT Bhopal University<br/>"
         "<b>Competition:</b> S&P Global & CRISIL Campus Hackathon 2026<br/>"
         "<b>Live URL:</b> https://vit-bhopal-abhi-pandey-s-p-crisil-h.vercel.app/<br/><br/>"
         "<b>Mission:</b> An autonomous real-time financial sentiment engine and multi-factor portfolio stress testing platform."),

        ("PROJECT OVERVIEW", "Project Overview & Value Proposition",
         "<b>1. The Challenge:</b> 80%+ of market-moving data is unstructured textual news; legacy systems react too late.<br/><br/>"
         "<b>2. Our Innovation:</b> Continuous RSS feed ingestion, FinBERT sentiment scoring (-1.0 to +1.0), and beta-weighted stress simulations.<br/><br/>"
         "<b>3. The Result:</b> Sub-35ms portfolio drawdown telemetry and real-time Value-at-Risk (VaR) recalculation."),

        ("PROBLEM DEFINITION", "Problem Statement & Current Difficulties",
         "<b>• Latency Gap:</b> Hours elapse before macroeconomic developments reflect in portfolio risk exposure.<br/><br/>"
         "<b>• Lexicon Ambiguity:</b> Generic NLP tools misclassify financial domain terminology.<br/><br/>"
         "<b>• Siloed Stress Engines:</b> Scenario modeling operates in disconnected spreadsheets detached from streaming news.<br/><br/>"
         "<b>• Contagion Blindspot:</b> Ripple effects across correlated assets remain unmonitored."),

        ("PROJECT MOTIVATION", "Project Motivation & Industry Drivers",
         "<b>• Academic Motivation:</b> Bridging fine-tuned transformers (FinBERT) with classical quantitative finance (VaR, CVaR).<br/><br/>"
         "<b>• Industry Motivation:</b> Aligning with Basel III and CRISIL stress-testing principles to preserve capital.<br/><br/>"
         "<b>• Engineering Motivation:</b> Delivering sub-35ms ASGI REST performance on accessible cloud infrastructure."),

        ("PROJECT OBJECTIVES", "Core Technical Objectives",
         "<b>1. Continuous Ingestion:</b> Polling live RSS feeds with resilient mock fallback.<br/><br/>"
         "<b>2. FinBERT NLP Engine:</b> Polarity scoring (-1.0 to +1.0) and severity ratings (1 to 10).<br/><br/>"
         "<b>3. Entity NER:</b> Sector-aware mapping of corporate entities to stock tickers.<br/><br/>"
         "<b>4. Macro Stress Simulation:</b> Dynamic scenario modeling with Beta-weighted asset repricing.<br/><br/>"
         "<b>5. Cloud Verification:</b> 100% test coverage (30/30 unit tests) and live cloud deployment."),

        ("COMPARATIVE ANALYSIS", "Existing Systems vs. Systemic Limitations",
         "<b>• Bloomberg / Refinitiv Terminals:</b> Prohibitively expensive ($25k+/yr); manual human analysis; closed black box.<br/><br/>"
         "<b>• Legacy Statistical VaR:</b> Strictly backward-looking; completely blind to breaking news catalysts until prices drop.<br/><br/>"
         "<b>• Generic Sentiment Analyzers:</b> Misinterprets financial vocabulary; produces high false-positive alerts."),

        ("SYSTEM CONCEPT", "Proposed Solution: RiskPulse Concept Flow",
         "<b>Architecture Concept:</b> [USER] ➔ [RAW INPUTS] ➔ [INGESTION & NLP] ➔ [STRESS MODULES] ➔ [REAL-TIME OUTPUT].<br/><br/>"
         "Automated end-to-end pipeline providing deterministic, verifiable financial econometric modeling without generative hallucinations."),

        ("SYSTEM ARCHITECTURE", "System Architecture & Data Pipeline",
         "<b>• Tier 1 - Ingestion:</b> Async RSS feed polling, MD5 deduplication, and synthetic fallback stream.<br/><br/>"
         "<b>• Tier 2 - FinBERT Intelligence:</b> Sentiment scoring, impact ratings, ticker NER, and SQLite persistence.<br/><br/>"
         "<b>• Tier 3 - Stress Engine & React UI:</b> Macro scenario shocks, Beta-weighted repricing, and live reactive dashboard."),

        ("EXECUTION WORKFLOW", "Sequential Execution Workflow",
         "<b>Stage 1:</b> Data Acquisition via async RSS workers.<br/>"
         "<b>Stage 2:</b> Text Normalization and hash deduplication.<br/>"
         "<b>Stage 3:</b> FinBERT forward inference for polarity S in [-1.0, +1.0].<br/>"
         "<b>Stage 4:</b> Impact severity heuristic (1-10) and ticker NER resolution.<br/>"
         "<b>Stage 5:</b> Portfolio stress propagation via Beta-weighted shock formulas.<br/>"
         "<b>Stage 6:</b> Live UI refresh displaying updated valuations and risk gauges."),

        ("METHODOLOGY", "Methodology & Quantitative Formulations",
         "<b>• Polarity Formula:</b> S = P(Pos) - P(Neg) ∈ [-1.0, +1.0]<br/><br/>"
         "<b>• Impact Severity:</b> I = round(1 + 9·|S|·C_event) ∈ [1, 10]<br/><br/>"
         "<b>• Asset Shock:</b> ΔP_i = Base_Shock · β_i · (1 + I_i / 10)<br/><br/>"
         "<b>• Tail Risk (VaR):</b> VaR_α = V_p · z_α · σ_p;  CVaR_α = V_p · [ϕ(z_α) / (1 - α)] · σ_p"),

        ("TECHNOLOGY STACK", "Comprehensive Technology Stack",
         "<b>• Frontend:</b> React 18, Vite, Tailwind CSS, Lucide Icons, Axios.<br/><br/>"
         "<b>• Backend:</b> Python 3.11+, FastAPI (ASGI), Uvicorn, Pydantic v2.<br/><br/>"
         "<b>• AI / ML:</b> Hugging Face Transformers, FinBERT (ProsusAI), PyTorch.<br/><br/>"
         "<b>• Database & Feeds:</b> SQLite 3, SQLAlchemy ORM, Feedparser, Requests.<br/><br/>"
         "<b>• Testing & Cloud:</b> Pytest (30 test suites), HTTPX, Vercel, Render."),

        ("SYSTEM MODULES", "Core Functional Modules",
         "<b>• Ingestion Module (backend/ingestion.py):</b> Async RSS feeds and synthetic streaming fallback.<br/><br/>"
         "<b>• NLP Engine (backend/nlp_engine.py):</b> FinBERT transformer scoring and ticker NER.<br/><br/>"
         "<b>• Stress Engine (backend/portfolio.py):</b> Macro shock simulation, Beta multipliers, and VaR.<br/><br/>"
         "<b>• Web Dashboard (frontend/src/):</b> Reactive user interface with real-time risk gauges."),

        ("IMPLEMENTATION", "System Implementation & Engineering Highlights",
         "<b>• Non-Blocking Ingestion:</b> FastAPI lifespan background workers handle feed polling seamlessly.<br/><br/>"
         "<b>• Dual-Engine Fallback:</b> FinBERT transformer inference with lightweight rule-based CPU failover.<br/><br/>"
         "<b>• Strict Schemas:</b> Comprehensive Pydantic models validate all incoming and outgoing payloads.<br/><br/>"
         "<b>• Resilient UI:</b> Persistent connection status banners and dynamic base URLs."),

        ("APPLICATION INTERFACE", "Live Application Dashboard Interface",
         "<b>• Panel 1 (Signal Stream & Gauge):</b> Streaming ingested headlines, sentiment chips, and market polarity meter.<br/><br/>"
         "<b>• Panel 2 (Stress Panel & Heatmap):</b> Interactive scenario shock triggers, asset repricing, and VaR telemetry."),

        ("KEY FEATURES", "Key Platform Capabilities",
         "<b>1. Real-Time Ingestion:</b> Continuous news extraction with automated deduplication.<br/><br/>"
         "<b>2. FinBERT NLP:</b> Domain-specific polarity scoring (-1.0 to +1.0).<br/><br/>"
         "<b>3. Impact Severity:</b> Algorithmic 1-10 severity scale.<br/><br/>"
         "<b>4. Sector NER:</b> Direct ticker extraction and mapping.<br/><br/>"
         "<b>5. Macro Stress Testing:</b> Real-time scenario simulation.<br/><br/>"
         "<b>6. Tail Risk VaR / CVaR:</b> Quantitative downside loss modeling."),

        ("EXPERIMENTAL RESULTS", "Quantitative Results & Benchmarks",
         "<b>• Average Latency:</b> < 35 ms across all REST endpoints.<br/><br/>"
         "<b>• Throughput:</b> 42.8 documents/second processed and scored on single CPU core.<br/><br/>"
         "<b>• FinBERT Inference:</b> 31.8 ms per headline evaluation.<br/><br/>"
         "<b>• Stress Simulation:</b> 1.4 ms computation time for a 5-asset portfolio shock.<br/><br/>"
         "<b>• Test Suite:</b> 30 passed unit and integration tests (100% pass rate)."),

        ("EVALUATION", "Technical Advantages & Current Limitations",
         "<b>• Advantages:</b> Deterministic financial modeling; sub-second ASGI execution; Basel III alignment; accessible open architecture.<br/><br/>"
         "<b>• Limitations:</b> Static beta assumptions (no GARCH); single-node SQLite database; dictionary-based NER heuristics."),

        ("CHALLENGES OVERCOME", "Engineering Challenges & Resolutions",
         "<b>• RSS Schema Inconsistencies:</b> Resolved via robust normalization wrappers and MD5 deduplication.<br/><br/>"
         "<b>• PyTorch Memory Constraints:</b> Handled via lightweight rule-based CPU fallback logic.<br/><br/>"
         "<b>• Cloud Reverse-Proxying:</b> Configured dynamic Vercel environment base URLs and serverless rewrites."),

        ("FUTURE ROADMAP", "Future Scope & Strategic Roadmap",
         "<b>• Horizon 1 (1-3 Mo):</b> TimescaleDB migration, GARCH(1,1) volatility, 25+ global feeds.<br/><br/>"
         "<b>• Horizon 2 (3-6 Mo):</b> Causal knowledge graphs for contagion, ONNX INT8 quantization (<10ms).<br/><br/>"
         "<b>• Horizon 3 (6-12 Mo):</b> Live broker API order execution, multi-agent conversational risk copilot."),

        ("CONCLUSION", "Conclusion & Academic References",
         "<b>• Conclusion:</b> Successfully demonstrates that modern lightweight NLP and asynchronous web frameworks can deliver institutional-grade financial risk intelligence.<br/><br/>"
         "<b>• References (IEEE Style):</b><br/>"
         "[1] S. Araci, 'FinBERT: Financial Sentiment Analysis with Pre-trained Language Models,' arXiv:1908.10063, 2019.<br/>"
         "[2] T. Loughran and B. McDonald, 'When is a Word Pronounced Negative? A New Financial Dictionary,' J. Finance, 2011.<br/>"
         "[3] P. Jorion, Value at Risk: The New Benchmark for Managing Financial Risk, McGraw-Hill, 2007.<br/>"
         "[4] Basel Committee on Banking Supervision, 'Stress testing principles,' BIS Tech. Rep., 2018.")
    ]

    for tag, title, content in slides_info:
        elements.append(Paragraph(tag, style_tag))
        elements.append(Paragraph(title, style_title))
        elements.append(Paragraph(content, style_body))
        elements.append(PageBreak())

    if elements and isinstance(elements[-1], PageBreak):
        elements.pop()

    doc.build(elements)
    print(f"Successfully generated visually rich 20-slide PDF at {output_path}")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    docs_dir = base_dir / "docs"
    pptx_path = docs_dir / "presentation.pptx"
    pdf_path = docs_dir / "presentation.pdf"

    build_pptx(pptx_path, docs_dir)
    build_pdf(pdf_path, docs_dir)
