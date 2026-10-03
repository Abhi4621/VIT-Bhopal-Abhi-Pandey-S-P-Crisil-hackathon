const BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export async function fetchSignals(filters = {}) {
  const params = new URLSearchParams();
  if (filters.company) params.append('company', filters.company);
  if (filters.eventType) params.append('event_type', filters.eventType);
  if (filters.minImpact) params.append('min_impact', filters.minImpact);

  const res = await fetch(`${BASE_URL}/signals?${params.toString()}`);
  if (!res.ok) throw new Error('Failed to fetch risk signals');
  return res.json();
}

export async function fetchPortfolio() {
  const res = await fetch(`${BASE_URL}/portfolio`);
  if (!res.ok) throw new Error('Failed to fetch portfolio data');
  return res.json();
}

export async function runStressTest(eventType = 'Geopolitical', impactScore = 9) {
  const res = await fetch(`${BASE_URL}/stress-test`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      event_type: eventType,
      impact_score: impactScore
    })
  });
  if (!res.ok) throw new Error('Failed to run stress test simulation');
  return res.json();
}

export async function analyzeText(text, company = null) {
  const res = await fetch(`${BASE_URL}/analyze`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, company })
  });
  if (!res.ok) throw new Error('Failed to analyze financial text');
  return res.json();
}
