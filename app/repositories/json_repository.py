from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from app.core.exceptions import StorageError


class JsonRepository:
    """File-backed JSON repository."""

    def __init__(self, file_path: Path, collection: str):
        self.file_path = file_path
        self.collection = collection
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self._ensure_file()

    def _ensure_file(self) -> None:
        if not self.file_path.exists():
            self._write_all(
                {"books": [],"members": [],
                 "loans": []}
            )
            
    def _read_all(self) -> dict[str, Any]:
        try:
            with self.file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, dict):
                raise TypeError("JSON root must be an object.")
            return data
        except (OSError, json.JSONDecodeError,TypeError) as e:
            raise StorageError(f"Could not read storage: {e}") from e
        
    def _write_all(self, data: dict[str, Any]) -> None:
        temp_file_path = self.file_path.with_suffix(".tmp")
        try:
            with temp_file_path.open("w",encoding="utf-8") as f:
                json.dump(data,f,indent=4)
            temp_file_path.replace(self.file_path)
        except OSError as e:
            raise StorageError(f"Could not write storage: {e}") from e    
    
    def get_all(self) -> list[dict[str, Any]]:
        return list(self._read_all().get(self.collection, []))
 
    def replace_all(self, items:list[dict[str, Any]]) -> None:
        data=self._read_all()
        data[self.collection] = items
        self._write_all(data)