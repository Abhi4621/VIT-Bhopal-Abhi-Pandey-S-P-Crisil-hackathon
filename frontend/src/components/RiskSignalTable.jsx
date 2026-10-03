import React, { useState } from 'react';

export default function RiskSignalTable({ signals = [] }) {
  const [filterCompany, setFilterCompany] = useState('');
  const [filterEvent, setFilterEvent] = useState('');
  const [filterImpact, setFilterImpact] = useState('');

  const companies = Array.from(new Set(signals.map(s => s.company))).filter(Boolean);
  const eventTypes = Array.from(new Set(signals.map(s => s.event_type))).filter(Boolean);

  const filteredSignals = signals.filter(s => {
    if (filterCompany && s.company !== filterCompany) return false;
    if (filterEvent && s.event_type !== filterEvent) return false;
    if (filterImpact && s.impact_score < parseInt(filterImpact, 10)) return false;
    return true;
  });

  const getRiskBadge = (level) => {
    const l = (level || '').toLowerCase();
    if (l === 'critical') return 'badge badge-critical';
    if (l === 'high') return 'badge badge-high';
    if (l === 'moderate') return 'badge badge-moderate';
    return 'badge badge-low';
  };

  const getSentimentBadge = (label) => {
    const l = (label || '').toLowerCase();
    if (l === 'positive') return 'badge badge-positive';
    if (l === 'negative') return 'badge badge-negative';
    return 'badge badge-neutral';
  };

  return (
    <div className="card-section">
      <div className="card-title">
        <span>Structured Risk Signals</span>
        <div style={{ display: 'flex', gap: '10px' }}>
          <select
            value={filterCompany}
            onChange={(e) => setFilterCompany(e.target.value)}
            style={{ padding: '6px 12px', background: '#111726', color: '#F3F4F6', border: '1px solid #24304A', borderRadius: '4px', fontSize: '12px' }}
          >
            <option value="">All Companies</option>
            {companies.map(c => <option key={c} value={c}>{c}</option>)}
          </select>

          <select
            value={filterEvent}
            onChange={(e) => setFilterEvent(e.target.value)}
            style={{ padding: '6px 12px', background: '#111726', color: '#F3F4F6', border: '1px solid #24304A', borderRadius: '4px', fontSize: '12px' }}
          >
            <option value="">All Event Categories</option>
            {eventTypes.map(e => <option key={e} value={e}>{e}</option>)}
          </select>

          <select
            value={filterImpact}
            onChange={(e) => setFilterImpact(e.target.value)}
            style={{ padding: '6px 12px', background: '#111726', color: '#F3F4F6', border: '1px solid #24304A', borderRadius: '4px', fontSize: '12px' }}
          >
            <option value="">All Impact Scores</option>
            <option value="7">Impact ≥ 7 (Trigger Qualified)</option>
            <option value="9">Impact ≥ 9 (Critical)</option>
          </select>
        </div>
      </div>

      <div className="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Company</th>
              <th>Event Category</th>
              <th>Sentiment</th>
              <th style={{ textAlign: 'right' }}>Score</th>
              <th style={{ textAlign: 'center' }}>Impact</th>
              <th>Risk Level</th>
              <th>Source</th>
              <th>Summary</th>
            </tr>
          </thead>
          <tbody>
            {filteredSignals.length === 0 ? (
              <tr>
                <td colSpan="8" style={{ textAlign: 'center', padding: '30px', color: '#94A3B8' }}>
                  No matching risk signals found.
                </td>
              </tr>
            ) : (
              filteredSignals.map(sig => (
                <tr key={sig.id}>
                  <td><strong>{sig.company}</strong></td>
                  <td>{sig.event_type}</td>
                  <td>
                    <span className={getSentimentBadge(sig.sentiment_label)}>
                      {sig.sentiment_label}
                    </span>
                  </td>
                  <td style={{ textAlign: 'right', fontFamily: 'monospace' }}>
                    {sig.sentiment_score > 0 ? `+${sig.sentiment_score.toFixed(2)}` : sig.sentiment_score.toFixed(2)}
                  </td>
                  <td style={{ textAlign: 'center', fontFamily: 'monospace', fontWeight: 'bold' }}>
                    {sig.impact_score} / 10
                  </td>
                  <td>
                    <span className={getRiskBadge(sig.risk_level)}>
                      {sig.risk_level}
                    </span>
                  </td>
                  <td style={{ fontSize: '12px', opacity: 0.8 }}>{sig.source}</td>
                  <td style={{ fontSize: '12px', maxWidth: '300px', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                    {sig.summary}
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
