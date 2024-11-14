import json
from datetime import datetime
from pathlib import Path

def update_test_results(test_output):
    results_file = Path(__file__).parent.parent / "backend" / "db.json"
    
    new_result = {
        "id": len(test_output["results"]) + 1,
        "testName": test_output["feature"],
        "status": "PASS" if test_output["success"] else "FAIL",
        "details": test_output["details"],
        "timestamp": datetime.utcnow().isoformat()
    }
    
    try:
        with open(results_file, 'r') as f:
            current_results = json.load(f)
    except FileNotFoundError:
        current_results = {"results": []}
    
    current_results["results"].append(new_result)
    
    with open(results_file, 'w') as f:
        json.dump(current_results, f, indent=2)

if __name__ == "__main__":
    # Example test output
    test_output = {
        "feature": "Semantic Model Validation",
        "success": True,
        "details": "All schema validations passed"
    }
    update_test_results(test_output) 