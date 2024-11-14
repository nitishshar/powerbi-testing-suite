import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatIconModule } from '@angular/material/icon';
import { TestResult } from '../../models/test-result.model';

interface CategorySummary {
  category: string;
  total: number;
  passed: number;
}

@Component({
  selector: 'app-test-summary',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatProgressBarModule, MatIconModule],
  template: `
    <div class="metrics-grid">
      <!-- Test Health Overview -->
      <mat-card class="metric-card glass-card">
        <mat-card-header>
          <div class="header-icon">
            <mat-icon [class.success]="passRate > 90" 
                     [class.warning]="passRate <= 90 && passRate > 70"
                     [class.error]="passRate <= 70">
              {{ passRate > 90 ? 'check_circle' : passRate > 70 ? 'warning_amber' : 'error_outline' }}
            </mat-icon>
          </div>
          <mat-card-title>Test Health Overview</mat-card-title>
        </mat-card-header>
        <mat-card-content>
          <div class="health-stats">
            <div class="pass-rate">{{ passRate }}%</div>
            <div class="pass-rate-label">Success Rate</div>
            <mat-progress-bar
              [mode]="'determinate'"
              [value]="passRate"
              [color]="passRate > 90 ? 'primary' : passRate > 70 ? 'accent' : 'warn'"
            ></mat-progress-bar>
            <div class="test-count">
              <span class="highlight">{{ passedTests }}</span> of <span class="highlight">{{ totalTests }}</span> Tests Passing
            </div>
          </div>
        </mat-card-content>
      </mat-card>

      <!-- Critical Tests Status -->
      <mat-card class="metric-card glass-card">
        <mat-card-header>
          <div class="header-icon">
            <mat-icon [class.error]="criticalFailures > 0">
              {{ criticalFailures > 0 ? 'error' : 'verified' }}
            </mat-icon>
          </div>
          <mat-card-title>Critical Tests Status</mat-card-title>
        </mat-card-header>
        <mat-card-content>
          <div class="critical-stats">
            <div class="stat">
              <div class="value error-text">{{ criticalFailures }}</div>
              <div class="label">Critical Failures</div>
            </div>
            <div class="stat">
              <div class="value">{{ criticalTests }}</div>
              <div class="label">Total Critical Tests</div>
            </div>
          </div>
        </mat-card-content>
      </mat-card>

      <!-- Performance Metrics -->
      <mat-card class="metric-card glass-card">
        <mat-card-header>
          <div class="header-icon">
            <mat-icon>speed</mat-icon>
          </div>
          <mat-card-title>Performance Metrics</mat-card-title>
        </mat-card-header>
        <mat-card-content>
          <div class="performance-stats">
            <div class="stat">
              <div class="value highlight">{{ avgDuration.toFixed(1) }}s</div>
              <div class="label">Average Duration</div>
            </div>
            <div class="stat">
              <div class="value highlight">{{ maxDuration.toFixed(1) }}s</div>
              <div class="label">Longest Duration</div>
            </div>
          </div>
        </mat-card-content>
      </mat-card>

      <!-- Category Analysis -->
      <mat-card class="metric-card glass-card full-width">
        <mat-card-header>
          <div class="header-icon">
            <mat-icon>analytics</mat-icon>
          </div>
          <mat-card-title>Category Analysis</mat-card-title>
        </mat-card-header>
        <mat-card-content>
          <div class="category-grid">
            <div *ngFor="let cat of getCategoryBreakdown()" class="category-item">
              <div class="category-header">
                <span class="category-name">{{ cat.category }}</span>
                <span class="category-ratio">
                  <span class="highlight">{{ cat.passed }}</span>/<span class="highlight">{{ cat.total }}</span>
                </span>
              </div>
              <mat-progress-bar
                [mode]="'determinate'"
                [value]="(cat.passed / cat.total) * 100"
                [color]="cat.passed === cat.total ? 'primary' : 'warn'"
              ></mat-progress-bar>
            </div>
          </div>
        </mat-card-content>
      </mat-card>
    </div>
  `,
  styles: [`
    .metrics-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      margin-bottom: 24px;
    }

    .metric-card {
      height: 100%;
      
      &.full-width {
        grid-column: 1 / -1;
      }

      .mat-mdc-card-header {
        padding: 16px;
        background: rgba(255, 255, 255, 0.1);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 0;
      }

      .mat-mdc-card-content {
        padding: 24px;
      }

      .header-icon {
        display: flex;
        align-items: center;
        margin-right: 12px;

        mat-icon {
          font-size: 28px;
          width: 28px;
          height: 28px;
          
          &.success { color: #4caf50; }
          &.warning { color: #ffa726; }
          &.error { color: #ef5350; }
        }
      }
    }

    .health-stats {
      text-align: center;
      
      .pass-rate {
        font-size: 48px;
        font-weight: 500;
        color: #ffffff;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
        margin-bottom: 4px;
      }

      .pass-rate-label {
        font-size: 16px;
        color: rgba(255, 255, 255, 0.7);
        margin-bottom: 16px;
      }

      .test-count {
        margin-top: 12px;
        font-size: 16px;
        color: rgba(255, 255, 255, 0.7);

        .highlight {
          color: #ffffff;
          font-weight: 500;
        }
      }
    }

    .critical-stats, .performance-stats {
      display: flex;
      justify-content: space-around;
      text-align: center;
      padding: 16px 0;

      .stat {
        .value {
          font-size: 36px;
          font-weight: 500;
          color: #ffffff;
          text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
          margin-bottom: 8px;

          &.error-text {
            color: #ef5350;
            text-shadow: 0 0 10px rgba(239, 83, 80, 0.3);
          }
        }

        .label {
          font-size: 14px;
          color: rgba(255, 255, 255, 0.7);
        }
      }
    }

    .category-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 24px;
      padding: 8px;

      .category-item {
        .category-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 12px;
          
          .category-name {
            font-size: 16px;
            font-weight: 500;
            color: #ffffff;
          }
          
          .category-ratio {
            color: rgba(255, 255, 255, 0.7);
            font-size: 14px;

            .highlight {
              color: #ffffff;
              font-weight: 500;
            }
          }
        }

        mat-progress-bar {
          height: 6px;
          border-radius: 3px;
        }
      }
    }

    .highlight {
      color: #ffffff;
      font-weight: 500;
    }
  `]
})
export class TestSummaryComponent {
  @Input() testResults: TestResult[] = [];

  get totalTests(): number {
    return this.testResults.length;
  }

  get passedTests(): number {
    return this.testResults.filter(test => test.status === 'Pass').length;
  }

  get failedTests(): number {
    return this.testResults.filter(test => test.status === 'Fail').length;
  }

  get passRate(): number {
    return this.passedTests / this.totalTests * 100;
  }

  get criticalFailures(): number {
    return this.testResults.filter(test => test.status === 'Fail' && test.priority === 'Critical').length;
  }

  get avgDuration(): number {
    return this.testResults.reduce((total, test) => total + test.duration, 0) / this.totalTests;
  }

  get maxDuration(): number {
    return Math.max(...this.testResults.map(test => test.duration));
  }

  get criticalTests(): number {
    return this.testResults.filter(test => test.priority === 'Critical').length;
  }

  getCategoryBreakdown(): CategorySummary[] {
    const categories = this.testResults.map(test => test.category);
    const uniqueCategories = [...new Set(categories)];
    return uniqueCategories.map(category => ({
      category,
      total: categories.filter(cat => cat === category).length,
      passed: this.testResults.filter(test => test.category === category && test.status === 'Pass').length
    }));
  }
} 