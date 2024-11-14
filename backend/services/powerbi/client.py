from typing import Dict, Any, Optional
import aiohttp
from fastapi import HTTPException
from ...config.settings import settings
import logging

logger = logging.getLogger(__name__)

class PowerBIClient:
    """Client for interacting with Power BI REST API"""
    
    def __init__(self):
        self.workspace_id = settings.POWERBI_WORKSPACE_ID
        self.base_url = "https://api.powerbi.com/v1.0/myorg"
        self._access_token: Optional[str] = None

    async def get_model_schema(self) -> Dict[str, Any]:
        """Get the semantic model schema"""
        return await self._make_request(
            f"/groups/{self.workspace_id}/datasets",
            method="GET"
        )

    async def execute_dax_query(self, query: str) -> Dict[str, Any]:
        """Execute a DAX query"""
        return await self._make_request(
            f"/groups/{self.workspace_id}/datasets/execute-queries",
            method="POST",
            json={"queries": [{"query": query}]}
        )

    async def _make_request(
        self, 
        endpoint: str, 
        method: str = "GET", 
        **kwargs
    ) -> Dict[str, Any]:
        """Make an authenticated request to the Power BI API"""
        token = await self._get_access_token()
        headers = {"Authorization": f"Bearer {token}"}
        if "json" in kwargs:
            headers["Content-Type"] = "application/json"
            
        async with aiohttp.ClientSession() as session:
            async with session.request(
                method,
                f"{self.base_url}{endpoint}",
                headers=headers,
                **kwargs
            ) as response:
                if response.status != 200:
                    raise HTTPException(
                        status_code=response.status,
                        detail=f"Power BI API error: {await response.text()}"
                    )
                return await response.json() 