from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from uuid import uuid4


class State(StrEnum):
    BORROWED = "borrowed"
    AVAILABLE = "available"


@dataclass(slots=True)
class Book:
    title: str
    author_name: str
    category: str
    state : State =State.AVAILABLE
    id: str = field(default_factory=lambda: str(uuid4()))

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Book":
        return cls(**data)


@dataclass(slots=True)
class Member:
    name: str
    phone_number: str
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
        if not self.name:
            raise ValueError("Name cannot be empty.")
        if not self.phone_number:
            raise ValueError("Phone number cannot be empty.")

    def to_dict(self) -> dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict) -> "Member":
        return cls(**data)   

