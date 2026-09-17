from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from uuid import uuid4


class State(StrEnum):
    TRUE = "true"
    FALSE = "false"


@dataclass(slots=True)
class Book:
    title: str
    author_name: str
    category: str
    state : State =State.FALSE
    id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(**data)


