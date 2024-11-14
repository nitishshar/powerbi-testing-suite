import pytest
from pathlib import Path
from ..services.powerbi.client import PowerBIClient
from ..config.test_config import TestConfig

@pytest.fixture
def test_config():
    return TestConfig.from_yaml(Path("tests/test_config.yaml"))

@pytest.fixture
def mock_pbi_client(mocker):
    return mocker.Mock(spec=PowerBIClient) 