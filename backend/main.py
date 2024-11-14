from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from services.test_execution.executor import TestExecutor
from services.powerbi.client import PowerBIClient
from config.test_config import TestConfig
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.PROJECT_NAME)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/tests/run")
async def run_tests():
    """Execute all configured tests"""
    try:
        config = TestConfig.from_yaml("config/test_config.yaml")
        executor = TestExecutor(config)
        results = await executor.run_all_tests()
        return {"results": [r.dict() for r in results]}
    except Exception as e:
        logger.error(f"Error running tests: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) 