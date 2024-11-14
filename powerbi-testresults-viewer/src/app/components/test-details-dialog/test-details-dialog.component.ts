import { Component, Inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatDialogModule, MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { TestResult } from '../../models/test-result.model';

@Component({
  selector: 'app-test-details-dialog',
  standalone: true,
  imports: [CommonModule, MatDialogModule, MatButtonModule, MatIconModule],
  template: `
    <div class="dialog-container glass-card">
      <div class="dialog-header">
        <h2 mat-dialog-title>
          <mat-icon [class]="data.status.toLowerCase()">
            {{ data.status === 'Pass' ? 'check_circle' : 'error' }}
          </mat-icon>
          <span class="title-text">{{ data.testName }}</span>
        </h2>
        <button mat-icon-button (click)="close()">
          <mat-icon>close</mat-icon>
        </button>
      </div>

      <mat-dialog-content>
        <div class="detail-grid">
          <div class="detail-item">
            <div class="label">Status</div>
            <div class="value">
              <span class="status-badge" [class]="data.status.toLowerCase()">
                {{ data.status }}
              </span>
            </div>
          </div>

          <div class="detail-item">
            <div class="label">Priority</div>
            <div class="value">
              <span class="priority-badge" [class]="data.priority.toLowerCase()">
                {{ data.priority }}
              </span>
            </div>
          </div>

          <div class="detail-item">
            <div class="label">Category</div>
            <div class="value highlight">{{ data.category }}</div>
          </div>

          <div class="detail-item">
            <div class="label">Owner</div>
            <div class="value highlight">{{ data.owner }}</div>
          </div>

          <div class="detail-item">
            <div class="label">Duration</div>
            <div class="value highlight">{{ data.duration.toFixed(1) }}s</div>
          </div>

          <div class="detail-item">
            <div class="label">Last Success</div>
            <div class="value highlight">{{ data.lastSuccess | date:'medium' }}</div>
          </div>

          <div class="detail-item full-width">
            <div class="label">Details</div>
            <div class="value details-text">{{ data.details }}</div>
          </div>
        </div>
      </mat-dialog-content>

      <mat-dialog-actions align="end">
        <button mat-button class="glass-button" (click)="close()">Close</button>
        <button mat-raised-button color="primary" (click)="handleRerun()">
          <mat-icon>refresh</mat-icon>
          Rerun Test
        </button>
      </mat-dialog-actions>
    </div>
  `,
  styles: [`
    .dialog-container {
      color: #ffffff;
      overflow: hidden;
    }

    .dialog-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 32px;
      background: rgba(255, 255, 255, 0.1);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);

      h2 {
        display: flex;
        align-items: center;
        margin: 0;
        
        mat-icon {
          margin-right: 12px;
          font-size: 28px;
          width: 28px;
          height: 28px;
          
          &.pass { color: #4caf50; }
          &.fail { color: #ef5350; }
        }

        .title-text {
          font-size: 24px;
          font-weight: 500;
          color: #ffffff;
        }
      }
    }

    mat-dialog-content {
      padding: 0 !important;
      margin: 0 !important;
      max-height: none !important;
      overflow: hidden !important;
    }

    .detail-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      padding: 32px;
      width: 100%;
      box-sizing: border-box;
    }

    .detail-item {
      &.full-width {
        grid-column: 1 / -1;
      }

      .label {
        font-size: 14px;
        color: rgba(255, 255, 255, 0.7);
        margin-bottom: 8px;
        font-weight: 500;
      }

      .value {
        font-size: 16px;
        color: #ffffff;
        
        &.details-text {
          line-height: 1.6;
          white-space: pre-wrap;
          background: rgba(255, 255, 255, 0.05);
          padding: 16px;
          border-radius: 8px;
          border: 1px solid rgba(255, 255, 255, 0.1);
        }
      }

      .highlight {
        color: #ffffff;
        font-weight: 500;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
      }
    }

    mat-dialog-actions {
      padding: 16px 24px;
      margin: 0;
      background: rgba(255, 255, 255, 0.05);
      border-top: 1px solid rgba(255, 255, 255, 0.1);
    }

    .glass-button {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.1);
      
      &:hover {
        background: rgba(255, 255, 255, 0.2);
      }
    }
  `]
})
export class TestDetailsDialogComponent {
  constructor(
    @Inject(MAT_DIALOG_DATA) public data: TestResult,
    private dialogRef: MatDialogRef<TestDetailsDialogComponent>
  ) {}

  close(): void {
    this.dialogRef.close();
  }

  handleRerun(): void {
    // Implement test rerun logic here
    console.log('Rerunning test:', this.data.testName);
    // You can emit an event or call a service method here
    this.dialogRef.close('rerun');
  }
} 