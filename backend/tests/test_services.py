import pytest
from services.powerbi_service import PowerBIService
from services.results_service import ResultsService

class TestPowerBIService:
    def test_get_model_schema(self, powerbi_service):
        schema = powerbi_service.get_model_schema()
        assert "tables" in schema
        assert len(schema["tables"]) > 0
        assert "name" in schema["tables"][0]
        assert "columns" in schema["tables"][0]

class TestResultsService:
    async def test_get_results(self, results_service, mock_test_results):
        results = await results_service.get_results()
        assert "results" in results
        assert isinstance(results["results"], list) 