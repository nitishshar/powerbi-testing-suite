import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatButtonToggleModule } from '@angular/material/button-toggle';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-test-filters',
  standalone: true,
  imports: [CommonModule, MatButtonToggleModule, FormsModule],
  template: `
    <mat-button-toggle-group [(ngModel)]="selectedCategory" 
                            (change)="categoryChange.emit(selectedCategory)">
      <mat-button-toggle value="all">All</mat-button-toggle>
      <mat-button-toggle value="Semantic">Semantic</mat-button-toggle>
      <mat-button-toggle value="Report">Report</mat-button-toggle>
      <mat-button-toggle value="Mock">Mock</mat-button-toggle>
    </mat-button-toggle-group>
  `,
  styles: [`
    :host {
      display: block;
      margin: 16px;
    }
  `]
})
export class TestFiltersComponent {
  @Output() categoryChange = new EventEmitter<string>();
  selectedCategory = 'all';
} 