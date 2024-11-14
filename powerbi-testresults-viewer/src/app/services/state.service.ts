import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { TestResult } from '../models/test-result.model';

export interface AppState {
  testResults: TestResult[];
  loading: boolean;
  error: string | null;
  selectedCategory: string;
}

const initialState: AppState = {
  testResults: [],
  loading: false,
  error: null,
  selectedCategory: 'all'
};

@Injectable({
  providedIn: 'root'
})
export class StateService {
  private state = new BehaviorSubject<AppState>(initialState);

  getState(): Observable<AppState> {
    return this.state.asObservable();
  }

  updateTestResults(results: TestResult[]) {
    this.state.next({
      ...this.state.value,
      testResults: results,
      loading: false,
      error: null
    });
  }

  setLoading(loading: boolean) {
    this.state.next({
      ...this.state.value,
      loading
    });
  }

  setError(error: string | null) {
    this.state.next({
      ...this.state.value,
      error,
      loading: false
    });
  }

  setSelectedCategory(category: string) {
    this.state.next({
      ...this.state.value,
      selectedCategory: category
    });
  }
} 