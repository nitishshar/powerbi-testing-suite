import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { TestResult } from '../models/test-result.model';

@Injectable({
  providedIn: 'root'
})
export class MockDataService {
  private mockResults: TestResult[] = [
    {
      testName: 'Revenue Calculation Validation',
      status: 'Pass',
      category: 'Semantic',
      details: 'All revenue calculations match expected values within 0.01% tolerance',
      timestamp: new Date().toISOString(),
      duration: 2.3,
      owner: 'Finance Analytics',
      priority: 'Critical',
      lastSuccess: new Date().toISOString()
    },
    {
      testName: 'Market Share Analysis',
      status: 'Fail',
      category: 'Semantic',
      details: 'Market share percentage exceeds 100% for APAC region',
      timestamp: new Date().toISOString(),
      duration: 3.1,
      owner: 'Market Intelligence',
      priority: 'High',
      lastSuccess: new Date(Date.now() - 86400000).toISOString()
    },
    {
      testName: 'Sales Performance Dashboard',
      status: 'Pass',
      category: 'Report',
      details: 'All KPIs refresh successfully, data matches source system',
      timestamp: new Date().toISOString(),
      duration: 5.7,
      owner: 'Sales Analytics',
      priority: 'High',
      lastSuccess: new Date().toISOString()
    },
    {
      testName: 'Customer Segmentation Model',
      status: 'Pass',
      category: 'Data Quality',
      details: 'Segmentation rules applied correctly across all customer groups',
      timestamp: new Date().toISOString(),
      duration: 8.2,
      owner: 'Customer Analytics',
      priority: 'Medium',
      lastSuccess: new Date().toISOString()
    },
    {
      testName: 'Regional Access Controls',
      status: 'Fail',
      category: 'Security',
      details: 'Row-level security not enforced for contractor accounts',
      timestamp: new Date().toISOString(),
      duration: 1.5,
      owner: 'Security Team',
      priority: 'Critical',
      lastSuccess: new Date(Date.now() - 172800000).toISOString()
    },
    {
      testName: 'Product Hierarchy Validation',
      status: 'Pass',
      category: 'Data Quality',
      details: 'Product categorization hierarchy maintains referential integrity',
      timestamp: new Date().toISOString(),
      duration: 4.8,
      owner: 'Product Analytics',
      priority: 'Medium',
      lastSuccess: new Date().toISOString()
    },
    {
      testName: 'Profit Margin Calculations',
      status: 'Pass',
      category: 'Semantic',
      details: 'Margin calculations validated against financial statements',
      timestamp: new Date().toISOString(),
      duration: 3.4,
      owner: 'Finance Analytics',
      priority: 'High',
      lastSuccess: new Date().toISOString()
    },
    {
      testName: 'Executive Summary Dashboard',
      status: 'Pass',
      category: 'Report',
      details: 'All executive metrics refresh within SLA threshold',
      timestamp: new Date().toISOString(),
      duration: 6.9,
      owner: 'Executive Reporting',
      priority: 'Critical',
      lastSuccess: new Date().toISOString()
    }
  ];

  getResults(): Observable<TestResult[]> {
    return of(this.mockResults);
  }
} 