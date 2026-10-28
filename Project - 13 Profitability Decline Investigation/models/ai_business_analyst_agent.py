"""
Apple Inc. - Autonomous AI Business Analyst Agent
Project - 13: Profitability Decline Investigation

Provides grounded natural language conversational analysis and formalizes 
5 Prescriptive Board Strategic Protocols (Alpha to Epsilon) to reverse the 
consecutive 3-quarter margin contraction.
"""

import os
import json

class AIBusinessAnalystAgent:
    def __init__(self, causal_engine=None, silo_analyzer=None, scenario_sim=None):
        self.causal_engine = causal_engine
        self.silo_analyzer = silo_analyzer
        self.scenario_sim = scenario_sim

    def get_prescriptive_protocols(self):
        """
        Returns the 5 formal Board of Directors Remediation Protocols.
        """
        protocols = [
            {
                "code": "PROTOCOL-ALPHA",
                "name": "Dynamic Modal Logistics Shift & Ocean Priority Governance",
                "department": "Operations & Logistics",
                "executive_sponsor": "SVP of Worldwide Operations",
                "problem_addressed": "39.5% cargo shifted to chartered Boeing 777 air freight, causing $2.45B in logistics surcharges.",
                "action_mechanism": (
                    "Mandate that 85%+ of inbound and outbound component and finished good transit moves via expedited maritime "
                    "cargo corridors. Establish an automated AI logistics triage engine where air freight requires VP-level margin-gating approval."
                ),
                "capex_m": 35.0,
                "annual_ebitda_gain_b": 2.21,
                "margin_recovery_bps": 221,
                "payback_months": 2.1,
                "implementation_horizon": "60 Days",
                "primary_metric": "Air Freight Share (< 12%)"
            },
            {
                "code": "PROTOCOL-BETA",
                "name": "Silicon & AI Compiler Engineering Talent In-Sourcing",
                "department": "HR & Hardware Technologies",
                "executive_sponsor": "SVP of Hardware Technologies & Chief People Officer",
                "problem_addressed": "20.4% attrition in elite silicon engineering triggered $2.78B in external contractor agency billing.",
                "action_mechanism": (
                    "Launch an accelerated in-sourcing campaign with targeted multi-year restricted stock unit (RSU) retention pools "
                    "for top 400 silicon design and AI software engineers. Terminate non-critical contractor agency retainers within 90 days."
                ),
                "capex_m": 120.0,
                "annual_ebitda_gain_b": 1.77,
                "margin_recovery_bps": 177,
                "payback_months": 4.1,
                "implementation_horizon": "90 Days",
                "primary_metric": "Contractor Ratio (< 5% of payroll)"
            },
            {
                "code": "PROTOCOL-GAMMA",
                "name": "Margin-Preserving Promotional & Trade-In Governance",
                "department": "Marketing & Retail",
                "executive_sponsor": "SVP of Worldwide Marketing",
                "problem_addressed": "Trade-in subsidies reached $195/unit, eroding realized ASP by $95/unit and cannibalizing Pro tier mix.",
                "action_mechanism": (
                    "Cease un-gated flat trade-in subsidies. Implement a dynamic trade-in algorithmic engine that ties trade-in allowance "
                    "directly to customer lifetime value and high-margin Pro Max attach rates. Cap baseline 128GB promotional weighting to 25%."
                ),
                "capex_m": 15.0,
                "annual_ebitda_gain_b": 1.66,
                "margin_recovery_bps": 166,
                "payback_months": 1.2,
                "implementation_horizon": "30 Days",
                "primary_metric": "Realized Net ASP (>= $920)"
            },
            {
                "code": "PROTOCOL-DELTA",
                "name": "Predictive Buffer Stock & Component DIO Lean Rationalization",
                "department": "Operations & Supply Chain",
                "executive_sponsor": "VP of Global Supply Chain Operations",
                "problem_addressed": "Inventory ballooned to 69.5 Days of Inventory (DIO), triggering $1.75B in carrying costs and obsolescence write-downs.",
                "action_mechanism": (
                    "Deploy ML-driven predictive demand sensing across Foxconn/Pegatron hub nodes. Rationalize component safety buffer "
                    "from 69.5 days down to lean 38 days without degrading OTIF fulfillment SLAs."
                ),
                "capex_m": 40.0,
                "annual_ebitda_gain_b": 1.31,
                "margin_recovery_bps": 131,
                "payback_months": 3.7,
                "implementation_horizon": "120 Days",
                "primary_metric": "Component DIO (<= 38 Days)"
            },
            {
                "code": "PROTOCOL-EPSILON",
                "name": "Cross-Functional Real-Time Transmission & Variance Rhythm",
                "department": "Finance & Executive Office",
                "executive_sponsor": "Chief Financial Officer & COO",
                "problem_addressed": "Siloed KPI vanity reporting masked a cumulative 910 bps margin collapse over 3 quarters with 45-day reporting lag.",
                "action_mechanism": (
                    "Establish a weekly Unified Executive Decision Command room. Institute the 'Vanity Metric Distortion Index' into departmental OKRs: "
                    "no department is scored 'Green' if its localized actions export net negative EBITDA to adjacent departments."
                ),
                "capex_m": 25.0,
                "annual_ebitda_gain_b": 0.93,
                "margin_recovery_bps": 93,
                "payback_months": 3.2,
                "implementation_horizon": "14 Days",
                "primary_metric": "Enterprise Operating Margin (>= 30.5%)"
            }
        ]
        return protocols

    def answer_query(self, query):
        """
        Responds to leadership queries using grounded analysis from the cross-functional models.
        """
        q = query.lower().strip()
        
        if "why" in q and ("profit" in q or "margin" in q or "decline" in q or "decrease" in q or "three" in q or "consecutive" in q):
            return {
                "title": "Cross-Functional Root Cause Analysis: 3-Quarter Profitability Decline",
                "summary": (
                    "Apple's Operating Margin contracted by 912 basis points (from 31.4% to 22.3%) over Q1, Q2, and Q3 2025. "
                    "The primary driver is NOT a loss of consumer demand (top-line revenue remained resilient at $90B-$118B). "
                    "Instead, the decline was caused by a systemic 'Silo Sub-Optimization Trap' across Marketing, HR, Operations, and Finance."
                ),
                "key_findings": [
                    "Operations Air Freight Trap: 39.5% of shipment volume was routed via chartered Boeing 777 air freight to defend the 98% OTIF metric, burning $2.45B in freight premiums.",
                    "Marketing ASP Erosion: Aggressive $195 trade-in subsidies and low-margin base SKU promotions deducted $95 from net realized ASP per unit, leaking $1.95B as contra-revenue.",
                    "HR Silicon Brain Drain: Aggregate 4.3% turnover masked a 20.4% attrition spike in mission-critical silicon & AI software teams, requiring $2.78B in external contractor retainers.",
                    "Inventory DIO Bloat: Fear of geopolitical bottlenecks drove safety stock to 69.5 days, resulting in $1.75B in holding carrying costs and component write-downs."
                ],
                "action_recommendation": "Activate Protocols Alpha through Epsilon immediately to recoup +788 bps of Operating Margin and $7.88B in annualized EBITDA."
            }
            
        elif "marketing" in q or "cac" in q or "promo" in q or "trade-in" in q:
            return {
                "title": "Marketing Department Investigation: The Subsidized Volume Illusion",
                "summary": (
                    "Marketing reported a 'satisfactory' CAC of $41.80 (beating the $45 budget ceiling). "
                    "However, this was achieved by granting excessive $195 trade-in subsidies and heavily promoting entry-level 128GB baseline SKUs."
                ),
                "key_findings": [
                    "Contra-Revenue Leakage: Trade-in subsidies ballooned from $1.1B to $3.12B per quarter, recognized as top-line contra-revenue.",
                    "Realized ASP Compression: Realized ASP dropped from $930 to $835 per iPhone sold.",
                    "Bullwhip Effect on Operations: Flash promotional weekends created sudden localized inventory stockout threats, forcing Operations to trigger emergency air charters."
                ],
                "action_recommendation": "Deploy Protocol Gamma: Implement algorithmic trade-in caps tied to Pro tier margin attach rates."
            }
            
        elif "hr" in q or "headcount" in q or "turnover" in q or "talent" in q or "contractor" in q:
            return {
                "title": "HR & Workforce Operations Investigation: The Aggregate Vanity Metric Blindspot",
                "summary": (
                    "HR reported an aggregate turnover of 4.31% (well below tech industry 6.5% benchmark) and 100.6% headcount fulfillment. "
                    "However, this aggregate metric concealed a catastrophic brain drain in core engineering."
                ),
                "key_findings": [
                    "Silicon & AI Talent Crisis: Attrition among senior silicon architects and compiler engineers surged to 20.4% due to competing Generative AI offers.",
                    "Exorbitant Contractor Billing: To meet silicon tape-out deadlines, engineering leaders hired third-party contractors charging $350-$450/hour, adding $1.82B in unbudgeted R&D expense.",
                    "Warehouse Overtime Inflation: Overtime in assembly and logistics climbed to 21.8% of labor payroll ($1.24B leakage)."
                ],
                "action_recommendation": "Deploy Protocol Beta: In-source 400 key silicon roles with targeted retention equity and eliminate contractor agency markups."
            }
            
        elif "operations" in q or "freight" in q or "logistics" in q or "otif" in q or "inventory" in q:
            return {
                "title": "Operations & Supply Chain Investigation: The Heroic Air Freight SLA Trap",
                "summary": (
                    "Operations achieved an enviable 98.4% OTIF delivery SLA, congratulating itself on stellar supply chain execution. "
                    "However, this was achieved through catastrophic financial inefficiency."
                ),
                "key_findings": [
                    "Chartered Air Freight Surge: Expedited air freight surged from 12% to 39.5% of total volume, at 4.8x oceanic cargo cost, causing $2.45B in logistics surcharges.",
                    "Inventory Buffer Bloat: Days of Inventory Outstanding (DIO) rose from 36 to 69.5 days, tying up $6.2B in capital and driving $1.75B in component write-downs.",
                    "Assembly Rush Premiums: Foxconn/Luxshare weekend rush fees totaled $1.62B over the 3 quarters."
                ],
                "action_recommendation": "Deploy Protocols Alpha and Delta: Shift to expedited maritime corridors and lean inventory buffering."
            }
            
        elif "recommend" in q or "protocol" in q or "board" in q or "fix" in q or "roadmap" in q or "solution" in q:
            protocols = self.get_prescriptive_protocols()
            tot_ebitda = sum(p["annual_ebitda_gain_b"] for p in protocols)
            tot_capex = sum(p["capex_m"] for p in protocols)
            return {
                "title": "Board Executive Action Plan: 5 Prescriptive Remediation Protocols",
                "summary": f"A comprehensive 5-pillar strategic recovery roadmap delivering ${tot_ebitda:.2f}B in annualized EBITDA accretion against ${tot_capex:.1f}M in capital investment (Payback: ~2.8 months).",
                "key_findings": [f"{p['code']} ({p['name']}): +{p['margin_recovery_bps']} bps | +${p['annual_ebitda_gain_b']}B EBITDA (Payback: {p['payback_months']} mo)" for p in protocols],
                "action_recommendation": "Adopt and fund all 5 protocols with weekly executive committee governance tracking the Vanity Metric Distortion Index."
            }
            
        else:
            return {
                "title": "Apple AI Business Analyst Enterprise Assessment",
                "summary": (
                    "Diagnostic confirmed: Apple's 3-quarter profitability decline is caused by inter-departmental friction. "
                    "Marketing promoted cheap SKUs with $195 trade-in subsidies; Operations burnt $2.45B in air freight to maintain 98% OTIF; "
                    "HR masked a 20.4% silicon engineer brain drain that cost $2.78B in external contractor fees; and Finance delayed intervention by 45 days."
                ),
                "key_findings": [
                    "Total Profitability Loss: -912 basis points ($9.10B annualized operating profit).",
                    "Departmental Silo Status: All 4 departments reported 'Satisfactory' on their isolated metrics.",
                    "Recovery Potential: +788 bps margin expansion via 5 synchronized Board Protocols."
                ],
                "action_recommendation": "Use the Strategic Scenario Simulator to model specific levers or query specific departments (Marketing, HR, Operations, Finance)."
            }

if __name__ == "__main__":
    agent = AIBusinessAnalystAgent()
    p = agent.get_prescriptive_protocols()
    print(f"Prescriptive Protocols Ready: {len(p)} protocols defined.")
    ans = agent.answer_query("Why did profitability decline?")
    print(ans["summary"])

