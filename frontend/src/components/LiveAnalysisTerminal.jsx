import React, { useState } from 'react';
import { analyzeText } from '../services/api';

const PRESET_EXAMPLES = [
  {
    label: "Geopolitical Crisis",
    company: "Tata Motors",
    text: "Tata Motors announces assembly shutdowns across major manufacturing hubs due to escalated maritime embargoes and semiconductor freight blockades."
  },
  {
    label: "Credit Rating Cut",
    company: "Adani Enterprises",
    text: "Credit rating agency downgrades Adani Enterprises debt instruments to negative outlook citing refinancing pressure and liquidity buffer squeeze."
  },
  {
    label: "Central Bank Rate Hike",
    company: "ICICI Bank",
    text: "Central bank unexpectedly raises benchmark repo rate by 50 basis points to combat accelerating core inflation, squeezing banking margin outlooks."
  },
  {
    label: "Quarterly Earnings Beat",
    company: "HDFC Bank",
    text: "HDFC Bank reports record quarterly net profit growth of 18% with non-performing loans declining to multi-year historic lows."
  }
];

export default function LiveAnalysisTerminal({ onNewSignalGenerated, onTriggerStressTest }) {
  const [inputText, setInputText] = useState(PRESET_EXAMPLES[0].text);
  const [company, setCompany] = useState(PRESET_EXAMPLES[0].company);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [lastAnalysis, setLastAnalysis] = useState(null);

  const handleAnalyze = async () => {
    if (!inputText.trim()) return;
    setIsAnalyzing(true);
    try {
      const result = await analyzeText(inputText, company);
      setLastAnalysis(result);
      if (onNewSignalGenerated) {
        onNewSignalGenerated(result);
      }
    } catch (err) {
      alert('Error during risk signal analysis');
    } finally {
      setIsAnalyzing(false);
    }
  };

  const loadPreset = (preset) => {
    setInputText(preset.text);
    setCompany(preset.company);
    setLastAnalysis(null);
  };

  return (
    <div className="card-section">
      <div className="card-title">
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ display: 'inline-block', width: '8px', height: '8px', borderRadius: '50%', background: '#10B981' }}></span>
          <span>Live Risk Signal Ingestion Terminal</span>
        </div>
        <div style={{ fontSize: '11px', color: '#94A3B8', fontFamily: 'monospace' }}>
          NLP ENGINE: ONLINE
        </div>
      </div>

      <div style={{ display: 'flex', gap: '8px', marginBottom: '16px', flexWrap: 'wrap' }}>
        <span style={{ fontSize: '12px', color: '#94A3B8', alignSelf: 'center', marginRight: '6px' }}>
          Preset Market Events:
        </span>
        {PRESET_EXAMPLES.map((p, idx) => (
          <button
            key={idx}
            type="button"
            onClick={() => loadPreset(p)}
            style={{
              padding: '5px 12px',
              fontSize: '11px',
              background: '#111726',
              border: '1px solid #24304A',
              color: '#F3F4F6',
              borderRadius: '4px',
              cursor: 'pointer',
              transition: 'all 0.15s ease'
            }}
            onMouseOver={(e) => e.currentTarget.style.borderColor = '#3B82F6'}
            onMouseOut={(e) => e.currentTarget.style.borderColor = '#24304A'}
          >
            {p.label} ({p.company})
          </button>
        ))}
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr', gap: '16px', marginBottom: '16px' }}>
        <div>
          <label style={{ fontSize: '11px', color: '#94A3B8', display: 'block', marginBottom: '6px', textTransform: 'uppercase' }}>
            Unstructured Financial Text / Wire Headline
          </label>
          <textarea
            rows={3}
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Paste financial news article or analyst commentary..."
            style={{
              width: '100%',
              padding: '10px 12px',
              background: '#0D1321',
              color: '#F3F4F6',
              border: '1px solid #24304A',
              borderRadius: '6px',
              fontSize: '13px',
              fontFamily: 'Inter, sans-serif',
              resize: 'vertical'
            }}
          />
        </div>

        <div>
          <label style={{ fontSize: '11px', color: '#94A3B8', display: 'block', marginBottom: '6px', textTransform: 'uppercase' }}>
            Entity / Target Company
          </label>
          <input
            type="text"
            value={company}
            onChange={(e) => setCompany(e.target.value)}
            placeholder="e.g. Tata Motors, Reliance"
            style={{
              width: '100%',
              padding: '10px 12px',
              background: '#0D1321',
              color: '#F3F4F6',
              border: '1px solid #24304A',
              borderRadius: '6px',
              fontSize: '13px',
              marginBottom: '10px'
            }}
          />
          <button
            className="btn-primary"
            onClick={handleAnalyze}
            disabled={isAnalyzing}
            style={{ width: '100%', justifyContent: 'center' }}
          >
            {isAnalyzing ? 'Processing NLP Pipeline...' : '⚡ Generate Structured Risk Signal'}
          </button>
        </div>
      </div>

      {lastAnalysis && (
        <div style={{
          padding: '16px',
          background: '#0D1321',
          border: '1px solid #24304A',
          borderRadius: '6px',
          marginTop: '12px'
        }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
            <span style={{ fontSize: '12px', fontWeight: 600, color: '#38BDF8', textTransform: 'uppercase' }}>
              Structured Risk Signal Output
            </span>
            {lastAnalysis.is_stress_test_trigger && (
              <span className="badge badge-critical" style={{ fontSize: '12px', padding: '4px 10px' }}>
                ⚠️ Stress Test Trigger Qualified (Impact ≥ 7)
              </span>
            )}
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: '12px' }}>
            <div style={{ background: '#111726', padding: '10px', borderRadius: '4px', border: '1px solid #1E2942' }}>
              <div style={{ fontSize: '10px', color: '#94A3B8', textTransform: 'uppercase' }}>Detected Entity</div>
              <div style={{ fontSize: '14px', fontWeight: 700, marginTop: '2px', color: '#FFFFFF' }}>{lastAnalysis.company}</div>
            </div>

            <div style={{ background: '#111726', padding: '10px', borderRadius: '4px', border: '1px solid #1E2942' }}>
              <div style={{ fontSize: '10px', color: '#94A3B8', textTransform: 'uppercase' }}>Sentiment Score</div>
              <div style={{ fontSize: '14px', fontWeight: 700, marginTop: '2px', fontFamily: 'monospace', color: lastAnalysis.sentiment_score < 0 ? '#EF4444' : '#10B981' }}>
                {lastAnalysis.sentiment_score > 0 ? `+${lastAnalysis.sentiment_score.toFixed(2)}` : lastAnalysis.sentiment_score.toFixed(2)} ({lastAnalysis.sentiment_label})
              </div>
            </div>

            <div style={{ background: '#111726', padding: '10px', borderRadius: '4px', border: '1px solid #1E2942' }}>
              <div style={{ fontSize: '10px', color: '#94A3B8', textTransform: 'uppercase' }}>Event Taxonomy</div>
              <div style={{ fontSize: '14px', fontWeight: 700, marginTop: '2px', color: '#FFFFFF' }}>{lastAnalysis.event_type}</div>
            </div>

            <div style={{ background: '#111726', padding: '10px', borderRadius: '4px', border: '1px solid #1E2942' }}>
              <div style={{ fontSize: '10px', color: '#94A3B8', textTransform: 'uppercase' }}>Prototype Impact Score</div>
              <div style={{ fontSize: '14px', fontWeight: 700, marginTop: '2px', fontFamily: 'monospace', color: lastAnalysis.impact_score >= 7 ? '#EF4444' : '#FBBF24' }}>
                {lastAnalysis.impact_score} / 10 ({lastAnalysis.risk_level})
              </div>
            </div>

            <div style={{ background: '#111726', padding: '10px', borderRadius: '4px', border: '1px solid #1E2942', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
              {lastAnalysis.is_stress_test_trigger ? (
                <button
                  type="button"
                  onClick={() => onTriggerStressTest && onTriggerStressTest(lastAnalysis.event_type, lastAnalysis.impact_score)}
                  style={{
                    background: '#DC2626',
                    color: '#FFFFFF',
                    border: 'none',
                    borderRadius: '4px',
                    padding: '8px',
                    fontSize: '11px',
                    fontWeight: 700,
                    cursor: 'pointer'
                  }}
                >
                  ⚡ Shock Portfolio
                </button>
              ) : (
                <span style={{ fontSize: '11px', color: '#94A3B8', textAlign: 'center' }}>
                  Below Threshold (&lt; 7)
                </span>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
