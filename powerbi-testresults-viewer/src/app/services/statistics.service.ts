import { Injectable } from '@angular/core';
import { TestResult } from '../models/test-result.model';

export interface TestStatistics {
  totalTests: number;
  passedTests: number;
  failedTests: number;
  passRate: number;
  categoryBreakdown: {
    [key: string]: {
      total: number;
      passed: number;
      failed: number;
    };
  };
}

@Injectable({
  providedIn: 'root'
})
export class StatisticsService {
  calculateStatistics(results: TestResult[]): TestStatistics {
    const stats: TestStatistics = {
      totalTests: results.length,
      passedTests: 0,
      failedTests: 0,
      passRate: 0,
      categoryBreakdown: {}
    };

    results.forEach(result => {
      // Update overall stats
      if (result.status === 'Pass') {
        stats.passedTests++;
      } else {
        stats.failedTests++;
      }

      // Update category breakdown
      if (!stats.categoryBreakdown[result.category]) {
        stats.categoryBreakdown[result.category] = {
          total: 0,
          passed: 0,
          failed: 0
        };
      }

      stats.categoryBreakdown[result.category].total++;
      if (result.status === 'Pass') {
        stats.categoryBreakdown[result.category].passed++;
      } else {
        stats.categoryBreakdown[result.category].failed++;
      }
    });

    stats.passRate = stats.totalTests > 0 
      ? (stats.passedTests / stats.totalTests) * 100 
      : 0;

    return stats;
  }
} 