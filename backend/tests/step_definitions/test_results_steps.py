from typing import Dict, List
import pytest
from pytest_bdd import given, when, then, parsers
from httpx import AsyncClient

# Shared test data and state
@pytest.fixture
def test_data() -> Dict:
    return {}

# Background steps
@given("the API is running")
async def api_running(client: AsyncClient):
    response = await client.get("/health")
    assert response.status_code == 200

@given("the database is initialized")
async def db_initialized(client: AsyncClient):
    response = await client.get("/health/db")
    assert response.status_code == 200

# Scenario steps
@when("I request all test results")
async def request_all_results(client: AsyncClient, test_data: Dict):
    response = await client.get("/api/v1/tests")
    test_data['response'] = response
    test_data['data'] = response.json()

@then("the response status code should be {status_code:d}")
def check_status_code(test_data: Dict, status_code: int):
    assert test_data['response'].status_code == status_code

@then("the response should contain a list of test results")
def check_response_list(test_data: Dict):
    assert isinstance(test_data['data'], list)
    assert len(test_data['data']) > 0

@then("each test result should have required fields")
def check_required_fields(test_data: Dict):
    required_fields = {'id', 'testName', 'status', 'category', 'priority', 'duration'}
    for result in test_data['data']:
        assert all(field in result for field in required_fields)

@when(parsers.parse('I request test results with status "{status}"'))
async def request_results_by_status(client: AsyncClient, test_data: Dict, status: str):
    response = await client.get(f"/api/v1/tests", params={"status": status})
    test_data['response'] = response
    test_data['data'] = response.json()

@then(parsers.parse('all returned tests should have "{status}" status'))
def check_status_filter(test_data: Dict, status: str):
    assert all(result['status'] == status for result in test_data['data'])

@given(parsers.parse('there is a test result with id "{test_id}"'))
async def ensure_test_exists(client: AsyncClient, test_data: Dict, test_id: str):
    # First try to get the test
    response = await client.get(f"/api/v1/tests/{test_id}")
    if response.status_code != 200:
        # Create test if it doesn't exist
        test_data = {
            "id": test_id,
            "testName": "Test Example",
            "status": "Failed",
            "category": "Semantic",
            "priority": "High",
            "duration": 1.5
        }
        response = await client.post("/api/v1/tests", json=test_data)
        assert response.status_code == 201

@when("I have valid test result data")
def prepare_valid_test_data(test_data: Dict):
    test_data['new_test'] = {
        "testName": "New Test Example",
        "status": "Passed",
        "category": "Report",
        "priority": "Medium",
        "duration": 2.0
    }

@when("I submit a new test result")
async def submit_new_test(client: AsyncClient, test_data: Dict):
    response = await client.post("/api/v1/tests", json=test_data['new_test'])
    test_data['response'] = response
    test_data['data'] = response.json() 