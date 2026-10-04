import React, { useState, useEffect } from 'react';
import { runStressTest } from '../services/api';

const SCENARIO_PARAMS = {
  Geopolitical: {
    description: "Maritime supply corridor embargo and energy price shock",
    shocks: [
      { asset: "Equity", shock: "-10.0%" },
      { asset: "Corporate Bonds", shock: "-5.0%" },
      { asset: "Government Bonds", shock: "+2.0%" },
      { asset: "Commodities", shock: "+8.0%" },
      { asset: "Derivatives", shock: "-6.0%" }
    ]
  },
  Macroeconomic: {
    description: "Benchmark policy rate hike (+50 bps) and persistent core inflation pressure",
    shocks: [
      { asset: "Equity", shock: "-7.0%" },
      { asset: "Corporate Bonds", shock: "-5.0%" },
      { asset: "Government Bonds", shock: "-3.0%" },
      { asset: "Loans", shock: "-8.0%" },
      { asset: "Derivatives", shock: "-4.0%" }
    ]
  },
  "Credit Event": {
    description: "Systemic rating downgrades and corporate debt refinancing spread widening",
    shocks: [
      { asset: "Corporate Bonds", shock: "-12.0%" },
      { asset: "Syndicated Loans", shock: "-8.0%" },
      { asset: "Derivatives", shock: "-5.0%" },
      { asset: "Equity", shock: "-8.0%" },
      { asset: "Government Bonds", shock: "+1.0%" }
    ]
  },
  Regulatory: {
    description: "Sector-wide compliance tariff review and environmental audit probes",
    shocks: [
      { asset: "Equity", shock: "-6.0%" },
      { asset: "Corporate Bonds", shock: "-2.0%" },
      { asset: "Loans", shock: "-2.0%" },
      { asset: "Derivatives", shock: "-3.0%" }
    ]
  }
};

export default function StressTestPanel({ preloadedEvent = 'Geopolitical', preloadedImpact = 9 }) {
  const [eventType, setEventType] = useState(preloadedEvent);
  const [impactScore, setImpactScore] = useState(preloadedImpact);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  useEffect(() => {
    executeSimulation(eventType, impactScore);
  }, [eventType, impactScore]);

  const executeSimulation = async (event, impact) => {
    setLoading(true);
    try {
      const data = await runStressTest(event, parseInt(impact, 10));
      setResult(data);
    } catch (err) {
      console.warn('Simulation execution note:', err.message);
    } finally {
      setLoading(false);
    }
  };

  const currentScenario = SCENARIO_PARAMS[eventType] || SCENARIO_PARAMS["Geopolitical"];

  return (
    <div className="card-section">
      <div className="card-title">
        <div>
          <span style={{ fontWeight: 700 }}>Macroprudential Stress Testing Engine (Module B)</span>
          <div style={{ fontSize: '12px', color: '#94A3B8', marginTop: '4px', fontWeight: 400 }}>
            Propagation: NLP High-Impact Risk Signal (≥ 7) → Factor Shocks → Balance Sheet Valuation
          </div>
        </div>

        <button
          className="btn-primary"
          onClick={() => executeSimulation(eventType, impactScore)}
          disabled={loading}
          style={{ background: '#DC2626' }}
        >
          {loading ? 'Re-calculating Shocks...' : '⚡ RUN STRESS TEST'}
        </button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1.2fr 1fr', gap: '20px', marginBottom: '20px', background: '#0D1321', padding: '16px', borderRadius: '6px', border: '1px solid #1F2937' }}>
        <div>
          <label style={{ fontSize: '11px', color: '#94A3B8', display: 'block', marginBottom: '6px', textTransform: 'uppercase' }}>
            Event Scenario Category
          </label>
          <select
            value={eventType}
            onChange={(e) => setEventType(e.target.value)}
            style={{ width: '100%', padding: '10px 14px', background: '#111726', color: '#F3F4F6', border: '1px solid #24304A', borderRadius: '6px', fontSize: '13px' }}
          >
            <option value="Geopolitical">Geopolitical (Energy/Freight Disruption)</option>
            <option value="Macroeconomic">Macroeconomic (Interest Rate Hike & Inflation)</option>
            <option value="Credit Event">Credit Event (Debt Spread Widening & Downgrade)</option>
            <option value="Regulatory">Regulatory (Tariff Inquiry & Compliance Probes)</option>
          </select>
          <div style={{ fontSize: '11px', color: '#64748B', marginTop: '6px' }}>
            {currentScenario.description}
          </div>
        </div>

        <div>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <label style={{ fontSize: '11px', color: '#94A3B8', textTransform: 'uppercase' }}>
              Prototype Risk Impact Score
            </label>
            <span style={{ fontFamily: 'monospace', fontWeight: 700, color: impactScore >= 7 ? '#EF4444' : '#10B981' }}>
              {impactScore} / 10 {impactScore >= 7 ? '● TRIGGER ACTIVE' : '○ NO SHOCKS'}
            </span>
          </div>
          <input
            type="range"
            min="1"
            max="10"
            value={impactScore}
            onChange={(e) => setImpactScore(parseInt(e.target.value, 10))}
            style={{ width: '100%', accentColor: impactScore >= 7 ? '#EF4444' : '#10B981', marginTop: '12px' }}
          />

          <div style={{ display: 'flex', gap: '6px', marginTop: '10px', flexWrap: 'wrap' }}>
            {currentScenario.shocks.map((s, idx) => (
              <span key={idx} style={{ fontSize: '10px', background: '#111726', padding: '3px 8px', borderRadius: '4px', border: '1px solid #24304A', fontFamily: 'monospace' }}>
                {s.asset}: <span style={{ color: s.shock.startsWith('-') ? '#EF4444' : '#10B981' }}>{s.shock}</span>
              </span>
            ))}
          </div>
        </div>
      </div>

      {result && (
        <div style={{ marginTop: '10px' }}>
          <div className="stress-result-grid">
            <div>
              <div className="stress-stat-label">Baseline Portfolio Value</div>
              <div className="stress-stat-value">₹{(result.portfolio_value_before / 10000000).toFixed(2)} Cr</div>
              <div style={{ fontSize: '11px', color: '#64748B', fontFamily: 'monospace' }}>
                ₹{result.portfolio_value_before.toLocaleString()}
              </div>
            </div>

            <div>
              <div className="stress-stat-label">Stressed Portfolio Value</div>
              <div className="stress-stat-value" style={{ color: result.absolute_loss > 0 ? '#EF4444' : '#F3F4F6' }}>
                ₹{(result.portfolio_value_after / 10000000).toFixed(2)} Cr
              </div>
              <div style={{ fontSize: '11px', color: '#64748B', fontFamily: 'monospace' }}>
                ₹{result.portfolio_value_after.toLocaleString()}
              </div>
            </div>

            <div>
              <div className="stress-stat-label">Absolute Value Loss (ΔV)</div>
              <div className="stress-stat-value stress-stat-loss">
                {result.absolute_loss > 0 ? `-₹${result.absolute_loss.toLocaleString()}` : '₹0.00'}
              </div>
              <div style={{ fontSize: '11px', color: '#64748B' }}>
                Net balance sheet drawdown
              </div>
            </div>

            <div>
              <div className="stress-stat-label">Portfolio Drawdown (%)</div>
              <div className="stress-stat-value stress-stat-loss">
                {result.percentage_change.toFixed(2)}%
              </div>
              <div style={{ fontSize: '11px', color: result.is_triggered ? '#EF4444' : '#10B981' }}>
                {result.is_triggered ? 'Threshold Exceeded (Impact ≥ 7)' : 'Below Trigger (Drawdown: 0.0%)'}
              </div>
            </div>
          </div>

          <div style={{ marginTop: '24px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
              <h4 style={{ fontSize: '13px', fontWeight: 600, color: '#F3F4F6', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                Asset-by-Asset Sensitivity Matrix
              </h4>
              <span style={{ fontSize: '11px', color: '#64748B', fontFamily: 'monospace' }}>
                {result.asset_breakdown.length} ASSETS MONITORED
              </span>
            </div>

            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Security</th>
                    <th>Asset Class</th>
                    <th>Sector</th>
                    <th style={{ textAlign: 'right' }}>Baseline Value</th>
                    <th style={{ textAlign: 'center' }}>Shock Factor</th>
                    <th style={{ textAlign: 'right' }}>Post-Shock Value</th>
                    <th style={{ textAlign: 'right' }}>Δ Valuation</th>
                  </tr>
                </thead>
                <tbody>
                  {result.asset_breakdown.map((item) => (
                    <tr key={item.asset_id}>
                      <td>
                        <strong>{item.asset_name}</strong>
                        <div style={{ fontSize: '10px', color: '#64748B', fontFamily: 'monospace' }}>{item.asset_id}</div>
                      </td>
                      <td>{item.asset_type}</td>
                      <td style={{ color: '#94A3B8' }}>{item.sector}</td>
                      <td style={{ textAlign: 'right', fontFamily: 'monospace' }}>
                        ₹{item.value_before.toLocaleString()}
                      </td>
                      <td style={{ textAlign: 'center', fontFamily: 'monospace', fontWeight: 600, color: item.shock_pct < 0 ? '#EF4444' : item.shock_pct > 0 ? '#10B981' : '#94A3B8' }}>
                        {item.shock_pct > 0 ? `+${item.shock_pct}%` : `${item.shock_pct}%`}
                      </td>
                      <td style={{ textAlign: 'right', fontFamily: 'monospace' }}>
                        ₹{item.value_after.toLocaleString()}
                      </td>
                      <td style={{ textAlign: 'right', fontFamily: 'monospace', fontWeight: 600, color: item.change_value < 0 ? '#EF4444' : item.change_value > 0 ? '#10B981' : '#94A3B8' }}>
                        {item.change_value < 0 ? `-₹${Math.abs(item.change_value).toLocaleString()}` : item.change_value > 0 ? `+₹${item.change_value.toLocaleString()}` : '₹0'}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <div style={{ marginTop: '16px', padding: '12px 16px', background: '#0D1321', border: '1px solid #1F2937', borderRadius: '4px', fontSize: '11px', color: '#94A3B8' }}>
            <strong>Institutional Model Disclosure:</strong> {result.disclaimer} Illustrative sensitivity parameters calibrated for hackathon risk evaluation.
          </div>
        </div>
      )}
    </div>
  );
}
