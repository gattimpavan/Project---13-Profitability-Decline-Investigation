"""
Apple Inc. - Strategic What-If Counterfactual Scenario Simulator
Project - 13: Profitability Decline Investigation

Enables the Board of Directors and Executive Leadership to simulate 
cross-functional interventions to reverse the 3-quarter profitability decline.

Levers:
1. Air Freight Reduction (Modal shift to maritime logistics)
2. Silicon In-sourcing & Contractor Spend Rationalization
3. Trade-In Subsidy Cap & High-Margin SKU Mix Balancing
4. Lean Inventory Optimization (Reducing DIO from ~70 to ~38 days)
5. Overtime & Assembly Shift Smoothing
"""

import os
import numpy as np

class ScenarioSimulator:
    def __init__(self, causal_engine=None):
        self.causal_engine = causal_engine
        
    def simulate(self, 
                 air_freight_reduction_pct=50.0, 
                 contractor_insourcing_pct=60.0, 
                 trade_in_cap_pct=50.0, 
                 inventory_dio_reduction_days=25.0, 
                 overtime_reduction_pct=50.0):
        """
        Simulates financial recovery based on input intervention parameters.
        Parameters range between 0% and 100% (or days for DIO).
        """
        # Baseline Crisis Peak Figures (Annualized or Run-Rate, $B)
        baseline_air_freight_leakage = 2.45
        baseline_contractor_leakage = 1.82
        baseline_trade_in_leakage = 1.95
        baseline_inventory_leakage = 1.64
        baseline_overtime_leakage = 1.24
        
        # 1. Freight Recovery
        # 100% reduction in air freight excess saves $2.45B
        freight_savings = (air_freight_reduction_pct / 100.0) * baseline_air_freight_leakage * 0.90
        freight_bps = (freight_savings / 100.0) * 10000.0 / 4.0 # approximate quarterly bps on $100B revenue
        
        # 2. Contractor In-sourcing Recovery
        # In-sourcing costs about 40% of external agency billing (saving 60% of targeted portion)
        gross_contractor_savings = (contractor_insourcing_pct / 100.0) * baseline_contractor_leakage
        net_contractor_savings = gross_contractor_savings * 0.65 # net of internal salary & equity
        contractor_bps = (net_contractor_savings / 100.0) * 10000.0 / 4.0
        
        # 3. Trade-In & Mix Balancing Recovery
        trade_in_savings = (trade_in_cap_pct / 100.0) * baseline_trade_in_leakage * 0.85
        trade_in_bps = (trade_in_savings / 100.0) * 10000.0 / 4.0
        
        # 4. Inventory Holding & Write-down Recovery
        # Target DIO reduction is ~31.5 days (from 69.5 to 38 days)
        dio_ratio = np.clip(inventory_dio_reduction_days / 31.5, 0.0, 1.0)
        inventory_savings = dio_ratio * baseline_inventory_leakage * 0.80
        inventory_bps = (inventory_savings / 100.0) * 10000.0 / 4.0
        
        # 5. Overtime Smoothing
        overtime_savings = (overtime_reduction_pct / 100.0) * baseline_overtime_leakage * 0.75
        overtime_bps = (overtime_savings / 100.0) * 10000.0 / 4.0
        
        # Total Financial Accretion
        total_annual_ebitda_gain_b = float(np.round(
            freight_savings + net_contractor_savings + trade_in_savings + inventory_savings + overtime_savings, 2
        ))
        
        total_operating_margin_bps = int(round(
            freight_bps + contractor_bps + trade_in_bps + inventory_bps + overtime_bps
        ))
        
        # Capital / Implementation Investment required ($M)
        # TMS software + In-sourcing signing bonuses + Inventory analytics platform
        capex_freight_m = 35.0 * (air_freight_reduction_pct / 100.0)
        capex_insource_m = 120.0 * (contractor_insourcing_pct / 100.0) # talent acquisition & retention pool
        capex_promo_m = 15.0 # promo engine governance
        capex_inventory_m = 40.0 * dio_ratio # predictive demand sensing
        total_capex_m = float(np.round(capex_freight_m + capex_insource_m + capex_promo_m + capex_inventory_m, 1))
        
        # Payback in months
        monthly_ebitda_gain_m = (total_annual_ebitda_gain_b * 1000.0) / 12.0
        payback_months = float(np.round(total_capex_m / max(monthly_ebitda_gain_m, 0.1), 1))
        
        # Post-intervention Operating Margin (from 22.3% crisis peak)
        recovered_operating_margin_pct = float(np.round(22.34 + (total_operating_margin_bps / 100.0), 2))
        
        return {
            "inputs": {
                "air_freight_reduction_pct": air_freight_reduction_pct,
                "contractor_insourcing_pct": contractor_insourcing_pct,
                "trade_in_cap_pct": trade_in_cap_pct,
                "inventory_dio_reduction_days": inventory_dio_reduction_days,
                "overtime_reduction_pct": overtime_reduction_pct
            },
            "total_annual_ebitda_recovery_b": total_annual_ebitda_gain_b,
            "margin_expansion_bps": total_operating_margin_bps,
            "new_operating_margin_pct": recovered_operating_margin_pct,
            "capital_investment_required_m": total_capex_m,
            "payback_period_months": payback_months,
            "levers_breakdown": [
                {
                    "lever": "Maritime Logistics Modal Shift",
                    "department": "Operations",
                    "savings_b": float(np.round(freight_savings, 2)),
                    "margin_bps": int(round(freight_bps)),
                    "color": "#0071e3"
                },
                {
                    "lever": "Silicon Talent In-Sourcing",
                    "department": "HR",
                    "savings_b": float(np.round(net_contractor_savings, 2)),
                    "margin_bps": int(round(contractor_bps)),
                    "color": "#30b0c7"
                },
                {
                    "lever": "Trade-In & Mix Balancing",
                    "department": "Marketing",
                    "savings_b": float(np.round(trade_in_savings, 2)),
                    "margin_bps": int(round(trade_in_bps)),
                    "color": "#ff9f0a"
                },
                {
                    "lever": "Lean Inventory Buffer",
                    "department": "Operations / Finance",
                    "savings_b": float(np.round(inventory_savings, 2)),
                    "margin_bps": int(round(inventory_bps)),
                    "color": "#34c759"
                },
                {
                    "lever": "Assembly Shift Smoothing",
                    "department": "Operations / HR",
                    "savings_b": float(np.round(overtime_savings, 2)),
                    "margin_bps": int(round(overtime_bps)),
                    "color": "#af52de"
                }
            ]
        }

if __name__ == "__main__":
    sim = ScenarioSimulator()
    res = sim.simulate()
    print("Scenario Simulator Test:")
    print(f"EBITDA Gain: ${res['total_annual_ebitda_recovery_b']}B | Margin Accretion: +{res['margin_expansion_bps']} bps")
    print(f"Payback: {res['payback_period_months']} Months")

