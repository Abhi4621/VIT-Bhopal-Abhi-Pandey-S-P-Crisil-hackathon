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
                <div className="card-title">Connected Ingestion Pipelines</div>
                <div style={{ color: '#94A3B8', fontSize: '13px', lineHeight: 1.8 }}>
                  <p>RiskPulse ingests and normalizes dual independent unstructured financial feeds:</p>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px', marginTop: '16px' }}>
                    <div style={{ background: '#0D1321', padding: '16px', borderRadius: '6px', border: '1px solid #1F2937' }}>
                      <h4 style={{ color: '#F3F4F6', fontSize: '14px', marginBottom: '8px' }}>1. Financial News Stream</h4>
                      <p style={{ color: '#94A3B8', fontSize: '12px' }}>
                        Structured wire reports with timestamps, editorial headlines, and detailed contextual article text.
                        Processes supply chain bottlenecks, monetary policy announcements, and legal/regulatory inquiries.
                      </p>
                    </div>

                    <div style={{ background: '#0D1321', padding: '16px', borderRadius: '6px', border: '1px solid #1F2937' }}>
                      <h4 style={{ color: '#F3F4F6', fontSize: '14px', marginBottom: '8px' }}>2. Market Social Feed</h4>
                      <p style={{ color: '#94A3B8', fontSize: '12px' }}>
                        Real-time analyst discussions and sentiment chatter. Normalized through text cleaning, emoji stripping,
                        and domain polarity scoring before classification.
                      </p>
                    </div>
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
