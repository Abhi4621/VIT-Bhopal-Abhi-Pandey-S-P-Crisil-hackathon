import React from 'react';

export default function MetricsCards({ signals = [], portfolio = null }) {
  const totalSignals = signals.length;
  const highImpactCount = signals.filter(s => s.impact_score >= 7).length;

  const avgSentiment = totalSignals > 0
    ? (signals.reduce((acc, s) => acc + s.sentiment_score, 0) / totalSignals).toFixed(2)
    : '0.00';

  const totalValue = portfolio?.total_value
    ? `₹${(portfolio.total_value / 1000000).toFixed(2)}M`
    : '₹14.00M';

  return (
    <div className="metrics-grid">
      <div className="metric-card">
        <div className="metric-label">Total Signals Ingested</div>
        <div className="metric-value">{totalSignals}</div>
        <div className="metric-sub">Multi-source news & social feed</div>
      </div>

      <div className="metric-card">
        <div className="metric-label">High Impact Alerts (≥ 7)</div>
        <div className="metric-value" style={{ color: highImpactCount > 0 ? '#EF4444' : '#10B981' }}>
          {highImpactCount}
        </div>
        <div className="metric-sub">Stress test threshold qualified</div>
      </div>

      <div className="metric-card">
        <div className="metric-label">Average Market Sentiment</div>
        <div className="metric-value" style={{ color: avgSentiment < 0 ? '#EF4444' : '#10B981' }}>
          {avgSentiment > 0 ? `+${avgSentiment}` : avgSentiment}
        </div>
        <div className="metric-sub">Continuous normalized [-1.0, +1.0]</div>
      </div>

      <div className="metric-card">
        <div className="metric-label">Portfolio Exposure (Baseline)</div>
        <div className="metric-value">{totalValue}</div>
        <div className="metric-sub">10 multi-asset synthetic holdings</div>
      </div>
    </div>
  );
}
