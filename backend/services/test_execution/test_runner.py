from typing import List
import asyncio
from services.results.models import TestResult
from services.powerbi.client import PowerBIClient
from services.test_execution.test_methods import PowerBITestMethods
from services.reporting.report_generator import TestReportGenerator
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class TestRunner:
    def __init__(self):
        self.pbi_client = PowerBIClient()
        self.test_methods = PowerBITestMethods(self.pbi_client)

    async def run_all_tests(self) -> List[TestResult]:
        """Runs all Power BI tests and generates a report"""
        logger.info("Starting Power BI test suite execution")
        
        results = []
        try:
            # Run semantic model tests
            schema_result = await self.test_methods.test_schema_integrity()
            results.append(schema_result)
            
            if schema_result.status == "Pass":
                # Only run measure tests if schema is valid
                measure_result = await self.test_methods.test_measure_calculations()
                results.append(measure_result)
            
            # Run report tests
            report_result = await self.test_methods.test_report_visuals()
            results.append(report_result)

            # Generate test report
            report_generator = TestReportGenerator(results)
            report_path = Path("reports") / f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
            report_generator.generate_html_report(report_path)
            
            logger.info(f"Test suite execution completed. Results saved to {report_path}")
            
            return results
            
        except Exception as e:
            logger.error(f"Error during test execution: {str(e)}")
            raise

    async def run_specific_tests(self, test_categories: List[str]) -> List[TestResult]:
        """Runs specific categories of tests"""
        results = []
        
        if "semantic" in test_categories:
            results.append(await self.test_methods.test_schema_integrity())
            results.append(await self.test_methods.test_measure_calculations())
            
        if "report" in test_categories:
            results.append(await self.test_methods.test_report_visuals())
            
        return results 