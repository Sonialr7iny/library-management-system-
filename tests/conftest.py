from pathlib import Path

import pytest

from app.core.config import Settings
from app.repositories.book_repository import BookRepository
from app.repositories.json_repository import JsonRepository
from app.repositories.loan_repository import LoanRepository
from app.repositories.member_repository import MemberRepository
from app.services.book_service import BookService
from app.services.loan_service import LoanService
from app.services.member_service import MemberService


@pytest.fixture
def storage_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "data.json"
    monkeypatch.setattr(
        "app.repositories.book_repository.settings",
        Settings(data_file=path),
    )
    return path


@pytest.fixture
def repositories(storage_path: Path):
    books = BookRepository()
    members = MemberRepository(storage_path)
    loans = LoanRepository(JsonRepository(storage_path, "loans"))
    return books, members, loans


@pytest.fixture
def services(repositories):
    books, members, loans = repositories
    return (
        BookService(books),
        MemberService(members),
        LoanService(loans, books, members),
    )
