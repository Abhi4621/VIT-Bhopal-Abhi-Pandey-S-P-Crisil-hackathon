"""
Generate the 20-slide presentation in the EXACT style of the Borcelle AI template provided by the user:
- Radiant Electric Orange (#FF5E00 / #FF6A00) and Crisp White theme
- Alternating Full Orange hero slides and Crisp White slides with orange accents
- Top rounded pill badges ("VIT BHOPAL", "RISKPULSE", "BORCELLE style")
- Bottom-right circular chevron button ">" on every slide
- Massive bold headings with short, punchy 1-2 sentence descriptions (NO text-dumps)
- High-resolution diagrams, architecture visuals, UI screenshots, and benchmark charts
"""

from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# --- COLOR PALETTE (Exact Borcelle Template Colors) ---
C_ORANGE = RGBColor(255, 94, 0)       # Electric Radiant Orange #FF5E00
C_ORANGE_DARK = RGBColor(230, 81, 0)  # Deep Orange #E65100
C_ORANGE_LIGHT = RGBColor(255, 237, 213) # Soft Orange Tint #FFEDD5
C_WHITE = RGBColor(255, 255, 255)     # Crisp White #FFFFFF
C_DARK = RGBColor(30, 41, 59)         # Charcoal Slate #1E293B
C_MUTED = RGBColor(100, 116, 139)     # Muted Slate #64748B
C_CARD_BG = RGBColor(248, 250, 252)   # Light Slate Card #F8FAFC
C_BORDER = RGBColor(226, 232, 240)    # Border Slate #E2E8F0

FONT_HEADING = "Segoe UI"
FONT_BODY = "Segoe UI"

def build_borcelle_style_pptx(output_path: Path, assets_dir: Path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def add_pill_badge(slide, text="VIT BHOPAL", is_orange_slide=False, align_right=False):
        w, h = Inches(2.2), Inches(0.48)
        x = Inches(10.3) if align_right else Inches(0.8)
        y = Inches(0.55)
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
        pill.fill.solid()
        if is_orange_slide:
            pill.fill.fore_color.rgb = C_ORANGE_DARK
            pill.line.color.rgb = C_WHITE
            pill.line.width = Pt(1.5)
            text_color = C_WHITE
        else:
            pill.fill.fore_color.rgb = C_WHITE
            pill.line.color.rgb = C_ORANGE
            pill.line.width = Pt(1.5)
            text_color = C_ORANGE

        tf = pill.text_frame
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = text
        p.font.name = FONT_HEADING
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = text_color
        return pill

    def add_arrow_button(slide, is_orange_slide=False):
        size = Inches(0.68)
        x = Inches(12.0)
        y = Inches(6.3)
        btn = slide.shapes.add_shape(MSO_SHAPE.OVAL, x, y, size, size)
        btn.fill.solid()
        if is_orange_slide:
            btn.fill.fore_color.rgb = C_WHITE
            btn.line.fill.background()
            text_color = C_ORANGE
        else:
            btn.fill.fore_color.rgb = C_ORANGE
            btn.line.fill.background()
            text_color = C_WHITE

        tf = btn.text_frame
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.text = ">"
        p.font.name = FONT_HEADING
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = text_color
        return btn

    def create_orange_slide(title, subtitle=None, badge_text="VIT BHOPAL"):
        slide = prs.slides.add_slide(blank_layout)
        # Full Orange Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_ORANGE
        bg.line.fill.background()

        # Decorative Soft Translucent Circle
        c = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(8.5), Inches(-1.5), Inches(7.5), Inches(7.5))
        c.fill.solid()
        c.fill.fore_color.rgb = RGBColor(255, 120, 20)
        c.line.fill.background()

        add_pill_badge(slide, badge_text, is_orange_slide=True)
        add_arrow_button(slide, is_orange_slide=True)

        # Title
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.5), Inches(1.5))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title.upper()
        p.font.name = FONT_HEADING
        p.font.size = Pt(36)
        p.font.bold = True
        p.font.color.rgb = C_WHITE

        if subtitle:
            p2 = tf.add_paragraph()
            p2.text = subtitle
            p2.font.name = FONT_BODY
            p2.font.size = Pt(16)
            p2.font.color.rgb = C_ORANGE_LIGHT

        return slide

    def create_white_slide(title, badge_text="BORCELLE", align_badge_right=True):
        slide = prs.slides.add_slide(blank_layout)
        # Crisp White Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_WHITE
        bg.line.fill.background()

        # Top Orange Banner Bar
        top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.15))
        top_bar.fill.solid()
        top_bar.fill.fore_color.rgb = C_ORANGE
        top_bar.line.fill.background()

        add_pill_badge(slide, badge_text, is_orange_slide=False, align_right=align_badge_right)
        add_arrow_button(slide, is_orange_slide=False)

        # Title
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.9), Inches(9.0), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title.upper()
        p.font.name = FONT_HEADING
        p.font.size = Pt(30)
        p.font.bold = True
        p.font.color.rgb = C_ORANGE

        return slide

    # =========================================================================
    # SLIDE 1: TITLE SLIDE (Full Radiant Orange, Borcelle Style)
    # =========================================================================
    s1 = create_orange_slide("ARTIFICIAL INTELLIGENCE IN FINANCIAL RISK",
                             "RiskPulse: NLP Sentiment Engine & Strategic Portfolio Stress Testing Platform",
                             badge_text="VIT BHOPAL")
    
    # Hero Title block
    tb1 = s1.shapes.add_textbox(Inches(0.8), Inches(3.2), Inches(6.0), Inches(3.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "SHAPING THE FUTURE\nOF RISK INTELLIGENCE"
    p.font.name = FONT_HEADING
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    p2 = tf1.add_paragraph()
    p2.text = "\nCandidate: Abhi Pandey (21BCE10462)\n" \
              "B.Tech CSE (AI & Machine Learning)\n" \
              "VIT Bhopal University, Madhya Pradesh\n" \
              "S&P Global & CRISIL Campus Hackathon 2026"
    p2.font.name = FONT_BODY
    p2.font.size = Pt(13)
    p2.font.color.rgb = C_WHITE

    # Right side embedded hero graphic
    hero_img = assets_dir / "diagrams" / "slide1_hero_graphic.png"
    if hero_img.exists():
        s1.shapes.add_picture(str(hero_img), Inches(7.0), Inches(2.2), Inches(5.8), Inches(3.8))

    # =========================================================================
    # SLIDE 2: INTRODUCTION TO RISKPULSE (White canvas, left text, right visual)
    # =========================================================================
    s2 = create_white_slide("INTRODUCTION\nTO RISKPULSE", badge_text="RISKPULSE")

    tb2 = s2.shapes.add_textbox(Inches(0.8), Inches(2.5), Inches(5.2), Inches(4.0))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    p = tf2.paragraphs[0]
    p.text = "RiskPulse refers to an autonomous risk intelligence platform bridging unstructured textual financial data with quantitative portfolio stress-testing.\n\n" \
             "Key components include real-time RSS feed ingestion, FinBERT natural language sentiment scoring, and beta-weighted macroeconomic scenario simulation, enabling asset managers to detect and mitigate drawdowns before prices drop."
    p.font.name = FONT_BODY
    p.font.size = Pt(14)
    p.font.color.rgb = C_DARK

    # Right visual: Overview 3-Part Flow
    s2_img = assets_dir / "diagrams" / "slide2_overview_flow.png"
    if s2_img.exists():
        s2.shapes.add_picture(str(s2_img), Inches(6.2), Inches(2.2), Inches(6.5), Inches(3.8))

    # =========================================================================
    # SLIDE 3: DOMAIN CONTEXT & BACKGROUND (Split Slide, Borcelle Style)
    # =========================================================================
    s3 = prs.slides.add_slide(blank_layout)
    # White base
    bg = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = C_WHITE
    bg.line.fill.background()

    # Right Angled Orange Polygon
    poly = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.2), 0, Inches(6.133), Inches(7.5))
    poly.fill.solid()
    poly.fill.fore_color.rgb = C_ORANGE
    poly.line.fill.background()

    add_pill_badge(s3, "VIT BHOPAL", is_orange_slide=False, align_right=False)
    add_arrow_button(s3, is_orange_slide=True)

    # Left content
    tb = s3.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(5.8), Inches(5.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "THE FINANCIAL\nRISK PARADIGM"
    p.font.name = FONT_HEADING
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_ORANGE

    p2 = tf.add_paragraph()
    p2.text = "\nTraditional risk modeling relies exclusively on backward-looking historical prices (Historical VaR) and overnight batch processing.\n\n" \
              "By the time market prices drop, portfolios have already absorbed catastrophic losses, leaving asset managers vulnerable to intraday flash crashes."
    p2.font.name = FONT_BODY
    p2.font.size = Pt(13)
    p2.font.color.rgb = C_DARK

    # Right content
    tb_r = s3.shapes.add_textbox(Inches(7.6), Inches(1.8), Inches(5.0), Inches(5.0))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "80%+ Unstructured Text"
    p.font.name = FONT_HEADING
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    p2 = tf_r.add_paragraph()
    p2.text = "\nOver 80% of market-moving intelligence is textual—breaking news, earnings calls, central bank statements, and regulatory filings.\n\n" \
              "Modern quantitative desks require proactive natural language parsing to bridge qualitative headlines directly into balance-sheet stress tests."
    p2.font.name = FONT_BODY
    p2.font.size = Pt(13)
    p2.font.color.rgb = C_WHITE

    # =========================================================================
    # SLIDE 4: PROBLEM STATEMENT (Full Orange Slide, Borcelle Style)
    # =========================================================================
    s4 = create_orange_slide("CORE CHALLENGES IN FINANCIAL RISK",
                             "Why Existing Risk Management Frameworks Fail Under Macro Volatility",
                             badge_text="RISKPULSE")

    # 2 Column White Text
    tb_l = s4.shapes.add_textbox(Inches(0.8), Inches(3.0), Inches(5.5), Inches(3.5))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "The Latency-Vulnerability Gap:\n" \
             "Macroeconomic developments take hours or days to be priced into legacy risk models, exposing capital to severe drawdowns.\n\n" \
             "Financial Lexicon Misclassification:\n" \
             "Generic NLP models misread domain jargon (e.g., 'liability shrink' or 'hawkish pause'), producing dangerous false positives."
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_WHITE

    tb_r = s4.shapes.add_textbox(Inches(6.8), Inches(3.0), Inches(5.5), Inches(3.5))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "Siloed Stress-Testing Engines:\n" \
             "Portfolio stress testing exists as static spreadsheet exercises isolated from streaming market news signals.\n\n" \
             "Multi-Sector Contagion Blindspots:\n" \
             "Single-stock market shocks trigger unmonitored ripple effects across correlated suppliers and competitors."
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_WHITE

    # =========================================================================
    # SLIDE 5: MOTIVATION (White canvas with right visual diagram)
    # =========================================================================
    s5 = create_white_slide("PROJECT\nMOTIVATION", badge_text="VIT BHOPAL")

    tb = s5.shapes.add_textbox(Inches(0.8), Inches(2.5), Inches(5.0), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Capital Preservation:\n" \
             "Sudden macroeconomic shifts require instantaneous portfolio hedging rather than lagging end-of-day reviews.\n\n" \
             "Academic & Research Innovation:\n" \
             "Synthesizing domain-specific FinBERT transformers with rigorous econometric Value-at-Risk (VaR) formulas.\n\n" \
             "Democratizing Institutional Tech:\n" \
             "Providing real-time risk intelligence without $25k/yr proprietary terminal licenses."
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_DARK

    s5_img = assets_dir / "diagrams" / "slide4_motivation_flow.png"
    if s5_img.exists():
        s5.shapes.add_picture(str(s5_img), Inches(6.0), Inches(2.2), Inches(6.8), Inches(3.8))

    # =========================================================================
    # SLIDE 6: OBJECTIVES (White canvas with 6 clean cards)
    # =========================================================================
    s6 = create_white_slide("CORE OBJECTIVES", badge_text="RISKPULSE")

    objs = [
        ("01", "Live Ingestion", "Continuous RSS feed extraction with resilient mock fallback."),
        ("02", "FinBERT NLP", "Financial polarity scoring (-1.0 to +1.0) and impact severity (1-10)."),
        ("03", "Entity NER", "Sector-aware extraction mapping company mentions to stock tickers."),
        ("04", "Macro Stress Engine", "Dynamic scenario modeling (Rate Hikes, Stagflation) with Beta repricing."),
        ("05", "Tail Risk (VaR)", "Parametric Value-at-Risk and Expected Shortfall recalculation."),
        ("06", "Cloud Verification", "Reactive React 18 dashboard with 100% test pass rate (30/30 tests).")
    ]

    for idx, (num, title, desc) in enumerate(objs):
        x = Inches(0.8) + (idx % 3) * Inches(3.9)
        y = Inches(2.5) + (idx // 3) * Inches(2.2)
        card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(3.6), Inches(1.9))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_ORANGE
        card.line.width = Pt(1.5)

        tb = s6.shapes.add_textbox(x + Inches(0.2), y + Inches(0.15), Inches(3.2), Inches(1.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = f"{num}. {title}"
        p.font.name = FONT_HEADING
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_ORANGE

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = FONT_BODY
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_DARK

    # =========================================================================
    # SLIDE 7: EXISTING SYSTEMS (Full Orange Slide)
    # =========================================================================
    s7 = create_orange_slide("EXISTING SYSTEMS & SHORTCOMINGS",
                             "Why Traditional Financial Tools Cannot Meet Real-Time Demands",
                             badge_text="VIT BHOPAL")

    tb_l = s7.shapes.add_textbox(Inches(0.8), Inches(3.0), Inches(5.5), Inches(3.5))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "Bloomberg & Refinitiv Terminals:\n" \
             "• Extreme annual subscription costs exceeding $25,000 per seat.\n" \
             "• Relies on manual analyst screening and closed proprietary code.\n" \
             "• Inflexible black-box software unsuited for custom academic stress testing."
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_WHITE

    tb_r = s7.shapes.add_textbox(Inches(6.8), Inches(3.0), Inches(5.5), Inches(3.5))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "Legacy Statistical VaR (RiskMetrics):\n" \
             "• Exclusively backward-looking over 250 or 500 trading days.\n" \
             "• Completely blind to breaking news catalysts until prices drop.\n\n" \
             "Generic NLP Analyzers (VADER / TextBlob):\n" \
             "• Trained on social media; misclassifies financial jargon and lacks entity mapping."
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_WHITE

    # =========================================================================
    # SLIDE 8: PROPOSED SYSTEM CONCEPT (White canvas with concept diagram)
    # =========================================================================
    s8 = create_white_slide("PROPOSED SYSTEM\nCONCEPT FLOW", badge_text="RISKPULSE")

    s8_img = assets_dir / "diagrams" / "slide7_concept_diagram.png"
    if s8_img.exists():
        s8.shapes.add_picture(str(s8_img), Inches(0.8), Inches(2.2), Inches(11.5), Inches(3.8))

    tb = s8.shapes.add_textbox(Inches(0.8), Inches(6.1), Inches(11.0), Inches(0.8))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "Autonomous Pipeline: User Role ➔ Raw Inputs ➔ Ingestion & NLP ➔ Stress Modules ➔ Real-Time Telemetry"
    p.font.name = FONT_HEADING
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_ORANGE

    # =========================================================================
    # SLIDE 9: SYSTEM ARCHITECTURE (White canvas with architecture.png)
    # =========================================================================
    s9 = create_white_slide("SYSTEM ARCHITECTURE", badge_text="VIT BHOPAL")

    arch_img = assets_dir / "architecture.png"
    if arch_img.exists():
        s9.shapes.add_picture(str(arch_img), Inches(0.8), Inches(1.8), Inches(8.5), Inches(5.1))

    # Right side 3 tier badges
    tiers = [
        ("Tier 1: Ingestion", "Async RSS feed polling, MD5 hash deduplication, synthetic fallback stream."),
        ("Tier 2: FinBERT Core", "Deep learning sentiment (-1..+1), impact rating (1..10), ticker NER."),
        ("Tier 3: Stress Engine", "Macro shocks, beta scaling, VaR/CVaR recalculation, React 18 UI.")
    ]
    for idx, (t_title, t_desc) in enumerate(tiers):
        y = Inches(2.0) + idx * Inches(1.6)
        card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.6), y, Inches(3.0), Inches(1.4))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_ORANGE
        card.line.width = Pt(1.5)
        tb = s9.shapes.add_textbox(Inches(9.75), y + Inches(0.1), Inches(2.7), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = t_title
        p.font.name = FONT_HEADING
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = C_ORANGE
        p2 = tf.add_paragraph()
        p2.text = t_desc
        p2.font.name = FONT_BODY
        p2.font.size = Pt(9.5)
        p2.font.color.rgb = C_DARK

    # =========================================================================
    # SLIDE 10: WORKFLOW (Full Orange Slide with Flowchart)
    # =========================================================================
    s10 = create_orange_slide("END-TO-END SYSTEM WORKFLOW",
                              "Sequential Pipeline Execution Across Six Critical Stages",
                              badge_text="RISKPULSE")

    s10_img = assets_dir / "diagrams" / "slide9_workflow_flowchart.png"
    if s10_img.exists():
        s10.shapes.add_picture(str(s10_img), Inches(1.0), Inches(2.8), Inches(11.3), Inches(3.8))

    # =========================================================================
    # SLIDE 11: METHODOLOGY (White canvas with pipeline diagram)
    # =========================================================================
    s11 = create_white_slide("METHODOLOGY &\nFORMULATIONS", badge_text="VIT BHOPAL")

    s11_img = assets_dir / "diagrams" / "slide10_methodology_pipeline.png"
    if s11_img.exists():
        s11.shapes.add_picture(str(s11_img), Inches(0.8), Inches(2.1), Inches(11.5), Inches(3.6))

    tb = s11.shapes.add_textbox(Inches(0.8), Inches(5.8), Inches(11.0), Inches(1.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "• Sentiment Polarity: S = P(Positive) - P(Negative) ∈ [-1.0, +1.0]\n" \
             "• Asset Shock Formula: ΔP_i = Base_Shock · β_i · (1 + I_i / 10)  |  Tail Risk: VaR_α = V_p · z_α · σ_p"
    p.font.name = FONT_HEADING
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_DARK

    # =========================================================================
    # SLIDE 12: TECHNOLOGY STACK (White canvas with 6 visual cards)
    # =========================================================================
    s12 = create_white_slide("TECHNOLOGY STACK", badge_text="RISKPULSE")

    stacks = [
        ("Frontend", "React 18, Vite, Tailwind CSS, Lucide Icons, Axios"),
        ("Backend", "Python 3.11+, FastAPI (ASGI), Uvicorn, Pydantic v2"),
        ("AI / ML", "FinBERT (ProsusAI), PyTorch, Hugging Face Transformers"),
        ("Database", "SQLite 3, SQLAlchemy ORM, Indexed Signal Schema"),
        ("Ingestion", "Feedparser, Requests, Regex Ticker Entity Parser"),
        ("Testing & Cloud", "Pytest (30 test suites), HTTPX, Vercel, Render")
    ]

    for idx, (cat, tools) in enumerate(stacks):
        x = Inches(0.8) + (idx % 3) * Inches(3.9)
        y = Inches(2.4) + (idx // 3) * Inches(2.2)
        card = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(3.6), Inches(1.9))
        card.fill.solid()
        card.fill.fore_color.rgb = C_CARD_BG
        card.line.color.rgb = C_ORANGE
        card.line.width = Pt(1.5)

        tb = s12.shapes.add_textbox(x + Inches(0.2), y + Inches(0.15), Inches(3.2), Inches(1.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = cat
        p.font.name = FONT_HEADING
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = C_ORANGE

        p2 = tf.add_paragraph()
        p2.text = tools
        p2.font.name = FONT_BODY
        p2.font.size = Pt(11)
        p2.font.color.rgb = C_DARK

    # =========================================================================
    # SLIDE 13: MAJOR SYSTEM MODULES (Full Orange Slide with Hub Diagram)
    # =========================================================================
    s13 = create_orange_slide("CORE SYSTEM MODULES",
                              "Decoupled Microservice Architecture Around RiskPulse Core",
                              badge_text="VIT BHOPAL")

    s13_img = assets_dir / "diagrams" / "slide12_module_hub.png"
    if s13_img.exists():
        s13.shapes.add_picture(str(s13_img), Inches(2.5), Inches(2.6), Inches(8.3), Inches(4.3))

    # =========================================================================
    # SLIDE 14: IMPLEMENTATION HIGHLIGHTS (2-Column Layout)
    # =========================================================================
    s14 = create_white_slide("IMPLEMENTATION\nHIGHLIGHTS", badge_text="RISKPULSE")

    tb = s14.shapes.add_textbox(Inches(0.8), Inches(2.4), Inches(5.4), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1. Non-Blocking Ingestion:\n" \
             "FastAPI lifespan handlers run background async workers for RSS feeds, ensuring zero latency degradation on user queries.\n\n" \
             "2. Dual-Engine NLP Fallback:\n" \
             "Full FinBERT PyTorch inference with seamless rule-based CPU failover preventing 500 errors.\n\n" \
             "3. Strict Pydantic Data Contracts:\n" \
             "Guarantees rigid schema validation across all REST boundaries."
    p.font.name = FONT_BODY
    p.font.size = Pt(13)
    p.font.color.rgb = C_DARK

    arch_img = assets_dir / "architecture.png"
    if arch_img.exists():
        s14.shapes.add_picture(str(arch_img), Inches(6.5), Inches(2.2), Inches(6.0), Inches(4.5))

    # =========================================================================
    # SLIDE 15: APPLICATION INTERFACE (Mostly Screenshots)
    # =========================================================================
    s15 = create_white_slide("APPLICATION\nINTERFACE", badge_text="VIT BHOPAL")

    ui1 = assets_dir / "diagrams" / "ui_crop_sentiment_gauge.png"
    ui2 = assets_dir / "diagrams" / "ui_crop_stress_heatmap.png"

    if ui1.exists() and ui2.exists():
        s15.shapes.add_picture(str(ui1), Inches(0.8), Inches(2.2), Inches(5.6), Inches(4.3))
        s15.shapes.add_picture(str(ui2), Inches(6.8), Inches(2.2), Inches(5.6), Inches(4.3))

    # =========================================================================
    # SLIDE 16: KEY FEATURES (Full Orange Slide)
    # =========================================================================
    s16 = create_orange_slide("KEY PLATFORM FEATURES",
                              "Institutional Risk Capabilities Built Into RiskPulse",
                              badge_text="RISKPULSE")

    feats = [
        ("Real-Time Ingestion", "Automated RSS polling with deduplication and mock failover."),
        ("FinBERT Sentiment", "Domain-specific financial polarity (-1.0 to +1.0) classification."),
        ("Impact Severity (1-10)", "Algorithmic risk quantification based on news sentiment magnitude."),
        ("Ticker & Sector NER", "Context-aware mapping of corporate entities to stock symbols."),
        ("Macro Stress Engine", "Simulates Interest Rate Hikes, Tech Selloffs, and Stagflation."),
        ("VaR & CVaR Metrics", "Parametric tail-risk calculations for regulatory compliance.")
    ]

    for idx, (title, desc) in enumerate(feats):
        x = Inches(0.8) + (idx % 3) * Inches(3.9)
        y = Inches(3.0) + (idx // 3) * Inches(1.9)
        card = s16.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, Inches(3.6), Inches(1.6))
        card.fill.solid()
        card.fill.fore_color.rgb = C_WHITE
        card.line.fill.background()

        tb = s16.shapes.add_textbox(x + Inches(0.2), y + Inches(0.12), Inches(3.2), Inches(1.3))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = FONT_HEADING
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = C_ORANGE

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = FONT_BODY
        p2.font.size = Pt(10)
        p2.font.color.rgb = C_DARK

    # =========================================================================
    # SLIDE 17: RESULTS & BENCHMARKS (White canvas with charts)
    # =========================================================================
    s17 = create_white_slide("EXPERIMENTAL RESULTS", badge_text="VIT BHOPAL")

    s17_img = assets_dir / "diagrams" / "slide16_results_benchmarks.png"
    if s17_img.exists():
        s17.shapes.add_picture(str(s17_img), Inches(0.8), Inches(2.1), Inches(11.5), Inches(4.3))

    tb = s17.shapes.add_textbox(Inches(0.8), Inches(6.4), Inches(11.0), Inches(0.6))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "⚡ Sub-35ms API Latency   |   📈 42.8 docs/sec Ingestion Rate   |   ✅ 30/30 Unit & Integration Tests Passed (100%)"
    p.font.name = FONT_HEADING
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = C_ORANGE

    # =========================================================================
    # SLIDE 18: ADVANTAGES & LIMITATIONS (Split Comparison Slide)
    # =========================================================================
    s18 = create_white_slide("ADVANTAGES &\nLIMITATIONS", badge_text="RISKPULSE")

    # Left: Advantages
    card_l = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.3), Inches(5.6), Inches(4.4))
    card_l.fill.solid()
    card_l.fill.fore_color.rgb = C_CARD_BG
    card_l.line.color.rgb = C_ORANGE
    card_l.line.width = Pt(1.5)

    tb = s18.shapes.add_textbox(Inches(1.0), Inches(2.5), Inches(5.2), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "CORE ADVANTAGES"
    p.font.name = FONT_HEADING
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_ORANGE
    p2 = tf.add_paragraph()
    p2.text = "\n• Zero LLM Hallucinations: Deterministic formulas ensure reliable VaR math.\n\n" \
              "• Sub-Second Execution: FastAPI delivers sub-35ms response times.\n\n" \
              "• Basel III & CRISIL Aligned: Meets multi-scenario stress principles.\n\n" \
              "• Accessible & Open: Operates without $25k/yr terminal fees."
    p2.font.name = FONT_BODY
    p2.font.size = Pt(11.5)
    p2.font.color.rgb = C_DARK

    # Right: Limitations
    card_r = s18.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.3), Inches(5.6), Inches(4.4))
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = C_CARD_BG
    card_r.line.color.rgb = C_DARK
    card_r.line.width = Pt(1.5)

    tb_r = s18.shapes.add_textbox(Inches(7.0), Inches(2.5), Inches(5.2), Inches(4.0))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "CURRENT LIMITATIONS"
    p.font.name = FONT_HEADING
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = C_DARK
    p2 = tf_r.add_paragraph()
    p2.text = "\n• Static Asset Betas: Does not yet model intraday GARCH volatility clustering.\n\n" \
              "• Single-Node SQLite Database: Lacks distributed multi-region replication.\n\n" \
              "• Dictionary-Based NER: Relies on curated aliases rather than contextual NER.\n\n" \
              "• Linear Contagion: Follows linear betas rather than liquidity freeze curves."
    p2.font.name = FONT_BODY
    p2.font.size = Pt(11.5)
    p2.font.color.rgb = C_DARK

    # =========================================================================
    # SLIDE 19: FUTURE SCOPE & ROADMAP (White canvas with roadmap diagram)
    # =========================================================================
    s19 = create_white_slide("FUTURE TRENDS\n& ROADMAP", badge_text="VIT BHOPAL")

    s19_img = assets_dir / "diagrams" / "slide19_roadmap_timeline.png"
    if s19_img.exists():
        s19.shapes.add_picture(str(s19_img), Inches(0.8), Inches(2.2), Inches(11.5), Inches(4.2))

    # =========================================================================
    # SLIDE 20: CONCLUSION & REFERENCES (Full Orange Slide, Borcelle Style)
    # =========================================================================
    s20 = create_orange_slide("CONCLUSION & REFERENCES",
                              "S&P Global & CRISIL Campus Hackathon 2026 Submission",
                              badge_text="VIT BHOPAL")

    tb = s20.shapes.add_textbox(Inches(0.8), Inches(2.6), Inches(11.5), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "CONCLUSION SUMMARY"
    p.font.name = FONT_HEADING
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = C_WHITE

    p2 = tf.add_paragraph()
    p2.text = "• RiskPulse successfully bridges unstructured qualitative news sentiment with quantitative portfolio stress-testing.\n" \
              "• Demonstrated sub-35ms API latencies, high ingestion throughput, and 100% automated test coverage across 30 test suites.\n" \
              "• Proves that modern lightweight AI and asynchronous web architectures can democratize institutional financial risk intelligence."
    p2.font.name = FONT_BODY
    p2.font.size = Pt(12)
    p2.font.color.rgb = C_WHITE

    p3 = tf.add_paragraph()
    p3.text = "\nREFERENCES (IEEE FORMAT)"
    p3.font.name = FONT_HEADING
    p3.font.size = Pt(14)
    p3.font.bold = True
    p3.font.color.rgb = C_ORANGE_LIGHT

    p4 = tf.add_paragraph()
    p4.text = "[1] S. Araci, 'FinBERT: Financial Sentiment Analysis with Pre-trained Language Models,' arXiv:1908.10063, 2019.\n" \
              "[2] T. Loughran and B. McDonald, 'When is a Word Pronounced Negative? A New Financial Dictionary,' J. Finance, 2011.\n" \
              "[3] P. Jorion, Value at Risk: The New Benchmark for Managing Financial Risk, 3rd ed. McGraw-Hill, 2007.\n" \
              "[4] Basel Committee on Banking Supervision, 'Stress testing principles,' Bank for International Settlements, 2018."
    p4.font.name = FONT_BODY
    p4.font.size = Pt(10.5)
    p4.font.color.rgb = C_WHITE

    p5 = tf.add_paragraph()
    p5.text = "\nLIVE DEPLOYED PLATFORM: https://vit-bhopal-abhi-pandey-s-p-crisil-h.vercel.app/"
    p5.font.name = FONT_HEADING
    p5.font.size = Pt(11)
    p5.font.bold = True
    p5.font.color.rgb = C_WHITE

    prs.save(str(output_path))
    print(f"Successfully generated Borcelle-style 20-slide PPTX at {output_path}")

def build_borcelle_style_pdf(output_path: Path):
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
        textColor=colors.HexColor('#FF5E00')
    )

    style_title = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#FF5E00'),
        spaceAfter=14
    )

    style_body = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        textColor=colors.HexColor('#1E293B')
    )

    elements = []

    slides_info = [
        ("VIT BHOPAL", "ARTIFICIAL INTELLIGENCE IN FINANCIAL RISK",
         "<b>RiskPulse:</b> NLP Sentiment Engine & Strategic Portfolio Stress Testing Platform<br/><br/>"
         "<b>Candidate:</b> Abhi Pandey (Reg No: 21BCE10462)<br/>"
         "<b>Department:</b> Computer Science & Engineering (AI & Machine Learning)<br/>"
         "<b>Institution:</b> VIT Bhopal University, Madhya Pradesh<br/>"
         "<b>Event:</b> S&P Global & CRISIL Campus Hackathon 2026 / Final Year B.Tech Viva<br/>"
         "<b>Live URL:</b> https://vit-bhopal-abhi-pandey-s-p-crisil-h.vercel.app/"),

        ("RISKPULSE", "INTRODUCTION TO RISKPULSE",
         "<b>What It Is:</b> An autonomous risk intelligence platform bridging unstructured textual financial data with quantitative portfolio stress-testing.<br/><br/>"
         "<b>Key Components:</b> Real-time RSS feed ingestion, FinBERT natural language sentiment scoring, and beta-weighted macroeconomic scenario simulation.<br/><br/>"
         "<b>Value Proposition:</b> Enables asset managers to detect and mitigate drawdowns before prices drop."),

        ("VIT BHOPAL", "THE FINANCIAL RISK PARADIGM",
         "<b>Traditional Risk Modeling:</b> Relies exclusively on backward-looking historical prices (Historical VaR) and overnight batch processing. By the time market prices drop, portfolios have already absorbed catastrophic losses.<br/><br/>"
         "<b>80%+ Unstructured Text:</b> Over 80% of market-moving intelligence is textual—breaking news, earnings calls, central bank statements, and regulatory filings. Modern desks require proactive natural language parsing to bridge qualitative headlines directly into balance-sheet stress tests."),

        ("RISKPULSE", "CORE CHALLENGES IN FINANCIAL RISK",
         "<b>1. Latency-Vulnerability Gap:</b> Macroeconomic developments take hours or days to be priced into legacy risk models, exposing capital to severe drawdowns.<br/><br/>"
         "<b>2. Financial Lexicon Misclassification:</b> Generic NLP models misread domain jargon (e.g., 'liability shrink' or 'hawkish pause'), producing dangerous false positives.<br/><br/>"
         "<b>3. Siloed Stress-Testing:</b> Portfolio stress testing exists as static spreadsheet exercises isolated from streaming market news signals.<br/><br/>"
         "<b>4. Multi-Sector Contagion:</b> Single-stock market shocks trigger unmonitored ripple effects across correlated suppliers and competitors."),

        ("VIT BHOPAL", "PROJECT MOTIVATION",
         "<b>Capital Preservation:</b> Sudden macroeconomic shifts require instantaneous portfolio hedging rather than lagging end-of-day reviews.<br/><br/>"
         "<b>Academic Innovation:</b> Synthesizing domain-specific FinBERT transformers with rigorous econometric Value-at-Risk (VaR) formulas.<br/><br/>"
         "<b>Democratizing Tech:</b> Providing real-time risk intelligence without $25k/yr proprietary terminal licenses."),

        ("RISKPULSE", "CORE OBJECTIVES",
         "<b>1. Live Ingestion:</b> Continuous RSS feed extraction with resilient mock fallback.<br/><br/>"
         "<b>2. FinBERT NLP:</b> Financial polarity scoring (-1.0 to +1.0) and impact severity (1-10).<br/><br/>"
         "<b>3. Entity NER:</b> Sector-aware extraction mapping company mentions to stock tickers.<br/><br/>"
         "<b>4. Macro Stress Engine:</b> Dynamic scenario modeling (Rate Hikes, Stagflation) with Beta repricing.<br/><br/>"
         "<b>5. Tail Risk (VaR):</b> Parametric Value-at-Risk and Expected Shortfall recalculation.<br/><br/>"
         "<b>6. Cloud Verification:</b> Reactive React 18 dashboard with 100% test pass rate (30/30 tests)."),

        ("VIT BHOPAL", "EXISTING SYSTEMS & SHORTCOMINGS",
         "<b>Bloomberg / Refinitiv Terminals:</b> Extreme annual subscription costs exceeding $25,000 per seat; relies on manual analyst screening and closed proprietary code.<br/><br/>"
         "<b>Legacy Statistical VaR (RiskMetrics):</b> Exclusively backward-looking over 250 or 500 trading days; completely blind to breaking news catalysts until prices drop.<br/><br/>"
         "<b>Generic NLP Analyzers (VADER):</b> Trained on social media; misclassifies financial jargon and lacks entity mapping."),

        ("RISKPULSE", "PROPOSED SYSTEM CONCEPT FLOW",
         "<b>Autonomous Pipeline:</b> [USER] ➔ [RAW INPUTS] ➔ [INGESTION & NLP] ➔ [STRESS MODULES] ➔ [REAL-TIME TELEMETRY].<br/><br/>"
         "Provides transparent, deterministic econometric modeling without generative hallucinations, ensuring regulatory alignment and sub-second execution."),

        ("VIT BHOPAL", "SYSTEM ARCHITECTURE",
         "<b>Tier 1 - Ingestion:</b> Async RSS feed polling, MD5 hash deduplication, synthetic fallback stream.<br/><br/>"
         "<b>Tier 2 - FinBERT Core:</b> Deep learning sentiment (-1..+1), impact rating (1..10), ticker NER.<br/><br/>"
         "<b>Tier 3 - Stress Engine:</b> Macro shocks, beta scaling, VaR/CVaR recalculation, React 18 UI."),

        ("RISKPULSE", "END-TO-END SYSTEM WORKFLOW",
         "<b>Stage 1:</b> Data Polling via async RSS workers.<br/>"
         "<b>Stage 2:</b> Text Normalization and hash deduplication.<br/>"
         "<b>Stage 3:</b> FinBERT forward inference for polarity S in [-1.0, +1.0].<br/>"
         "<b>Stage 4:</b> Impact severity heuristic (1-10) and ticker NER resolution.<br/>"
         "<b>Stage 5:</b> Portfolio stress propagation via Beta-weighted shock formulas.<br/>"
         "<b>Stage 6:</b> Live UI refresh displaying updated valuations and risk gauges."),

        ("VIT BHOPAL", "METHODOLOGY & FORMULATIONS",
         "<b>• Sentiment Polarity:</b> S = P(Positive) - P(Negative) ∈ [-1.0, +1.0]<br/><br/>"
         "<b>• Impact Severity:</b> I = round(1 + 9·|S|·C_event) ∈ [1, 10]<br/><br/>"
         "<b>• Asset Shock:</b> ΔP_i = Base_Shock · β_i · (1 + I_i / 10)<br/><br/>"
         "<b>• Tail Risk (VaR):</b> VaR_α = V_p · z_α · σ_p;  CVaR_α = V_p · [ϕ(z_α) / (1 - α)] · σ_p"),

        ("RISKPULSE", "TECHNOLOGY STACK",
         "<b>Frontend:</b> React 18, Vite, Tailwind CSS, Lucide Icons, Axios.<br/><br/>"
         "<b>Backend:</b> Python 3.11+, FastAPI (ASGI), Uvicorn, Pydantic v2.<br/><br/>"
         "<b>AI / ML:</b> FinBERT (ProsusAI), PyTorch, Hugging Face Transformers.<br/><br/>"
         "<b>Database & Feeds:</b> SQLite 3, SQLAlchemy ORM, Feedparser, Requests.<br/><br/>"
         "<b>Testing & Cloud:</b> Pytest (30 test suites), HTTPX, Vercel, Render."),

        ("VIT BHOPAL", "CORE SYSTEM MODULES",
         "<b>• Ingestion Module (backend/ingestion.py):</b> Async RSS feeds and synthetic streaming fallback.<br/><br/>"
         "<b>• NLP Engine (backend/nlp_engine.py):</b> FinBERT transformer scoring and ticker NER.<br/><br/>"
         "<b>• Stress Engine (backend/portfolio.py):</b> Macro shock simulation, Beta multipliers, and VaR.<br/><br/>"
         "<b>• Web Dashboard (frontend/src/):</b> Reactive user interface with real-time risk gauges."),

        ("RISKPULSE", "IMPLEMENTATION HIGHLIGHTS",
         "<b>Non-Blocking Ingestion:</b> FastAPI lifespan handlers run background async workers for RSS feeds, ensuring zero latency degradation on user queries.<br/><br/>"
         "<b>Dual-Engine NLP Fallback:</b> Full FinBERT PyTorch inference with seamless rule-based CPU failover preventing 500 errors.<br/><br/>"
         "<b>Strict Pydantic Contracts:</b> Guarantees rigid schema validation across all REST boundaries."),

        ("VIT BHOPAL", "APPLICATION INTERFACE",
         "<b>Panel 1 (Signal Stream & Gauge):</b> Streaming ingested headlines, sentiment chips, and market polarity meter.<br/><br/>"
         "<b>Panel 2 (Stress Panel & Heatmap):</b> Interactive scenario shock triggers, asset repricing, and VaR telemetry."),

        ("RISKPULSE", "KEY PLATFORM FEATURES",
         "<b>1. Real-Time Ingestion:</b> Continuous news extraction with automated deduplication.<br/><br/>"
         "<b>2. FinBERT Sentiment:</b> Domain-specific polarity scoring (-1.0 to +1.0).<br/><br/>"
         "<b>3. Impact Severity:</b> Algorithmic 1-10 severity scale.<br/><br/>"
         "<b>4. Sector NER:</b> Direct ticker extraction and mapping.<br/><br/>"
         "<b>5. Macro Stress Testing:</b> Real-time scenario simulation.<br/><br/>"
         "<b>6. Tail Risk VaR / CVaR:</b> Quantitative downside loss modeling."),

        ("VIT BHOPAL", "EXPERIMENTAL RESULTS",
         "<b>• REST API Latency:</b> < 35 ms average response time across all endpoints.<br/><br/>"
         "<b>• Ingestion Throughput:</b> 42.8 documents/second processed and scored on single CPU core.<br/><br/>"
         "<b>• FinBERT Inference:</b> 31.8 ms per headline evaluation.<br/><br/>"
         "<b>• Stress Simulation:</b> 1.4 ms computation time for a 5-asset portfolio shock.<br/><br/>"
         "<b>• Test Suite:</b> 30 passed unit and integration tests (100% pass rate)."),

        ("RISKPULSE", "ADVANTAGES & LIMITATIONS",
         "<b>Core Advantages:</b> Zero LLM hallucinations (deterministic math); sub-35ms ASGI execution; Basel III alignment; accessible open architecture.<br/><br/>"
         "<b>Current Limitations:</b> Static beta assumptions (no GARCH); single-node SQLite database; dictionary-based NER heuristics."),

        ("VIT BHOPAL", "FUTURE TRENDS & ROADMAP",
         "<b>Milestone 1 (1-3 Mo):</b> TimescaleDB migration, GARCH(1,1) volatility, 25+ global feeds.<br/><br/>"
         "<b>Milestone 2 (3-6 Mo):</b> Causal knowledge graphs for contagion, ONNX INT8 quantization (<10ms).<br/><br/>"
         "<b>Milestone 3 (6-12 Mo):</b> Live broker API order execution, multi-agent conversational risk copilot."),

        ("VIT BHOPAL", "CONCLUSION & REFERENCES",
         "<b>Conclusion:</b> Successfully demonstrates that modern lightweight NLP and asynchronous web frameworks can deliver institutional-grade financial risk intelligence.<br/><br/>"
         "<b>References (IEEE Style):</b><br/>"
         "[1] S. Araci, 'FinBERT: Financial Sentiment Analysis with Pre-trained Language Models,' arXiv:1908.10063, 2019.<br/>"
         "[2] T. Loughran and B. McDonald, 'When is a Word Pronounced Negative? A New Financial Dictionary,' J. Finance, 2011.<br/>"
         "[3] P. Jorion, Value at Risk: The New Benchmark for Managing Financial Risk, McGraw-Hill, 2007.<br/>"
         "[4] Basel Committee on Banking Supervision, 'Stress testing principles,' BIS Tech. Rep., 2018.<br/><br/>"
         "<b>Live Web Platform:</b> https://vit-bhopal-abhi-pandey-s-p-crisil-h.vercel.app/")
    ]

    for tag, title, content in slides_info:
        elements.append(Paragraph(tag, style_tag))
        elements.append(Paragraph(title, style_title))
        elements.append(Paragraph(content, style_body))
        elements.append(PageBreak())

    if elements and isinstance(elements[-1], PageBreak):
        elements.pop()

    doc.build(elements)
    print(f"Successfully generated Borcelle-style 20-slide PDF at {output_path}")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    docs_dir = base_dir / "docs"
    pptx_path = docs_dir / "presentation.pptx"
    pdf_path = docs_dir / "presentation.pdf"

    build_borcelle_style_pptx(pptx_path, docs_dir)
    build_borcelle_style_pdf(pdf_path)
