import React from 'react';

export default function ChartsPanel({ signals = [] }) {
  // Event category counts
  const categoryCounts = {};
  signals.forEach(s => {
    categoryCounts[s.event_type] = (categoryCounts[s.event_type] || 0) + 1;
  });

  // Sentiment distribution (Positive, Neutral, Negative)
  const sentimentCounts = {
    Positive: signals.filter(s => s.sentiment_label === 'Positive').length,
    Neutral: signals.filter(s => s.sentiment_label === 'Neutral').length,
    Negative: signals.filter(s => s.sentiment_label === 'Negative').length,
  };

  const total = signals.length || 1;

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px', marginBottom: '28px' }}>
      {/* Event Category Distribution */}
      <div className="card-section" style={{ marginBottom: 0 }}>
        <div className="card-title">Event Category Breakdown</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
          {Object.entries(categoryCounts).map(([cat, count]) => {
            const pct = Math.round((count / total) * 100);
            return (
              <div key={cat}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '12px', marginBottom: '4px' }}>
                  <span>{cat}</span>
                  <span style={{ fontFamily: 'monospace', color: '#94A3B8' }}>{count} ({pct}%)</span>
                </div>
                <div style={{ height: '8px', background: '#111726', borderRadius: '4px', overflow: 'hidden' }}>
                  <div style={{ width: `${pct}%`, height: '100%', background: '#3B82F6', borderRadius: '4px' }}></div>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Sentiment Distribution */}
      <div className="card-section" style={{ marginBottom: 0 }}>
        <div className="card-title">Sentiment Polarity Distribution</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: '16px', marginTop: '10px' }}>
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '12px', marginBottom: '4px' }}>
              <span style={{ color: '#10B981', fontWeight: 600 }}>Positive Sentiment</span>
              <span style={{ fontFamily: 'monospace' }}>{sentimentCounts.Positive} ({Math.round(sentimentCounts.Positive / total * 100)}%)</span>
            </div>
            <div style={{ height: '10px', background: '#111726', borderRadius: '4px', overflow: 'hidden' }}>
              <div style={{ width: `${Math.round(sentimentCounts.Positive / total * 100)}%`, height: '100%', background: '#10B981' }}></div>
            </div>
          </div>

          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '12px', marginBottom: '4px' }}>
              <span style={{ color: '#94A3B8', fontWeight: 600 }}>Neutral Sentiment</span>
              <span style={{ fontFamily: 'monospace' }}>{sentimentCounts.Neutral} ({Math.round(sentimentCounts.Neutral / total * 100)}%)</span>
            </div>
            <div style={{ height: '10px', background: '#111726', borderRadius: '4px', overflow: 'hidden' }}>
              <div style={{ width: `${Math.round(sentimentCounts.Neutral / total * 100)}%`, height: '100%', background: '#64748B' }}></div>
            </div>
          </div>

          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '12px', marginBottom: '4px' }}>
              <span style={{ color: '#EF4444', fontWeight: 600 }}>Negative Sentiment (Risk Elevating)</span>
              <span style={{ fontFamily: 'monospace' }}>{sentimentCounts.Negative} ({Math.round(sentimentCounts.Negative / total * 100)}%)</span>
            </div>
            <div style={{ height: '10px', background: '#111726', borderRadius: '4px', overflow: 'hidden' }}>
              <div style={{ width: `${Math.round(sentimentCounts.Negative / total * 100)}%`, height: '100%', background: '#EF4444' }}></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
