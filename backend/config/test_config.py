from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field
import yaml
from pathlib import Path

class ColumnConfig(BaseModel):
    """Configuration for a required column in a table"""
    name: str
    data_type: str
    nullable: bool = True
    description: Optional[str] = None

class TableConfig(BaseModel):
    """Configuration for a required table in the semantic model"""
    name: str
    required_columns: List[ColumnConfig]
    description: Optional[str] = None
    row_count_threshold: Optional[int] = None

class RelationshipConfig(BaseModel):
    """Configuration for a required relationship"""
    name: str
    from_table: str
    from_column: str
    to_table: str
    to_column: str
    type: str = "Single"  # Single or Many
    cross_filter: str = "Both"  # Both, Single, None

class VisualConfig(BaseModel):
    """Configuration for a report visual"""
    name: str
    type: str
    load_threshold_ms: int = 2000
    required_fields: List[str] = []

class PerformanceConfig(BaseModel):
    """Performance thresholds configuration"""
    visual_load_threshold_ms: int = 2000
    page_load_threshold_ms: int = 5000
    query_timeout_ms: int = 30000
    refresh_timeout_ms: int = 300000

class TestConfig(BaseModel):
    """Main test configuration"""
    workspace_id: str
    dataset_id: str
    semantic_tests: Dict[str, Any] = Field(default_factory=dict)
    report_tests: Dict[str, Any] = Field(default_factory=dict)
    data_quality_tests: Dict[str, Any] = Field(default_factory=dict)
    performance_config: PerformanceConfig = Field(default_factory=PerformanceConfig)

    @classmethod
    def from_yaml(cls, path: Path) -> 'TestConfig':
        """Load configuration from YAML file"""
        with open(path, 'r') as f:
            config_dict = yaml.safe_load(f)
        return cls(**config_dict)

    def to_yaml(self, path: Path) -> None:
        """Save configuration to YAML file"""
        with open(path, 'w') as f:
            yaml.dump(self.dict(), f) 