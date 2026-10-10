import React from 'react';

/**
 * Clean & Simple Graph Flow Chart for RiskPulse System Architecture.
 * Shows the exact end-to-end execution path from raw news to stress decision.
 */
export default function SystemArchitectureDiagram() {
  const steps = [
    {
      num: '01',
      title: 'Data Ingestion',
      badge: 'Layer 1 & 2',
      color: '#38BDF8',
      desc: 'Raw news collected from RSS feeds, news wires, and user input.',
      details: 'HTML unescaping, URL removal & company alias resolution.'
    },
    {
      num: '02',
      title: 'NLP & Sentiment Analysis',
      badge: 'Module A',
      color: '#818CF8',
      desc: 'Scores financial sentiment and classifies into 8 event taxonomies.',
      details: 'Sentiment (-1.0 to +1.0) with negation & intensifier handling.'
    },
    {
      num: '03',
      title: 'Impact Scoring & Gate',
      badge: 'Gatekeeper',
      color: '#F43F5E',
      isGate: true,
      desc: 'Calculates severity score (1–10). Evaluates trigger threshold.',
      details: 'Impact ≥ 7 automatically triggers Portfolio Stress Testing.'
    },
    {
      num: '04',
      title: 'Portfolio Stress Test',
      badge: 'Module B',
      color: '#F59E0B',
      desc: 'Applies scenario haircuts across multi-asset allocations.',
      details: 'Calculates stressed values, net loss ($), and drawdown (%).'
    },
    {
      num: '05',
      title: 'Results & Dashboard',
      badge: 'Presentation',
      color: '#10B981',
      desc: 'Displays real-time telemetry, risk signals, and sector heatmaps.',
      details: 'Live terminal, structured audit stream, and executive cards.'
    }
  ];

  return (
    <div style={{ color: '#F3F4F6', fontFamily: "'Inter', sans-serif" }}>
      {/* Header */}
      <div style={{
        background: '#111726',
        border: '1px solid #1E293B',
        borderRadius: '8px',
        padding: '16px 20px',
        marginBottom: '24px',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        flexWrap: 'wrap',
        gap: '12px'
      }}>
        <div>
          <h2 style={{ fontSize: '18px', fontWeight: 700, color: '#FFFFFF', margin: 0 }}>
            System Architecture Flow Chart
          </h2>
          <p style={{ color: '#94A3B8', fontSize: '13px', margin: '4px 0 0 0' }}>
            Deterministic End-to-End Pipeline: Text Ingestion → Sentiment Engine → Impact Gate → Stress Testing
          </p>
        </div>
        <div style={{
          background: '#0B0F19',
          border: '1px solid #1E293B',
          borderRadius: '6px',
          padding: '6px 12px',
          fontSize: '12px',
          color: '#38BDF8',
          fontWeight: 600
        }}>
          Abhi Pandey · VIT Bhopal University · S&P Global & CRISIL Hackathon 2026
        </div>
      </div>

      {/* Clean Vertical Flow Chart */}
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '0px',
        maxWidth: '700px',
        margin: '0 auto'
      }}>
        {steps.map((step, idx) => (
          <React.Fragment key={step.num}>
            {/* Step Card */}
            <div style={{
              width: '100%',
              background: step.isGate ? 'linear-gradient(135deg, #1E1B4B 0%, #311042 100%)' : '#151D30',
              border: `1px solid ${step.isGate ? '#EF4444' : '#24304A'}`,
              borderRadius: '8px',
              padding: '16px 20px',
              boxShadow: step.isGate ? '0 0 16px rgba(239, 68, 68, 0.2)' : '0 2px 8px rgba(0,0,0,0.2)',
              position: 'relative'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <span style={{
                    background: `${step.color}22`,
                    color: step.color,
                    border: `1px solid ${step.color}66`,
                    padding: '2px 8px',
                    borderRadius: '4px',
                    fontSize: '11px',
                    fontWeight: 700,
                    fontFamily: 'monospace'
                  }}>
                    {step.num}
                  </span>
                  <h3 style={{ fontSize: '16px', fontWeight: 700, color: step.isGate ? '#FCA5A5' : '#FFFFFF', margin: 0 }}>
                    {step.title}
                  </h3>
                </div>
                <span style={{
                  fontSize: '11px',
                  padding: '2px 8px',
                  borderRadius: '12px',
                  fontWeight: 600,
                  background: step.isGate ? '#DC2626' : '#1E293B',
                  color: '#FFFFFF'
                }}>
                  {step.badge}
                </span>
              </div>

              <p style={{ color: '#E2E8F0', fontSize: '13px', margin: '0 0 4px 0', lineHeight: 1.5 }}>
                {step.desc}
              </p>
              <div style={{ color: '#94A3B8', fontSize: '12px', fontFamily: 'monospace' }}>
                ↳ {step.details}
              </div>
            </div>

            {/* Connecting Flow Arrow */}
            {idx < steps.length - 1 && (
              <div style={{
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                margin: '8px 0'
              }}>
                <div style={{ width: '2px', height: '16px', background: idx === 1 ? '#EF4444' : '#38BDF8' }}></div>
                <div style={{
                  fontSize: '10px',
                  fontFamily: 'monospace',
                  color: idx === 1 ? '#EF4444' : '#38BDF8',
                  background: '#0B0F19',
                  padding: '2px 8px',
                  borderRadius: '10px',
                  border: `1px solid ${idx === 1 ? '#EF4444' : '#24304A'}`,
                  margin: '2px 0'
                }}>
                  {idx === 0 && '↓ Cleaned Text'}
                  {idx === 1 && '↓ Sentiment & Event'}
                  {idx === 2 && '⚡ Impact ≥ 7 Trigger'}
                  {idx === 3 && '↓ Stressed Valuation'}
                </div>
                <div style={{ width: '2px', height: '16px', background: idx === 1 ? '#EF4444' : '#38BDF8' }}></div>
                <div style={{
                  width: 0,
                  height: 0,
                  borderLeft: '5px solid transparent',
                  borderRight: '5px solid transparent',
                  borderTop: `6px solid ${idx === 1 ? '#EF4444' : '#38BDF8'}`
                }}></div>
              </div>
            )}
          </React.Fragment>
        ))}
      </div>
    </div>
  );
}
