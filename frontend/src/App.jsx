import React, { useState, useEffect } from 'react';
import Sidebar from './components/Sidebar';
import MetricsCards from './components/MetricsCards';
import RiskSignalTable from './components/RiskSignalTable';
import StressTestPanel from './components/StressTestPanel';
import ChartsPanel from './components/ChartsPanel';
import { fetchSignals, fetchPortfolio } from './services/api';

export default function App() {
  const [activeTab, setActiveTab] = useState('overview');
  const [signals, setSignals] = useState([]);
  const [portfolio, setPortfolio] = useState(null);
  const [loading, setLoading] = useState(true);

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
      console.error('Data load notice:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <Sidebar activeTab={activeTab} onSelectTab={setActiveTab} />

      <main className="main-content">
        <header className="header-banner">
          <div>
            <h1 className="page-title">
              {activeTab === 'overview' && 'Executive Risk Overview'}
              {activeTab === 'signals' && 'Financial Risk Signals Stream'}
              {activeTab === 'portfolio' && 'Multi-Asset Portfolio Exposure'}
              {activeTab === 'stress-tests' && 'Strategic Portfolio Stress Testing'}
              {activeTab === 'datasources' && 'Ingested Benchmark Data Feeds'}
              {activeTab === 'about' && 'About RiskPulse Platform'}
            </h1>
            <p className="page-subtitle">
              S&P Global & CRISIL Campus Hackathon 2026 — Real-time AI/NLP Risk Analytics
            </p>
          </div>

          <button className="btn-primary" onClick={loadData}>
            ↻ Refresh Feed
          </button>
        </header>

        {loading ? (
          <div style={{ padding: '60px', textAlign: 'center', color: '#94A3B8' }}>
            Loading market risk signals and portfolio state...
          </div>
        ) : (
          <>
            <MetricsCards signals={signals} portfolio={portfolio} />

            {(activeTab === 'overview' || activeTab === 'signals') && (
              <>
                <ChartsPanel signals={signals} />
                <RiskSignalTable signals={signals} />
              </>
            )}

            {(activeTab === 'overview' || activeTab === 'stress-tests') && (
              <StressTestPanel />
            )}

            {activeTab === 'portfolio' && portfolio && (
              <div className="card-section">
                <div className="card-title">Current Asset Holdings & Duration</div>
                <div className="table-wrapper">
                  <table>
                    <thead>
                      <tr>
                        <th>Asset ID</th>
                        <th>Asset Name</th>
                        <th>Type</th>
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
                          <td>{a.sector}</td>
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
                <div className="card-title">Active Ingestion Feeds</div>
                <p style={{ color: '#94A3B8', fontSize: '13px', lineHeight: 1.6 }}>
                  RiskPulse processes dual logically independent financial feeds:
                </p>
                <ul style={{ color: '#F3F4F6', fontSize: '13px', marginLeft: '20px', marginTop: '12px', lineHeight: 1.8 }}>
                  <li><strong>Financial News Wire (`data/news_sample.csv`):</strong> High-density structured reporting covering supply chain disruptions, regulatory probes, earnings beats, and sovereign debt policy changes.</li>
                  <li><strong>Social Sentiment Feed (`data/social_sample.csv`):</strong> Real-time analyst chatter and commentary with sentiment polarity cues.</li>
                  <li><strong>Multi-Asset Portfolio (`data/portfolio.csv`):</strong> Synthetic balance sheet exposure spanning Equity, Corporate Bonds, Government G-Secs, Loans, and Derivatives.</li>
                </ul>
              </div>
            )}

            {activeTab === 'about' && (
              <div className="card-section">
                <div className="card-title">About RiskPulse</div>
                <div style={{ color: '#94A3B8', fontSize: '13px', lineHeight: 1.8 }}>
                  <p><strong>Developed by:</strong> Abhi Pandey (VIT Bhopal University, B.Tech CSE AI & ML)</p>
                  <p><strong>Target:</strong> S&P Global & Crisil Campus Hackathon 2026</p>
                  <p style={{ marginTop: '12px' }}>
                    RiskPulse translates unstructured textual announcements into actionable financial risk signals,
                    producing a normalized Sentiment Score (-1.0 to +1.0), an 8-category Event Classification,
                    and a Prototype Risk Impact Score (1-10). Signals with impact ≥ 7 trigger automated Module B
                    Strategic Portfolio Stress Testing across multi-asset allocations.
                  </p>
                </div>
              </div>
            )}
          </>
        )}
      </main>
    </div>
  );
}
