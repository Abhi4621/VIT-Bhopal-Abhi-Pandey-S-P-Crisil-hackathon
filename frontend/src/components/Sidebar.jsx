import React from 'react';

export default function Sidebar({ activeTab, onSelectTab }) {
  const navItems = [
    {
      id: 'overview',
      label: 'Executive Overview',
      icon: (
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <rect x="3" y="3" width="7" height="7"></rect>
          <rect x="14" y="3" width="7" height="7"></rect>
          <rect x="14" y="14" width="7" height="7"></rect>
          <rect x="3" y="14" width="7" height="7"></rect>
        </svg>
      )
    },
    {
      id: 'signals',
      label: 'Risk Signal Stream',
      icon: (
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
        </svg>
      )
    },
    {
      id: 'portfolio',
      label: 'Portfolio Holdings',
      icon: (
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect>
          <path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path>
        </svg>
      )
    },
    {
      id: 'stress-tests',
      label: 'Stress Testing Studio',
      icon: (
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
        </svg>
      )
    },
    {
      id: 'datasources',
      label: 'Ingestion Feeds',
      icon: (
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <ellipse cx="12" cy="5" rx="9" ry="3"></ellipse>
          <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path>
          <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path>
        </svg>
      )
    },
    {
      id: 'about',
      label: 'System Architecture',
      icon: (
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <circle cx="12" cy="12" r="10"></circle>
          <line x1="12" y1="16" x2="12" y2="12"></line>
          <line x1="12" y1="8" x2="12.01" y2="8"></line>
        </svg>
      )
    }
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

      <div style={{ padding: '12px 20px', borderBottom: '1px solid #1F2937', fontSize: '11px', color: '#64748B', display: 'flex', alignItems: 'center', gap: '8px' }}>
        <span style={{ width: '6px', height: '6px', borderRadius: '50%', background: '#10B981' }}></span>
        <span>ENGINE STATUS: OPERATIONAL</span>
      </div>

      <ul className="nav-links">
        {navItems.map((item) => (
          <li
            key={item.id}
            className={`nav-item ${activeTab === item.id ? 'active' : ''}`}
            onClick={() => onSelectTab(item.id)}
          >
            <span style={{ display: 'flex', alignItems: 'center' }}>{item.icon}</span>
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
