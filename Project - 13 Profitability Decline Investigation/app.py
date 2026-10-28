"""
Apple Inc. - Executive Decision Intelligence Engine
Flask Application & REST API Server (Port 5013)
Project - 13: Profitability Decline Investigation

Serves:
- Executive Cupertino Glassmorphic Profitability Diagnostic Dashboard
- Departmental Silo Paradox vs Enterprise Reality Engine
- Real-Time Counterfactual Scenario What-If Simulator
- Grounded AI Business Analyst Natural Language Terminal
- 5 Prescriptive Board Strategic Protocols (Alpha to Epsilon)
- Publication-Grade High-Resolution PDF Report Generator & Download
"""

import os
import sys
import json
from flask import Flask, render_template, jsonify, request, send_file

# Set environment variable to silence loky warnings
os.environ["LOKY_MAX_CPU_COUNT"] = "4"

# Add project root to sys.path
base_dir = os.path.dirname(os.path.abspath(__file__))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from data.generate_apple_cross_functional_data import generate_apple_cross_functional_dataset
from models.causal_attribution_engine import CausalAttributionEngine
from models.silo_paradox_analyzer import SiloParadoxAnalyzer
from models.scenario_simulator import ScenarioSimulator
from models.ai_business_analyst_agent import AIBusinessAnalystAgent
from report.generate_pdf_report import build_pdf_report

app = Flask(__name__, static_folder="static", template_folder="templates")

DATA_DIR = os.path.join(base_dir, "data")
CSV_PATH = os.path.join(DATA_DIR, "apple_cross_functional_quarterly_data.csv")
MONTHLY_CSV_PATH = os.path.join(DATA_DIR, "apple_monthly_telemetry_data.csv")
REPORT_PATH = os.path.join(base_dir, "report", "Apple_Profitability_Decline_Investigation_Report.pdf")

# Step 1: Ensure dataset exists
if not os.path.exists(CSV_PATH) or not os.path.exists(MONTHLY_CSV_PATH):
    print("[INIT] Generating enterprise cross-functional telemetry datasets...")
    generate_apple_cross_functional_dataset(output_dir=DATA_DIR)

# Step 2: Initialize Analytical Engines
print("[INIT] Loading AI Causal Attribution & Silo Engines...")
causal_engine = CausalAttributionEngine(data_path=CSV_PATH, monthly_path=MONTHLY_CSV_PATH)
silo_analyzer = SiloParadoxAnalyzer(data_path=CSV_PATH)
scenario_simulator = ScenarioSimulator(causal_engine=causal_engine)
analyst_agent = AIBusinessAnalystAgent(causal_engine, silo_analyzer, scenario_simulator)

# Step 3: Ensure pre-compiled PDF report exists
if not os.path.exists(REPORT_PATH):
    print("[INIT] Pre-compiling executive PDF deliverable...")
    build_pdf_report(CSV_PATH, REPORT_PATH)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/summary", methods=["GET"])
def get_summary():
    """
    Returns high-level summary metrics, 16-quarter telemetry, waterfall breakdown, and elasticities.
    """
    quarterly_data = causal_engine.df_quarterly.to_dict(orient="records")
    return jsonify({
        "quarterly_telemetry": quarterly_data,
        "waterfall": causal_engine.waterfall_breakdown,
        "importance_rankings": causal_engine.importance_rankings,
        "elasticities": causal_engine.elasticities
    })

@app.route("/api/silo-paradox", methods=["GET"])
def get_silo_paradox():
    """
    Returns the Departmental Silo Paradox vs True Enterprise Reality analysis.
    """
    paradox_data = silo_analyzer.analyze_paradox()
    return jsonify(paradox_data)

@app.route("/api/correlations", methods=["GET"])
def get_correlations():
    """
    Returns cross-functional correlation matrix and monthly transmission lag analysis.
    """
    corr_matrix = causal_engine.get_cross_functional_correlation_matrix()
    monthly_lags = causal_engine.get_monthly_transmission_lags()
    return jsonify({
        "correlation_matrix": corr_matrix,
        "monthly_lags": monthly_lags
    })

@app.route("/api/simulate", methods=["POST"])
def run_simulation():
    """
    Simulates counterfactual Board recovery levers in real time.
    """
    payload = request.get_json() or {}
    air_freight = float(payload.get("air_freight_reduction_pct", 50.0))
    contractors = float(payload.get("contractor_insourcing_pct", 60.0))
    trade_in = float(payload.get("trade_in_cap_pct", 50.0))
    inventory = float(payload.get("inventory_dio_reduction_days", 25.0))
    overtime = float(payload.get("overtime_reduction_pct", 50.0))

    sim_result = scenario_simulator.simulate(
        air_freight_reduction_pct=air_freight,
        contractor_insourcing_pct=contractors,
        trade_in_cap_pct=trade_in,
        inventory_dio_reduction_days=inventory,
        overtime_reduction_pct=overtime
    )
    return jsonify(sim_result)

@app.route("/api/ask-analyst", methods=["POST"])
def ask_analyst():
    """
    Natural language query interface to the grounded AI Business Analyst agent.
    """
    payload = request.get_json() or {}
    query = payload.get("query", "")
    response = analyst_agent.answer_query(query)
    return jsonify(response)

@app.route("/api/protocols", methods=["GET"])
def get_protocols():
    """
    Returns the 5 Prescriptive Board Strategic Protocols (Alpha to Epsilon).
    """
    protocols = analyst_agent.get_prescriptive_protocols()
    return jsonify(protocols)

@app.route("/download-report", methods=["GET"])
def download_report():
    """
    Transfers the publication-grade PDF report directly to the client.
    """
    if not os.path.exists(REPORT_PATH):
        build_pdf_report(CSV_PATH, REPORT_PATH)
    return send_file(
        REPORT_PATH,
        as_attachment=True,
        download_name="Apple_Profitability_Decline_Investigation_Report.pdf",
        mimetype="application/pdf"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5013))
    print(f"Starting Apple Decision Intelligence Server on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)

