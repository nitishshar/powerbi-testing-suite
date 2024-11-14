from pydantic_settings import BaseSettings
from pathlib import Path
from typing import List

class Settings(BaseSettings):
    """Application settings and configuration"""
    
    # API Configuration
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Power BI Test Results API"
    
    # Power BI Configuration
    POWERBI_WORKSPACE_ID: str
    POWERBI_CLIENT_ID: str
    POWERBI_CLIENT_SECRET: str
    POWERBI_TENANT_ID: str
    
    # Security
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS Configuration
    CORS_ORIGINS: List[str] = ["http://localhost:4200"]
    
    # Paths
    REPORTS_DIR: Path = Path("reports")
    RESULTS_DB_PATH: Path = Path("db/results.json")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 