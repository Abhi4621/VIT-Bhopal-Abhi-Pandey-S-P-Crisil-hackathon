import React, { useState } from 'react';
import { runStressTest } from '../services/api';

export default function StressTestPanel() {
  const [eventType, setEventType] = useState('Geopolitical');
  const [impactScore, setImpactScore] = useState(9);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleRunTest = async () => {
    setLoading(true);
    try {
      const data = await runStressTest(eventType, parseInt(impactScore, 10));
      setResult(data);
    } catch (err) {
      alert('Error running stress test simulation');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card-section">
      <div className="card-title">
        <span>Strategic Portfolio Stress Testing (Module B)</span>
        <button
          className="btn-primary"
          onClick={handleRunTest}
          disabled={loading}
          style={{ background: '#DC2626' }}
        >
          {loading ? 'Simulating Shocks...' : 'RUN STRESS TEST'}
        </button>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginBottom: '20px' }}>
        <div>
          <label style={{ fontSize: '12px', color: '#94A3B8', display: 'block', marginBottom: '6px' }}>
            Event Scenario Category
          </label>
          <select
            value={eventType}
            onChange={(e) => setEventType(e.target.value)}
            style={{ width: '100%', padding: '10px 14px', background: '#111726', color: '#F3F4F6', border: '1px solid #24304A', borderRadius: '6px' }}
          >
            <option value="Geopolitical">Geopolitical (Energy/Freight Shocks)</option>
            <option value="Macroeconomic">Macroeconomic (Interest Rate / Inflation)</option>
            <option value="Credit Event">Credit Event (Debt / Loan Spread Widening)</option>
            <option value="Regulatory">Regulatory (Compliance & Tariffs)</option>
          </select>
        </div>

        <div>
          <label style={{ fontSize: '12px', color: '#94A3B8', display: 'block', marginBottom: '6px' }}>
            Prototype Risk Impact Score: <strong>{impactScore} / 10</strong> ({impactScore >= 7 ? 'Trigger Active' : 'No Trigger'})
          </label>
          <input
            type="range"
            min="1"
            max="10"
            value={impactScore}
            onChange={(e) => setImpactScore(e.target.value)}
            style={{ width: '100%', accentColor: impactScore >= 7 ? '#EF4444' : '#10B981', marginTop: '10px' }}
          />
        </div>
      </div>

      {result && (
        <div style={{ marginTop: '20px' }}>
          <div className="stress-result-grid">
            <div>
              <div className="stress-stat-label">Baseline Portfolio Value</div>
              <div className="stress-stat-value">₹{result.portfolio_value_before.toLocaleString()}</div>
            </div>

            <div>
              <div className="stress-stat-label">Stressed Portfolio Value</div>
              <div className="stress-stat-value">₹{result.portfolio_value_after.toLocaleString()}</div>
            </div>

            <div>
              <div className="stress-stat-label">Absolute Net Loss</div>
              <div className="stress-stat-value stress-stat-loss">
                {result.absolute_loss > 0 ? `-₹${result.absolute_loss.toLocaleString()}` : '₹0.00'}
              </div>
            </div>

            <div>
              <div className="stress-stat-label">Portfolio Drawdown (%)</div>
              <div className="stress-stat-value stress-stat-loss">
                {result.percentage_change.toFixed(2)}%
              </div>
            </div>
          </div>

          <div style={{ marginTop: '20px' }}>
            <h4 style={{ fontSize: '14px', color: '#F3F4F6', marginBottom: '12px' }}>
              Asset-Level Scenario Impact Breakdown
            </h4>
            <div className="table-wrapper">
              <table>
                <thead>
                  <tr>
                    <th>Asset ID</th>
                    <th>Asset Name</th>
                    <th>Type</th>
                    <th>Sector</th>
                    <th style={{ textAlign: 'right' }}>Before Value</th>
                    <th style={{ textAlign: 'center' }}>Shock %</th>
                    <th style={{ textAlign: 'right' }}>After Value</th>
                    <th style={{ textAlign: 'right' }}>Delta Value</th>
                  </tr>
                </thead>
                <tbody>
                  {result.asset_breakdown.map((item) => (
                    <tr key={item.asset_id}>
                      <td style={{ fontFamily: 'monospace' }}>{item.asset_id}</td>
                      <td><strong>{item.asset_name}</strong></td>
                      <td>{item.asset_type}</td>
                      <td style={{ color: '#94A3B8' }}>{item.sector}</td>
                      <td style={{ textAlign: 'right', fontFamily: 'monospace' }}>
                        ₹{item.value_before.toLocaleString()}
                      </td>
                      <td style={{ textAlign: 'center', fontFamily: 'monospace', color: item.shock_pct < 0 ? '#EF4444' : item.shock_pct > 0 ? '#10B981' : '#94A3B8' }}>
                        {item.shock_pct > 0 ? `+${item.shock_pct}%` : `${item.shock_pct}%`}
                      </td>
                      <td style={{ textAlign: 'right', fontFamily: 'monospace' }}>
                        ₹{item.value_after.toLocaleString()}
                      </td>
                      <td style={{ textAlign: 'right', fontFamily: 'monospace', color: item.change_value < 0 ? '#EF4444' : '#10B981' }}>
                        {item.change_value < 0 ? `-₹${Math.abs(item.change_value).toLocaleString()}` : `₹${item.change_value.toLocaleString()}`}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          <div style={{ marginTop: '14px', fontSize: '11px', color: '#94A3B8', fontStyle: 'italic' }}>
            * {result.disclaimer}
          </div>
        </div>
      )}
    </div>
  );
}
