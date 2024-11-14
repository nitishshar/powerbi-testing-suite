from typing import List
from pathlib import Path
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd
from ..test_execution.base_test_methods import TestResult
from ...config.settings import settings

class TestReportGenerator:
    """Generates HTML reports from test results"""
    
    def __init__(self, results: List[TestResult]):
        self.results = results
        
    def generate_report(self) -> Path:
        """Generate and save an HTML report"""
        df = pd.DataFrame([r.dict() for r in self.results])
        
        # Create visualizations
        status_pie = self._create_status_pie(df)
        category_bar = self._create_category_bar(df)
        
        # Generate HTML
        html_content = self._generate_html_content(df, status_pie, category_bar)
        
        # Save report
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = settings.REPORTS_DIR / f"test_report_{timestamp}.html"
        report_path.write_text(html_content)
        
        return report_path

    def _create_status_pie(self, df: pd.DataFrame) -> go.Figure:
        """Create pie chart of test statuses"""
        return go.Figure(data=[go.Pie(
            labels=df['status'].value_counts().index,
            values=df['status'].value_counts().values
        )])

    def _create_category_bar(self, df: pd.DataFrame) -> go.Figure:
        """Create bar chart of test categories"""
        return go.Figure(data=[go.Bar(
            x=df['category'].value_counts().index,
            y=df['category'].value_counts().values
        )]) 