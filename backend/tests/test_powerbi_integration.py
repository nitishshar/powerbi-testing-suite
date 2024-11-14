import pytest
from services.powerbi.client import PowerBIClient
from services.test_execution.executor import TestExecutor
from services.results.models import TestStatus, TestCategory
from config.test_config import TestConfig
import aiohttp
from unittest.mock import patch, MagicMock

class TestPowerBIIntegration:
    @pytest.fixture
    def test_config(self):
        return TestConfig(
            workspace_id="test-workspace",
            dataset_id="test-dataset",
            semantic_tests={
                "required_tables": [
                    {
                        "name": "Sales",
                        "required_columns": [
                            {"name": "Date", "data_type": "datetime"},
                            {"name": "Revenue", "data_type": "decimal"}
                        ]
                    }
                ]
            }
        )

    @pytest.fixture
    async def mock_pbi_client(self):
        with patch('services.powerbi.client.PowerBIClient') as mock:
            yield mock

    @pytest.mark.asyncio
    async def test_schema_validation_success(self, mock_pbi_client, test_config):
        mock_pbi_client.get_model_schema.return_value = {
            "tables": [
                {
                    "name": "Sales",
                    "columns": [
                        {"name": "Date", "dataType": "datetime"},
                        {"name": "Revenue", "dataType": "decimal"}
                    ]
                }
            ]
        }
        
        executor = TestExecutor(test_config, pbi_client=mock_pbi_client)
        results = await executor.run_specific_tests(["semantic"])
        
        assert len(results) == 1
        assert results[0].status == TestStatus.PASS
        assert results[0].category == TestCategory.SEMANTIC

    @pytest.mark.asyncio
    async def test_schema_validation_failure(self, mock_pbi_client):
        mock_pbi_client.get_model_schema.side_effect = Exception("API Error")
        
        executor = TestExecutor()
        results = await executor.run_semantic_tests()
        
        assert len(results) == 1
        assert results[0].status == TestStatus.FAIL
        assert results[0].category == TestCategory.SEMANTIC
        assert results[0].errorMessage == "API Error" 