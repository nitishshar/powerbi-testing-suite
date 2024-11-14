import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { MockDataService } from './mock-data.service';

export interface TestResult {
  testName: string;
  status: 'Pass' | 'Fail';
  details: string;
  timestamp: string;
  category: 'Semantic' | 'Report' | 'Mock';
}

@Injectable({
  providedIn: 'root'
})
export class ResultsService {
  constructor(private mockDataService: MockDataService) {}

  getTestResults(): Observable<TestResult[]> {
    // Using mock data for now
    return this.mockDataService.getResults();
  }
}
