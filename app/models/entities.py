from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import StrEnum
from uuid import uuid4

from app.core.exceptions import ValidationError




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
    def from_dict(cls, data: dict) -> Book:
        return cls(**data)


@dataclass(slots=True)
class Member:
    id: str 
    name: str
    phone_number: str

    def __post_init__(self):
        if not self.id:
            raise ValidationError("Member ID cannot be empty.")
        if not self.name:
            raise ValidationError("Name cannot be empty.")
        if not self.phone_number:
            raise ValidationError("Phone number cannot be empty.")

    def to_dict(self) -> dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict) -> Member:
        return cls(**data)   

@dataclass(slots=True)
class Loan:
    book_id: str
    member_id: str
    borrow_date: str
    return_date: str | None=None
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
            if not self.book_id:
                raise ValidationError("Book id cannot be empty.")
            if not self.member_id:
                raise ValidationError("Member id cannot be empty.")
            if not self.borrow_date:
                raise ValidationError("Borrow date cannot be empty.")

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> Loan:
        return cls(**data)    

