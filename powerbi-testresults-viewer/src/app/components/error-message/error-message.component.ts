import { Component, Input, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-error-message',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatButtonModule],
  template: `
    <mat-card class="error-card">
      <mat-card-content>
        <div class="error-icon">⚠️</div>
        <div class="error-text">{{ message }}</div>
        <button mat-raised-button color="primary" (click)="retry.emit()">
          Retry
        </button>
      </mat-card-content>
    </mat-card>
  `,
  styles: [`
    .error-card {
      margin: 20px;
      text-align: center;
    }
    .error-icon {
      font-size: 48px;
      margin-bottom: 16px;
    }
    .error-text {
      color: #f44336;
      margin-bottom: 16px;
    }
  `]
})
export class ErrorMessageComponent {
  @Input() message = 'An error occurred while loading the data.';
  @Output() retry = new EventEmitter<void>();
} 