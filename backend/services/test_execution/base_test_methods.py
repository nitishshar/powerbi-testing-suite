from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from datetime import datetime
import uuid
import time
import traceback
import logging
from config.test_config import TestConfig
from services.results.models import TestResult, TestStatus, TestCategory

logger = logging.getLogger(__name__)

class BaseTestMethods(ABC):
    """Base class for implementing test methods"""
    
    def __init__(self, config: TestConfig):
        self.config = config
        self._start_time: Optional[float] = None

    def _start_timer(self) -> None:
        """Start timing a test execution"""
        self._start_time = time.time()

    def _get_duration(self) -> float:
        """Get the duration since timer was started"""
        if self._start_time is None:
            return 0.0
        return time.time() - self._start_time

    def create_result(
        self,
        test_name: str,
        category: TestCategory,
        status: TestStatus,
        details: str,
        error_message: Optional[str] = None,
        stack_trace: Optional[str] = None
    ) -> TestResult:
        """Create a standardized test result"""
        return TestResult(
            id=str(uuid.uuid4()),
            testName=test_name,
            status=status,
            category=category,
            details=details,
            timestamp=datetime.utcnow(),
            duration=self._get_duration(),
            errorMessage=error_message,
            stackTrace=stack_trace
        )

    @abstractmethod
    async def execute(self) -> List[TestResult]:
        """Execute all test methods in this class"""
        pass

    async def _handle_test_execution(
        self,
        test_name: str,
        category: TestCategory,
        test_func: callable,
        *args,
        **kwargs
    ) -> TestResult:
        """Generic test execution handler with error handling"""
        self._start_timer()
        try:
            result = await test_func(*args, **kwargs)
            return self.create_result(
                test_name=test_name,
                category=category,
                status=TestStatus.PASS,
                details=result
            )
        except Exception as e:
            logger.error(f"Error in {test_name}: {str(e)}")
            return self.create_result(
                test_name=test_name,
                category=category,
                status=TestStatus.FAIL,
                details="Test execution failed",
                error_message=str(e),
                stack_trace=traceback.format_exc()
            ) 