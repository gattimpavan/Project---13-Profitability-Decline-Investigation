"""
Apple Inc. - Enterprise Cross-Functional Telemetry & Financial Synthesis
Project - 13: Profitability Decline Investigation

Generates high-fidelity synthetic enterprise telemetry across Marketing, HR, 
Operations, and Finance spanning 16 Quarters (Q1 2022 to Q4 2025) and 48 Months.
Explicitly models the 'Silo Paradox' and cross-functional causal transmissions:
- Marketing flash promotions & trade-in subsidies -> Realized ASP erosion & Air Freight surge
- HR silicon talent attrition -> Emergency external contractor spend inflation & overtime
- Operations safety buffer bloat -> Inventory carrying costs & obsolescence write-downs
- Finance margin compression across 3 consecutive quarters despite green departmental KPIs
"""

import os
import numpy as np
import pandas as pd

def generate_apple_cross_functional_dataset(output_dir=None):
    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)
    
    np.random.seed(42)
    
    # -------------------------------------------------------------------------
    # 1. Quarterly Telemetry (16 Quarters: 2022 Q1 to 2025 Q4)
    # The 3 consecutive decline quarters are FY2025 Q1, Q2, and Q3
    # -------------------------------------------------------------------------
    quarters = [
        "2022-Q1", "2022-Q2", "2022-Q3", "2022-Q4",
        "2023-Q1", "2023-Q2", "2023-Q3", "2023-Q4",
        "2024-Q1", "2024-Q2", "2024-Q3", "2024-Q4",
        "2025-Q1", "2025-Q2", "2025-Q3", "2025-Q4"  # Q1-Q3 2025 = 3-quarter crisis period
    ]
    
    records = []
    
    # Baseline normal values
    for i, q in enumerate(quarters):
        is_crisis_q1 = (q == "2025-Q1")
        is_crisis_q2 = (q == "2025-Q2")
        is_crisis_q3 = (q == "2025-Q3")
        is_crisis_q4 = (q == "2025-Q4") # incipient stabilization or post-investigation
        is_crisis = is_crisis_q1 or is_crisis_q2 or is_crisis_q3
        
        # Quarter seasonality (Q1 is typically holiday launch peak)
        q_num = (i % 4) + 1
        seasonal_vol_mult = 1.35 if q_num == 1 else (0.95 if q_num == 2 else (0.90 if q_num == 3 else 1.15))
        
        # Base Revenue: ~90B - 120B
        base_rev = 88.0 * seasonal_vol_mult + np.random.uniform(-1.5, 2.0)
        
        if not is_crisis and not is_crisis_q4:
            # Normal historical quarters (2022-Q1 through 2024-Q4)
            # Marketing
            cac = float(np.round(np.random.uniform(43.5, 47.0), 2))
            ad_spend = float(np.round(base_rev * np.random.uniform(0.024, 0.028), 2))
            campaign_impressions = float(np.round(np.random.uniform(8.5, 10.2) * seasonal_vol_mult, 2))
            dtc_conversion_rate = float(np.round(np.random.uniform(3.2, 3.6), 2))
            trade_in_subsidy_per_unit = float(np.round(np.random.uniform(65.0, 85.0), 1))
            trade_in_spend = float(np.round(np.random.uniform(0.9, 1.3) * seasonal_vol_mult, 2))
            low_margin_sku_mix = float(np.round(np.random.uniform(28.0, 32.0), 1))
            brand_sentiment = float(np.round(np.random.uniform(86.0, 91.0), 1))
            
            # HR
            headcount_target_achievement = float(np.round(np.random.uniform(98.5, 101.5), 1))
            voluntary_turnover = float(np.round(np.random.uniform(3.8, 4.6), 2))
            silicon_eng_attrition = float(np.round(np.random.uniform(4.5, 6.5), 2))
            contractor_spend = float(np.round(np.random.uniform(0.85, 1.15), 2))
            overtime_hours_pct = float(np.round(np.random.uniform(6.5, 8.8), 2))
            time_to_hire_days = float(np.round(np.random.uniform(37.0, 43.0), 1))
            employee_satisfaction = float(np.round(np.random.uniform(4.1, 4.4), 2))
            sbc_amortization = float(np.round(np.random.uniform(2.5, 2.9), 2))
            
            # Operations
            otif_delivery_pct = float(np.round(np.random.uniform(98.1, 99.2), 2))
            air_freight_share_pct = float(np.round(np.random.uniform(11.0, 15.5), 1))
            logistics_freight_spend = float(np.round(np.random.uniform(1.1, 1.5) * seasonal_vol_mult, 2))
            factory_capacity_util = float(np.round(np.random.uniform(88.0, 93.0), 1))
            days_inventory_outstanding = float(np.round(np.random.uniform(34.0, 39.0), 1))
            buffer_write_downs = float(np.round(np.random.uniform(0.25, 0.45), 2))
            supplier_defect_rate = float(np.round(np.random.uniform(0.35, 0.48), 2))
            contract_mfg_rush_premiums = float(np.round(np.random.uniform(0.30, 0.55), 2))
            
            # Finance calculations
            revenue = float(np.round(base_rev, 2))
            # Healthy gross margin around 44.5% - 46.5%
            gross_margin_pct = float(np.round(np.random.uniform(44.8, 46.5), 2))
            gross_profit = float(np.round(revenue * (gross_margin_pct / 100.0), 2))
            cogs = float(np.round(revenue - gross_profit, 2))
            
            # Opex: ~14.0% - 15.0% of revenue
            rd_expense = float(np.round(revenue * np.random.uniform(0.075, 0.082), 2))
            sga_expense = float(np.round(revenue * np.random.uniform(0.065, 0.072), 2))
            opex = float(np.round(rd_expense + sga_expense, 2))
            
            operating_profit = float(np.round(gross_profit - opex, 2))
            operating_margin_pct = float(np.round((operating_profit / revenue) * 100.0, 2))
            
            tax_rate = 0.165
            net_profit = float(np.round(operating_profit * (1 - tax_rate), 2))
            net_margin_pct = float(np.round((net_profit / revenue) * 100.0, 2))
            
            realized_asp = float(np.round(np.random.uniform(910.0, 935.0), 1))
            cash_liquidity = float(np.round(np.random.uniform(155.0, 168.0), 1))
            
        else:
            # Crisis quarters: 2025-Q1, 2025-Q2, 2025-Q3 (and 2025-Q4 stabilization)
            # Departmental Vanity KPIs remain "GREEN" or "SATISFACTORY",
            # but cross-functional causal distortions balloon downstream costs.
            
            if is_crisis_q1:
                # Q1 2025: Massive holiday promotions launched to hit top-line volume
                revenue = float(np.round(118.4, 2)) # Record top-line! Looks great to uncritical eyes
                
                # Marketing: Looks fantastic on vanity metrics!
                cac = 41.8  # "Under budget! Efficient!"
                ad_spend = 3.65
                campaign_impressions = 14.2
                dtc_conversion_rate = 3.65
                brand_sentiment = 88.5
                # The hidden drivers:
                trade_in_subsidy_per_unit = 168.0 # Aggressive $170 trade-in bump
                trade_in_spend = 3.12 # Surged
                low_margin_sku_mix = 41.5 # Shifted mix toward cheap baseline 128GB SKUs
                
                # HR: Satisfactory vanity metrics!
                headcount_target_achievement = 101.4 # "All positions filled!"
                voluntary_turnover = 4.15 # "Industry leading low turnover!"
                time_to_hire_days = 36.5
                employee_satisfaction = 4.18
                sbc_amortization = 3.42
                # The hidden drivers:
                silicon_eng_attrition = 16.8 # Severe brain drain in elite compiler/silicon talent
                contractor_spend = 1.95 # Exorbitant tech consulting substitution
                overtime_hours_pct = 16.5 # Factory/warehouse overtime spike
                
                # Operations: Satisfactory SLA metrics!
                otif_delivery_pct = 98.6 # "Met 98% target! Green SLA!"
                factory_capacity_util = 92.4 # "High asset utilization!"
                supplier_defect_rate = 0.39 # "Low defect rate!"
                # The hidden drivers:
                air_freight_share_pct = 32.5 # Chartered 777 air-freight to meet delivery SLAs
                logistics_freight_spend = 3.25 # Logistics spend doubled
                days_inventory_outstanding = 56.0 # Hoarding buffer stock
                buffer_write_downs = 0.95
                contract_mfg_rush_premiums = 1.25 # Weekend rush bonuses to assemblers
                
                # Finance: Severe margin compression begins
                gross_margin_pct = 43.10 # Down 270 bps from 45.8%
                gross_profit = float(np.round(revenue * (gross_margin_pct / 100.0), 2))
                cogs = float(np.round(revenue - gross_profit, 2))
                
                rd_expense = 9.85
                sga_expense = 7.75
                opex = float(np.round(rd_expense + sga_expense, 2)) # Surged to $17.6B
                operating_profit = float(np.round(gross_profit - opex, 2)) # $33.43B
                operating_margin_pct = float(np.round((operating_profit / revenue) * 100.0, 2)) # 28.24% (Down from 31.4%)
                
                tax_rate = 0.165
                net_profit = float(np.round(operating_profit * (1 - tax_rate), 2)) # $27.91B
                net_margin_pct = float(np.round((net_profit / revenue) * 100.0, 2)) # 23.57%
                realized_asp = 878.0 # ASP eroded due to trade-in contra-revenue & promo mix
                cash_liquidity = 159.2
                
            elif is_crisis_q2:
                # Q2 2025: Second quarter of steep decline. Volume dips post-holiday, cost tail remains
                revenue = float(np.round(94.6, 2))
                
                # Marketing
                cac = 42.2 # "Still below $45 target!"
                ad_spend = 2.75
                campaign_impressions = 10.8
                dtc_conversion_rate = 3.35
                brand_sentiment = 87.2
                trade_in_subsidy_per_unit = 185.0 # Doubled down on promos to defend volume
                trade_in_spend = 2.65
                low_margin_sku_mix = 43.8
                
                # HR
                headcount_target_achievement = 99.8 # "Met hiring targets!"
                voluntary_turnover = 4.35
                time_to_hire_days = 39.0
                employee_satisfaction = 4.08
                sbc_amortization = 3.35
                silicon_eng_attrition = 18.9 # Silicon attrition deepens
                contractor_spend = 2.45 # External vendors charging peak rates
                overtime_hours_pct = 19.2 # High overtime continues
                
                # Operations
                otif_delivery_pct = 98.4 # "Still meeting 98% target!"
                factory_capacity_util = 90.5
                supplier_defect_rate = 0.41
                air_freight_share_pct = 36.8 # Air freight relied upon to clear supplier bottlenecks
                logistics_freight_spend = 3.48
                days_inventory_outstanding = 64.0 # Excess inventory building up
                buffer_write_downs = 1.38 # Obsolete packaging / early silicon write-downs
                contract_mfg_rush_premiums = 1.45
                
                # Finance: Margin drops again
                gross_margin_pct = 41.50 # Down another 160 bps
                gross_profit = float(np.round(revenue * (gross_margin_pct / 100.0), 2))
                cogs = float(np.round(revenue - gross_profit, 2))
                
                rd_expense = 8.75
                sga_expense = 7.05
                opex = float(np.round(rd_expense + sga_expense, 2)) # $15.8B
                operating_profit = float(np.round(gross_profit - opex, 2)) # $23.46B
                operating_margin_pct = float(np.round((operating_profit / revenue) * 100.0, 2)) # 24.80% (Down 344 bps)
                
                tax_rate = 0.165
                net_profit = float(np.round(operating_profit * (1 - tax_rate), 2))
                net_margin_pct = float(np.round((net_profit / revenue) * 100.0, 2)) # 20.71%
                realized_asp = 852.0
                cash_liquidity = 153.5
                
            elif is_crisis_q3:
                # Q3 2025: Third consecutive quarter of decline - Crisis Peak
                revenue = float(np.round(89.5, 2))
                
                # Marketing
                cac = 43.1 # "CAC still within SLA ceiling ($45)!"
                ad_spend = 2.60
                campaign_impressions = 9.9
                dtc_conversion_rate = 3.20
                brand_sentiment = 86.4
                trade_in_subsidy_per_unit = 195.0 # Highest subsidy ever
                trade_in_spend = 2.80
                low_margin_sku_mix = 46.2 # Base models dominating channel sell-through
                
                # HR
                headcount_target_achievement = 100.5
                voluntary_turnover = 4.45 # "Overall attrition low!"
                time_to_hire_days = 41.0
                employee_satisfaction = 3.98
                sbc_amortization = 3.48
                silicon_eng_attrition = 20.4 # Peak engineer turnover
                contractor_spend = 2.78 # Peak external contractor spend
                overtime_hours_pct = 21.8 # Overtime hours peak
                
                # Operations
                otif_delivery_pct = 98.2 # "OTIF green at 98.2%!"
                factory_capacity_util = 89.2
                supplier_defect_rate = 0.44
                air_freight_share_pct = 39.5 # 40% of units shipped via expedited air!
                logistics_freight_spend = 3.65 # Peak logistics blowout
                days_inventory_outstanding = 69.5 # Peak safety buffer
                buffer_write_downs = 1.75 # Substantial silicon & case write-downs
                contract_mfg_rush_premiums = 1.62
                
                # Finance: 3rd consecutive drop - Operating margin at 22.35%
                gross_margin_pct = 40.10 # Down to 40.10% (cumulative -570 bps)
                gross_profit = float(np.round(revenue * (gross_margin_pct / 100.0), 2))
                cogs = float(np.round(revenue - gross_profit, 2))
                
                rd_expense = 8.90
                sga_expense = 7.00
                opex = float(np.round(rd_expense + sga_expense, 2)) # $15.9B
                operating_profit = float(np.round(gross_profit - opex, 2)) # $19.99B
                operating_margin_pct = float(np.round((operating_profit / revenue) * 100.0, 2)) # 22.34% (Down another 246 bps)
                
                tax_rate = 0.165
                net_profit = float(np.round(operating_profit * (1 - tax_rate), 2))
                net_margin_pct = float(np.round((net_profit / revenue) * 100.0, 2)) # 17.65%
                realized_asp = 835.0 # Cumulative $95/unit erosion in realized ASP
                cash_liquidity = 148.2
                
            else:
                # 2025-Q4: Initial corrective pilot initiated
                revenue = float(np.round(112.5, 2))
                cac = 44.0
                ad_spend = 3.10
                campaign_impressions = 12.8
                dtc_conversion_rate = 3.45
                brand_sentiment = 88.0
                trade_in_subsidy_per_unit = 135.0
                trade_in_spend = 2.10
                low_margin_sku_mix = 36.5
                
                headcount_target_achievement = 100.0
                voluntary_turnover = 4.20
                time_to_hire_days = 38.5
                employee_satisfaction = 4.15
                sbc_amortization = 3.20
                silicon_eng_attrition = 12.5
                contractor_spend = 1.85
                overtime_hours_pct = 14.2
                
                otif_delivery_pct = 98.4
                factory_capacity_util = 91.0
                supplier_defect_rate = 0.38
                air_freight_share_pct = 24.5
                logistics_freight_spend = 2.45
                days_inventory_outstanding = 48.0
                buffer_write_downs = 0.85
                contract_mfg_rush_premiums = 0.95
                
                gross_margin_pct = 42.80
                gross_profit = float(np.round(revenue * (gross_margin_pct / 100.0), 2))
                cogs = float(np.round(revenue - gross_profit, 2))
                
                rd_expense = 9.20
                sga_expense = 7.20
                opex = float(np.round(rd_expense + sga_expense, 2))
                operating_profit = float(np.round(gross_profit - opex, 2))
                operating_margin_pct = float(np.round((operating_profit / revenue) * 100.0, 2)) # 25.07%
                
                tax_rate = 0.165
                net_profit = float(np.round(operating_profit * (1 - tax_rate), 2))
                net_margin_pct = float(np.round((net_profit / revenue) * 100.0, 2))
                realized_asp = 885.0
                cash_liquidity = 152.0

        records.append({
            "quarter": q,
            "quarter_index": i + 1,
            "is_crisis_period": int(is_crisis),
            # Finance
            "revenue_b": revenue,
            "cogs_b": cogs,
            "gross_profit_b": gross_profit,
            "gross_margin_pct": gross_margin_pct,
            "rd_expense_b": rd_expense,
            "sga_expense_b": sga_expense,
            "opex_b": opex,
            "operating_profit_b": operating_profit,
            "operating_margin_pct": operating_margin_pct,
            "net_profit_b": net_profit,
            "net_margin_pct": net_margin_pct,
            "realized_asp_usd": realized_asp,
            "cash_liquidity_b": cash_liquidity,
            # Marketing
            "mkt_cac_usd": cac,
            "mkt_ad_spend_b": ad_spend,
            "mkt_campaign_impressions_b": campaign_impressions,
            "mkt_dtc_conversion_pct": dtc_conversion_rate,
            "mkt_trade_in_subsidy_usd": trade_in_subsidy_per_unit,
            "mkt_trade_in_spend_b": trade_in_spend,
            "mkt_low_margin_sku_mix_pct": low_margin_sku_mix,
            "mkt_brand_sentiment": brand_sentiment,
            # HR
            "hr_headcount_target_achieve_pct": headcount_target_achievement,
            "hr_voluntary_turnover_pct": voluntary_turnover,
            "hr_silicon_eng_attrition_pct": silicon_eng_attrition,
            "hr_contractor_spend_b": contractor_spend,
            "hr_overtime_hours_pct": overtime_hours_pct,
            "hr_time_to_hire_days": time_to_hire_days,
            "hr_employee_satisfaction": employee_satisfaction,
            "hr_sbc_amortization_b": sbc_amortization,
            # Operations
            "ops_otif_delivery_pct": otif_delivery_pct,
            "ops_air_freight_share_pct": air_freight_share_pct,
            "ops_logistics_freight_spend_b": logistics_freight_spend,
            "ops_factory_capacity_util_pct": factory_capacity_util,
            "ops_days_inventory_outstanding": days_inventory_outstanding,
            "ops_buffer_write_downs_b": buffer_write_downs,
            "ops_supplier_defect_rate_pct": supplier_defect_rate,
            "ops_contract_mfg_rush_premiums_b": contract_mfg_rush_premiums
        })
        
    df_quarterly = pd.DataFrame(records)
    quarterly_path = os.path.join(output_dir, "apple_cross_functional_quarterly_data.csv")
    df_quarterly.to_csv(quarterly_path, index=False)
    print(f"Generated 16-quarter enterprise dataset -> {quarterly_path} ({len(df_quarterly)} quarters)")
    
    # -------------------------------------------------------------------------
    # 2. Monthly Granular Telemetry (48 Months: Jan 2022 to Dec 2025)
    # Enables Granger-Causal time-lag analysis (e.g. Month T promo -> Month T+1 air freight)
    # -------------------------------------------------------------------------
    monthly_records = []
    start_date = pd.date_range(start="2022-01-01", periods=48, freq="MS")
    
    for idx, dt in enumerate(start_date):
        # Determine quarter index (0 to 15)
        q_idx = idx // 3
        q_row = df_quarterly.iloc[q_idx]
        
        # Add monthly jitter around quarterly values
        m_noise = np.random.normal(0, 0.02)
        m_rev = float(np.round((q_row["revenue_b"] / 3.0) * (1 + m_noise), 3))
        
        # Monthly lag dynamics
        # In crisis months (months 36 to 44: Jan 2025 to Sep 2025)
        is_crisis_m = (36 <= idx <= 44)
        
        trade_in_sub = float(np.round(q_row["mkt_trade_in_subsidy_usd"] * (1 + np.random.normal(0, 0.03)), 1))
        air_freight = float(np.round(q_row["ops_air_freight_share_pct"] * (1 + np.random.normal(0, 0.04)), 1))
        contractor = float(np.round((q_row["hr_contractor_spend_b"] / 3.0) * (1 + np.random.normal(0, 0.03)), 3))
        overtime = float(np.round(q_row["hr_overtime_hours_pct"] * (1 + np.random.normal(0, 0.03)), 2))
        logistics = float(np.round((q_row["ops_logistics_freight_spend_b"] / 3.0) * (1 + np.random.normal(0, 0.03)), 3))
        otif = float(np.round(np.clip(q_row["ops_otif_delivery_pct"] + np.random.normal(0, 0.15), 97.5, 99.5), 2))
        cac = float(np.round(q_row["mkt_cac_usd"] * (1 + np.random.normal(0, 0.02)), 2))
        op_margin = float(np.round(q_row["operating_margin_pct"] * (1 + np.random.normal(0, 0.02)), 2))
        
        monthly_records.append({
            "date": dt.strftime("%Y-%m-%d"),
            "month_name": dt.strftime("%b %Y"),
            "month_index": idx + 1,
            "quarter": q_row["quarter"],
            "is_crisis": int(is_crisis_m),
            "monthly_revenue_b": m_rev,
            "monthly_operating_margin_pct": op_margin,
            "trade_in_subsidy_usd": trade_in_sub,
            "air_freight_share_pct": air_freight,
            "contractor_spend_b": contractor,
            "overtime_hours_pct": overtime,
            "logistics_freight_spend_b": logistics,
            "otif_delivery_pct": otif,
            "cac_usd": cac,
            "days_inventory_outstanding": float(np.round(q_row["ops_days_inventory_outstanding"] * (1 + np.random.normal(0, 0.02)), 1)),
            "silicon_eng_attrition_pct": float(np.round(q_row["hr_silicon_eng_attrition_pct"] * (1 + np.random.normal(0, 0.03)), 2))
        })
        
    df_monthly = pd.DataFrame(monthly_records)
    monthly_path = os.path.join(output_dir, "apple_monthly_telemetry_data.csv")
    df_monthly.to_csv(monthly_path, index=False)
    print(f"Generated 48-month granular telemetry -> {monthly_path} ({len(df_monthly)} months)")
    
    return quarterly_path, monthly_path

if __name__ == "__main__":
    generate_apple_cross_functional_dataset()

