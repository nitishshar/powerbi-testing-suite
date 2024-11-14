import pytest
from services.test_execution.test_methods import PowerBITestMethods
from tests.mock_data.powerbi_responses import PowerBIMockData
from services.results.models import TestStatus, TestCategory
from unittest.mock import AsyncMock, patch

class TestPowerBIMethods:
    @pytest.fixture
    def mock_pbi_client(self):
        client = AsyncMock()
        client.get_model_schema.return_value = PowerBIMockData.get_dataset_response()
        client.execute_dax_query.return_value = PowerBIMockData.get_dax_query_response()
        client.get_report.return_value = PowerBIMockData.get_report_response()
        return client

    @pytest.fixture
    def test_methods(self, mock_pbi_client):
        return PowerBITestMethods(mock_pbi_client)

    @pytest.mark.asyncio
    async def test_schema_integrity_success(self, test_methods):
        result = await test_methods.test_schema_integrity()
        assert result.status == TestStatus.PASS
        assert result.category == TestCategory.SEMANTIC
        assert "All required tables" in result.details

    @pytest.mark.asyncio
    async def test_schema_integrity_failure(self, mock_pbi_client, test_methods):
        # Modify mock response to simulate missing table
        modified_response = PowerBIMockData.get_dataset_response()
        modified_response["value"][0]["tables"] = [t for t in modified_response["value"][0]["tables"] 
                                                 if t["name"] != "Sales"]
        mock_pbi_client.get_model_schema.return_value = modified_response
        
        result = await test_methods.test_schema_integrity()
        assert result.status == TestStatus.FAIL
        assert "Missing required tables" in result.errorMessage

    @pytest.mark.asyncio
    async def test_measure_calculations_success(self, test_methods):
        result = await test_methods.test_measure_calculations()
        assert result.status == TestStatus.PASS
        assert result.category == TestCategory.SEMANTIC
        assert "measures calculate correctly" in result.details

    @pytest.mark.asyncio
    async def test_report_visuals_success(self, test_methods):
        result = await test_methods.test_report_visuals()
        assert result.status == TestStatus.PASS
        assert result.category == TestCategory.REPORT
        assert "report visuals present" in result.details 