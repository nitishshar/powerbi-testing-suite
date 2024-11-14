from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Column(BaseModel):
    """Power BI column definition"""
    name: str
    dataType: str
    isHidden: Optional[bool] = False

class Table(BaseModel):
    """Power BI table definition"""
    name: str
    columns: List[Column]

class Relationship(BaseModel):
    """Power BI relationship definition"""
    name: str
    fromTable: str
    fromColumn: str
    toTable: str
    toColumn: str
    crossFilteringBehavior: str = "bothDirections"

class Measure(BaseModel):
    """Power BI measure definition"""
    name: str
    expression: str
    formatString: Optional[str] = None 