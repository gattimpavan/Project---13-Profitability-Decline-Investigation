/**
 * Apple Inc. - Executive Decision Intelligence Engine
 * Project - 13: Profitability Decline Investigation
 * Frontend Dashboard Controller
 */

document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    loadOverviewData();
    loadSiloParadoxData();
    loadCorrelationData();
    initSimulator();
    initChatTerminal();
    loadProtocols();
});

// Chart instances
let trajectoryChart = null;
let waterfallChart = null;
let lagChart = null;
let simBreakdownChart = null;

/**
 * Tab Navigation
 */
function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            tabButtons.forEach(b => b.classList.remove('active'));
            tabPanes.forEach(p => p.classList.remove('active'));

            btn.classList.add('active');
            const target = btn.getAttribute('data-tab');
            const targetPane = document.getElementById(target);
            if (targetPane) targetPane.classList.add('active');
        });
    });
}

/**
 * Load Overview & Waterfall Data
 */
async function loadOverviewData() {
    try {
        const res = await fetch('/api/summary');
        const data = await res.json();

        renderTrajectoryChart(data.quarterly_telemetry);
        renderWaterfallChart(data.waterfall);
        renderElasticityTable(data.elasticities);
    } catch (err) {
        console.error("Failed to load overview data:", err);
    }
}

/**
 * Render 16-Quarter Operating Margin Trajectory Chart
 */
function renderTrajectoryChart(quarterly) {
    const ctx = document.getElementById('trajectoryChart');
    if (!ctx) return;

    const labels = quarterly.map(q => q.quarter);
    const margins = quarterly.map(q => q.operating_margin_pct);
    const revenues = quarterly.map(q => q.revenue_b);

    // Crisis quarters index: 12, 13, 14
    const pointColors = margins.map((_, i) => (i >= 12 && i <= 14) ? '#ff3b30' : '#0071e3');
    const pointRadius = margins.map((_, i) => (i >= 12 && i <= 14) ? 6 : 4);

    if (trajectoryChart) trajectoryChart.destroy();

    trajectoryChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Operating Margin (%)',
                    data: margins,
                    borderColor: '#0071e3',
                    backgroundColor: 'rgba(0, 113, 227, 0.08)',
                    borderWidth: 2.5,
                    pointBackgroundColor: pointColors,
                    pointBorderColor: '#ffffff',
                    pointBorderWidth: 1.5,
                    pointRadius: pointRadius,
                    tension: 0.3,
                    fill: true,
                    yAxisID: 'y'
                },
                {
                    type: 'bar',
                    label: 'Revenue ($B)',
                    data: revenues,
                    backgroundColor: 'rgba(210, 210, 215, 0.45)',
                    borderRadius: 4,
                    yAxisID: 'y1'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'top', labels: { boxWidth: 12, font: { size: 11 } } },
                tooltip: {
                    callbacks: {
                        afterLabel: (ctx) => {
                            if (ctx.dataIndex >= 12 && ctx.dataIndex <= 14) {
                                return 'CRISIS QUARTER: Consecutive Profitability Erosion';
                            }
                        }
                    }
                }
            },
            scales: {
                y: {
                    min: 15,
                    max: 36,
                    title: { display: true, text: 'Operating Margin (%)', font: { size: 11, weight: 'bold' } },
                    grid: { color: 'rgba(0, 0, 0, 0.05)' }
                },
                y1: {
                    position: 'right',
                    min: 60,
                    max: 140,
                    title: { display: true, text: 'Revenue ($B)', font: { size: 11 } },
                    grid: { display: false }
                },
                x: {
                    grid: { display: false },
                    ticks: { maxRotation: 45, minRotation: 45, font: { size: 10 } }
                }
            }
        }
    });
}

/**
 * Render Profitability Waterfall Chart
 */
function renderWaterfallChart(waterfall) {
    const ctx = document.getElementById('waterfallChart');
    if (!ctx) return;

    const categories = [
        'Q4 2024 Baseline',
        'Air Freight Surge',
        'Trade-In Contra-Rev',
        'Silicon Contractors',
        'Buffer DIO Bloat',
        'Assembly Overtime',
        'Q3 2025 Trough'
    ];

    const values = [31.46, -2.45, -1.95, -1.82, -1.64, -1.24, 22.34];
    const colors = ['#34c759', '#ff3b30', '#ff9500', '#af52de', '#5856d6', '#ff2d55', '#0071e3'];

    if (waterfallChart) waterfallChart.destroy();

    waterfallChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: categories,
            datasets: [{
                data: values,
                backgroundColor: colors,
                borderRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: (ctx) => {
                            const val = ctx.raw;
                            if (ctx.dataIndex === 0 || ctx.dataIndex === 6) {
                                return `Operating Margin: ${val.toFixed(2)}%`;
                            } else {
                                return `Impact: ${val.toFixed(2)}% (${Math.round(val * 100)} bps)`;
                            }
                        }
                    }
                }
            },
            scales: {
                y: {
                    title: { display: true, text: 'Contribution / Margin (%)', font: { size: 11, weight: 'bold' } },
                    grid: { color: 'rgba(0, 0, 0, 0.05)' }
                },
                x: {
                    grid: { display: false },
                    ticks: { font: { size: 10 } }
                }
            }
        }
    });
}

/**
 * Render Elasticity Table
 */
function renderElasticityTable(elasticities) {
    const tbody = document.querySelector('#elasticityTable tbody');
    if (!tbody) return;

    tbody.innerHTML = '';
    const keys = Object.keys(elasticities);

    keys.forEach(k => {
        const item = elasticities[k];
        const isNegative = item.bps_impact_per_unit < 0;
        const riskLevel = Math.abs(item.bps_impact_per_unit) > 20 ? 'CRITICAL' : (Math.abs(item.bps_impact_per_unit) > 8 ? 'HIGH' : 'MODERATE');
        const badgeClass = riskLevel === 'CRITICAL' ? 'badge-danger' : (riskLevel === 'HIGH' ? 'badge-warning' : 'badge-success');

        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td><strong>${item.label}</strong></td>
            <td><span class="badge" style="background:#f0f0f4;color:#1d1d1f">${item.department}</span></td>
            <td>+1.0 ${item.unit}</td>
            <td class="${isNegative ? 'text-danger' : 'text-success'}"><strong>${item.bps_impact_per_unit > 0 ? '+' : ''}${item.bps_impact_per_unit} bps</strong></td>
            <td class="${item.ebitda_impact_m_per_unit < 0 ? 'text-danger' : 'text-success'}"><strong>${item.ebitda_impact_m_per_unit > 0 ? '+' : ''}$${item.ebitda_impact_m_per_unit} M</strong></td>
            <td><span class="badge ${badgeClass}">${riskLevel}</span></td>
        `;
        tbody.appendChild(tr);
    });
}

/**
 * Load & Render Silo Paradox Data
 */
async function loadSiloParadoxData() {
    try {
        const res = await fetch('/api/silo-paradox');
        const data = await res.json();
        const container = document.getElementById('siloCardsContainer');
        if (!container) return;

        container.innerHTML = '';

        data.departments.forEach(dept => {
            const card = document.createElement('div');
            card.className = 'silo-card';
            card.innerHTML = `
                <div>
                    <div class="silo-card-header">
                        <span class="silo-dept">${dept.department}</span>
                        <span class="silo-status-badge">${dept.reported_status}</span>
                    </div>
                    <div class="silo-metric-row">
                        <div class="silo-metric-label">Reported Vanity KPI</div>
                        <div class="silo-metric-value">${dept.reported_kpi}</div>
                        <div class="small text-muted">${dept.reported_value} (${dept.reported_variance_pct})</div>
                    </div>
                    <div class="silo-divider"></div>
                    <div>
                        <div class="silo-reality-tag"><i class="fa-solid fa-triangle-exclamation"></i> True Enterprise Reality</div>
                        <div class="silo-leakage-stat">${dept.true_enterprise_margin_impact_bps} bps</div>
                        <div class="silo-leakage-sub">$${dept.annualized_financial_leakage_b.toFixed(2)}B Annualized Profit Loss</div>
                    </div>
                    <div class="silo-desc">${dept.silo_blindspot_summary}</div>
                </div>
                <div class="mt-3">
                    <span class="badge badge-warning" style="font-size:10px;">VMDI: ${dept.vmdi_score}/10</span>
                </div>
            `;
            container.appendChild(card);
        });

        // Initialize Departmental Deep Dive Viewer
        initDepartmentDeepDive(data.departments);
    } catch (err) {
        console.error("Failed to load Silo Paradox data:", err);
    }
}

/**
 * Departmental Deep Dive Subnav
 */
function initDepartmentDeepDive(departments) {
    const pills = document.querySelectorAll('.dept-pill');
    const container = document.getElementById('deptDetailContainer');
    if (!container) return;

    function renderDept(deptName) {
        const d = departments.find(item => item.department.toLowerCase().includes(deptName.toLowerCase()));
        if (!d) return;

        container.innerHTML = `
            <div class="card">
                <div class="card-header">
                    <h3><i class="fa-solid fa-building"></i> ${d.department} Detailed Telemetry & Silo Anatomy</h3>
                    <span class="badge ${d.vmdi_score > 9 ? 'badge-danger' : 'badge-warning'}">VMDI Distortion: ${d.vmdi_score}/10</span>
                </div>
                <div class="card-body">
                    <div class="grid-2">
                        <div class="card" style="background:#fbfbfd;">
                            <div class="card-body">
                                <h4 class="text-success"><i class="fa-solid fa-circle-check"></i> What the Department Reported (Green)</h4>
                                <p class="mt-2"><strong>Primary Metric:</strong> ${d.reported_kpi}</p>
                                <p><strong>Reported Figure:</strong> ${d.reported_value}</p>
                                <p><strong>Target SLA:</strong> ${d.target_benchmark}</p>
                                <p><strong>Department Self-Assessment:</strong> ${d.reported_variance_pct}</p>
                            </div>
                        </div>

                        <div class="card" style="background:#fff8f8; border-color: rgba(255,59,48,0.2);">
                            <div class="card-body">
                                <h4 class="text-danger"><i class="fa-solid fa-triangle-exclamation"></i> What Actually Happened (Enterprise Leakage)</h4>
                                <p class="mt-2"><strong>Hidden Driver:</strong> ${d.hidden_transmission_driver}</p>
                                <p><strong>Observed Telemetry:</strong> ${d.hidden_driver_metric}</p>
                                <p><strong>Margin Destruction:</strong> <span class="text-danger font-weight-bold">${d.true_enterprise_margin_impact_bps} basis points</span></p>
                                <p><strong>Financial Loss:</strong> <span class="text-danger font-weight-bold">$${d.annualized_financial_leakage_b.toFixed(2)} Billion</span></p>
                            </div>
                        </div>
                    </div>

                    <div class="callout callout-info mt-4">
                        <strong>Downstream Victim Functions:</strong> ${d.downstream_victims ? d.downstream_victims.join(', ') : 'Adjacent operational nodes'}
                    </div>

                    <div class="mt-3">
                        <p class="text-muted" style="font-size:13px; line-height: 1.6;"><strong>Root Cause Diagnostic:</strong> ${d.silo_blindspot_summary}</p>
                    </div>
                </div>
            </div>
        `;
    }

    pills.forEach(pill => {
        pill.addEventListener('click', () => {
            pills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            renderDept(pill.getAttribute('data-dept'));
        });
    });

    // Initial render
    renderDept('Marketing');
}

/**
 * Load Correlation & Time-Lag Data
 */
async function loadCorrelationData() {
    try {
        const res = await fetch('/api/correlations');
        const data = await res.json();

        // Populate Table
        const table = document.getElementById('corrTable');
        if (table) {
            let html = '<thead><tr><th>Indicator</th>';
            data.correlation_matrix.labels.forEach(lbl => {
                html += `<th>${lbl}</th>`;
            });
            html += '</tr></thead><tbody>';

            data.correlation_matrix.matrix.forEach(row => {
                html += `<tr><td><strong>${row.label}</strong></td>`;
                row.values.forEach(val => {
                    const bg = val > 0.5 ? 'rgba(255, 59, 48, 0.15)' : (val < -0.5 ? 'rgba(0, 113, 227, 0.15)' : 'transparent');
                    const color = val > 0.5 ? '#ff3b30' : (val < -0.5 ? '#0071e3' : '#1d1d1f');
                    html += `<td style="background:${bg}; color:${color}; font-weight:600; text-align:center;">${val.toFixed(2)}</td>`;
                });
                html += '</tr>';
            });
            html += '</tbody>';
            table.innerHTML = html;
        }

        // Render Lag Chart
        renderLagChart(data.monthly_lags);
    } catch (err) {
        console.error("Failed to load correlation data:", err);
    }
}

/**
 * Render Time-Lag Chart
 */
function renderLagChart(lags) {
    const ctx = document.getElementById('lagChart');
    if (!ctx || !lags || !lags.length) return;

    const labels = lags.map(l => l.interpretation);
    const corrFreight = lags.map(l => l.correlation_freight);
    const corrContractor = lags.map(l => l.correlation_contractor);

    if (lagChart) lagChart.destroy();

    lagChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Trade-In Promo -> Air Freight Surge (Ops)',
                    data: corrFreight,
                    borderColor: '#ff3b30',
                    backgroundColor: 'rgba(255, 59, 48, 0.1)',
                    borderWidth: 2.5,
                    pointRadius: 5,
                    tension: 0.3
                },
                {
                    label: 'Trade-In Promo -> Contractor Spend (HR)',
                    data: corrContractor,
                    borderColor: '#af52de',
                    backgroundColor: 'rgba(175, 82, 222, 0.1)',
                    borderWidth: 2.5,
                    pointRadius: 5,
                    tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { position: 'top', labels: { boxWidth: 12 } }
            },
            scales: {
                y: {
                    min: 0,
                    max: 1.0,
                    title: { display: true, text: 'Correlation Coefficient', font: { size: 11, weight: 'bold' } }
                },
                x: {
                    grid: { display: false }
                }
            }
        }
    });
}

/**
 * Initialize What-If Simulator
 */
function initSimulator() {
    const sliders = [
        { id: 'sliderAirFreight', valId: 'valAirFreight', suffix: '%' },
        { id: 'sliderContractors', valId: 'valContractors', suffix: '%' },
        { id: 'sliderTradeIn', valId: 'valTradeIn', suffix: '%' },
        { id: 'sliderDIO', valId: 'valDIO', suffix: ' Days' },
        { id: 'sliderOvertime', valId: 'valOvertime', suffix: '%' }
    ];

    sliders.forEach(s => {
        const input = document.getElementById(s.id);
        const display = document.getElementById(s.valId);
        if (input && display) {
            input.addEventListener('input', () => {
                display.innerText = `${input.value}${s.suffix}`;
                triggerSimulation();
            });
        }
    });

    const resetBtn = document.getElementById('resetSlidersBtn');
    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            document.getElementById('sliderAirFreight').value = 50;
            document.getElementById('valAirFreight').innerText = '50%';
            document.getElementById('sliderContractors').value = 60;
            document.getElementById('valContractors').innerText = '60%';
            document.getElementById('sliderTradeIn').value = 50;
            document.getElementById('valTradeIn').innerText = '50%';
            document.getElementById('sliderDIO').value = 25;
            document.getElementById('valDIO').innerText = '25 Days';
            document.getElementById('sliderOvertime').value = 50;
            document.getElementById('valOvertime').innerText = '50%';
            triggerSimulation();
        });
    }

    // Trigger initial simulation
    triggerSimulation();
}

let simDebounceTimer = null;
function triggerSimulation() {
    clearTimeout(simDebounceTimer);
    simDebounceTimer = setTimeout(async () => {
        const payload = {
            air_freight_reduction_pct: parseFloat(document.getElementById('sliderAirFreight').value),
            contractor_insourcing_pct: parseFloat(document.getElementById('sliderContractors').value),
            trade_in_cap_pct: parseFloat(document.getElementById('sliderTradeIn').value),
            inventory_dio_reduction_days: parseFloat(document.getElementById('sliderDIO').value),
            overtime_reduction_pct: parseFloat(document.getElementById('sliderOvertime').value)
        };

        try {
            const res = await fetch('/api/simulate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            updateSimUI(data);
        } catch (err) {
            console.error("Simulation request failed:", err);
        }
    }, 150);
}

function updateSimUI(data) {
    document.getElementById('simNewMargin').innerText = `${data.new_operating_margin_pct.toFixed(2)}%`;
    document.getElementById('simMarginDelta').innerText = `+${data.margin_expansion_bps} bps`;
    document.getElementById('simEbitdaGain').innerText = `+$${data.total_annual_ebitda_recovery_b.toFixed(2)} B`;
    document.getElementById('simCapex').innerText = `$${data.capital_investment_required_m.toFixed(1)} M`;
    document.getElementById('simPayback').innerText = `${data.payback_period_months.toFixed(1)} Mo`;

    renderSimBreakdownChart(data.levers_breakdown);
}

function renderSimBreakdownChart(levers) {
    const ctx = document.getElementById('simBreakdownChart');
    if (!ctx) return;

    const labels = levers.map(l => l.lever);
    const savings = levers.map(l => l.savings_b);
    const colors = levers.map(l => l.color);

    if (simBreakdownChart) simBreakdownChart.destroy();

    simBreakdownChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                data: savings,
                backgroundColor: colors,
                borderRadius: 4
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: (ctx) => `Annual Savings: $${ctx.raw.toFixed(2)}B (${levers[ctx.dataIndex].margin_bps} bps)`
                    }
                }
            },
            scales: {
                x: {
                    title: { display: true, text: 'Annual EBITDA Savings ($B)', font: { size: 10 } },
                    grid: { color: 'rgba(0, 0, 0, 0.05)' }
                },
                y: {
                    ticks: { font: { size: 10 } }
                }
            }
        }
    });
}

/**
 * Initialize AI Business Analyst Chat Terminal
 */
function initChatTerminal() {
    const form = document.getElementById('chatForm');
    const input = document.getElementById('chatInput');
    const messages = document.getElementById('chatMessages');

    // Preset pills
    const pills = document.querySelectorAll('.prompt-pill');
    pills.forEach(p => {
        p.addEventListener('click', () => {
            const query = p.getAttribute('data-query');
            sendQuery(query);
        });
    });

    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const q = input.value.trim();
            if (q) {
                sendQuery(q);
                input.value = '';
            }
        });
    }

    async function sendQuery(query) {
        // Append user message
        const userMsg = document.createElement('div');
        userMsg.className = 'message user-message';
        userMsg.innerHTML = `
            <div class="avatar"><i class="fa-solid fa-user-tie"></i></div>
            <div class="msg-content">${query}</div>
        `;
        messages.appendChild(userMsg);
        messages.scrollTop = messages.scrollHeight;

        // Loading message
        const loadMsg = document.createElement('div');
        loadMsg.className = 'message system-message';
        loadMsg.innerHTML = `
            <div class="avatar"><i class="fa-brands fa-apple"></i></div>
            <div class="msg-content"><i class="fa-solid fa-circle-notch fa-spin"></i> Synthesizing cross-functional telemetry...</div>
        `;
        messages.appendChild(loadMsg);
        messages.scrollTop = messages.scrollHeight;

        try {
            const res = await fetch('/api/ask-analyst', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: query })
            });
            const data = await res.json();

            let findingsHtml = '';
            if (data.key_findings && data.key_findings.length) {
                findingsHtml = '<ul style="margin: 8px 0 8px 18px; font-size:12.5px;">';
                data.key_findings.forEach(f => {
                    findingsHtml += `<li>${f}</li>`;
                });
                findingsHtml += '</ul>';
            }

            loadMsg.innerHTML = `
                <div class="avatar"><i class="fa-brands fa-apple"></i></div>
                <div class="msg-content">
                    <strong style="color:#0071e3; font-size:13.5px;">${data.title}</strong>
                    <p style="margin-top:6px;">${data.summary}</p>
                    ${findingsHtml}
                    <div style="background:#eaf8ee; border-left:3px solid #34c759; padding:8px 12px; border-radius:4px; margin-top:8px; font-size:12px; color:#1e5e2e;">
                        <strong>Prescriptive Action:</strong> ${data.action_recommendation}
                    </div>
                </div>
            `;
            messages.scrollTop = messages.scrollHeight;
        } catch (err) {
            loadMsg.innerHTML = `
                <div class="avatar"><i class="fa-brands fa-apple"></i></div>
                <div class="msg-content text-danger">An error occurred while querying the AI analyst engine.</div>
            `;
        }
    }
}

/**
 * Load & Render Prescriptive Board Protocols
 */
async function loadProtocols() {
    try {
        const res = await fetch('/api/protocols');
        const protocols = await res.json();
        const container = document.getElementById('protocolsContainer');
        if (!container) return;

        container.innerHTML = '';
        protocols.forEach(p => {
            const card = document.createElement('div');
            card.className = 'protocol-card';
            card.innerHTML = `
                <div>
                    <div class="protocol-code">${p.code}</div>
                    <div class="protocol-title">${p.name}</div>
                    <div class="protocol-meta">
                        <i class="fa-solid fa-user-gear"></i> ${p.department} • <strong>${p.executive_sponsor}</strong>
                    </div>
                    <div class="protocol-desc">
                        <p><strong>Friction Addressed:</strong> ${p.problem_addressed}</p>
                        <p class="mt-2"><strong>Core Mechanism:</strong> ${p.action_mechanism}</p>
                    </div>
                </div>
                <div>
                    <div class="protocol-stats">
                        <div class="protocol-stat-item">
                            <div class="stat-num text-primary">+$${p.annual_ebitda_gain_b.toFixed(2)}B</div>
                            <div class="stat-lbl">Annual EBITDA</div>
                        </div>
                        <div class="protocol-stat-item">
                            <div class="stat-num text-success">+${p.margin_recovery_bps} bps</div>
                            <div class="stat-lbl">Margin Accretion</div>
                        </div>
                        <div class="protocol-stat-item">
                            <div class="stat-num text-warning">${p.payback_months} mo</div>
                            <div class="stat-lbl">Payback Horizon</div>
                        </div>
                    </div>
                    <div class="mt-3 text-muted small">
                        <span>Horizon: <strong>${p.implementation_horizon}</strong></span> • 
                        <span>Target: <strong>${p.primary_metric}</strong></span>
                    </div>
                </div>
            `;
            container.appendChild(card);
        });
    } catch (err) {
        console.error("Failed to load protocols:", err);
    }
}

