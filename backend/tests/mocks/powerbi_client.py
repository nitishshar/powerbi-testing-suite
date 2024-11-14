class PowerBIClient:
    def __init__(self):
        self.workspace_id = "test-workspace"
        
    def get_model_schema(self):
        # Mock implementation
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
    
    def execute_dax_query(self, query):
        # Mock DAX query execution
        return {
            "results": [
                {"value": 12500}  # Mock result
            ]
        } 