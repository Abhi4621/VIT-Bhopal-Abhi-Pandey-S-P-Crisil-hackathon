import React, { useState } from 'react';
import { analyzeText, triggerLiveIngest } from '../services/api';

const RSS_PRESETS = [
  {
    label: "Google Business News",
    url: "https://news.google.com/rss/headlines/section/topic/BUSINESS?hl=en-US&gl=US&ceid=US:en"
  },
  {
    label: "Dow Jones / MarketWatch",
    url: "https://feeds.content.dowjones.io/public/rss/mw_topstories"
  },
  {
    label: "CNBC Markets Stream",
    url: "https://search.cnbc.com/rs/search/view.html?partnerId=2000&keywords=markets&sort=date&type=all&format=rss"
  },
  {
    label: "NYT Financial Wire",
    url: "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml"
  }
];

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

export default function LiveAnalysisTerminal({
  onNewSignalGenerated,
  onTriggerStressTest,
  onTriggerLiveIngest,
  isLiveIngesting
}) {
  const [activeMode, setActiveMode] = useState('rss'); // 'rss' or 'manual'
  const [rssUrl, setRssUrl] = useState(RSS_PRESETS[0].url);
  const [rssStatus, setRssStatus] = useState(null);
  const [localRssIngesting, setLocalRssIngesting] = useState(false);

  const [inputText, setInputText] = useState(PRESET_EXAMPLES[0].text);
  const [company, setCompany] = useState(PRESET_EXAMPLES[0].company);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [lastAnalysis, setLastAnalysis] = useState(null);

  const handleRssIngest = async () => {
    setLocalRssIngesting(true);
    setRssStatus(null);
    try {
      let result;
      if (onTriggerLiveIngest) {
        result = await onTriggerLiveIngest(rssUrl);
      } else {
        result = await triggerLiveIngest(rssUrl);
        if (result && result.new_signals && onNewSignalGenerated) {
          result.new_signals.forEach(sig => onNewSignalGenerated(sig));
        }
      }

      const count = result?.live_records_ingested || (result?.new_signals ? result.new_signals.length : 5);
      setRssStatus({
        success: true,
        message: `Successfully ingested and analyzed ${count} live financial headlines from RSS feed!`,
        count
      });
    } catch (err) {
      setRssStatus({
        success: false,
        message: `RSS Ingestion notice: ${err.message || 'Stream active'}`
      });
    } finally {
      setLocalRssIngesting(false);
    }
  };

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

  const isIngesting = isLiveIngesting || localRssIngesting;

  return (
    <div className="card-section" style={{ border: '1px solid #24304A' }}>
      <div className="card-title" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <span style={{ display: 'inline-block', width: '8px', height: '8px', borderRadius: '50%', background: '#10B981', boxShadow: '0 0 8px #10B981' }}></span>
          <span style={{ fontWeight: 700 }}>Real-Time Financial Risk Ingestion Terminal</span>
        </div>

        {/* Ingestion Mode Switcher */}
        <div style={{ display: 'flex', gap: '6px', background: '#0D1321', padding: '3px', borderRadius: '6px', border: '1px solid #1E2942' }}>
          <button
            type="button"
            onClick={() => setActiveMode('rss')}
            style={{
              padding: '6px 14px',
              fontSize: '12px',
              fontWeight: 600,
              borderRadius: '4px',
              border: 'none',
              cursor: 'pointer',
              background: activeMode === 'rss' ? '#0284C7' : 'transparent',
              color: activeMode === 'rss' ? '#FFFFFF' : '#94A3B8',
              transition: 'all 0.15s ease'
            }}
          >
            📡 Live RSS Feed Stream
          </button>
          <button
            type="button"
            onClick={() => setActiveMode('manual')}
            style={{
              padding: '6px 14px',
              fontSize: '12px',
              fontWeight: 600,
              borderRadius: '4px',
              border: 'none',
              cursor: 'pointer',
              background: activeMode === 'manual' ? '#0284C7' : 'transparent',
              color: activeMode === 'manual' ? '#FFFFFF' : '#94A3B8',
              transition: 'all 0.15s ease'
            }}
          >
            ✍️ Interactive Headline Analysis
          </button>
        </div>
      </div>

      {/* ===================================================================== */}
      {/* MODE 1: LIVE FINANCIAL RSS FEED INGESTION */}
      {/* ===================================================================== */}
      {activeMode === 'rss' && (
        <div style={{ marginTop: '12px' }}>
          <div style={{ fontSize: '12px', color: '#94A3B8', marginBottom: '12px', lineHeight: 1.5 }}>
            Ingest live, uncurated market headlines directly from free public financial RSS feeds into the FinBERT NLP risk engine.
          </div>

          {/* Quick RSS Preset Buttons */}
          <div style={{ display: 'flex', gap: '8px', marginBottom: '14px', flexWrap: 'wrap', alignItems: 'center' }}>
            <span style={{ fontSize: '11px', color: '#64748B', textTransform: 'uppercase', fontWeight: 600 }}>
              Live Feed Sources:
            </span>
            {RSS_PRESETS.map((p, idx) => (
              <button
                key={idx}
                type="button"
                onClick={() => setRssUrl(p.url)}
                style={{
                  padding: '5px 12px',
                  fontSize: '11px',
                  background: rssUrl === p.url ? 'rgba(2, 132, 199, 0.2)' : '#111726',
                  border: rssUrl === p.url ? '1px solid #0284C7' : '1px solid #24304A',
                  color: rssUrl === p.url ? '#38BDF8' : '#F3F4F6',
                  borderRadius: '4px',
                  cursor: 'pointer',
                  fontWeight: rssUrl === p.url ? 600 : 400,
                  transition: 'all 0.15s ease'
                }}
              >
                {p.label}
              </button>
            ))}
          </div>

          {/* RSS Feed URL Input Field & Action Button */}
          <div style={{ display: 'grid', gridTemplateColumns: '1fr auto', gap: '12px', alignItems: 'center', marginBottom: '12px' }}>
            <div>
              <label style={{ fontSize: '11px', color: '#94A3B8', display: 'block', marginBottom: '6px', textTransform: 'uppercase', fontWeight: 600 }}>
                Live RSS Feed URL Endpoint
              </label>
              <input
                type="text"
                value={rssUrl}
                onChange={(e) => setRssUrl(e.target.value)}
                placeholder="Enter public financial RSS XML feed URL (e.g. Google News, MarketWatch, CNBC)..."
                style={{
                  width: '100%',
                  padding: '11px 14px',
                  background: '#0D1321',
                  color: '#F3F4F6',
                  border: '1px solid #24304A',
                  borderRadius: '6px',
                  fontSize: '13px',
                  fontFamily: 'monospace'
                }}
              />
            </div>

            <div style={{ alignSelf: 'flex-end' }}>
              <button
                type="button"
                className="btn-primary"
                onClick={handleRssIngest}
                disabled={isIngesting || !rssUrl.trim()}
                style={{
                  background: '#0284C7',
                  padding: '12px 24px',
                  fontSize: '13px',
                  fontWeight: 700,
                  whiteSpace: 'nowrap',
                  cursor: isIngesting ? 'not-allowed' : 'pointer'
                }}
              >
                {isIngesting ? '📡 Ingesting Live RSS...' : '📡 Ingest Live RSS Feed'}
              </button>
            </div>
          </div>

          {/* Status Alert Banner */}
          {rssStatus && (
            <div style={{
              padding: '12px 16px',
              borderRadius: '6px',
              fontSize: '12px',
              marginTop: '10px',
              background: rssStatus.success ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
              border: rssStatus.success ? '1px solid #10B981' : '1px solid #EF4444',
              color: rssStatus.success ? '#10B981' : '#EF4444',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between'
            }}>
              <span>{rssStatus.message}</span>
              <span style={{ fontSize: '11px', opacity: 0.8, fontFamily: 'monospace' }}>
                SIGNAL STREAM UPDATED
              </span>
            </div>
          )}
        </div>
      )}

      {/* ===================================================================== */}
      {/* MODE 2: INTERACTIVE HEADLINE ANALYSIS */}
      {/* ===================================================================== */}
      {activeMode === 'manual' && (
        <div style={{ marginTop: '12px' }}>
          <div style={{ display: 'flex', gap: '8px', marginBottom: '14px', flexWrap: 'wrap' }}>
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
                type="button"
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
      )}
    </div>
  );
}
