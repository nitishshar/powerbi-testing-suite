from powerbi_client import PowerBIClient
import pytest
from typing import Dict, Any

class TestPowerBIModel:
    def setup_method(self):
        self.pbi_client = PowerBIClient()
        self.expected_schema = self.load_expected_schema()

    def load_expected_schema(self) -> Dict[str, Any]:
        return {
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

    def test_schema_validation(self):
        current_schema = self.pbi_client.get_model_schema()
        assert current_schema == self.expected_schema 