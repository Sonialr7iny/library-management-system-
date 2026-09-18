import pytest

from app.core.exceptions import ValidationError
from app.models.entities import Book, Loan, Member, State


def test_book_creation_defaults_to_available_and_round_trips():
    book = Book("Dune", "Frank Herbert", "Fiction")

    assert book.state is State.AVAILABLE
    assert Book.from_dict(book.to_dict()) == book


@pytest.mark.parametrize(
    "field",
    ["title", "author_name", "category"],
)
def test_book_rejects_empty_required_fields(field):
    values = {"title": "Dune", "author_name": "Frank Herbert", "category": "Fiction"}
    values[field] = ""

    with pytest.raises(ValidationError):
        Book(**values)


def test_book_preserves_borrowed_state():
    book = Book("Dune", "Frank Herbert", "Fiction", State.BORROWED)

    assert book.state is State.BORROWED
    assert Book.from_dict(book.to_dict()).state is State.BORROWED


@pytest.mark.parametrize(
    "factory",
    [
        lambda: Member("", "555-0100"),
        lambda: Member("Alex", ""),
        lambda: Loan("", "member-id", "2026-01-01"),
        lambda: Loan("book-id", "", "2026-01-01"),
        lambda: Loan("book-id", "member-id", ""),
    ],
)
def test_member_and_loan_validation(factory):
    with pytest.raises(ValidationError):
        factory()


def test_member_and_loan_round_trip():
    member = Member("Alex", "555-0100")
    loan = Loan("book-id", member.id, "2026-01-01T00:00:00+00:00")

    assert Member.from_dict(member.to_dict()) == member
    assert Loan.from_dict(loan.to_dict()) == loan
