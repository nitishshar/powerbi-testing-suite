from typing import List, Dict, Any
from .base_test_methods import BaseTestMethods
from services.results.models import TestResult, TestCategory
from services.powerbi.client import PowerBIClient

class SemanticTestMethods(BaseTestMethods):
    """Implementation of semantic model test methods"""

    def __init__(self, config: TestConfig, pbi_client: PowerBIClient):
        super().__init__(config)
        self.pbi_client = pbi_client

    async def execute(self) -> List[TestResult]:
        """Execute all semantic test methods"""
        results = []
        results.append(await self._handle_test_execution(
            "Schema Validation",
            TestCategory.SEMANTIC,
            self._validate_schema
        ))
        results.append(await self._handle_test_execution(
            "Relationships Validation",
            TestCategory.SEMANTIC,
            self._validate_relationships
        ))
        results.append(await self._handle_test_execution(
            "Measures Validation",
            TestCategory.SEMANTIC,
            self._validate_measures
        ))
        return results

    async def _validate_schema(self) -> str:
        """Validate the semantic model schema"""
        schema = await self.pbi_client.get_model_schema()
        
        # Validate required tables
        for table_config in self.config.semantic_tests.get("required_tables", []):
            table = next((t for t in schema["tables"] if t["name"] == table_config.name), None)
            if not table:
                raise ValueError(f"Required table {table_config.name} not found")
            
            # Validate columns
            for col_config in table_config.required_columns:
                col = next((c for c in table["columns"] if c["name"] == col_config.name), None)
                if not col:
                    raise ValueError(f"Required column {col_config.name} not found in table {table_config.name}")
                if col["dataType"] != col_config.data_type:
                    raise ValueError(
                        f"Column {col_config.name} in table {table_config.name} "
                        f"has incorrect data type: {col['dataType']} != {col_config.data_type}"
                    )
        
        return "Schema validation completed successfully"

    async def _validate_relationships(self) -> str:
        """Validate model relationships"""
        schema = await self.pbi_client.get_model_schema()
        
        for rel_config in self.config.semantic_tests.get("required_relationships", []):
            rel = next((r for r in schema["relationships"] 
                       if r["fromTable"] == rel_config.from_table 
                       and r["toTable"] == rel_config.to_table), None)
            
            if not rel:
                raise ValueError(
                    f"Required relationship from {rel_config.from_table} "
                    f"to {rel_config.to_table} not found"
                )
        
        return "Relationship validation completed successfully"

    async def _validate_measures(self) -> str:
        """Validate DAX measures"""
        measures = await self.pbi_client.get_measures()
        
        for measure_config in self.config.semantic_tests.get("required_measures", []):
            measure = next((m for m in measures if m["name"] == measure_config["name"]), None)
            if not measure:
                raise ValueError(f"Required measure {measure_config['name']} not found")
            
            # Validate measure calculation if test data is provided
            if "test_data" in measure_config:
                result = await self.pbi_client.execute_dax_query(
                    f"EVALUATE ROW(\"Value\", [{measure_config['name']}])"
                )
                actual_value = result["results"][0]["tables"][0]["rows"][0]["Value"]
                expected_value = measure_config["test_data"]["expected_value"]
                
                if abs(actual_value - expected_value) > 0.0001:  # Allow small floating-point differences
                    raise ValueError(
                        f"Measure {measure_config['name']} calculation mismatch. "
                        f"Expected: {expected_value}, Got: {actual_value}"
                    )
        
        return "Measure validation completed successfully" 