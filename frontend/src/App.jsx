import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import MetricsCards from './components/MetricsCards';
import RiskSignalTable from './components/RiskSignalTable';
import StressTestPanel from './components/StressTestPanel';
import ChartsPanel from './components/ChartsPanel';
import LiveAnalysisTerminal from './components/LiveAnalysisTerminal';
import SystemArchitectureDiagram from './components/SystemArchitectureDiagram';
import { fetchSignals, fetchPortfolio, triggerLiveIngest } from './services/api';

export default function App() {
  const [activeTab, setActiveTab] = useState('overview');
  const [signals, setSignals] = useState([]);
  const [portfolio, setPortfolio] = useState(null);
  const [loading, setLoading] = useState(true);
  const [liveIngesting, setLiveIngesting] = useState(false);
  const [activeShockScenario, setActiveShockScenario] = useState({ event: 'Geopolitical', impact: 9 });

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    setLoading(true);
    try {
      const [signalsData, portfolioData] = await Promise.all([
        fetchSignals(),
        fetchPortfolio()
      ]);
      setSignals(signalsData);
      setPortfolio(portfolioData);
    } catch (err) {
      console.warn('Initial data load notice:', err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleLiveIngest = async (customUrl) => {
    setLiveIngesting(true);
    try {
      const res = await triggerLiveIngest(customUrl);
      if (res && res.new_signals && res.new_signals.length > 0) {
        setSignals(prev => [...res.new_signals, ...prev]);
      } else {
        await loadData();
      }
      return res;
    } catch (err) {
      console.warn('Live ingest notice:', err.message);
    } finally {
      setLiveIngesting(false);
    }
  };

  const handleNewSignal = (newSignal) => {
    setSignals(prev => [newSignal, ...prev]);
  };

  const handleTriggerStressTest = (eventType, impactScore) => {
    setActiveShockScenario({ event: eventType, impact: impactScore });
    setActiveTab('stress-tests');
  };

  return (
    <div className="app-container">
      <Sidebar activeTab={activeTab} onSelectTab={setActiveTab} />

      <main className="main-content">
        <header className="header-banner" style={{ flexWrap: 'wrap', gap: '16px' }}>
          <div>
            <h1 className="page-title">
              {activeTab === 'overview' && 'Executive Risk Dashboard'}
              {activeTab === 'signals' && 'Financial Risk Signal Feed'}
              {activeTab === 'portfolio' && 'Multi-Asset Portfolio Exposure'}
              {activeTab === 'stress-tests' && 'Strategic Portfolio Stress Testing'}
              {activeTab === 'datasources' && 'Ingested Benchmark Feeds'}
              {activeTab === 'about' && 'Platform Architecture & Methodology'}
            </h1>
            <p className="page-subtitle">
              S&P Global & CRISIL Campus Hackathon 2026 — AI/NLP Financial Risk Intelligence Platform
            </p>
          </div>

          <div style={{ display: 'flex', gap: '10px', alignItems: 'center', flexWrap: 'wrap' }}>
            <button
              className="btn-primary"
              onClick={() => handleLiveIngest()}
              disabled={liveIngesting}
              style={{ background: '#0284C7', border: '1px solid #38BDF8' }}
              title="Fetch and analyze live public financial RSS feed"
            >
              {liveIngesting ? 'Ingesting RSS...' : '📡 Live RSS Feed'}
            </button>
            <button className="btn-primary" onClick={loadData}>
              ↻ Refresh Feeds
            </button>
          </div>
        </header>

        {loading ? (
          <div style={{ padding: '60px', textAlign: 'center', color: '#94A3B8' }}>
            Loading market risk signals and portfolio state...
          </div>
        ) : (
          <>
            <MetricsCards signals={signals} portfolio={portfolio} />

            {/* Live Interactive Analysis Terminal on Overview & Signals view */}
            {(activeTab === 'overview' || activeTab === 'signals') && (
              <LiveAnalysisTerminal
                onNewSignalGenerated={handleNewSignal}
                onTriggerStressTest={handleTriggerStressTest}
                onTriggerLiveIngest={handleLiveIngest}
                isLiveIngesting={liveIngesting}
              />
            )}

            {(activeTab === 'overview' || activeTab === 'signals') && (
              <>
                <ChartsPanel signals={signals} />
                <RiskSignalTable
                  signals={signals}
                  onTriggerStressTest={handleTriggerStressTest}
                />
              </>
            )}

            {(activeTab === 'overview' || activeTab === 'stress-tests') && (
              <StressTestPanel
                key={`${activeShockScenario.event}-${activeShockScenario.impact}`}
                preloadedEvent={activeShockScenario.event}
                preloadedImpact={activeShockScenario.impact}
              />
            )}

            {activeTab === 'portfolio' && portfolio && (
              <div className="card-section">
                <div className="card-title">
                  <span>Balance Sheet Portfolio Allocation</span>
                  <span style={{ fontSize: '13px', color: '#94A3B8', fontFamily: 'monospace' }}>
                    TOTAL ASSETS: {portfolio.asset_count} | DURATION: {portfolio.weighted_duration} YRS
                  </span>
                </div>
                <div className="table-wrapper">
                  <table>
                    <thead>
                      <tr>
                        <th>Asset ID</th>
                        <th>Asset Name</th>
                        <th>Asset Class</th>
                        <th>Sector</th>
                        <th>Duration (Yrs)</th>
                        <th>Credit Risk</th>
                        <th style={{ textAlign: 'right' }}>Market Value</th>
                      </tr>
                    </thead>
                    <tbody>
                      {portfolio.assets.map(a => (
                        <tr key={a.asset_id}>
                          <td style={{ fontFamily: 'monospace' }}>{a.asset_id}</td>
                          <td><strong>{a.asset_name}</strong></td>
                          <td>{a.asset_type}</td>
                          <td style={{ color: '#94A3B8' }}>{a.sector}</td>
                          <td style={{ fontFamily: 'monospace' }}>{a.duration > 0 ? a.duration : '—'}</td>
                          <td>
                            <span className="badge badge-low">{a.credit_risk}</span>
                          </td>
                          <td style={{ textAlign: 'right', fontFamily: 'monospace' }}>
                            ₹{a.value.toLocaleString()}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            )}

            {activeTab === 'datasources' && (
              <div className="card-section">
                <div className="card-title" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span>Ingested Benchmark Feeds</span>
                  <span style={{ fontSize: '11px', color: '#10B981', background: '#064E3B', padding: '3px 8px', borderRadius: '12px', fontWeight: 600 }}>
                    ● All Pipelines Operational
                  </span>
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '14px', marginTop: '12px' }}>
                  <div style={{ background: '#0D1321', padding: '16px', borderRadius: '6px', border: '1px solid #1F2937' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                      <h4 style={{ color: '#F3F4F6', fontSize: '14px', margin: 0 }}>1. Financial News Wire</h4>
                      <span className="badge badge-low">Active</span>
                    </div>
                    <p style={{ color: '#94A3B8', fontSize: '12px', margin: '0 0 8px 0', lineHeight: 1.5 }}>
                      Official corporate disclosures, regulatory subpoenas, and monetary policy news.
                    </p>
                    <div style={{ fontSize: '11px', color: '#38BDF8', fontFamily: 'monospace' }}>
                      Sources: Reuters, Dow Jones, Bloomberg Wire
                    </div>
                  </div>

                  <div style={{ background: '#0D1321', padding: '16px', borderRadius: '6px', border: '1px solid #1F2937' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                      <h4 style={{ color: '#F3F4F6', fontSize: '14px', margin: 0 }}>2. Market Social Feed</h4>
                      <span className="badge badge-low">Active</span>
                    </div>
                    <p style={{ color: '#94A3B8', fontSize: '12px', margin: '0 0 8px 0', lineHeight: 1.5 }}>
                      Real-time analyst chatter and sentiment commentary with ticker detection.
                    </p>
                    <div style={{ fontSize: '11px', color: '#38BDF8', fontFamily: 'monospace' }}>
                      Sources: StockTwits, Financial Social Streams
                    </div>
                  </div>

                  <div style={{ background: '#0D1321', padding: '16px', borderRadius: '6px', border: '1px solid #1F2937' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                      <h4 style={{ color: '#F3F4F6', fontSize: '14px', margin: 0 }}>3. Live Public RSS</h4>
                      <span className="badge badge-low">Connected</span>
                    </div>
                    <p style={{ color: '#94A3B8', fontSize: '12px', margin: '0 0 8px 0', lineHeight: 1.5 }}>
                      Automated RSS fetcher with multi-feed failover and duplicate handling.
                    </p>
                    <div style={{ fontSize: '11px', color: '#38BDF8', fontFamily: 'monospace' }}>
                      Sources: Google News, MarketWatch, CNBC
                    </div>
                  </div>
                </div>

                <div style={{ marginTop: '20px' }}>
                  <h4 style={{ color: '#F3F4F6', fontSize: '13px', marginBottom: '10px' }}>Recent Ingested Benchmark Samples</h4>
                  <div className="table-wrapper">
                    <table>
                      <thead>
                        <tr>
                          <th>ID</th>
                          <th>Source</th>
                          <th>Company</th>
                          <th>Event Category</th>
                          <th>Sentiment</th>
                          <th>Impact</th>
                        </tr>
                      </thead>
                      <tbody>
                        {signals.slice(0, 5).map(s => (
                          <tr key={s.id}>
                            <td style={{ fontFamily: 'monospace' }}>{s.id}</td>
                            <td>{s.source}</td>
                            <td><strong>{s.company}</strong></td>
                            <td>{s.event_type}</td>
                            <td style={{ color: s.sentiment_score < 0 ? '#EF4444' : '#10B981', fontFamily: 'monospace' }}>
                              {s.sentiment_score > 0 ? `+${s.sentiment_score.toFixed(2)}` : s.sentiment_score.toFixed(2)}
                            </td>
                            <td>
                              <span style={{
                                padding: '2px 6px',
                                borderRadius: '4px',
                                fontSize: '11px',
                                fontWeight: 700,
                                background: s.impact_score >= 7 ? '#7F1D1D' : '#064E3B',
                                color: s.impact_score >= 7 ? '#FCA5A5' : '#6EE7B7'
                              }}>
                                {s.impact_score}/10
                              </span>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'about' && (
              <div className="card-section" style={{ padding: '24px' }}>
                <SystemArchitectureDiagram />
              </div>
            )}
          </>
        )}
      </main>
    </div>
  );
}
