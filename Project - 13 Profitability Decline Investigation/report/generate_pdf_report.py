"""
Apple Inc. - Publication-Grade Executive PDF Report Generator
Project - 13: Profitability Decline Investigation

Compiles an exhaustive, C-suite executive diagnostic report in PDF format:
- Executive Summary & The Silo Paradox Anatomy
- Multi-Quarter Financial & Operational Telemetry Audit Table
- 5 Publication-Grade High-DPI Matplotlib Visualizations:
    1. 16-Quarter Operating Margin Trajectory (Highlighting 3-Quarter Decline)
    2. Causal Profitability Waterfall Margin Decomposition (-912 bps)
    3. Departmental Silo Reported Metric vs True Financial Leakage
    4. Inter-Departmental Cross-Functional Correlation Heatmap
    5. Prescriptive Board Protocols ROI & Payback Matrix
- Econometric Marginal Elasticity Profiling
- 5 Prescriptive Board Strategic Protocols (Alpha to Epsilon)
- Governance OKR Realignment via Vanity Metric Distortion Index (VMDI)
"""

import os
import sys
import tempfile
import numpy as np
import pandas as pd

# Configure Loky & Matplotlib to avoid permissions & thread warnings
os.environ["LOKY_MAX_CPU_COUNT"] = "4"
mpl_dir = os.path.join(tempfile.gettempdir(), "mpl_apple_13")
os.makedirs(mpl_dir, exist_ok=True)
os.environ["MPLCONFIGDIR"] = mpl_dir

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from models.causal_attribution_engine import CausalAttributionEngine
from models.silo_paradox_analyzer import SiloParadoxAnalyzer
from models.ai_business_analyst_agent import AIBusinessAnalystAgent

class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and print total page numbers: Page X of Y.
    Adds executive header and footer.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#6e6e73"))
        
        # Omit header/footer on cover page if page 1
        if self._pageNumber > 1:
            # Header
            self.drawString(54, 755, "APPLE INC. — EXECUTIVE DECISION INTELLIGENCE REPORT")
            self.drawRightString(612 - 54, 755, "PROJECT - 13: PROFITABILITY DECLINE INVESTIGATION")
            self.setStrokeColor(colors.HexColor("#d2d2d7"))
            self.setLineWidth(0.5)
            self.line(54, 747, 612 - 54, 747)
            
            # Footer
            self.line(54, 45, 612 - 54, 45)
            self.drawString(54, 32, "STRICTLY CONFIDENTIAL — FOR APPLE EXECUTIVE BOARD REVIEW ONLY")
            page_text = f"Page {self._pageNumber} of {page_count}"
            self.drawRightString(612 - 54, 32, page_text)
            
        self.restoreState()


def generate_high_res_charts(chart_dir, df_quarterly, engine, silo_data):
    """
    Generates 5 publication-grade high-DPI visual charts.
    """
    os.makedirs(chart_dir, exist_ok=True)
    chart_paths = {}
    
    # Set global style
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")
    plt.rcParams["font.sans-serif"] = "Arial"
    plt.rcParams["axes.edgecolor"] = "#d2d2d7"
    plt.rcParams["axes.linewidth"] = 0.8
    
    # -------------------------------------------------------------------------
    # Chart 1: 16-Quarter Operating Margin Trajectory & Consecutive 3-Quarter Decline
    # -------------------------------------------------------------------------
    fig, ax1 = plt.subplots(figsize=(8.5, 3.8), dpi=300)
    quarters = df_quarterly["quarter"].tolist()
    op_margins = df_quarterly["operating_margin_pct"].tolist()
    revenues = df_quarterly["revenue_b"].tolist()
    x = np.arange(len(quarters))
    
    # Dual axis: Bar for revenue, Line for Operating Margin
    ax2 = ax1.twinx()
    ax2.bar(x, revenues, width=0.45, color="#e5e5ea", alpha=0.7, label="Quarterly Revenue ($B)")
    ax2.set_ylabel("Total Revenue ($B)", color="#86868b", fontsize=9, fontweight="bold")
    ax2.set_ylim(60, 140)
    ax2.grid(False)
    
    # Highlight crisis quarters (12, 13, 14 -> Q1, Q2, Q3 2025)
    crisis_indices = [12, 13, 14]
    ax1.plot(x, op_margins, marker="o", color="#0071e3", linewidth=2.5, label="Operating Margin (%)")
    ax1.plot(x[12:15], op_margins[12:15], marker="s", color="#ff3b30", linewidth=3.2, label="3-Quarter Consecutive Decline (-912 bps)")
    
    # Highlight band
    ax1.axvspan(11.5, 14.5, color="#ff3b30", alpha=0.12, label="Crisis Investigation Window")
    
    # Annotations
    ax1.annotate("Q4 2024 (Baseline)\n31.4% Margin", xy=(11, op_margins[11]), xytext=(9.5, 34),
                 arrowprops=dict(arrowstyle="->", color="#1d1d1f", lw=1), fontsize=8, fontweight="bold")
    ax1.annotate("Q3 2025 (Trough)\n22.3% Margin (-912 bps)", xy=(14, op_margins[14]), xytext=(12.2, 18),
                 arrowprops=dict(arrowstyle="->", color="#ff3b30", lw=1.2), fontsize=8, fontweight="bold", color="#ff3b30")
    
    ax1.set_xticks(x)
    ax1.set_xticklabels(quarters, rotation=45, ha="right", fontsize=7.5)
    ax1.set_ylabel("Operating Margin (%)", color="#1d1d1f", fontsize=9, fontweight="bold")
    ax1.set_ylim(15, 38)
    ax1.set_title("Apple Inc. 16-Quarter Operating Margin Trajectory & Crisis Window", fontsize=11, fontweight="bold", pad=12, color="#1d1d1f")
    
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper right", fontsize=7.5, framealpha=0.9)
    plt.tight_layout()
    
    p1 = os.path.join(chart_dir, "chart_1_margin_trajectory.png")
    fig.savefig(p1, dpi=300)
    plt.close(fig)
    chart_paths["p1"] = p1
    
    # -------------------------------------------------------------------------
    # Chart 2: Causal Profitability Waterfall Margin Decomposition (-912 bps)
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 3.8), dpi=300)
    
    categories = [
        "Q4 2024\nBaseline",
        "Air Freight\nSurge",
        "Trade-In Subsidy\nContra-Rev",
        "Silicon Contractor\nSpend",
        "Buffer DIO\nWrite-downs",
        "Assembly Rush\nOvertime",
        "Q3 2025\nTrough"
    ]
    
    values = [31.46, -2.45, -1.95, -1.82, -1.64, -1.24, 22.34] # in % or approx bps
    
    # Compute bottom coordinates for waterfall
    bottoms = [0, 31.46 - 2.45, 29.01 - 1.95, 27.06 - 1.82, 25.24 - 1.64, 23.60 - 1.24, 0]
    heights = [31.46, 2.45, 1.95, 1.82, 1.64, 1.24, 22.34]
    bar_colors = ["#34c759", "#ff3b30", "#ff9500", "#af52de", "#5856d6", "#ff2d55", "#0071e3"]
    
    # Bars
    bars = ax.bar(categories, heights, bottom=bottoms, color=bar_colors, width=0.55, edgecolor="#1d1d1f", linewidth=0.6)
    
    # Labels
    for i, b in enumerate(bars):
        if i == 0 or i == 6:
            val_txt = f"{values[i]:.1f}%"
            y_pos = values[i] + 0.8
        else:
            val_txt = f"{values[i]:+.2f}%\n({int(values[i]*100)} bps)"
            y_pos = bottoms[i] + heights[i] / 2 - 0.4
        ax.text(b.get_x() + b.get_width() / 2, y_pos, val_txt, ha="center", va="center", 
                fontsize=7.5, fontweight="bold", color="white" if 0 < i < 6 else "#1d1d1f")
        
    ax.set_ylabel("Operating Margin (%)", fontsize=9, fontweight="bold")
    ax.set_ylim(0, 37)
    ax.set_title("Causal Margin Waterfall: Anatomy of the -912 bps Profitability Collapse", fontsize=11, fontweight="bold", pad=12)
    plt.tight_layout()
    
    p2 = os.path.join(chart_dir, "chart_2_waterfall_decomposition.png")
    fig.savefig(p2, dpi=300)
    plt.close(fig)
    chart_paths["p2"] = p2

    # -------------------------------------------------------------------------
    # Chart 3: Departmental Reported Status vs True Financial Leakage ($B)
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 3.4), dpi=300)
    depts = ["Operations\n(Logistics)", "Marketing\n(Trade-in & Mix)", "HR\n(Silicon Contractors)", "Operations / Fin\n(Buffer DIO)", "HR / Ops\n(Overtime Rushes)"]
    leakage = [2.45, 1.95, 1.82, 1.64, 1.24]
    y_pos = np.arange(len(depts))
    
    bars = ax.barh(y_pos, leakage, color=["#ff3b30", "#ff9500", "#af52de", "#5856d6", "#ff2d55"], height=0.55)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(depts, fontsize=8.5, fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlabel("Annualized Financial Leakage ($ Billions)", fontsize=9, fontweight="bold")
    ax.set_xlim(0, 3.2)
    ax.set_title("The Silo Paradox: Annualized Margin Leakage by Cross-Functional Driver ($9.10B Total)", fontsize=11, fontweight="bold", pad=12)
    
    for b in bars:
        w = b.get_width()
        ax.text(w + 0.08, b.get_y() + b.get_height() / 2, f"${w:.2f}B Leakage\n(Reported Status: GREEN)", 
                ha="left", va="center", fontsize=7.5, fontweight="bold", color="#1d1d1f")
        
    plt.tight_layout()
    p3 = os.path.join(chart_dir, "chart_3_silo_leakage_bars.png")
    fig.savefig(p3, dpi=300)
    plt.close(fig)
    chart_paths["p3"] = p3

    # -------------------------------------------------------------------------
    # Chart 4: Inter-Departmental Cross-Correlation Matrix
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 4.0), dpi=300)
    corr_data = engine.get_cross_functional_correlation_matrix()
    matrix_vals = np.array([row["values"] for row in corr_data["matrix"]])
    short_labels = [
        "Op Margin %", "Mkt Trade-In $", "Low-Margin SKU %",
        "Silicon Attrition %", "HR Contractors $", "Overtime %",
        "Air Freight %", "Logistics Spend $", "DIO Days", "Buffer Write-Down $"
    ]
    
    im = ax.imshow(matrix_vals, cmap="coolwarm", vmin=-1.0, vmax=1.0)
    ax.set_xticks(np.arange(len(short_labels)))
    ax.set_yticks(np.arange(len(short_labels)))
    ax.set_xticklabels(short_labels, rotation=45, ha="right", fontsize=7.5)
    ax.set_yticklabels(short_labels, fontsize=7.5)
    
    for i in range(len(short_labels)):
        for j in range(len(short_labels)):
            val = matrix_vals[i, j]
            color_txt = "white" if abs(val) > 0.55 else "black"
            ax.text(j, i, f"{val:.2f}", ha="center", va="center", color=color_txt, fontsize=6.5, fontweight="bold")
            
    cbar = fig.colorbar(im, ax=ax, fraction=0.035, pad=0.04)
    cbar.ax.tick_params(labelsize=7)
    ax.set_title("Cross-Functional Transmission Matrix: Inter-Departmental Correlation Contagion", fontsize=11, fontweight="bold", pad=12)
    plt.tight_layout()
    p4 = os.path.join(chart_dir, "chart_4_correlation_heatmap.png")
    fig.savefig(p4, dpi=300)
    plt.close(fig)
    chart_paths["p4"] = p4

    # -------------------------------------------------------------------------
    # Chart 5: Prescriptive Board Protocols ROI & Payback
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 3.4), dpi=300)
    protocols = ["Protocol Alpha\n(Ocean Shift)", "Protocol Beta\n(Silicon Insource)", "Protocol Gamma\n(Promo Gate)", "Protocol Delta\n(Lean DIO)", "Protocol Epsilon\n(Variance Rhythm)"]
    gains = [2.21, 1.77, 1.66, 1.31, 0.93] # $B
    paybacks = [2.1, 4.1, 1.2, 3.7, 3.2] # Months
    
    x_pos = np.arange(len(protocols))
    w = 0.38
    
    ax1 = ax
    ax2 = ax.twinx()
    
    b1 = ax1.bar(x_pos - w/2, gains, width=w, color="#0071e3", label="Annual EBITDA Gain ($B)")
    b2 = ax2.bar(x_pos + w/2, paybacks, width=w, color="#ff9500", label="Payback Horizon (Months)")
    
    ax1.set_ylabel("Annual EBITDA Accretion ($B)", color="#0071e3", fontsize=8.5, fontweight="bold")
    ax2.set_ylabel("Payback Horizon (Months)", color="#ff9500", fontsize=8.5, fontweight="bold")
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(protocols, fontsize=7.5, fontweight="bold")
    ax1.set_ylim(0, 2.8)
    ax2.set_ylim(0, 6.0)
    ax2.grid(False)
    
    for b in b1:
        ax1.text(b.get_x() + b.get_width()/2, b.get_height() + 0.08, f"${b.get_height():.2f}B", ha="center", fontsize=7, fontweight="bold", color="#0071e3")
    for b in b2:
        ax2.text(b.get_x() + b.get_width()/2, b.get_height() + 0.15, f"{b.get_height():.1f} mo", ha="center", fontsize=7, fontweight="bold", color="#ff9500")
        
    ax1.set_title("5 Prescriptive Board Strategic Protocols: Financial Accretion vs Payback Speed", fontsize=11, fontweight="bold", pad=12)
    plt.tight_layout()
    p5 = os.path.join(chart_dir, "chart_5_protocols_roi.png")
    fig.savefig(p5, dpi=300)
    plt.close(fig)
    chart_paths["p5"] = p5
    
    return chart_paths


def build_pdf_report(data_path=None, output_pdf=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if data_path is None:
        data_path = os.path.join(base_dir, "data", "apple_cross_functional_quarterly_data.csv")
    if output_pdf is None:
        output_pdf = os.path.join(base_dir, "report", "Apple_Profitability_Decline_Investigation_Report.pdf")
        
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)
    chart_dir = os.path.join(base_dir, "report", "assets")
    
    df_quarterly = pd.read_csv(data_path)
    engine = CausalAttributionEngine(data_path=data_path)
    silo_analyzer = SiloParadoxAnalyzer(data_path=data_path)
    silo_data = silo_analyzer.analyze_paradox()
    agent = AIBusinessAnalystAgent(engine, silo_analyzer)
    protocols = agent.get_prescriptive_protocols()
    
    # Generate charts
    chart_paths = generate_high_res_charts(chart_dir, df_quarterly, engine, silo_data)
    
    # Document Setup
    margin = 54 # 0.75 in
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        leftMargin=margin,
        rightMargin=margin,
        topMargin=margin,
        bottomMargin=margin
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Apple-Themed Palette Styles
    title_style = ParagraphStyle(
        "CoverTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=24,
        leading=28,
        textColor=colors.HexColor("#1d1d1f"),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        "CoverSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#86868b"),
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=19,
        textColor=colors.HexColor("#1d1d1f"),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        "Heading2_Custom",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#0071e3"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        "Body_Custom",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1d1d1f"),
        spaceAfter=6
    )
    
    bullet_style = ParagraphStyle(
        "Bullet_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.2,
        leading=11.5,
        textColor=colors.HexColor("#333336"),
        leftIndent=12,
        spaceAfter=4
    )
    
    callout_style = ParagraphStyle(
        "Callout_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor("#ff3b30"),
        spaceAfter=4
    )
    
    table_cell = ParagraphStyle(
        "TableCell",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=7.2,
        leading=9.5,
        textColor=colors.HexColor("#1d1d1f")
    )
    
    table_cell_bold = ParagraphStyle(
        "TableCellBold",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.2,
        leading=9.5,
        textColor=colors.HexColor("#1d1d1f")
    )
    
    table_cell_green = ParagraphStyle(
        "TableCellGreen",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.0,
        leading=9.0,
        textColor=colors.HexColor("#28a745")
    )
    
    table_cell_red = ParagraphStyle(
        "TableCellRed",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=7.0,
        leading=9.0,
        textColor=colors.HexColor("#ff3b30")
    )
    
    elements = []
    
    # -------------------------------------------------------------------------
    # COVER / HEADER BANNER
    # -------------------------------------------------------------------------
    meta_table_data = [
        [
            Paragraph("<b>APPLE INC. EXECUTIVE BOARD MEMORANDUM</b>", ParagraphStyle("HdrMeta", fontName="Helvetica-Bold", fontSize=9, textColor=colors.HexColor("#0071e3"))),
            Paragraph("<b>CLASSIFICATION:</b> STRICTLY CONFIDENTIAL // C-SUITE", ParagraphStyle("HdrRight", fontName="Helvetica-Bold", fontSize=8, alignment=2, textColor=colors.HexColor("#ff3b30")))
        ]
    ]
    t_meta = Table(meta_table_data, colWidths=[320, 184])
    t_meta.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    elements.append(t_meta)
    elements.append(Spacer(1, 4))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0071e3"), spaceAfter=12, spaceBefore=4))
    
    elements.append(Paragraph("Project - 13: Profitability Decline Investigation", title_style))
    elements.append(Paragraph("Cross-Functional AI Diagnostic: Synthesizing Marketing, HR, Operations & Finance Telemetry to Solve the Consecutive 3-Quarter Profitability Contraction", subtitle_style))
    
    # Executive Metadata Box
    exec_box_data = [
        [
            Paragraph("<b>Date of Inquiry:</b> October 2026", table_cell),
            Paragraph("<b>Target Entity:</b> Apple Inc. (Global)", table_cell),
            Paragraph("<b>Primary Engine:</b> AI Business Analyst", table_cell)
        ],
        [
            Paragraph("<b>Crisis Window:</b> FY25-Q1 through FY25-Q3", table_cell),
            Paragraph("<b>Baseline vs Trough:</b> 31.4% -> 22.3% (-912 bps)", table_cell_red),
            Paragraph("<b>Annualized Leakage:</b> $9.10 Billion USD", table_cell_bold)
        ]
    ]
    t_exec_box = Table(exec_box_data, colWidths=[168, 168, 168])
    t_exec_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f5f5f7")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#d2d2d7")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#e5e5ea")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(t_exec_box)
    elements.append(Spacer(1, 10))
    
    # -------------------------------------------------------------------------
    # SECTION 1: EXECUTIVE PROBLEM STATEMENT & THE SILO PARADOX
    # -------------------------------------------------------------------------
    elements.append(Paragraph("1. Executive Summary & The Departmental 'Silo Paradox'", h1_style))
    elements.append(Paragraph(
        "Apple Company profitability has declined for <b>three consecutive quarters</b> (FY2025-Q1: 28.2%, FY2025-Q2: 24.8%, "
        "FY2025-Q3: 22.3%), representing an aggregate operating margin contraction of <b>912 basis points</b> and an annualized "
        "operating profit leakage of <b>$9.10 Billion</b>. Crucially, when executive leadership polled departmental leaders, "
        "<b>every single department reported satisfactory performance</b> against their isolated scorecard benchmarks:",
        body_style
    ))
    
    elements.append(Paragraph("• <b>Marketing:</b> Reported CAC of $41.80 (beating the $45 budget ceiling by 7.1%) and DTC conversion rates meeting target.", bullet_style))
    elements.append(Paragraph("• <b>HR & People:</b> Reported voluntary employee turnover at 4.31% (33.7% better than tech benchmark) and 100.6% headcount fulfillment.", bullet_style))
    elements.append(Paragraph("• <b>Operations & Supply Chain:</b> Reported On-Time In-Full (OTIF) fulfillment at 98.4% (exceeding the 98.0% SLA commitment).", bullet_style))
    elements.append(Paragraph("• <b>Finance & Treasury:</b> Maintained quarterly top-line revenue between $94.6B and $118.4B and held $153B+ in cash liquidity.", bullet_style))
    
    elements.append(Paragraph(
        "<b>The AI Business Analyst Core Finding:</b> This investigation demonstrates that Apple did not experience an external demand or macro crisis. "
        "Rather, the enterprise succumbed to a <b>Cross-Functional Silo Sub-Optimization Trap</b>. Individual departments hit localized target metrics "
        "by unintentionally exporting massive friction and costs into adjacent operational nodes. To maintain green surface KPIs, departments engaged "
        "in heroic but financially catastrophic behaviors—specifically chartered emergency air freight, exorbitant contractor substitution, "
        "and aggressive trade-in contra-revenue allowances.",
        body_style
    ))
    
    # Embed Chart 1: Trajectory
    elements.append(Spacer(1, 4))
    elements.append(Image(chart_paths["p1"], width=504, height=225))
    elements.append(Spacer(1, 8))
    
    # -------------------------------------------------------------------------
    # SECTION 2: TELEMETRY & MULTI-QUARTER FINANCIAL AUDIT TABLE
    # -------------------------------------------------------------------------
    elements.append(Paragraph("2. Financial Telemetry & Profitability Decomposition Audit", h1_style))
    elements.append(Paragraph(
        "The table below details Apple's cross-functional performance across 8 representative quarters, highlighting the transition "
        "from the healthy FY2024 baseline into the 3-quarter crisis period (FY2025 Q1-Q3).",
        body_style
    ))
    
    audit_table_data = [
        ["Quarter", "Rev ($B)", "COGS ($B)", "Gross %", "Opex ($B)", "Op Profit ($B)", "Op Margin %", "Air Frt %", "Contractor $B", "Trade-In Sub"]
    ]
    
    # Select sample quarters: 2024-Q1 through 2025-Q4
    selected_quarters = df_quarterly[df_quarterly["quarter_index"] >= 9]
    for _, row in selected_quarters.iterrows():
        is_crisis = row["is_crisis_period"] == 1
        q_style = table_cell_red if is_crisis else table_cell_bold
        margin_style = table_cell_red if is_crisis else table_cell
        
        audit_table_data.append([
            Paragraph(f"<b>{row['quarter']}</b>" + (" *" if is_crisis else ""), q_style),
            Paragraph(f"${row['revenue_b']:.1f}", table_cell),
            Paragraph(f"${row['cogs_b']:.1f}", table_cell),
            Paragraph(f"{row['gross_margin_pct']:.1f}%", margin_style),
            Paragraph(f"${row['opex_b']:.1f}", table_cell),
            Paragraph(f"${row['operating_profit_b']:.1f}", margin_style),
            Paragraph(f"<b>{row['operating_margin_pct']:.2f}%</b>", margin_style),
            Paragraph(f"{row['ops_air_freight_share_pct']:.1f}%", margin_style if is_crisis else table_cell),
            Paragraph(f"${row['hr_contractor_spend_b']:.2f}", margin_style if is_crisis else table_cell),
            Paragraph(f"${row['mkt_trade_in_subsidy_usd']:.0f}", margin_style if is_crisis else table_cell)
        ])
        
    t_audit = Table(audit_table_data, colWidths=[54, 48, 48, 46, 46, 56, 56, 48, 54, 48])
    t_audit.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1d1d1f")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#fbfbfd")]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#d2d2d7")),
    ]))
    # Quick fix for text color in header
    for c in range(len(audit_table_data[0])):
        t_audit.setStyle(TableStyle([('TEXTCOLOR', (c,0), (c,0), colors.white)]))
        audit_table_data[0][c] = Paragraph(f"<font color='white'><b>{audit_table_data[0][c]}</b></font>", table_cell_bold)
        
    elements.append(t_audit)
    elements.append(Paragraph("<font size='6.5' color='#86868b'>* Highlighted crisis quarters indicate consecutive margin deterioration despite robust top-line revenues.</font>", body_style))
    elements.append(Spacer(1, 8))
    
    # -------------------------------------------------------------------------
    # SECTION 3: THE SILO PARADOX DEEP-DIVE & VMDI AUDIT
    # -------------------------------------------------------------------------
    elements.append(PageBreak())
    elements.append(Paragraph("3. Departmental Silo Paradox & Vanity Metric Distortion Index (VMDI)", h1_style))
    elements.append(Paragraph(
        "To measure the disconnect between departmental self-assessment and enterprise reality, the AI Analyst computed the "
        "<b>Vanity Metric Distortion Index (VMDI)</b> on a 1-to-10 scale. A high VMDI indicates that a department celebrated "
        "satisfactory local performance while causing severe downstream financial destruction.",
        body_style
    ))
    
    silo_table_data = [
        [
            Paragraph("<font color='white'><b>Department</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Reported Metric</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Reported Status</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Hidden Causal Distortion</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Enterprise Margin Hit</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Leakage ($B)</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>VMDI</b></font>", table_cell_bold),
        ]
    ]
    
    for d in silo_data["departments"]:
        silo_table_data.append([
            Paragraph(f"<b>{d['department']}</b>", table_cell_bold),
            Paragraph(f"{d['reported_kpi']}<br/><font color='#666'>Value: {d['reported_value']}</font>", table_cell),
            Paragraph(f"{d['reported_status']}", table_cell_green if "GREEN" in d['reported_status'] else table_cell),
            Paragraph(f"<b>{d['hidden_transmission_driver']}</b><br/><font color='#666'>{d['hidden_driver_metric']}</font>", table_cell),
            Paragraph(f"<b>{d['true_enterprise_margin_impact_bps']} bps</b>", table_cell_red),
            Paragraph(f"<b>${d['annualized_financial_leakage_b']:.2f}B</b>", table_cell_red),
            Paragraph(f"<b>{d['vmdi_score']}/10</b>", table_cell_bold)
        ])
        
    t_silo = Table(silo_table_data, colWidths=[70, 78, 65, 145, 56, 50, 40])
    t_silo.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1d1d1f")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#d2d2d7")),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#fbfbfd")]),
    ]))
    elements.append(t_silo)
    elements.append(Spacer(1, 8))
    
    # Embed Chart 3: Silo Leakage Bars
    elements.append(Image(chart_paths["p3"], width=504, height=200))
    elements.append(Spacer(1, 10))
    
    # Embed Chart 2: Waterfall Decomposition
    elements.append(Paragraph("4. Causal Margin Waterfall Decomposition (-912 bps)", h1_style))
    elements.append(Paragraph(
        "The AI attribution model deconstructed the net 912 basis point operating margin collapse between baseline (31.46%) "
        "and crisis trough (22.34%) into 5 distinct transmission components:",
        body_style
    ))
    elements.append(Image(chart_paths["p2"], width=504, height=225))
    elements.append(Spacer(1, 8))
    
    # Detailed Waterfall Bullet Points
    for comp in engine.waterfall_breakdown["components"]:
        elements.append(Paragraph(
            f"• <b>{comp['category']} ({comp['department']}):</b> "
            f"<font color='#ff3b30'><b>{comp['bps_impact']} bps</b> (${comp['cost_leakage_b']:.2f}B Leakage)</font> — {comp['explanation']}",
            bullet_style
        ))
        
    # -------------------------------------------------------------------------
    # SECTION 4: CROSS-FUNCTIONAL TRANSMISSION MATRIX & TIME LAGS
    # -------------------------------------------------------------------------
    elements.append(PageBreak())
    elements.append(Paragraph("5. Cross-Functional Transmission & Inter-Departmental Contagion", h1_style))
    elements.append(Paragraph(
        "Isolated departmental analysis failed because decisions in Marketing propagated into Operations and HR with 30-to-60 day "
        "lags. The correlation matrix below illustrates that Marketing's Trade-In Spikes (+0.88 correlation with Air Freight) and "
        "HR's Silicon Attrition (+0.92 correlation with Contractor Spend) directly drove Operating Margin collapse (-0.91 correlation).",
        body_style
    ))
    elements.append(Image(chart_paths["p4"], width=504, height=235))
    elements.append(Spacer(1, 10))
    
    elements.append(Paragraph("<b>Econometric Marginal Elasticity Profile:</b>", h2_style))
    elements.append(Paragraph(
        "Using gradient boosted regression models ($R^2 = 0.94$), the AI Analyst calculated the marginal enterprise sensitivity "
        "for every 1-unit operational shift:",
        body_style
    ))
    
    elasticity_table_data = [
        [
            Paragraph("<font color='white'><b>Operational Indicator</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Department</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Marginal Shift (+1 Unit)</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Operating Margin Shift</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Quarterly EBITDA Impact</b></font>", table_cell_bold),
        ]
    ]
    
    for feat, el in list(engine.elasticities.items())[:6]:
        elasticity_table_data.append([
            Paragraph(f"<b>{el['label']}</b>", table_cell_bold),
            Paragraph(f"{el['department']}", table_cell),
            Paragraph(f"+1.0 {el['unit']}", table_cell),
            Paragraph(f"<font color='{'#ff3b30' if el['bps_impact_per_unit'] < 0 else '#28a745'}'><b>{el['bps_impact_per_unit']:+.1f} bps</b></font>", table_cell),
            Paragraph(f"<font color='{'#ff3b30' if el['ebitda_impact_m_per_unit'] < 0 else '#28a745'}'><b>${el['ebitda_impact_m_per_unit']:+.1f}M</b></font>", table_cell_bold)
        ])
        
    t_elasticity = Table(elasticity_table_data, colWidths=[150, 80, 90, 94, 90])
    t_elasticity.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1d1d1f")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#d2d2d7")),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#fbfbfd")]),
    ]))
    elements.append(t_elasticity)
    elements.append(Spacer(1, 12))
    
    # -------------------------------------------------------------------------
    # SECTION 5: PRESCRIPTIVE BOARD STRATEGIC PROTOCOLS
    # -------------------------------------------------------------------------
    elements.append(Paragraph("6. Prescriptive Board Strategic Protocols (Alpha to Epsilon)", h1_style))
    elements.append(Paragraph(
        "To reverse the 3-quarter margin decline and restore Apple's operating margin above 30.5%, the AI Business Analyst "
        "engineered 5 integrated cross-functional protocols delivering <b>$7.88 Billion in Annualized EBITDA Recovery</b> "
        "against <b>$235 Million in Capital Investment</b> (Enterprise Payback: <b>2.8 Months</b>).",
        body_style
    ))
    
    elements.append(Image(chart_paths["p5"], width=504, height=200))
    elements.append(Spacer(1, 10))
    
    # Protocols Table
    proto_table_data = [
        [
            Paragraph("<font color='white'><b>Code & Protocol</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Owner</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Core Mechanism</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Capex ($M)</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Annual EBITDA ($B)</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Margin Gain</b></font>", table_cell_bold),
            Paragraph("<font color='white'><b>Payback</b></font>", table_cell_bold)
        ]
    ]
    
    for p in protocols:
        proto_table_data.append([
            Paragraph(f"<b>{p['code']}</b><br/>{p['name']}", table_cell_bold),
            Paragraph(f"{p['department']}<br/><font color='#666'>{p['executive_sponsor']}</font>", table_cell),
            Paragraph(f"{p['action_mechanism']}", table_cell),
            Paragraph(f"${p['capex_m']:.1f}M", table_cell),
            Paragraph(f"<b>+${p['annual_ebitda_gain_b']:.2f}B</b>", table_cell_green),
            Paragraph(f"<b>+{p['margin_recovery_bps']} bps</b>", table_cell_green),
            Paragraph(f"<b>{p['payback_months']} mo</b>", table_cell_bold)
        ])
        
    t_proto = Table(proto_table_data, colWidths=[80, 80, 160, 44, 52, 48, 40])
    t_proto.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1d1d1f")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#d2d2d7")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor("#ffffff"), colors.HexColor("#fbfbfd")]),
    ]))
    elements.append(t_proto)
    elements.append(Spacer(1, 12))
    
    # -------------------------------------------------------------------------
    # SECTION 6: BOARD RECOMMENDATIONS & GOVERNANCE OKRS
    # -------------------------------------------------------------------------
    elements.append(Paragraph("7. Governance Framework: Banishing Departmental Vanity Blindspots", h1_style))
    elements.append(Paragraph(
        "To permanently eradicate the Silo Paradox, the Board of Directors must enact three structural governance reforms:",
        body_style
    ))
    elements.append(Paragraph(
        "1. <b>Incorporate VMDI into Departmental Executive Compensation:</b> Department heads shall no longer receive bonuses "
        "solely for local KPI attainment (e.g. CAC, Headcount, or OTIF) if their actions export net negative EBITDA to partner divisions. "
        "Every departmental OKR must include a cross-functional friction penalty.",
        bullet_style
    ))
    elements.append(Paragraph(
        "2. <b>Institute Real-Time Causal Telemetry in Place of 45-Day Post-Close Reviews:</b> Finance must deploy the AI Business Analyst "
        "telemetry pipeline to track weekly modal freight shifts, contractor billings, and promotional ASP dilutions in real time, "
        "enabling immediate course correction within the active operational quarter.",
        bullet_style
    ))
    elements.append(Paragraph(
        "3. <b>Immediate Execution of Protocols Alpha & Beta:</b> Prioritize the logistics modal shift (saving $2.21B) and silicon talent "
        "in-sourcing (saving $1.77B), which together account for more than 50% of the entire 3-quarter profitability decline.",
        bullet_style
    ))
    
    # Signature block
    elements.append(Spacer(1, 15))
    sig_data = [
        [
            Paragraph("<b>Diagnostic Certified by:</b><br/>AI Enterprise Business Analyst System<br/>Special Investigation Unit", table_cell),
            Paragraph("<b>Presented To:</b><br/>Apple Inc. Executive Committee<br/>& Board of Directors", table_cell),
            Paragraph("<b>Authorization Status:</b><br/><font color='#28a745'><b>APPROVED FOR BOARD ACTION</b></font><br/>Immediate Implementation", table_cell)
        ]
    ]
    t_sig = Table(sig_data, colWidths=[168, 168, 168])
    t_sig.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#0071e3")),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f5f5f7")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    elements.append(t_sig)

    # Build Document
    doc.build(elements, canvasmaker=NumberedCanvas)
    print(f"Executive PDF Report successfully generated -> {output_pdf}")
    print(f"File Size: {os.path.getsize(output_pdf) / 1024:.1f} KB")
    return output_pdf

if __name__ == "__main__":
    build_pdf_report()

