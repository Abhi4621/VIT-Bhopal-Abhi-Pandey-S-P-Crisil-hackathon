import React from 'react';

export default function Sidebar({ activeTab, onSelectTab }) {
  const navItems = [
    { id: 'overview', label: 'Overview', icon: '📊' },
    { id: 'signals', label: 'Risk Signals', icon: '⚡' },
    { id: 'portfolio', label: 'Portfolio', icon: '💼' },
    { id: 'stress-tests', label: 'Stress Tests', icon: '🛡️' },
    { id: 'datasources', label: 'Data Sources', icon: '📁' },
    { id: 'about', label: 'About', icon: 'ℹ️' },
  ];

  return (
    <aside className="sidebar">
      <div className="brand-container">
        <div className="brand-title">
          <span className="brand-dot"></span>
          RiskPulse
        </div>
        <div className="brand-tagline">
          Turning financial noise into actionable risk signals.
        </div>
      </div>

      <ul className="nav-links">
        {navItems.map((item) => (
          <li
            key={item.id}
            className={`nav-item ${activeTab === item.id ? 'active' : ''}`}
            onClick={() => onSelectTab(item.id)}
          >
            <span>{item.icon}</span>
            <span>{item.label}</span>
          </li>
        ))}
      </ul>

      <div className="sidebar-footer">
        <div><strong>Candidate:</strong> Abhi Pandey</div>
        <div>VIT Bhopal University</div>
        <div style={{ marginTop: '4px', opacity: 0.7 }}>B.Tech CSE (AI & ML)</div>
      </div>
    </aside>
  );
}
