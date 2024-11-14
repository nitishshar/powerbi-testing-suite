import { Injectable } from '@angular/core';
import { TestResult } from '../models/test-result.model';

@Injectable({
  providedIn: 'root'
})
export class ExportService {
  exportToCsv(results: TestResult[]) {
    const headers = ['Test Name', 'Status', 'Category', 'Details', 'Timestamp'];
    const csvData = results.map(result => [
      result.testName,
      result.status,
      result.category,
      result.details,
      result.timestamp
    ]);

    const csvContent = [
      headers.join(','),
      ...csvData.map(row => row.join(','))
    ].join('\n');

    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `test-results-${new Date().toISOString()}.csv`;
    link.click();
    window.URL.revokeObjectURL(url);
  }

  exportToJson(results: TestResult[]) {
    const jsonContent = JSON.stringify(results, null, 2);
    const blob = new Blob([jsonContent], { type: 'application/json' });
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `test-results-${new Date().toISOString()}.json`;
    link.click();
    window.URL.revokeObjectURL(url);
  }
} 