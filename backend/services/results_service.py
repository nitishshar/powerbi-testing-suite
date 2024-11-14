import json
from pathlib import Path

class ResultsService:
    def __init__(self):
        self.results_file = Path("tests/results.json")

    async def get_results(self):
        if not self.results_file.exists():
            return {"results": []}
        
        with open(self.results_file, "r") as f:
            return json.load(f) 