export interface TestResult {
  testName: string;
  status: 'Pass' | 'Fail';
  category: 'Semantic' | 'Report' | 'Data Quality' | 'Security';
  details: string;
  timestamp: string;
  duration: number;
  owner: string;
  priority: 'Critical' | 'High' | 'Medium' | 'Low';
  lastSuccess: string;
}

export interface TestMetrics {
  totalTests: number;
  passRate: number;
  criticalFailures: number;
  avgDuration: number;
  lastRunTimestamp: string;
  categoryBreakdown: {
    category: string;
    total: number;
    passed: number;
  }[];
} 