import React, { useState } from 'react';

export default function RiskSignalTable({ signals = [], onTriggerStressTest }) {
  const [searchTerm, setSearchTerm] = useState('');
  const [filterCompany, setFilterCompany] = useState('');
  const [filterEvent, setFilterEvent] = useState('');
  const [filterImpact, setFilterImpact] = useState('');

  const companies = Array.from(new Set(signals.map(s => s.company))).filter(Boolean);
  const eventTypes = Array.from(new Set(signals.map(s => s.event_type))).filter(Boolean);

  const filteredSignals = signals.filter(s => {
    if (searchTerm) {
      const q = searchTerm.toLowerCase();
      const match = (s.company || '').toLowerCase().includes(q) ||
                    (s.summary || '').toLowerCase().includes(q) ||
                    (s.raw_text || '').toLowerCase().includes(q);
      if (!match) return false;
    }
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
        <div>
          <span>Risk Signal Terminal</span>
          <div style={{ fontSize: '11px', color: '#94A3B8', fontWeight: 400, marginTop: '2px' }}>
            Showing {filteredSignals.length} of {signals.length} structured risk records
          </div>
        </div>

        <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
          <input
            type="text"
            placeholder="Search headline / keywords..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            style={{ padding: '6px 12px', background: '#111726', color: '#F3F4F6', border: '1px solid #24304A', borderRadius: '4px', fontSize: '12px', minWidth: '180px' }}
          />

          <select
            value={filterCompany}
            onChange={(e) => setFilterCompany(e.target.value)}
            style={{ padding: '6px 10px', background: '#111726', color: '#F3F4F6', border: '1px solid #24304A', borderRadius: '4px', fontSize: '12px' }}
          >
            <option value="">All Entities</option>
            {companies.map(c => <option key={c} value={c}>{c}</option>)}
          </select>

          <select
            value={filterEvent}
            onChange={(e) => setFilterEvent(e.target.value)}
            style={{ padding: '6px 10px', background: '#111726', color: '#F3F4F6', border: '1px solid #24304A', borderRadius: '4px', fontSize: '12px' }}
          >
            <option value="">All Categories</option>
            {eventTypes.map(e => <option key={e} value={e}>{e}</option>)}
          </select>

          <select
            value={filterImpact}
            onChange={(e) => setFilterImpact(e.target.value)}
            style={{ padding: '6px 10px', background: '#111726', color: '#F3F4F6', border: '1px solid #24304A', borderRadius: '4px', fontSize: '12px' }}
          >
            <option value="">All Severities</option>
            <option value="7">Impact ≥ 7 (Trigger Active)</option>
            <option value="9">Impact ≥ 9 (Critical Only)</option>
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
              <th>Risk Rating</th>
              <th>Source Feed</th>
              <th>Event Summary</th>
              <th style={{ textAlign: 'center' }}>Action</th>
            </tr>
          </thead>
          <tbody>
            {filteredSignals.length === 0 ? (
              <tr>
                <td colSpan="9" style={{ textAlign: 'center', padding: '36px', color: '#94A3B8' }}>
                  No matching risk signals found.
                </td>
              </tr>
            ) : (
              filteredSignals.map(sig => (
                <tr key={sig.id}>
                  <td>
                    <strong>{sig.company}</strong>
                    <div style={{ fontSize: '10px', color: '#64748B', fontFamily: 'monospace' }}>{sig.id}</div>
                  </td>
                  <td>{sig.event_type}</td>
                  <td>
                    <span className={getSentimentBadge(sig.sentiment_label)}>
                      {sig.sentiment_label}
                    </span>
                  </td>
                  <td style={{ textAlign: 'right', fontFamily: 'monospace' }}>
                    {sig.sentiment_score > 0 ? `+${sig.sentiment_score.toFixed(2)}` : sig.sentiment_score.toFixed(2)}
                  </td>
                  <td style={{ textAlign: 'center', fontFamily: 'monospace', fontWeight: 700 }}>
                    <span style={{ color: sig.impact_score >= 7 ? '#EF4444' : '#FBBF24' }}>
                      {sig.impact_score}
                    </span> / 10
                  </td>
                  <td>
                    <span className={getRiskBadge(sig.risk_level)}>
                      {sig.risk_level}
                    </span>
                  </td>
                  <td style={{ fontSize: '11px', color: '#94A3B8' }}>{sig.source}</td>
                  <td style={{ fontSize: '12px', maxWidth: '320px', lineHeight: 1.4 }}>
                    {sig.summary}
                  </td>
                  <td style={{ textAlign: 'center' }}>
                    {sig.impact_score >= 7 ? (
                      <button
                        type="button"
                        onClick={() => onTriggerStressTest && onTriggerStressTest(sig.event_type, sig.impact_score)}
                        style={{
                          padding: '4px 10px',
                          fontSize: '11px',
                          fontWeight: 600,
                          background: 'rgba(239, 68, 68, 0.15)',
                          color: '#EF4444',
                          border: '1px solid rgba(239, 68, 68, 0.4)',
                          borderRadius: '4px',
                          cursor: 'pointer'
                        }}
                      >
                        ⚡ Shock
                      </button>
                    ) : (
                      <span style={{ fontSize: '11px', color: '#64748B' }}>—</span>
                    )}
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
