export const BENCHMARK_SIGNALS = [
  {
    id: "SIG-N101",
    timestamp: "2026-09-15T08:30:00Z",
    source: "Synthetic Financial News Wire",
    company: "Tata Motors",
    summary: "Tata Motors faces supply chain disruption amid regional conflict.",
    sentiment_score: -0.78,
    sentiment_label: "Negative",
    event_type: "Geopolitical",
    confidence: 0.94,
    impact_score: 9,
    risk_level: "Critical",
    is_stress_test_trigger: true
  },
  {
    id: "SIG-N102",
    timestamp: "2026-09-16T10:15:00Z",
    source: "Market Synthetic Dispatch",
    company: "HDFC Bank",
    summary: "HDFC Bank posts record quarterly net profit growth.",
    sentiment_score: 0.82,
    sentiment_label: "Positive",
    event_type: "Earnings/Financial",
    confidence: 0.96,
    impact_score: 3,
    risk_level: "Low",
    is_stress_test_trigger: false
  },
  {
    id: "SIG-N103",
    timestamp: "2026-09-17T11:45:00Z",
    source: "Synthetic Financial News Wire",
    company: "Reliance Industries",
    summary: "Regulatory probe initiated over alleged refining tariff irregularities.",
    sentiment_score: -0.71,
    sentiment_label: "Negative",
    event_type: "Regulatory",
    confidence: 0.92,
    impact_score: 8,
    risk_level: "High",
    is_stress_test_trigger: true
  },
  {
    id: "SIG-N104",
    timestamp: "2026-09-18T14:20:00Z",
    source: "Financial Press Release",
    company: "Infosys",
    summary: "Infosys launches next-generation enterprise AI orchestration suite.",
    sentiment_score: 0.74,
    sentiment_label: "Positive",
    event_type: "Product Launch",
    confidence: 0.95,
    impact_score: 4,
    risk_level: "Moderate",
    is_stress_test_trigger: false
  },
  {
    id: "SIG-N105",
    timestamp: "2026-09-19T09:00:00Z",
    source: "Market Synthetic Dispatch",
    company: "Adani Enterprises",
    summary: "Credit rating downgraded to negative outlook on high leverage.",
    sentiment_score: -0.85,
    sentiment_label: "Negative",
    event_type: "Credit Event",
    confidence: 0.95,
    impact_score: 9,
    risk_level: "Critical",
    is_stress_test_trigger: true
  },
  {
    id: "SIG-N106",
    timestamp: "2026-09-20T13:10:00Z",
    source: "Synthetic Financial News Wire",
    company: "ICICI Bank",
    summary: "Central Bank unexpectedly raises benchmark repo rate by 50 basis points.",
    sentiment_score: -0.62,
    sentiment_label: "Negative",
    event_type: "Macroeconomic",
    confidence: 0.93,
    impact_score: 7,
    risk_level: "High",
    is_stress_test_trigger: true
  },
  {
    id: "SIG-N107",
    timestamp: "2026-09-21T15:30:00Z",
    source: "Market Synthetic Dispatch",
    company: "Tata Steel",
    summary: "Tata Steel announces merger discussions with regional infrastructure supplier.",
    sentiment_score: 0.65,
    sentiment_label: "Positive",
    event_type: "Merger/Acquisition",
    confidence: 0.91,
    impact_score: 5,
    risk_level: "Moderate",
    is_stress_test_trigger: false
  },
  {
    id: "SIG-N108",
    timestamp: "2026-09-22T08:45:00Z",
    source: "Synthetic Financial News Wire",
    company: "Tesla",
    summary: "Major cross-border sanctions disrupt battery component logistics.",
    sentiment_score: -0.88,
    sentiment_label: "Negative",
    event_type: "Geopolitical",
    confidence: 0.95,
    impact_score: 9,
    risk_level: "Critical",
    is_stress_test_trigger: true
  }
];

export const BENCHMARK_PORTFOLIO = {
  total_value: 14000000.0,
  asset_count: 10,
  weighted_duration: 4.85,
  asset_type_allocation: {
    "Equity": 7300000.0,
    "Corporate Bond": 2300000.0,
    "Government Bond": 2000000.0,
    "Loan": 1900000.0,
    "Derivative": 600000.0,
    "Commodity Exposure": 900000.0
  },
  sector_allocation: {
    "Automotive": 2500000.0,
    "Energy": 3600000.0,
    "Banking": 2300000.0,
    "Infrastructure": 1200000.0,
    "Sovereign": 2000000.0,
    "Materials": 900000.0,
    "Technology": 1800000.0,
    "Real Estate": 700000.0
  },
  assets: [
    { asset_id: "A001", asset_name: "Tata Motors Equity", asset_type: "Equity", sector: "Automotive", value: 2500000.0, duration: 0.0, credit_risk: "Moderate" },
    { asset_id: "A002", asset_name: "Reliance Industries Equity", asset_type: "Equity", sector: "Energy", value: 3000000.0, duration: 0.0, credit_risk: "Low" },
    { asset_id: "A003", asset_name: "HDFC Bank Senior Debt", asset_type: "Corporate Bond", sector: "Banking", value: 1500000.0, duration: 4.2, credit_risk: "Low" },
    { asset_id: "A004", asset_name: "Adani Enterprises Term Loan", asset_type: "Loan", sector: "Infrastructure", value: 1200000.0, duration: 3.5, credit_risk: "High" },
    { asset_id: "A005", asset_name: "India Sovereign 10Y G-Sec", asset_type: "Government Bond", sector: "Sovereign", value: 2000000.0, duration: 7.1, credit_risk: "Very Low" },
    { asset_id: "A006", asset_name: "ICICI Subordinated Note", asset_type: "Corporate Bond", sector: "Banking", value: 800000.0, duration: 5.8, credit_risk: "Moderate" },
    { asset_id: "A007", asset_name: "Crude Oil Energy Swap", asset_type: "Derivative", sector: "Energy", value: 600000.0, duration: 1.2, credit_risk: "High" },
    { asset_id: "A008", asset_name: "Industrial Metals Index ETF", asset_type: "Commodity Exposure", sector: "Materials", value: 900000.0, duration: 0.0, credit_risk: "Moderate" },
    { asset_id: "A009", asset_name: "Infosys Technologies Equity", asset_type: "Equity", sector: "Technology", value: 1800000.0, duration: 0.0, credit_risk: "Low" },
    { asset_id: "A010", asset_name: "Commercial Real Estate Syndicate Loan", asset_type: "Loan", sector: "Real Estate", value: 700000.0, duration: 2.8, credit_risk: "High" }
  ]
};

export const DEFAULT_STRESS_RESULT = {
  event_type: "Geopolitical",
  impact_score: 9,
  is_triggered: true,
  trigger_threshold: 7,
  scenario_name: "Synthetic Geopolitical Shock Scenario",
  portfolio_value_before: 14000000.0,
  portfolio_value_after: 12768000.0,
  absolute_loss: 1232000.0,
  percentage_change: -8.8,
  disclaimer: "Synthetic hackathon assumptions for demonstration purposes, not real financial forecasts.",
  asset_breakdown: [
    { asset_id: "A001", asset_name: "Tata Motors Equity", asset_type: "Equity", sector: "Automotive", value_before: 2500000.0, shock_pct: -10.0, value_after: 2250000.0, change_value: -250000.0 },
    { asset_id: "A002", asset_name: "Reliance Industries Equity", asset_type: "Equity", sector: "Energy", value_before: 3000000.0, shock_pct: -10.0, value_after: 2700000.0, change_value: -300000.0 },
    { asset_id: "A003", asset_name: "HDFC Bank Senior Debt", asset_type: "Corporate Bond", sector: "Banking", value_before: 1500000.0, shock_pct: -5.0, value_after: 1425000.0, change_value: -75000.0 },
    { asset_id: "A004", asset_name: "Adani Enterprises Term Loan", asset_type: "Loan", sector: "Infrastructure", value_before: 1200000.0, shock_pct: -4.0, value_after: 1152000.0, change_value: -48000.0 },
    { asset_id: "A005", asset_name: "India Sovereign 10Y G-Sec", asset_type: "Government Bond", sector: "Sovereign", value_before: 2000000.0, shock_pct: 2.0, value_after: 2040000.0, change_value: 40000.0 },
    { asset_id: "A006", asset_name: "ICICI Subordinated Note", asset_type: "Corporate Bond", sector: "Banking", value_before: 800000.0, shock_pct: -5.0, value_after: 760000.0, change_value: -40000.0 },
    { asset_id: "A007", asset_name: "Crude Oil Energy Swap", asset_type: "Derivative", sector: "Energy", value_before: 600000.0, shock_pct: -6.0, value_after: 564000.0, change_value: -36000.0 },
    { asset_id: "A008", asset_name: "Industrial Metals Index ETF", asset_type: "Commodity Exposure", sector: "Materials", value_before: 900000.0, shock_pct: 8.0, value_after: 972000.0, change_value: 72000.0 },
    { asset_id: "A009", asset_name: "Infosys Technologies Equity", asset_type: "Equity", sector: "Technology", value_before: 1800000.0, shock_pct: -10.0, value_after: 1620000.0, change_value: -180000.0 },
    { asset_id: "A010", asset_name: "Commercial Real Estate Syndicate Loan", asset_type: "Loan", sector: "Real Estate", value_before: 700000.0, shock_pct: -4.0, value_after: 672000.0, change_value: -28000.0 }
  ]
};
