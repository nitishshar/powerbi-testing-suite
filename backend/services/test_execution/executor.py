from typing import List, Type, Optional
from config.test_config import TestConfig
from services.results.models import TestResult
from services.powerbi.client import PowerBIClient
from .base_test_methods import BaseTestMethods
from .semantic_test_methods import SemanticTestMethods
from .report_test_methods import ReportTestMethods
from .data_quality_test_methods import DataQualityTestMethods
import logging

logger = logging.getLogger(__name__)

class TestExecutor:
    """
    Main test executor that manages test execution and results collection
    
    This class is responsible for:
    1. Loading test configuration
    2. Initializing test method classes
    3. Executing tests based on configuration
    4. Collecting and aggregating results
    """

    def __init__(
        self,
        config: TestConfig,
        pbi_client: Optional[PowerBIClient] = None,
        custom_test_methods: Optional[List[Type[BaseTestMethods]]] = None
    ):
        self.config = config
        self.pbi_client = pbi_client or PowerBIClient()
        
        # Initialize standard test methods
        self.test_methods = [
            SemanticTestMethods(config, self.pbi_client),
            ReportTestMethods(config, self.pbi_client),
            DataQualityTestMethods(config, self.pbi_client)
        ]
        
        # Add custom test methods if provided
        if custom_test_methods:
            for method_class in custom_test_methods:
                self.test_methods.append(method_class(config, self.pbi_client))

    async def run_all_tests(self) -> List[TestResult]:
        """Execute all configured tests"""
        logger.info("Starting test execution")
        all_results = []
        
        try:
            for test_method in self.test_methods:
                logger.info(f"Executing {test_method.__class__.__name__}")
                results = await test_method.execute()
                all_results.extend(results)
        except Exception as e:
            logger.error(f"Error during test execution: {str(e)}")
            raise
        
        logger.info(f"Test execution completed. Total tests: {len(all_results)}")
        return all_results

    async def run_specific_tests(self, categories: List[str]) -> List[TestResult]:
        """Execute tests for specific categories"""
        logger.info(f"Starting test execution for categories: {categories}")
        all_results = []
        
        try:
            for test_method in self.test_methods:
                if test_method.__class__.__name__.lower().replace('testmethods', '') in categories:
                    logger.info(f"Executing {test_method.__class__.__name__}")
                    results = await test_method.execute()
                    all_results.extend(results)
        except Exception as e:
            logger.error(f"Error during test execution: {str(e)}")
            raise
        
        logger.info(f"Test execution completed. Total tests: {len(all_results)}")
        return all_results