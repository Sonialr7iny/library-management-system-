from dataclasses import dataclass
from pathlib import Path

@dataclass(slots=True,frozen=True)
class Settings:
    app_name: str="Library Management System"
    app_version: str="1.0.0"
    data_file: Path=Path("data/data.json")
    
    
settings = Settings()