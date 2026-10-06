"""
Generate high-resolution visual diagram assets for the RiskPulse 20-slide presentation.
Generates:
1. docs/diagrams/slide1_hero_graphic.png (Financial risk intelligence overview visual)
2. docs/diagrams/slide2_overview_flow.png (3-Part: PROBLEM -> SOLUTION -> RESULT)
3. docs/diagrams/slide4_motivation_flow.png (Current Situation -> Problems -> Need -> RiskPulse)
4. docs/diagrams/slide7_concept_diagram.png (User -> Input -> Processing -> Modules -> Output)
5. docs/diagrams/slide9_workflow_flowchart.png (6-Step sequential workflow flowchart)
6. docs/diagrams/slide10_methodology_pipeline.png (6-Stage quantitative methodology pipeline)
7. docs/diagrams/slide12_module_hub.png (Hub-and-spoke central architecture module diagram)
8. docs/diagrams/slide16_results_benchmarks.png (Dual-panel quantitative benchmark chart)
9. docs/diagrams/slide19_roadmap_timeline.png (4-Horizon visual engineering roadmap)
10. docs/diagrams/ui_crop_signals.png & ui_crop_stress.png (Cropped UI screenshot widgets)
"""

import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image

output_dir = Path("docs/diagrams")
output_dir.mkdir(parents=True, exist_ok=True)

# Colors
C_ORANGE = "#EA580C"
C_NAVY = "#0F172A"
C_SLATE = "#1E293B"
C_BLUE = "#0284C7"
C_GREEN = "#10B981"
C_RED = "#DC2626"
C_BG_CARD = "#FFFFFF"
C_BG_TINT = "#F8FAFC"
C_BORDER = "#E2E8F0"

plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = C_BORDER

# -----------------------------------------------------------------------------
# 1. SLIDE 1 HERO GRAPHIC: Real-Time Risk Analytics Dashboard Visual
# -----------------------------------------------------------------------------
def make_slide1_hero():
    fig, ax = plt.subplots(figsize=(6.5, 4.2), dpi=200)
    fig.patch.set_facecolor(C_BG_TINT)
    ax.set_facecolor(C_BG_TINT)

    # Time series simulation of asset portfolio vs stressed benchmark
    np.random.seed(42)
    t = np.linspace(0, 10, 100)
    normal_p = 100 + np.cumsum(np.random.randn(100) * 0.8)
    stressed_p = 100 + np.cumsum(np.random.randn(100) * 0.8)
    stressed_p[60:] -= np.linspace(0, 14.5, 40) # shock injection at t=6

    ax.plot(t[:60], normal_p[:60], color=C_BLUE, lw=2.5, label="Baseline Portfolio Value")
    ax.plot(t[59:], normal_p[59:], color=C_BLUE, lw=2.5, linestyle="--")
    ax.plot(t[59:], stressed_p[59:], color=C_RED, lw=3.0, label="Macro Stressed Trajectory (-14.5%)")

    # Shock event indicator
    ax.axvline(x=6.0, color=C_ORANGE, linestyle=":", lw=2.0)
    ax.text(6.1, 98, "FinBERT Catalyst:\nRate Spike Signal (-0.84)", fontsize=8, color=C_ORANGE, fontweight="bold")

    # Fill risk drawdown area
    ax.fill_between(t[59:], stressed_p[59:], normal_p[59:], color=C_RED, alpha=0.15)

    ax.set_title("Autonomous Sentiment Catalyst & Portfolio Drawdown Simulation", fontsize=10, fontweight="bold", color=C_NAVY, pad=10)
    ax.set_xlabel("Time (Trading Hours)", fontsize=8, color=C_SLATE)
    ax.set_ylabel("Portfolio Valuation ($k)", fontsize=8, color=C_SLATE)
    ax.legend(loc="lower left", fontsize=7.5, framealpha=0.9)
    ax.grid(True, linestyle="--", alpha=0.5, color=C_BORDER)

    plt.tight_layout()
    out_file = output_dir / "slide1_hero_graphic.png"
    plt.savefig(out_file, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_file}")

# -----------------------------------------------------------------------------
# 2. SLIDE 2 OVERVIEW: 3-Part Flow (PROBLEM -> SOLUTION -> RESULT)
# -----------------------------------------------------------------------------
def make_slide2_overview():
    fig, ax = plt.subplots(figsize=(10, 3.2), dpi=200)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.2)
    ax.axis('off')

    cards = [
        (0.4, 2.7, "1. THE PROBLEM", [
            "• 80%+ market data is unstructured text",
            "• Traditional VaR reacts post-facto",
            "• Critical multi-hour reporting latency"
        ], C_RED),
        (3.7, 2.7, "2. OUR SOLUTION", [
            "• Autonomous live RSS feed ingestion",
            "• FinBERT sentiment (-1.0 to +1.0)",
            "• Beta-weighted macro stress engine"
        ], C_ORANGE),
        (7.0, 2.7, "3. THE RESULT", [
            "• Sub-35ms risk recalculation",
            "• Instant portfolio VaR / CVaR updates",
            "• Interactive real-time cloud dashboard"
        ], C_GREEN)
    ]

    for x, w, title, points, color in cards:
        # Card background
        rect = patches.FancyBboxPatch((x, 0.3), w, 2.5, boxstyle="round,pad=0.1", fc="#F8FAFC", ec=C_BORDER, lw=1.5)
        ax.add_patch(rect)
        # Header strip
        strip = patches.Rectangle((x, 2.45), w, 0.35, fc=color, ec="none")
        ax.add_patch(strip)
        ax.text(x + w/2, 2.62, title, color="#FFFFFF", fontsize=10, fontweight="bold", ha="center", va="center")

        # Points
        y_text = 2.05
        for pt in points:
            ax.text(x + 0.15, y_text, pt, color=C_SLATE, fontsize=8.5, va="top")
            y_text -= 0.55

    # Arrows between cards
    ax.annotate("", xy=(3.6, 1.55), xytext=(3.15, 1.55),
                arrowprops=dict(facecolor=C_NAVY, edgecolor="none", width=3, headwidth=8))
    ax.annotate("", xy=(6.9, 1.55), xytext=(6.45, 1.55),
                arrowprops=dict(facecolor=C_NAVY, edgecolor="none", width=3, headwidth=8))

    plt.tight_layout()
    out_file = output_dir / "slide2_overview_flow.png"
    plt.savefig(out_file, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_file}")

# -----------------------------------------------------------------------------
# 3. SLIDE 4 MOTIVATION: 4-Stage Visual Progression
# -----------------------------------------------------------------------------
def make_slide4_motivation():
    fig, ax = plt.subplots(figsize=(10.5, 3.2), dpi=200)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 3.2)
    ax.axis('off')

    stages = [
        (0.3, "CURRENT SITUATION", "Manual Analyst Screening\nLagging EOD Price Reports\nSpreadsheet Stress Models", C_SLATE),
        (2.9, "SYSTEMIC PROBLEMS", "Latency-Vulnerability Gap\nMisunderstood Financial Jargon\nMulti-Million Flash Crashes", C_RED),
        (5.5, "NEED FOR SOLUTION", "Sub-Second NLP Parsing\nObjective Severity Scoring (1-10)\nReal-Time Portfolio Links", C_ORANGE),
        (8.1, "RISKPULSE PLATFORM", "Automated FinBERT Intelligence\nDynamic Multi-Asset VaR/CVaR\nAccessible Web Dashboard", C_GREEN)
    ]

    for idx, (x, title, text, col) in enumerate(stages):
        box = patches.FancyBboxPatch((x, 0.4), 2.1, 2.4, boxstyle="round,pad=0.08", fc="#F8FAFC", ec=C_BORDER, lw=1.5)
        ax.add_patch(box)
        header = patches.Rectangle((x, 2.35), 2.1, 0.45, fc=col, ec="none")
        ax.add_patch(header)
        ax.text(x + 1.05, 2.57, title, color="#FFFFFF", fontsize=8.5, fontweight="bold", ha="center", va="center")
        ax.text(x + 0.15, 1.9, text, color=C_SLATE, fontsize=8, va="top", linespacing=1.6)

        if idx < 3:
            ax.annotate("", xy=(x + 2.35, 1.6), xytext=(x + 2.15, 1.6),
                        arrowprops=dict(facecolor=C_ORANGE, edgecolor="none", width=2.5, headwidth=7))

    plt.tight_layout()
    out_file = output_dir / "slide4_motivation_flow.png"
    plt.savefig(out_file, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_file}")

# -----------------------------------------------------------------------------
# 4. SLIDE 7 PROPOSED SYSTEM: Large Visual Concept Diagram
# -----------------------------------------------------------------------------
def make_slide7_concept():
    fig, ax = plt.subplots(figsize=(10.5, 3.6), dpi=200)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 3.6)
    ax.axis('off')

    nodes = [
        (0.3, "1. USER ROLE", "Portfolio Managers\nRisk Committees\nQuantitative Desks", C_NAVY),
        (2.35, "2. RAW INPUTS", "Live News Feeds\nFinancial RSS Stream\nSynthetic Fallback", C_SLATE),
        (4.4, "3. INGESTION & NLP", "Headline Deduplication\nFinBERT Sentiment (-1..+1)\nSeverity Scoring (1..10)", C_ORANGE),
        (6.45, "4. STRESS MODULES", "Beta-Weighted Repricing\nMacro Scenarios\nParametric VaR / CVaR", C_BLUE),
        (8.5, "5. REAL-TIME OUTPUT", "Live Sentiment Gauge\nAsset Loss Heatmap\nInstant Alert Telemetry", C_GREEN)
    ]

    for idx, (x, title, text, col) in enumerate(nodes):
        box = patches.FancyBboxPatch((x, 0.4), 1.7, 2.8, boxstyle="round,pad=0.08", fc="#F8FAFC", ec=C_BORDER, lw=1.5)
        ax.add_patch(box)
        head = patches.Rectangle((x, 2.65), 1.7, 0.55, fc=col, ec="none")
        ax.add_patch(head)
        ax.text(x + 0.85, 2.92, title, color="#FFFFFF", fontsize=8.5, fontweight="bold", ha="center", va="center")
        ax.text(x + 0.12, 2.25, text, color=C_SLATE, fontsize=7.8, va="top", linespacing=1.6)

        if idx < 4:
            ax.annotate("", xy=(x + 1.95, 1.8), xytext=(x + 1.72, 1.8),
                        arrowprops=dict(facecolor=C_ORANGE, edgecolor="none", width=2.5, headwidth=7))

    plt.tight_layout()
    out_file = output_dir / "slide7_concept_diagram.png"
    plt.savefig(out_file, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_file}")

# -----------------------------------------------------------------------------
# 5. SLIDE 9 WORKFLOW: Professional End-to-End Flowchart
# -----------------------------------------------------------------------------
def make_slide9_workflow():
    fig, ax = plt.subplots(figsize=(10.5, 3.8), dpi=200)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 3.8)
    ax.axis('off')

    # 6 Steps in 2 horizontal rows (3 per row) connected in serpentine flow
    steps = [
        (0.5, 2.2, "Step 1: Ingest Data", "Async RSS feed polling\n(Yahoo Finance & Reuters)", C_ORANGE),
        (3.8, 2.2, "Step 2: Clean & Tokenize", "Boilerplate strip, MD5 dedupe,\nand Pydantic normalization", C_NAVY),
        (7.1, 2.2, "Step 3: FinBERT Scoring", "Deep learning inference for\npolarity S in [-1.0, +1.0]", C_BLUE),
        (7.1, 0.4, "Step 4: Severity & NER", "Impact rating (1-10) and\nstock ticker resolution", C_SLATE),
        (3.8, 0.4, "Step 5: Macro Stress Test", "Beta-adjusted price shocks &\nVaR / CVaR recalculation", C_RED),
        (0.5, 0.4, "Step 6: Dashboard Telemetry", "Instant WebSocket/REST push\nto interactive React UI", C_GREEN)
    ]

    for x, y, title, desc, col in steps:
        box = patches.FancyBboxPatch((x, y), 2.9, 1.35, boxstyle="round,pad=0.08", fc="#F8FAFC", ec=C_BORDER, lw=1.5)
        ax.add_patch(box)
        strip = patches.Rectangle((x, y + 0.95), 2.9, 0.4, fc=col, ec="none")
        ax.add_patch(strip)
        ax.text(x + 1.45, y + 1.15, title, color="#FFFFFF", fontsize=8.5, fontweight="bold", ha="center", va="center")
        ax.text(x + 0.15, y + 0.72, desc, color=C_SLATE, fontsize=7.8, va="top", linespacing=1.4)

    # Arrows: 1 -> 2 -> 3 -> down to 4 -> 5 -> 6
    ax.annotate("", xy=(3.75, 2.87), xytext=(3.42, 2.87), arrowprops=dict(facecolor=C_ORANGE, edgecolor="none", width=2.5, headwidth=6))
    ax.annotate("", xy=(7.05, 2.87), xytext=(6.72, 2.87), arrowprops=dict(facecolor=C_ORANGE, edgecolor="none", width=2.5, headwidth=6))
    ax.annotate("", xy=(8.55, 1.8), xytext=(8.55, 2.15), arrowprops=dict(facecolor=C_ORANGE, edgecolor="none", width=2.5, headwidth=6))
    ax.annotate("", xy=(6.75, 1.07), xytext=(7.08, 1.07), arrowprops=dict(facecolor=C_ORANGE, edgecolor="none", width=2.5, headwidth=6))
    ax.annotate("", xy=(3.45, 1.07), xytext=(3.78, 1.07), arrowprops=dict(facecolor=C_ORANGE, edgecolor="none", width=2.5, headwidth=6))

    plt.tight_layout()
    out_file = output_dir / "slide9_workflow_flowchart.png"
    plt.savefig(out_file, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_file}")

# -----------------------------------------------------------------------------
# 6. SLIDE 10 METHODOLOGY: 6-Stage Process Pipeline
# -----------------------------------------------------------------------------
def make_slide10_methodology():
    fig, ax = plt.subplots(figsize=(10.5, 3.4), dpi=200)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 3.4)
    ax.axis('off')

    stages = [
        (0.2, "1. INGESTION", "Live RSS feeds\nFallback stream", C_SLATE),
        (1.9, "2. CLEANING", "Regex stripping\nMD5 deduplication", C_NAVY),
        (3.6, "3. FINBERT", "ProsusAI FinBERT\nPolarity S ∈ [-1,1]", C_ORANGE),
        (5.3, "4. SEVERITY", "Category multiplier\nScale I ∈ [1,10]", C_BLUE),
        (7.0, "5. BETA SHOCK", "ΔP = Shock·β·(1+I/10)\nSector adjustments", C_RED),
        (8.7, "6. RISK METRICS", "Parametric VaR_95\nExpected Shortfall", C_GREEN)
    ]

    for idx, (x, title, text, col) in enumerate(stages):
        box = patches.FancyBboxPatch((x, 0.4), 1.55, 2.6, boxstyle="round,pad=0.06", fc="#F8FAFC", ec=C_BORDER, lw=1.5)
        ax.add_patch(box)
        head = patches.Rectangle((x, 2.45), 1.55, 0.55, fc=col, ec="none")
        ax.add_patch(head)
        ax.text(x + 0.77, 2.72, title, color="#FFFFFF", fontsize=8.0, fontweight="bold", ha="center", va="center")
        ax.text(x + 0.12, 2.05, text, color=C_SLATE, fontsize=7.5, va="top", linespacing=1.5)

        if idx < 5:
            ax.annotate("", xy=(x + 1.82, 1.7), xytext=(x + 1.57, 1.7),
                        arrowprops=dict(facecolor=C_ORANGE, edgecolor="none", width=2.2, headwidth=6))

    plt.tight_layout()
    out_file = output_dir / "slide10_methodology_pipeline.png"
    plt.savefig(out_file, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_file}")

# -----------------------------------------------------------------------------
# 7. SLIDE 12 SYSTEM MODULES: Hub-and-Spoke Central Architecture Diagram
# -----------------------------------------------------------------------------
def make_slide12_modules():
    fig, ax = plt.subplots(figsize=(8.5, 4.4), dpi=200)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Center Hub
    hub = patches.Circle((5, 3), 1.25, fc=C_NAVY, ec=C_ORANGE, lw=3)
    ax.add_patch(hub)
    ax.text(5, 3.2, "RISKPULSE\nCORE", color="#FFFFFF", fontsize=11, fontweight="bold", ha="center", va="center")
    ax.text(5, 2.45, "FastAPI & SQLite", color=C_ORANGE, fontsize=8, ha="center")

    # 4 Surrounding Modules
    mods = [
        (1.5, 4.5, "INGESTION MODULE", "backend/ingestion.py\n• RSS Feeds & Fallback Stream\n• Deduplication & Cleaning", C_ORANGE),
        (8.5, 4.5, "NLP ENGINE", "backend/nlp_engine.py\n• FinBERT Transformer Scoring\n• Impact Rating & Entity NER", C_BLUE),
        (1.5, 1.5, "STRESS ENGINE", "backend/portfolio.py\n• Multi-Asset Beta Shock\n• VaR / CVaR Tail Metrics", C_RED),
        (8.5, 1.5, "WEB DASHBOARD", "frontend/src/\n• Real-Time Signal Stream\n• Interactive Scenario Panel", C_GREEN)
    ]

    for x, y, title, desc, col in mods:
        # Connecting line to center
        ax.plot([5, x], [3, y], color=C_BORDER, lw=2.5, zorder=1)
        # Module Card
        w, h = 2.7, 1.4
        box = patches.FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.08", fc="#F8FAFC", ec=col, lw=2, zorder=2)
        ax.add_patch(box)
        strip = patches.Rectangle((x - w/2, y + h/2 - 0.4), w, 0.4, fc=col, ec="none", zorder=3)
        ax.add_patch(strip)
        ax.text(x, y + h/2 - 0.2, title, color="#FFFFFF", fontsize=8.5, fontweight="bold", ha="center", va="center", zorder=4)
        ax.text(x - w/2 + 0.12, y + 0.12, desc, color=C_SLATE, fontsize=7.5, va="top", linespacing=1.35, zorder=4)

    plt.tight_layout()
    out_file = output_dir / "slide12_module_hub.png"
    plt.savefig(out_file, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_file}")

# -----------------------------------------------------------------------------
# 8. SLIDE 16 RESULTS: Dual-Panel Benchmark Chart
# -----------------------------------------------------------------------------
def make_slide16_results():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 3.8), dpi=200)
    fig.patch.set_facecolor("#FFFFFF")

    # Panel 1: Sub-Second Latency Benchmark
    endpoints = ["Health Check", "Portfolio VaR", "Signals Query", "FinBERT NLP", "Industry Target"]
    latencies = [3.2, 1.4, 18.0, 31.8, 100.0]
    bar_colors = [C_GREEN, C_GREEN, C_BLUE, C_ORANGE, C_SLATE]

    ax1.set_facecolor("#F8FAFC")
    bars = ax1.barh(endpoints, latencies, color=bar_colors, edgecolor="none", height=0.55)
    ax1.axvline(x=100.0, color=C_RED, linestyle="--", lw=1.5, label="Industry Target (<100ms)")
    ax1.set_title("REST API & Inference Latency (ms)", fontsize=10, fontweight="bold", color=C_NAVY, pad=8)
    ax1.set_xlabel("Latency (Milliseconds)", fontsize=8, color=C_SLATE)
    ax1.grid(True, axis='x', linestyle="--", alpha=0.6, color=C_BORDER)

    for bar in bars:
        w = bar.get_width()
        ax1.text(w + 2.0, bar.get_y() + bar.get_height()/2, f"{w:.1f}ms", va='center', fontsize=7.5, fontweight="bold", color=C_NAVY)

    # Panel 2: Portfolio Stress-Test Loss Distribution (Rate Hike Scenario)
    assets = ["AAPL (Tech)", "NVDA (Semis)", "JPM (Bank)", "XOM (Energy)", "Total Portfolio"]
    losses = [-7.8, -11.2, -3.4, -1.9, -6.1]
    loss_colors = [C_ORANGE, C_RED, C_BLUE, C_GREEN, C_NAVY]

    ax2.set_facecolor("#F8FAFC")
    bars2 = ax2.bar(assets, losses, color=loss_colors, edgecolor="none", width=0.55)
    ax2.axhline(y=0, color=C_BORDER, lw=1)
    ax2.set_title("Stress-Test Drawdown Simulation (-5% Rate Shock)", fontsize=10, fontweight="bold", color=C_NAVY, pad=8)
    ax2.set_ylabel("Asset Return Impact (%)", fontsize=8, color=C_SLATE)
    ax2.tick_params(axis='x', rotation=18, labelsize=7.5)
    ax2.grid(True, axis='y', linestyle="--", alpha=0.6, color=C_BORDER)

    for bar in bars2:
        h = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, h - 0.9, f"{h:.1f}%", ha='center', fontsize=7.5, fontweight="bold", color=C_NAVY)

    plt.tight_layout()
    out_file = output_dir / "slide16_results_benchmarks.png"
    plt.savefig(out_file, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_file}")

# -----------------------------------------------------------------------------
# 9. SLIDE 19 FUTURE SCOPE: Roadmap Timeline Graphic
# -----------------------------------------------------------------------------
def make_slide19_roadmap():
    fig, ax = plt.subplots(figsize=(10.5, 3.4), dpi=200)
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FFFFFF")
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 3.4)
    ax.axis('off')

    milestones = [
        (0.3, "CURRENT PLATFORM", "• Sub-35ms FinBERT\n• SQLite Ingestion\n• 5-Asset Portfolio VaR", C_GREEN),
        (2.9, "MILESTONE 1 (1-3 Mo)", "• TimescaleDB Migration\n• GARCH(1,1) Volatility\n• 25+ Global News Feeds", C_ORANGE),
        (5.5, "MILESTONE 2 (3-6 Mo)", "• Causal Knowledge Graphs\n• ONNX INT8 Quantization\n• 10k Monte Carlo Paths", C_BLUE),
        (8.1, "MILESTONE 3 (6-12 Mo)", "• Live Broker API Execution\n• Multi-Agent Risk Copilot\n• Derivatives & CDS Modeling", C_NAVY)
    ]

    for idx, (x, title, text, col) in enumerate(milestones):
        box = patches.FancyBboxPatch((x, 0.4), 2.1, 2.5, boxstyle="round,pad=0.08", fc="#F8FAFC", ec=C_BORDER, lw=1.5)
        ax.add_patch(box)
        head = patches.Rectangle((x, 2.4), 2.1, 0.5, fc=col, ec="none")
        ax.add_patch(head)
        ax.text(x + 1.05, 2.65, title, color="#FFFFFF", fontsize=8.0, fontweight="bold", ha="center", va="center")
        ax.text(x + 0.15, 1.95, text, color=C_SLATE, fontsize=7.5, va="top", linespacing=1.6)

        if idx < 3:
            ax.annotate("", xy=(x + 2.35, 1.65), xytext=(x + 2.15, 1.65),
                        arrowprops=dict(facecolor=C_ORANGE, edgecolor="none", width=2.5, headwidth=7))

    plt.tight_layout()
    out_file = output_dir / "slide19_roadmap_timeline.png"
    plt.savefig(out_file, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print(f"Generated {out_file}")

# -----------------------------------------------------------------------------
# 10. CROPPED UI SCREENSHOTS FOR SLIDE 14
# -----------------------------------------------------------------------------
def make_cropped_ui_screens():
    dash_path = Path("docs/dashboard_preview.png")
    if not dash_path.exists():
        print("dashboard_preview.png not found, skipping crops.")
        return

    img = Image.open(dash_path)
    w, h = img.size

    # Crop 1: Top header & gauge area (w, 0.45*h)
    crop_top = img.crop((0, 0, w, int(h * 0.48)))
    crop_top_out = output_dir / "ui_crop_sentiment_gauge.png"
    crop_top.save(crop_top_out)
    print(f"Generated {crop_top_out}")

    # Crop 2: Bottom table & scenario stress test area (w, from 0.45*h to h)
    crop_bottom = img.crop((0, int(h * 0.45), w, h))
    crop_bottom_out = output_dir / "ui_crop_stress_heatmap.png"
    crop_bottom.save(crop_bottom_out)
    print(f"Generated {crop_bottom_out}")

if __name__ == "__main__":
    make_slide1_hero()
    make_slide2_overview()
    make_slide4_motivation()
    make_slide7_concept()
    make_slide9_workflow()
    make_slide10_methodology()
    make_slide12_modules()
    make_slide16_results()
    make_slide19_roadmap()
    make_cropped_ui_screens()
    print("All visual diagrams successfully created in docs/diagrams/")
