"""
Generate an ultra-crisp high-resolution UI preview image of the RiskPulse platform.
Used for Slide 8 (Implementation & Live Dashboard) in the presentation.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

def generate_dashboard_preview(output_path: str):
    fig, ax = plt.subplots(figsize=(16, 9), dpi=250)
    fig.patch.set_facecolor('#0A0E17')
    ax.set_facecolor('#0A0E17')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Color Palette
    c_bg = '#0A0E17'
    c_sidebar = '#111726'
    c_card = '#141C2E'
    c_border = '#202B42'
    c_text_bright = '#FFFFFF'
    c_text_muted = '#94A3B8'
    c_blue = '#0284C7'
    c_blue_tint = '#1E3A8A'
    c_green = '#10B981'
    c_red = '#EF4444'
    c_red_tint = '#3B1824'
    c_amber = '#FBBF24'

    def draw_box(x, y, w, h, bg=c_card, border=c_border, rad=0.8):
        rect = patches.FancyBboxPatch((x, y), w, h,
                                      boxstyle=f"round,pad=0.0,rounding_size={rad}",
                                      facecolor=bg, edgecolor=border, linewidth=1.0)
        ax.add_patch(rect)

    # 1. SIDEBAR (X: 1.5 to 20.5, Y: 2 to 98)
    draw_box(1.5, 2, 19, 96, bg=c_sidebar, border=c_border)
    ax.text(3, 94, "S&P Global × CRISIL", fontsize=8, fontweight='bold', color=c_blue)
    ax.text(3, 91.5, "RiskPulse Terminal", fontsize=11, fontweight='bold', color=c_text_bright)
    ax.text(3, 89, "Financial Risk Intelligence", fontsize=7.5, color=c_text_muted)

    # Nav items
    navs = [
        ("● Executive Overview", True),
        ("  Risk Signal Stream", False),
        ("  Portfolio Holdings", False),
        ("  Stress Testing Studio", False),
        ("  Ingestion Feeds", False),
        ("  System Architecture", False)
    ]
    for idx, (lbl, active) in enumerate(navs):
        ny = 83 - idx * 5.2
        if active:
            draw_box(2.5, ny - 1.2, 17, 4.2, bg=c_blue_tint, border=c_blue, rad=0.5)
            ax.text(4, ny + 0.8, lbl, fontsize=8.5, fontweight='bold', color='#38BDF8')
        else:
            ax.text(4, ny + 0.8, lbl, fontsize=8, color=c_text_muted)

    ax.text(3, 6, "Candidate: Abhi Pandey", fontsize=8, fontweight='bold', color='#E2E8F0')
    ax.text(3, 4, "VIT Bhopal University (4th Yr)", fontsize=7.5, color=c_text_muted)

    # 2. TOP BANNER (X: 22 to 98.5, Y: 90 to 98)
    draw_box(22, 90, 76.5, 8, bg=c_card, border=c_border)
    ax.text(24, 95, "Executive Risk Dashboard", fontsize=13, fontweight='bold', color=c_text_bright)
    ax.text(24, 92, "Real-time unstructured financial news ingestion & dynamic Module B portfolio stress testing", fontsize=8, color=c_text_muted)
    
    # Live Pill & Buttons
    draw_box(84, 92, 13, 4.2, bg=c_blue, border=c_blue, rad=0.5)
    ax.text(90.5, 94.1, "LIVE RSS FEED", fontsize=8, fontweight='bold', color='#FFFFFF', ha='center')

    # 3. TOP METRICS CARDS (X: 22 to 98.5, Y: 75 to 88.5)
    metrics = [
        ("TOTAL SIGNALS", "18", "Multi-source news & social feeds", c_blue),
        ("HIGH IMPACT (≥7)", "6", "Trigger threshold qualified", c_red),
        ("MARKET SENTIMENT", "-0.42", "Normalized continuous [-1.0, +1.0]", c_amber),
        ("PORTFOLIO EXPOSURE", "$1,000,000", "10 multi-asset positions", c_green)
    ]
    card_w = 18.2
    gap = 1.23
    for idx, (lbl, val, sub, col) in enumerate(metrics):
        cx = 22 + idx * (card_w + gap)
        draw_box(cx, 75, card_w, 13.5, bg=c_card, border=c_border)
        ax.text(cx + 1.5, 85.5, lbl, fontsize=7.5, fontweight='bold', color=c_text_muted)
        ax.text(cx + 1.5, 80.5, val, fontsize=15, fontweight='bold', color=col)
        ax.text(cx + 1.5, 77.2, sub, fontsize=6.8, color=c_text_muted)

    # 4. INTERACTIVE TEXT ANALYSIS TERMINAL (X: 22 to 58, Y: 43 to 73.5)
    draw_box(22, 43, 36.5, 30.5, bg=c_card, border=c_border)
    ax.text(24, 70.5, "Live Risk Signal Ingestion Terminal", fontsize=10, fontweight='bold', color=c_text_bright)
    ax.text(56, 70.5, "NLP: ONLINE", fontsize=7.5, color=c_green, ha='right')

    # Input Box Mockup
    draw_box(23.5, 54, 33.5, 14, bg=c_sidebar, border=c_border)
    sample_text = "NVIDIA receives severe antitrust subpoenas from DOJ\nover AI chip monopoly and cloud market dominance..."
    ax.text(24.5, 63, sample_text, fontsize=8, color='#E2E8F0', va='top')

    # Output Card Inside Terminal
    draw_box(23.5, 45, 33.5, 7.5, bg=c_red_tint, border='#B91C1C')
    ax.text(24.5, 49.8, "Entity: NVIDIA | Sent: -0.84 (Neg) | Event: Regulatory", fontsize=7.5, fontweight='bold', color='#FFFFFF')
    ax.text(24.5, 46.8, "Impact Score: 8 / 10 (High Risk) → STRESS TEST TRIGGERED", fontsize=7.5, fontweight='bold', color='#F87171')

    # 5. MODULE B STRESS TESTING RESULT PANEL (X: 60 to 98.5, Y: 43 to 73.5)
    draw_box(60, 43, 38.5, 30.5, bg=c_card, border=c_border)
    ax.text(62, 70.5, "Module B: Portfolio Stress Simulation", fontsize=10, fontweight='bold', color=c_text_bright)
    ax.text(96, 70.5, "IMPACT ≥ 7 TRIGGERED", fontsize=7.5, fontweight='bold', color=c_red, ha='right')

    # Valuation Stat Boxes
    v_boxes = [
        ("Pre-Stress Value", "$1,000,000", c_text_bright),
        ("Stressed Value", "$836,000", c_red),
        ("Net Drawdown", "-$164,000 (-16.4%)", c_red)
    ]
    for idx, (v_lbl, v_val, v_col) in enumerate(v_boxes):
        vx = 62 + idx * 11.8
        draw_box(vx, 57.5, 11, 10.5, bg=c_sidebar, border=c_border)
        ax.text(vx + 5.5, 65, v_lbl, fontsize=7, color=c_text_muted, ha='center')
        ax.text(vx + 5.5, 60.5, v_val, fontsize=9.5, fontweight='bold', color=v_col, ha='center')

    # Asset Shock Highlights
    ax.text(62, 53.5, "Applied Scenario Shocks (Regulatory Shock Matrix):", fontsize=7.5, fontweight='bold', color=c_text_muted)
    shocks_text = "• Tech Equities: -15.0%  • General Equities: -8.0%  • Crypto Assets: -25.0%  • Bonds: 0.0%"
    ax.text(62, 50, shocks_text, fontsize=7, color='#E2E8F0')

    # 6. RISK SIGNAL STREAM TABLE (X: 22 to 98.5, Y: 2 to 41.5)
    draw_box(22, 2, 76.5, 39.5, bg=c_card, border=c_border)
    ax.text(24, 38.5, "Structured Financial Risk Signal Stream", fontsize=10, fontweight='bold', color=c_text_bright)
    ax.text(96, 38.5, "Showing Ingested Signals", fontsize=7.5, color=c_text_muted, ha='right')

    # Table Header
    draw_box(23.5, 33, 73.5, 3.5, bg=c_sidebar, border=c_border)
    headers = [("TIME", 25), ("COMPANY", 33), ("SOURCE", 44), ("EVENT CATEGORY", 56), ("SENTIMENT", 70), ("IMPACT", 81), ("ACTION", 91)]
    for h_txt, h_x in headers:
        ax.text(h_x, 34.8, h_txt, fontsize=7, fontweight='bold', color=c_text_muted)

    # Table Rows
    rows = [
        ("09:30:15", "NVIDIA", "Financial News", "Regulatory", "-0.84 (Neg)", "8 / 10", "⚡ SHOCKED", c_red),
        ("09:31:40", "Tesla", "Social Stream", "Regulatory", "-0.76 (Neg)", "8 / 10", "⚡ SHOCKED", c_red),
        ("09:33:10", "CrowdStrike", "Financial News", "Cyber Attack", "-0.92 (Neg)", "9 / 10", "⚡ SHOCKED", c_red),
        ("09:35:25", "JPMorgan", "Financial News", "Earnings Beat", "+0.81 (Pos)", "3 / 10", "Bypassed (<7)", c_green),
        ("09:37:05", "Apple Inc", "Social Stream", "Operational", "+0.68 (Pos)", "2 / 10", "Bypassed (<7)", c_green),
        ("09:39:50", "Taiwan Semi", "Financial News", "Supply Chain", "-0.71 (Neg)", "7 / 10", "⚡ SHOCKED", c_red)
    ]
    for r_idx, (t_time, t_comp, t_src, t_ev, t_sent, t_imp, t_act, t_col) in enumerate(rows):
        ry = 28 - r_idx * 4.2
        ax.text(25, ry + 1.2, t_time, fontsize=7, color=c_text_muted)
        ax.text(33, ry + 1.2, t_comp, fontsize=7.5, fontweight='bold', color=c_text_bright)
        ax.text(44, ry + 1.2, t_src, fontsize=7, color=c_text_muted)
        ax.text(56, ry + 1.2, t_ev, fontsize=7.5, color='#E2E8F0')
        ax.text(70, ry + 1.2, t_sent, fontsize=7, color=t_col)
        ax.text(81, ry + 1.2, t_imp, fontsize=7.5, fontweight='bold', color=t_col)
        ax.text(91, ry + 1.2, t_act, fontsize=7, fontweight='bold', color=t_col)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=250, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Successfully generated dashboard preview at {output_path}")

if __name__ == "__main__":
    generate_dashboard_preview("docs/dashboard_preview.png")
