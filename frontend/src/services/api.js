import { BENCHMARK_SIGNALS, BENCHMARK_PORTFOLIO, DEFAULT_STRESS_RESULT } from './benchmarkData';

// Determine API base URL:
// 1. Explicit VITE_API_URL if provided
// 2. Relative URL ("") in production so Vercel rewrites work seamlessly
// 3. Fallback to localhost:8000 for local development
const BASE_URL = import.meta.env.VITE_API_URL || (import.meta.env.PROD ? '' : 'http://localhost:8000');

export async function fetchSignals(filters = {}) {
  try {
    const params = new URLSearchParams();
    if (filters.company) params.append('company', filters.company);
    if (filters.eventType) params.append('event_type', filters.eventType);
    if (filters.minImpact) params.append('min_impact', filters.minImpact);

    const url = `${BASE_URL}/signals${params.toString() ? `?${params.toString()}` : ''}`;
    const res = await fetch(url, { headers: { 'Accept': 'application/json' } });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    return Array.isArray(data) && data.length > 0 ? data : BENCHMARK_SIGNALS;
  } catch (err) {
    console.warn('API fetchSignals notice (using benchmark signals):', err.message);
    return BENCHMARK_SIGNALS;
  }
}

export async function fetchPortfolio() {
  try {
    const res = await fetch(`${BASE_URL}/portfolio`, { headers: { 'Accept': 'application/json' } });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('API fetchPortfolio notice (using benchmark portfolio):', err.message);
    return BENCHMARK_PORTFOLIO;
  }
}

export async function runStressTest(eventType = 'Geopolitical', impactScore = 9) {
  try {
    const res = await fetch(`${BASE_URL}/stress-test`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        event_type: eventType,
        impact_score: impactScore
      })
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('API runStressTest notice (calculating client-side synthetic shocks):', err.message);
    // If backend is not reached, calculate synthetic shock client-side
    return calculateClientStressTest(eventType, impactScore);
  }
}

export async function analyzeText(text, company = null) {
  try {
    const res = await fetch(`${BASE_URL}/analyze`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text, company })
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('API analyzeText notice:', err.message);
    return {
      company: company || 'General Market',
      sentiment_score: -0.75,
      sentiment_label: 'Negative',
      event_type: 'Regulatory',
      impact_score: 8,
      risk_level: 'High',
      is_stress_test_trigger: true
    };
  }
}

export async function triggerLiveIngest() {
  try {
    const res = await fetch(`${BASE_URL}/ingest/live`, {
      method: 'POST',
      headers: { 'Accept': 'application/json' }
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('Live RSS ingest notice:', err.message);
    return { status: 'fallback', live_records_ingested: 0 };
  }
}

function calculateClientStressTest(eventType, impactScore) {
  const isTriggered = impactScore >= 7;
  const shocks = {
    Geopolitical: { Equity: -0.10, "Corporate Bond": -0.05, "Government Bond": 0.02, "Commodity Exposure": 0.08, Derivative: -0.06, Loan: -0.04 },
    Macroeconomic: { Equity: -0.07, "Corporate Bond": -0.05, "Government Bond": -0.03, "Commodity Exposure": -0.02, Derivative: -0.04, Loan: -0.08 },
    "Credit Event": { "Corporate Bond": -0.12, Loan: -0.08, Derivative: -0.05, Equity: -0.08, "Government Bond": 0.01, "Commodity Exposure": 0.00 },
    Regulatory: { Equity: -0.06, "Corporate Bond": -0.02, Derivative: -0.03, Loan: -0.02, "Government Bond": 0.00, "Commodity Exposure": 0.00 }
  }[eventType] || { Equity: -0.04, "Corporate Bond": -0.02 };

  let totalBefore = 0;
  let totalAfter = 0;
  const breakdown = BENCHMARK_PORTFOLIO.assets.map(asset => {
    const valBefore = asset.value;
    const shockPct = isTriggered ? (shocks[asset.asset_type] || 0.0) : 0.0;
    const valAfter = Math.max(0, valBefore * (1 + shockPct));
    const changeVal = valAfter - valBefore;
    totalBefore += valBefore;
    totalAfter += valAfter;
    return {
      asset_id: asset.asset_id,
      asset_name: asset.asset_name,
      asset_type: asset.asset_type,
      sector: asset.sector,
      value_before: Math.round(valBefore),
      shock_pct: +(shockPct * 100).toFixed(2),
      value_after: Math.round(valAfter),
      change_value: Math.round(changeVal)
    };
  });

  return {
    event_type: eventType,
    impact_score: impactScore,
    is_triggered: isTriggered,
    trigger_threshold: 7,
    scenario_name: `Synthetic ${eventType} Shock Scenario`,
    portfolio_value_before: Math.round(totalBefore),
    portfolio_value_after: Math.round(totalAfter),
    absolute_loss: Math.round(totalBefore - totalAfter),
    percentage_change: +(((totalAfter - totalBefore) / totalBefore) * 100).toFixed(2),
    asset_breakdown: breakdown,
    disclaimer: "Synthetic hackathon assumptions for demonstration purposes, not real financial forecasts."
  };
}
