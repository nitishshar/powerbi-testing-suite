import { Component, OnInit, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTableModule } from '@angular/material/table';
import { MatCardModule } from '@angular/material/card';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatPaginatorModule, MatPaginator } from '@angular/material/paginator';
import { MatSortModule, MatSort } from '@angular/material/sort';
import { MatDialog, MatDialogModule } from '@angular/material/dialog';
import { TestResult } from '../models/test-result.model';
import { MockDataService } from '../services/mock-data.service';
import { TestSummaryComponent } from '../components/test-summary/test-summary.component';
import { TestFiltersComponent } from '../components/test-filters/test-filters.component';
import { TestDetailsDialogComponent } from '../components/test-details-dialog/test-details-dialog.component';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    MatTableModule,
    MatCardModule,
    MatProgressSpinnerModule,
    MatPaginatorModule,
    MatSortModule,
    MatDialogModule,
    TestSummaryComponent,
    TestFiltersComponent
  ],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  testResults: TestResult[] = [];
  filteredResults: TestResult[] = [];
  displayedColumns: string[] = [
    'status',
    'priority',
    'testName',
    'category',
    'duration',
    'owner',
    'lastSuccess'
  ];
  loading = false;
  error: string | null = null;

  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(
    private mockDataService: MockDataService,
    private dialog: MatDialog
  ) {}

  ngOnInit() {
    this.loading = true;
    this.mockDataService.getResults().subscribe({
      next: (results) => {
        this.testResults = results;
        this.filteredResults = results;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Failed to load test results';
        this.loading = false;
      }
    });
  }

  onCategoryChange(category: string) {
    this.filteredResults = category === 'all' 
      ? this.testResults 
      : this.testResults.filter(test => test.category === category);
  }

  openDetails(result: TestResult): void {
    const dialogRef = this.dialog.open(TestDetailsDialogComponent, {
      data: result,
      width: '800px',
      maxWidth: '90vw',
      panelClass: ['glass-card', 'centered-dialog'],
      backdropClass: 'dialog-backdrop',
      autoFocus: false,
      disableClose: false,
      hasBackdrop: true,
      enterAnimationDuration: '150ms',
      exitAnimationDuration: '150ms',
      maxHeight: '90vh',
      restoreFocus: false
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result === 'rerun') {
        // Handle test rerun
        console.log('Test rerun requested');
      }
    });
  }
}
