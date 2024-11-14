from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal, Optional
from enum import Enum

class TestCategory(str, Enum):
    SEMANTIC = "Semantic"
    REPORT = "Report"
    MOCK = "Mock"

class TestStatus(str, Enum):
    PASS = "Pass"
    FAIL = "Fail"
    ERROR = "Error"
    SKIPPED = "Skipped"

class TestResult(BaseModel):
    id: str = Field(..., description="Unique identifier for the test result")
    testName: str = Field(..., description="Name of the test")
    status: TestStatus
    category: TestCategory
    details: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    duration: float = Field(..., description="Test duration in seconds")
    errorMessage: Optional[str] = None
    stackTrace: Optional[str] = None

class TestResultCreate(BaseModel):
    testName: str
    status: TestStatus
    category: TestCategory
    details: str
    duration: float
    errorMessage: Optional[str] = None
    stackTrace: Optional[str] = None 