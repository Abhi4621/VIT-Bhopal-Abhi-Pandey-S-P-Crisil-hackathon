"""
Generate high-resolution architecture diagram for RiskPulse platform.
S&P Global & CRISIL Campus Hackathon 2026.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

def create_architecture_diagram(output_path: str):
    fig, ax = plt.subplots(figsize=(20, 13), dpi=300)
    fig.patch.set_facecolor('#0B0F19')  # Deep modern dark slate background
    ax.set_facecolor('#0B0F19')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Color palette
    c_card_bg = '#111827'
    c_card_border = '#374151'
    c_accent_blue = '#38BDF8'
    c_accent_indigo = '#818CF8'
    c_accent_green = '#34D399'
    c_accent_amber = '#FBBF24'
    c_accent_rose = '#F87171'
    c_accent_purple = '#C084FC'
    c_text_bright = '#F9FAFB'
    c_text_muted = '#9CA3AF'
    c_text_subtle = '#6B7280'
    c_inner_box = '#1F2937'

    def draw_card(x, y, w, h, title, subtitle="", border_color=c_card_border, bg_color=c_card_bg, rad=1.5):
        rect = patches.FancyBboxPatch((x, y), w, h,
                                      boxstyle=f"round,pad=0.0,rounding_size={rad}",
                                      facecolor=bg_color, edgecolor=border_color, linewidth=1.5)
        ax.add_patch(rect)
        if title:
            ax.text(x + w/2, y + h - 2.8, title, ha='center', va='center',
                    fontsize=12, fontweight='bold', color=c_text_bright, fontfamily='sans-serif')
        if subtitle:
            ax.text(x + w/2, y + h - 5.2, subtitle, ha='center', va='center',
                    fontsize=8.5, color=c_text_muted, fontfamily='sans-serif')

    def draw_inner_box(x, y, w, h, text, subtext="", badge="", badge_color=c_accent_blue, bg_color=c_inner_box):
        rect = patches.FancyBboxPatch((x, y), w, h,
                                      boxstyle="round,pad=0.0,rounding_size=1.0",
                                      facecolor=bg_color, edgecolor=c_card_border, linewidth=1.0)
        ax.add_patch(rect)
        if badge:
            badge_rect = patches.FancyBboxPatch((x + 1.2, y + h - 2.5), len(badge)*1.0 + 1.5, 1.8,
                                                boxstyle="round,pad=0.0,rounding_size=0.4",
                                                facecolor=badge_color, edgecolor='none')
            ax.add_patch(badge_rect)
            ax.text(x + 1.2 + (len(badge)*1.0 + 1.5)/2, y + h - 1.6, badge,
                    ha='center', va='center', fontsize=6.5, fontweight='bold', color='#000000')
        ax.text(x + w/2, y + h/2 + (0.8 if subtext else 0), text, ha='center', va='center',
                fontsize=9.5, fontweight='bold', color=c_text_bright, fontfamily='sans-serif')
        if subtext:
            ax.text(x + w/2, y + h/2 - 1.6, subtext, ha='center', va='center',
                    fontsize=7.5, color=c_text_muted, fontfamily='sans-serif')

    def draw_arrow(x1, y1, x2, y2, color=c_accent_blue, style='->', lw=1.8, label="", lpos=(0, 0)):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle=style, color=color, lw=lw,
                                    shrinkA=4, shrinkB=4, mutation_scale=15))
        if label:
            lx = (x1 + x2)/2 + lpos[0]
            ly = (y1 + y2)/2 + lpos[1]
            ax.text(lx, ly, label, ha='center', va='center', fontsize=7.5,
                    color=color, fontweight='bold',
                    bbox=dict(boxstyle='round,pad=0.2', facecolor='#0B0F19', edgecolor=color, lw=0.8))

    # HEADER
    ax.text(50, 96.5, "RiskPulse: AI/NLP Financial Risk Intelligence & Strategic Stress Testing",
            ha='center', va='center', fontsize=20, fontweight='bold', color=c_text_bright, fontfamily='sans-serif')
    ax.text(50, 93.8, "End-to-End System Architecture | S&P Global & CRISIL Campus Hackathon 2026 | Candidate: Abhi Pandey (VIT Bhopal)",
            ha='center', va='center', fontsize=11, color=c_accent_blue, fontfamily='sans-serif')

    # ROW 1: DATA INGESTION SOURCES (Y: 77 to 90)
    # Box 1: Ingestion Layer Container
    draw_card(4, 76, 92, 15.5, "1. MULTI-SOURCE INGESTION & NORMALIZATION LAYER",
              "Ingests structured and unstructured text feeds across financial markets",
              border_color=c_accent_blue, bg_color='#0E1726')

    # Source 1: Financial News
    draw_inner_box(6, 78, 20, 9.5, "Financial News Wire", "Dow Jones, Reuters, Bloomberg",
                   badge="SOURCE 1", badge_color=c_accent_blue)

    # Source 2: Social/Market Feed
    draw_inner_box(28, 78, 20, 9.5, "Social / Market Feed", "StockTwits, Twitter/X Market Sentiment",
                   badge="SOURCE 2", badge_color=c_accent_purple)

    # Source 3: Live RSS Feeds (Optional)
    draw_inner_box(50, 78, 20, 9.5, "Public Live RSS Feed", "Yahoo Finance / Open Financial News",
                   badge="SOURCE 3", badge_color=c_accent_green)

    # Preprocessing Engine
    draw_inner_box(72, 78, 22, 9.5, "Text Cleaning & Normalization", "Regex, Noise Removal, Entity Resolution",
                   badge="PIPELINE", badge_color=c_accent_amber)

    # Connect Sources to Preprocessing
    draw_arrow(26, 82.5, 28, 82.5, color=c_accent_blue)
    draw_arrow(48, 82.5, 50, 82.5, color=c_accent_purple)
    draw_arrow(70, 82.5, 72, 82.5, color=c_accent_green)

    # Flow from Layer 1 to Layer 2
    draw_arrow(83, 76, 83, 71.5, color=c_accent_amber, label="Cleaned Unstructured Text", lpos=(0, 0))

    # ROW 2: NLP RISK ENGINE (Y: 50 to 71.5)
    draw_card(4, 49.5, 92, 22, "2. INTERPRETABLE NLP FINANCIAL RISK ENGINE",
              "Deterministic, rule-calibrated lexicon engine with zero black-box hallucination",
              border_color=c_accent_indigo, bg_color='#0F172A')

    # Sub-component A: Entity Resolution
    draw_inner_box(6.5, 52, 19, 14, "Entity & Ticker Extraction",
                   "Resolves Company Names\n& Symbols (e.g., NVDA, AAPL)",
                   badge="STAGE A", badge_color=c_accent_blue)

    # Sub-component B: Sentiment Analyzer
    draw_inner_box(27.5, 52, 20, 14, "Sentiment Scoring Engine",
                   "Domain-Specific Financial Lexicon\nNormalized Score: [-1.0 to +1.0]\nLabels: Negative, Neutral, Positive",
                   badge="STAGE B", badge_color=c_accent_indigo)

    # Sub-component C: Event Classifier
    draw_inner_box(49.5, 52, 21.5, 14, "Financial Event Classifier",
                   "8 Taxonomy Classes:\nRegulatory, Geopolitical, Earnings,\nSupply Chain, Cyber, Operational...",
                   badge="STAGE C", badge_color=c_accent_purple)

    # Sub-component D: Impact Score
    draw_inner_box(73, 52, 21, 14, "Impact & Risk Formulator",
                   "Weighted Score: 1 to 10 Scale\nRisk Levels: Low, Med, High, Severe\nExplainable Risk Justification",
                   badge="STAGE D", badge_color=c_accent_rose)

    # Internal pipeline arrows
    draw_arrow(25.5, 59, 27.5, 59, color=c_accent_blue)
    draw_arrow(47.5, 59, 49.5, 59, color=c_accent_indigo)
    draw_arrow(71, 59, 73, 59, color=c_accent_purple)

    # External output arrow
    draw_arrow(83.5, 49.5, 83.5, 44.5, color=c_accent_rose, label="Structured Risk Signals", lpos=(0, 0))

    # ROW 3: PERSISTENCE & API LAYER (Y: 28 to 44.5)
    draw_card(4, 27.5, 42, 17, "3. STORAGE & REST API BACKEND (FastAPI)",
              "Deterministic persistence and high-throughput async REST endpoints",
              border_color=c_accent_green, bg_color='#062017')

    draw_inner_box(6.5, 29.5, 17.5, 11, "SQLite Database",
                   "schema: signals, portfolios\nDynamic: /tmp for serverless\nZero-maintenance local ACID",
                   badge="STORAGE", badge_color=c_accent_green)

    draw_inner_box(26, 29.5, 18, 11, "FastAPI Service Endpoints",
                   "GET /health  •  POST /analyze\nGET /signals •  POST /ingest\nGET /portfolio • POST /stress-test",
                   badge="API ROUTER", badge_color=c_accent_blue)

    draw_arrow(24, 35, 26, 35, color=c_accent_green)

    # ROW 3 RIGHT: MODULE B - STRATEGIC PORTFOLIO STRESS TESTING (Y: 27.5 to 44.5)
    draw_card(50, 27.5, 46, 17, "MODULE B: STRATEGIC PORTFOLIO STRESS TESTING",
              "Macroprudential scenario shocks triggered when Impact Score >= 7",
              border_color=c_accent_amber, bg_color='#1C1608')

    draw_inner_box(52, 29.5, 12.5, 11, "Trigger Gate",
                   "Condition Check:\nImpact Score >= 7\nAutomatic Activation",
                   badge="GATE", badge_color=c_accent_rose)

    draw_inner_box(66.5, 29.5, 14, 11, "Shock Engine",
                   "Asset-Class Haircuts:\nEquities (-8% to -25%)\nTech / Crypto Haircuts",
                   badge="SHOCK MATRIX", badge_color=c_accent_amber)

    draw_inner_box(82.5, 29.5, 12, 11, "Valuation (MtM)",
                   "Pre-Stress Value\nPost-Stress Value\nAbsolute Loss & %",
                   badge="METRICS", badge_color=c_accent_green)

    draw_arrow(46, 36, 50, 36, color=c_accent_amber, label="Impact >= 7 Trigger", lpos=(0, 0))
    draw_arrow(64.5, 35, 66.5, 35, color=c_accent_amber)
    draw_arrow(80.5, 35, 82.5, 35, color=c_accent_amber)

    # ROW 4: REACT DASHBOARD FRONTEND (Y: 4 to 22.5)
    draw_card(4, 4, 92, 19, "4. INSTITUTIONAL REACT 18 RISK INTELLIGENCE DASHBOARD (Vite + Tailwind CSS)",
              "Live risk signal feeds, interactive NLP stress lab, and executive portfolio drawdown analytics",
              border_color=c_accent_purple, bg_color='#130D24')

    draw_inner_box(6.5, 6, 20, 12.5, "Live Signal Feed & Filter",
                   "• Dual Source Badges (News / Social)\n• Event Classification Badges\n• Sentiment Meters (-1 to +1)\n• Impact Score (1-10) & Risk Level",
                   badge="MODULE A UI", badge_color=c_accent_blue)

    draw_inner_box(28.5, 6, 20, 12.5, "Interactive NLP Analyzer",
                   "• Ad-hoc Unstructured Text Input\n• Real-Time Entity Extraction\n• Deterministic Sentiment Gauge\n• Instant Impact Formulator",
                   badge="SANDBOX UI", badge_color=c_accent_indigo)

    draw_inner_box(50.5, 6, 21, 12.5, "Module B Stress Visualizer",
                   "• Portfolio Pre-Stress ($1,000,000)\n• Post-Stress MtM Valuation\n• Total Value at Risk & Drawdown %\n• Shock Breakdown by Asset Class",
                   badge="MODULE B UI", badge_color=c_accent_rose)

    draw_inner_box(73.5, 6, 20.5, 12.5, "System & Feeds Telemetry",
                   "• Live RSS Feed Ingestion Button\n• API Health Status & Latency (<50ms)\n• Deterministic Explainability Notes\n• Standalone Offline Mode Support",
                   badge="OPS & TELEMETRY", badge_color=c_accent_green)

    # Connections between Backend & Frontend
    draw_arrow(25, 27.5, 25, 23, color=c_accent_green, label="REST API Responses (JSON)", lpos=(0, 0))
    draw_arrow(75, 27.5, 75, 23, color=c_accent_amber, label="Portfolio Stress State", lpos=(0, 0))

    # FOOTER BAR
    ax.text(50, 1.8, "Built for S&P Global & CRISIL Campus Hackathon 2026 | Verified 30/30 Test Suite Passed | Deterministic & Fully Explainable",
            ha='center', va='center', fontsize=9, color=c_text_muted, fontfamily='sans-serif')

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Successfully generated architecture diagram at {output_path}")

if __name__ == "__main__":
    create_architecture_diagram("docs/architecture.png")
