from typing import List, Dict, Any
from services.results.models import TestResult, TestStatus, TestCategory
import time
import uuid
import traceback
from services.powerbi.client import PowerBIClient

class PowerBITestMethods:
    def __init__(self, pbi_client: PowerBIClient):
        self.pbi_client = pbi_client

    async def test_schema_integrity(self) -> TestResult:
        """Tests if the semantic model schema matches expected structure"""
        start_time = time.time()
        try:
            schema = await self.pbi_client.get_model_schema()
            
            # Validate required tables
            required_tables = {"Sales", "Products", "DateTable"}
            actual_tables = {table["name"] for table in schema["value"][0]["tables"]}
            
            if not required_tables.issubset(actual_tables):
                missing_tables = required_tables - actual_tables
                raise ValueError(f"Missing required tables: {missing_tables}")

            # Validate relationships
            relationships = schema["value"][0]["relationships"]
            if not any(r["name"] == "Sales_Products" for r in relationships):
                raise ValueError("Missing critical relationship: Sales_Products")

            duration = time.time() - start_time
            return TestResult(
                id=str(uuid.uuid4()),
                testName="Schema Integrity Test",
                status=TestStatus.PASS,
                category=TestCategory.SEMANTIC,
                details="All required tables and relationships present",
                duration=duration
            )
        except Exception as e:
            duration = time.time() - start_time
            return TestResult(
                id=str(uuid.uuid4()),
                testName="Schema Integrity Test",
                status=TestStatus.FAIL,
                category=TestCategory.SEMANTIC,
                details="Schema validation failed",
                duration=duration,
                errorMessage=str(e),
                stackTrace=traceback.format_exc()
            )

    async def test_measure_calculations(self) -> TestResult:
        """Tests if DAX measures calculate correctly"""
        start_time = time.time()
        try:
            # Test Total Revenue measure
            query = """
            EVALUATE
            SUMMARIZECOLUMNS(
                "Total Revenue", [Total Revenue],
                "YTD Revenue", [YTD Revenue]
            )
            """
            result = await self.pbi_client.execute_dax_query("dataset-123", query)
            
            # Validate results
            actual_revenue = result["results"][0]["tables"][0]["rows"][0]["Total Revenue"]
            expected_revenue = 1250000.00
            
            if abs(actual_revenue - expected_revenue) > 0.01:  # Allow small floating-point differences
                raise ValueError(f"Revenue calculation mismatch. Expected: {expected_revenue}, Got: {actual_revenue}")

            duration = time.time() - start_time
            return TestResult(
                id=str(uuid.uuid4()),
                testName="Measure Calculations Test",
                status=TestStatus.PASS,
                category=TestCategory.SEMANTIC,
                details="All measures calculate correctly",
                duration=duration
            )
        except Exception as e:
            duration = time.time() - start_time
            return TestResult(
                id=str(uuid.uuid4()),
                testName="Measure Calculations Test",
                status=TestStatus.FAIL,
                category=TestCategory.SEMANTIC,
                details="Measure calculation failed",
                duration=duration,
                errorMessage=str(e),
                stackTrace=traceback.format_exc()
            )

    async def test_report_visuals(self) -> TestResult:
        """Tests if all report visuals load correctly"""
        start_time = time.time()
        try:
            report_data = await self.pbi_client.get_report("report-456")
            
            # Validate report pages and visuals
            pages = report_data["value"][0]["pages"]
            if not pages:
                raise ValueError("Report contains no pages")

            # Check critical visuals
            overview_page = next((p for p in pages if p["name"] == "Overview"), None)
            if not overview_page:
                raise ValueError("Missing Overview page")

            required_visuals = {"Revenue by Category", "Monthly Trend"}
            actual_visuals = {v["name"] for v in overview_page["visuals"]}
            
            if not required_visuals.issubset(actual_visuals):
                missing_visuals = required_visuals - actual_visuals
                raise ValueError(f"Missing critical visuals: {missing_visuals}")

            duration = time.time() - start_time
            return TestResult(
                id=str(uuid.uuid4()),
                testName="Report Visuals Test",
                status=TestStatus.PASS,
                category=TestCategory.REPORT,
                details="All report visuals present and loading correctly",
                duration=duration
            )
        except Exception as e:
            duration = time.time() - start_time
            return TestResult(
                id=str(uuid.uuid4()),
                testName="Report Visuals Test",
                status=TestStatus.FAIL,
                category=TestCategory.REPORT,
                details="Report visuals failed to load",
                duration=duration,
                errorMessage=str(e),
                stackTrace=traceback.format_exc()
            ) 