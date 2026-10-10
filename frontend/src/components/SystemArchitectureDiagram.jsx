import React, { useState } from 'react';

/**
 * Technical System Architecture Diagram for RiskPulse.
 * Accurately reflects the codebase components, data flow, Module A / Module B boundaries,
 * and integration points verified across:
 * - backend/ingestion (cleaner.py, rss_loader.py, news_loader.py, social_loader.py)
 * - backend/nlp (risk_engine.py, sentiment.py, event_classifier.py, impact_score.py)
 * - backend/api (routes.py, schemas.py)
 * - backend/database (db.py, SQLite risk_signals)
 * - backend/portfolio (stress_test.py, portfolio.py)
 * - frontend/src/components (MetricsCards, RiskSignalTable, StressTestPanel, LiveAnalysisTerminal, ChartsPanel)
 */

export default function SystemArchitectureDiagram() {
  const [activeLayer, setActiveLayer] = useState(null);
  const [selectedNode, setSelectedNode] = useState(null);

  const layers = [
    {
      id: 'layer1',
      number: 'Layer 1',
      title: 'Data Sources & Ingestion Streams',
      subtitle: 'Multi-Source Financial Text Acquisition',
      color: '#38BDF8',
      nodes: [
        {
          id: 'src-wires',
          title: 'Financial News Wires',
          tech: 'news_loader.py',
          status: 'implemented',
          desc: '10 structured wire reports with timestamps, editorial headlines, and contextual body text.',
          details: 'Ingests news from sources including Reuters, Dow Jones, Bloomberg benchmark formats.'
        },
        {
          id: 'src-social',
          title: 'Market Social Feeds',
          tech: 'social_loader.py',
          status: 'implemented',
          desc: '10 real-time analyst posts and market sentiment commentary across financial social channels.',
          details: 'Captures short-form chatter with emojis, ticker tags ($NVDA, $TSLA), and market sentiment.'
        },
        {
          id: 'src-rss',
          title: 'Live Financial RSS Feeds',
          tech: 'rss_loader.py (urllib + xml)',
          status: 'implemented',
          desc: 'Asynchronous fetcher with Google News, MarketWatch, CNBC presets and custom RSS URL input.',
          details: 'Direct HTTP XML stream parsing with resilient fallback if feed is unreachable.'
        },
        {
          id: 'src-manual',
          title: 'Interactive User Ingestion',
          tech: 'LiveAnalysisTerminal.jsx',
          status: 'implemented',
          desc: 'Direct text input sandbox allowing risk analysts to submit bespoke headlines on the fly.',
          details: 'Includes presets (Geopolitical crisis, Credit rating cut, Rate hike, Earnings beat).'
        }
      ]
    },
    {
      id: 'layer2',
      number: 'Layer 2',
      title: 'Preprocessing & Text Sanitization',
      techBadge: 'backend/ingestion/cleaner.py',
      color: '#60A5FA',
      nodes: [
        {
          id: 'prep-html',
          title: 'HTML Unescaping',
          tech: 'html.unescape()',
          status: 'implemented',
          desc: 'Decodes HTML entities (&amp; -> &, &quot; -> ", etc.) across syndicated web feeds.'
        },
        {
          id: 'prep-url',
          title: 'URL Stripping',
          tech: 're.sub(r"https?://...", "")',
          status: 'implemented',
          desc: 'Removes hyperlinks, tracking parameters, and protocol strings from raw incoming text.'
        },
        {
          id: 'prep-norm',
          title: 'Whitespace & Character Normalization',
          tech: 'Regex curly quote/dash normalizer',
          status: 'implemented',
          desc: 'Normalizes smart quotes, em-dashes, and multiple spaces while preserving financial numbers & currency symbols.'
        },
        {
          id: 'prep-dedup',
          title: 'Deduplication & Entity Resolution',
          tech: 'COMPANY_ALIASES mapping in risk_engine.py',
          status: 'implemented',
          desc: 'Resolves brand aliases (tatamotors -> Tata Motors, ril -> Reliance, infy -> Infosys) or defaults to "General Market".'
        }
      ]
    },
    {
      id: 'layer3',
      number: 'Layer 3',
      title: 'Module A: NLP & Financial Signal Engine',
      techBadge: 'backend/nlp/risk_engine.py',
      color: '#A855F7',
      isModuleA: true,
      nodes: [
        {
          id: 'nlp-sentiment',
          title: 'Domain Sentiment Scoring',
          tech: 'sentiment.py (Lexicon + Negation)',
          status: 'implemented',
          output: 'Score ∈ [-1.0, +1.0], Label (Pos/Neu/Neg)',
          desc: 'Domain-adapted financial dictionaries with 25+ positive & 25+ negative terms, intensifier multipliers (1.3x - 1.5x), and negation window handling (not, never, barely).'
        },
        {
          id: 'nlp-classifier',
          title: '8-Class Financial Taxonomy',
          tech: 'event_classifier.py',
          status: 'implemented',
          output: 'Event Type + Confidence Score',
          desc: 'Classifies text into: 1. Geopolitical, 2. Macroeconomic, 3. Credit Event, 4. Merger/Acquisition, 5. Product Launch, 6. Regulatory, 7. Earnings/Financial, 8. Other.'
        },
        {
          id: 'nlp-impact',
          title: 'Impact Scoring & Gate Formula',
          tech: 'impact_score.py',
          status: 'implemented',
          output: 'Impact Score (1-10), Risk Level (Low to Critical)',
          desc: 'Formula combines Event Base Weight (3.0-7.0) + Directional Sentiment Delta (up to +2.5 for negative, -2.0 for positive) + Severity Keyword Boost (default, bankruptcy, sanctions, etc. up to +3.0).'
        },
        {
          id: 'nlp-gate',
          title: 'High-Impact Gatekeeper',
          tech: 'is_stress_test_trigger = impact_score >= 7',
          status: 'implemented',
          isGate: true,
          desc: 'Threshold gate: Any signal scoring Impact ≥ 7 qualifies as a high-impact risk event and activates Module B downstream portfolio stress testing.'
        }
      ]
    },
    {
      id: 'layer4',
      number: 'Layer 4',
      title: 'Backend API, Persistence & Inter-Module Bus',
      techBadge: 'backend/api/routes.py & backend/database/db.py',
      color: '#34D399',
      nodes: [
        {
          id: 'api-fastapi',
          title: 'FastAPI REST Service Tier',
          tech: 'FastAPI / Pydantic (sub-35ms)',
          status: 'implemented',
          desc: 'Exposes POST /api/analyze, GET /api/signals, POST /api/ingest, GET /api/portfolio, and POST /api/stress-test with schema validation.'
        },
        {
          id: 'db-sqlite',
          title: 'SQLite Signal Store',
          tech: 'risk_signals table (ACID)',
          status: 'implemented',
          desc: 'Persists structured signals: id (UUID), timestamp, source, company, raw_text, summary, sentiment_score, event_type, impact_score, risk_level, trigger_flag.'
        },
        {
          id: 'bus-trigger',
          title: 'Structured Handoff to Module B',
          tech: 'POST /api/stress-test or Client Dispatch',
          status: 'implemented',
          desc: 'Passes event_type ("Regulatory", "Geopolitical", etc.) and impact_score (7-10) directly into the portfolio simulation engine.'
        }
      ]
    },
    {
      id: 'layer5',
      number: 'Layer 5',
      title: 'Module B: Strategic Portfolio Stress Testing',
      techBadge: 'backend/portfolio/stress_test.py',
      color: '#F59E0B',
      isModuleB: true,
      nodes: [
        {
          id: 'port-book',
          title: 'Multi-Asset Portfolio Book',
          tech: 'portfolio.py (10 Assets, $1.00M Book)',
          status: 'implemented',
          desc: 'Baseline portfolio: Equities (HDFC, Reliance, Tata, Apple, Microsoft, NVDA), Corporate Bonds (Tata Motors 7.5%, Reliance 7.2%), Govt Bonds (10Y G-Sec), and Loans.'
        },
        {
          id: 'port-matrix',
          title: 'Scenario Shock Matrix',
          tech: 'SCENARIO_SHOCKS dictionary',
          status: 'implemented',
          desc: 'Calibrated asset-class haircuts: Geopolitical (Equity -10%, Corp Bond -5%, Govt Bond +2%), Macroeconomic (Equity -7%, Loans -8%), Credit Event (Corp Bond -12%, Loans -8%), Regulatory (Equity -6%).'
        },
        {
          id: 'port-valuation',
          title: 'Mark-to-Market Valuation Engine',
          tech: 'run_stress_test()',
          status: 'implemented',
          desc: 'Calculates asset-level value_after = max(0, val_before * (1 + shock_pct)), net post-stress valuation, total dollar loss ($), and portfolio drawdown percentage (%).'
        },
        {
          id: 'port-var',
          title: 'Parametric VaR / Copula Engine',
          tech: 'GARCH(1,1) & Monte Carlo (Theoretical / Planned)',
          status: 'planned',
          desc: 'Extends fixed haircuts into 10,000-path Monte Carlo simulations and Student-t Copula tail risk evaluations (detailed in IEEE project paper).'
        }
      ]
    },
    {
      id: 'layer6',
      number: 'Layer 6',
      title: 'Results Presentation & Visual Telemetry',
      techBadge: 'React 18 + Vite SPA (Client Tier)',
      color: '#EC4899',
      nodes: [
        {
          id: 'ui-exec',
          title: 'Executive Metrics & Gauges',
          tech: 'MetricsCards.jsx',
          status: 'implemented',
          desc: 'Real-time counters for Total Signals, High Impact (≥7), Continuous Market Sentiment Gauge (-1.0 to +1.0), and Portfolio Exposure ($1,000,000).'
        },
        {
          id: 'ui-terminal',
          title: 'Live Ingestion Terminal',
          tech: 'LiveAnalysisTerminal.jsx',
          status: 'implemented',
          desc: 'Interactive news inspection terminal with instant sentiment score badge, event taxonomy chip, and "⚡ Shock Portfolio" trigger action button.'
        },
        {
          id: 'ui-stream',
          title: 'Structured Signal Stream Table',
          tech: 'RiskSignalTable.jsx',
          status: 'implemented',
          desc: 'Tabular audit record with timestamps, company, source, event category, sentiment pill, impact bar, and action status (SHOCKED vs BYPASSED).'
        },
        {
          id: 'ui-stress',
          title: 'Module B Stress Studio & Heatmap',
          tech: 'StressTestPanel.jsx & ChartsPanel.jsx',
          status: 'implemented',
          desc: 'Pre-stress vs. Stressed value comparison, net drawdown percentage, applied shock matrix chips, and asset-by-asset color-coded drawdown bars.'
        }
      ]
    }
  ];

  return (
    <div style={{ color: '#F3F4F6', fontFamily: "'Inter', sans-serif" }}>
      {/* Header Metadata Bar */}
      <div style={{
        background: 'linear-gradient(135deg, #111726 0%, #151D30 100%)',
        border: '1px solid #24304A',
        borderRadius: '8px',
        padding: '20px',
        marginBottom: '24px'
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <div style={{ width: '10px', height: '10px', borderRadius: '50%', background: '#38BDF8', boxShadow: '0 0 10px #38BDF8' }}></div>
              <h2 style={{ fontSize: '18px', fontWeight: 700, color: '#FFFFFF', margin: 0, letterSpacing: '-0.3px' }}>
                RiskPulse System Architecture & Technical Flow
              </h2>
            </div>
            <p style={{ color: '#94A3B8', fontSize: '13px', marginTop: '6px', marginBottom: 0 }}>
              End-to-End Execution Pipeline: Unstructured Financial Ingestion → NLP Signal Processing (Module A) → High-Impact Gate (≥7) → Strategic Stress Simulation (Module B)
            </p>
          </div>

          <div style={{
            display: 'flex',
            gap: '12px',
            alignItems: 'center',
            background: '#0B0F19',
            padding: '8px 14px',
            borderRadius: '6px',
            border: '1px solid #1E293B',
            fontSize: '12px'
          }}>
            <div><span style={{ color: '#94A3B8' }}>Author:</span> <strong style={{ color: '#F3F4F6' }}>Abhi Pandey (23BAI10909)</strong></div>
            <div style={{ color: '#334155' }}>|</div>
            <div><span style={{ color: '#94A3B8' }}>Institution:</span> <strong style={{ color: '#F3F4F6' }}>VIT Bhopal University</strong></div>
            <div style={{ color: '#334155' }}>|</div>
            <div style={{ color: '#38BDF8', fontWeight: 600 }}>S&P Global & CRISIL Hackathon 2026</div>
          </div>
        </div>

        {/* Legend */}
        <div style={{
          marginTop: '16px',
          paddingTop: '14px',
          borderTop: '1px solid #1E293B',
          display: 'flex',
          gap: '20px',
          flexWrap: 'wrap',
          alignItems: 'center',
          fontSize: '11px',
          color: '#94A3B8'
        }}>
          <span style={{ fontWeight: 600, color: '#CBD5E1', textTransform: 'uppercase', letterSpacing: '0.5px' }}>Architecture Legend:</span>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span style={{ width: '10px', height: '10px', borderRadius: '2px', background: '#10B981', display: 'inline-block' }}></span>
            <span>Implemented Component (In Codebase)</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span style={{ width: '10px', height: '10px', borderRadius: '2px', background: '#F59E0B', border: '1px dashed #F59E0B', display: 'inline-block' }}></span>
            <span>Planned / Academic Extension</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span style={{ width: '18px', height: '2px', background: '#38BDF8', display: 'inline-block' }}></span>
            <span>Solid Line: Implemented Data Flow</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span style={{ width: '18px', height: '2px', borderTop: '2px dashed #94A3B8', display: 'inline-block' }}></span>
            <span>Dashed Line: Extension / Research Path</span>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <span style={{ padding: '2px 6px', borderRadius: '4px', background: '#DC2626', color: '#FFF', fontWeight: 700, fontSize: '10px' }}>Impact ≥ 7</span>
            <span>Automated Stress Trigger Gate</span>
          </div>
        </div>
      </div>

      {/* Main Diagram Area */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
        {layers.map((layer, layerIdx) => (
          <div
            key={layer.id}
            onMouseEnter={() => setActiveLayer(layer.id)}
            onMouseLeave={() => setActiveLayer(null)}
            style={{
              background: activeLayer === layer.id ? '#131B2E' : '#0F1626',
              border: `1px solid ${activeLayer === layer.id ? layer.color : '#1E293B'}`,
              borderRadius: '8px',
              padding: '18px',
              transition: 'all 0.2s ease',
              position: 'relative',
              boxShadow: activeLayer === layer.id ? `0 0 15px ${layer.color}22` : 'none'
            }}
          >
            {/* Layer Header */}
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '14px', flexWrap: 'wrap', gap: '8px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <span style={{
                  background: `${layer.color}22`,
                  color: layer.color,
                  border: `1px solid ${layer.color}66`,
                  padding: '3px 8px',
                  borderRadius: '4px',
                  fontSize: '11px',
                  fontWeight: 700,
                  fontFamily: 'monospace'
                }}>
                  {layer.number}
                </span>
                <h3 style={{ fontSize: '15px', fontWeight: 700, color: '#FFFFFF', margin: 0 }}>
                  {layer.title}
                </h3>
                {layer.isModuleA && (
                  <span style={{ background: '#7C3AED', color: '#FFF', fontSize: '10px', padding: '2px 8px', borderRadius: '12px', fontWeight: 700 }}>
                    MODULE A: FINANCIAL INTELLIGENCE
                  </span>
                )}
                {layer.isModuleB && (
                  <span style={{ background: '#D97706', color: '#FFF', fontSize: '10px', padding: '2px 8px', borderRadius: '12px', fontWeight: 700 }}>
                    MODULE B: STRESS TESTING ENGINE
                  </span>
                )}
              </div>

              {layer.techBadge && (
                <span style={{ color: '#94A3B8', fontSize: '11px', fontFamily: 'monospace', background: '#0A0E17', padding: '4px 10px', borderRadius: '4px', border: '1px solid #1E293B' }}>
                  source: {layer.techBadge}
                </span>
              )}
            </div>

            {/* Nodes Grid */}
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))',
              gap: '12px'
            }}>
              {layer.nodes.map(node => {
                const isSelected = selectedNode?.id === node.id;
                return (
                  <div
                    key={node.id}
                    onClick={() => setSelectedNode(isSelected ? null : node)}
                    style={{
                      background: node.isGate ? 'linear-gradient(135deg, #1E1B4B 0%, #311042 100%)' : '#151D30',
                      border: `1px ${node.status === 'planned' ? 'dashed' : 'solid'} ${
                        isSelected ? '#38BDF8' : node.isGate ? '#DC2626' : '#24304A'
                      }`,
                      borderRadius: '6px',
                      padding: '14px',
                      cursor: 'pointer',
                      transition: 'all 0.15s ease',
                      position: 'relative'
                    }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '6px' }}>
                      <h4 style={{ fontSize: '13px', fontWeight: 600, color: node.isGate ? '#FCA5A5' : '#F1F5F9', margin: 0 }}>
                        {node.title}
                      </h4>
                      <span style={{
                        fontSize: '9px',
                        padding: '2px 6px',
                        borderRadius: '3px',
                        fontWeight: 700,
                        textTransform: 'uppercase',
                        background: node.status === 'implemented' ? '#065F46' : '#78350F',
                        color: node.status === 'implemented' ? '#6EE7B7' : '#FCD34D'
                      }}>
                        {node.status}
                      </span>
                    </div>

                    <div style={{ fontSize: '11px', color: '#38BDF8', fontFamily: 'monospace', marginBottom: '8px' }}>
                      {node.tech}
                    </div>

                    <p style={{ fontSize: '12px', color: '#94A3B8', margin: 0, lineHeight: 1.5 }}>
                      {node.desc}
                    </p>

                    {node.output && (
                      <div style={{
                        marginTop: '10px',
                        padding: '6px 8px',
                        background: '#0B0F19',
                        borderRadius: '4px',
                        border: '1px solid #1E293B',
                        fontSize: '11px',
                        color: '#A5B4FC',
                        fontFamily: 'monospace'
                      }}>
                        ↳ Output: {node.output}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>

            {/* Downward Data Flow Connector */}
            {layerIdx < layers.length - 1 && (
              <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '14px 0 -8px 0',
                gap: '8px'
              }}>
                <div style={{ height: '14px', width: '2px', background: layerIdx === 2 ? '#DC2626' : '#38BDF8' }}></div>
                <div style={{
                  fontSize: '10px',
                  fontFamily: 'monospace',
                  color: layerIdx === 2 ? '#EF4444' : '#38BDF8',
                  background: '#0A0E17',
                  padding: '2px 8px',
                  borderRadius: '10px',
                  border: `1px solid ${layerIdx === 2 ? '#DC2626' : '#24304A'}`
                }}>
                  {layerIdx === 0 && '↓ Clean Text Stream → Ingestion Sanitizer'}
                  {layerIdx === 1 && '↓ Sanitized Text + Resolved Entities → Module A Risk Engine'}
                  {layerIdx === 2 && '⚡ High-Impact Signal (Impact ≥ 7) → Trigger Hand-off to Module B'}
                  {layerIdx === 3 && '↓ Restructured Scenario Shocks & Asset Holdings'}
                  {layerIdx === 4 && '↓ Stressed Valuations, Loss & Drawdown Telemetry'}
                </div>
                <div style={{ height: '14px', width: '2px', background: layerIdx === 2 ? '#DC2626' : '#38BDF8' }}></div>
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Selected Node Deep-Dive Drawer */}
      {selectedNode && (
        <div style={{
          marginTop: '20px',
          background: '#111726',
          border: '1px solid #38BDF8',
          borderRadius: '8px',
          padding: '16px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'flex-start',
          gap: '16px'
        }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
              <span style={{ color: '#38BDF8', fontWeight: 700, fontSize: '13px', textTransform: 'uppercase' }}>Inspected Component:</span>
              <strong style={{ fontSize: '14px', color: '#FFFFFF' }}>{selectedNode.title}</strong>
              <code style={{ fontSize: '11px', color: '#94A3B8', background: '#0A0E17', padding: '2px 6px', borderRadius: '4px' }}>{selectedNode.tech}</code>
            </div>
            <p style={{ color: '#CBD5E1', fontSize: '13px', marginTop: '6px', marginBottom: 0 }}>
              {selectedNode.details || selectedNode.desc}
            </p>
          </div>
          <button
            onClick={() => setSelectedNode(null)}
            style={{
              background: '#1E293B',
              color: '#94A3B8',
              border: 'none',
              borderRadius: '4px',
              padding: '6px 12px',
              fontSize: '11px',
              cursor: 'pointer'
            }}
          >
            ✕ Close
          </button>
        </div>
      )}

      {/* Technical Summary Paragraph (Retained as per user specification) */}
      <div style={{
        marginTop: '24px',
        padding: '18px',
        background: '#0D1321',
        borderRadius: '8px',
        border: '1px solid #1E293B',
        fontSize: '13px',
        color: '#94A3B8',
        lineHeight: 1.8
      }}>
        <h4 style={{ color: '#FFFFFF', fontSize: '14px', marginBottom: '8px' }}>
          Methodology & Execution Summary
        </h4>
        <p style={{ margin: 0 }}>
          RiskPulse bridges the gap between unstructured financial textual noise and quantitative balance sheet decision support.
          Text records undergo automated HTML unescaping, URL removal, entity resolution, and continuous sentiment scoring (-1.0 to +1.0)
          via financial polarity dictionaries. Events are categorized into 8 distinct financial taxonomies. High-impact signals (Impact ≥ 7)
          automatically cross the high-impact gatekeeper and trigger <strong>Module B Strategic Portfolio Stress Testing</strong>,
          evaluating mark-to-market drawdowns across a 10-asset institutional book ($1,000,000 baseline).
        </p>
      </div>
    </div>
  );
}
