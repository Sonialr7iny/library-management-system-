from pathlib import Path

import pytest

from app.core.exceptions import BookNotFoundError, MemberNotFoundError
from app.models.entities import Book, Loan, Member, State
from app.repositories.book_repository import BookRepository
from app.repositories.json_repository import JsonRepository
from app.repositories.loan_repository import LoanRepository
from app.repositories.member_repository import MemberRepository


def test_json_repository_creates_and_persists_collection(tmp_path: Path):
    path = tmp_path / "nested" / "data.json"
    repository = JsonRepository(path, "books")
    repository.replace_all([{"id": "book-1", "title": "DUNE"}])

    reopened = JsonRepository(path, "books")

    assert reopened.get_all() == [{"id": "book-1", "title": "DUNE"}]


def test_book_repository_crud_and_filters(storage_path: Path):
    repository = BookRepository()
    first = Book("Dune", "Frank Herbert", "Fiction")
    second = Book("Foundation", "Isaac Asimov", "Fiction", State.BORROWED)
    repository.save(first)
    repository.save(second)

    assert repository.get_all() == [first, second]
    assert repository.get_by_id(first.id) == first
    assert repository.get_by_author("Frank Herbert") == [first]
    assert repository.get_by_title("Foundation") == [second]
    assert repository.get_by_category("Fiction") == [first, second]
    assert repository.get_by_state(State.BORROWED) == [second]

    updated = Book("Dune Messiah", first.author_name, first.category, id=first.id)
    assert repository.save(updated) == updated
    assert repository.get_by_id(first.id) == updated
    assert repository.delete(first.id) == updated
    assert repository.get_all() == [second]


def test_book_repository_missing_id_raises(storage_path: Path):
    with pytest.raises(BookNotFoundError):
        BookRepository().get_by_id("missing")


def test_member_repository_crud_search_and_persistence(storage_path: Path):
    repository = MemberRepository(storage_path)
    member = Member("Alex Smith", "555-0100")
    repository.add(member)
    assert repository.get_all() == [member]
    assert repository.get_by_id(member.id) == member
    assert repository.search_by_name(" smith ") == [member]

    updated = Member("Alex Jones", "555-0111", id=member.id)
    repository.update(updated)
    assert MemberRepository(storage_path).get_by_id(member.id) == updated
    repository.delete(member.id)
    assert repository.get_all() == []


def test_member_repository_rejects_duplicate_and_missing_records(storage_path: Path):
    repository = MemberRepository(storage_path)
    member = Member("Alex", "555-0100")
    repository.add(member)

    with pytest.raises(ValueError):
        repository.add(member)
    with pytest.raises(MemberNotFoundError):
        repository.update(Member("Missing", "555-0101", id="missing"))
    with pytest.raises(MemberNotFoundError):
        repository.delete("missing")


def test_loan_repository_crud_and_active_filter(storage_path: Path):
    repository = LoanRepository(JsonRepository(storage_path, "loans"))
    active = Loan("book-1", "member-1", "2026-01-01")
    returned = Loan("book-2", "member-2", "2026-01-01", "2026-01-02")
    repository.add(active)
    repository.add(returned)

    assert repository.get_all() == [active, returned]
    assert repository.get_by_id(active.id) == active
    assert repository.get_by_id("missing") is None
    assert repository.get_active_loans() == [active]

    active.return_date = "2026-01-03"
    repository.update(active)
    assert repository.get_by_id(active.id) == active
    assert repository.get_active_loans() == []
