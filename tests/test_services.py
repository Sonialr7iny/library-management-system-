import pytest

from app.core.exceptions import (
    BookNotFoundError,
    LoanNotFoundError,
    MemberNotFoundError,
    ValidationError,
)
from app.models.entities import State


def test_book_service_normalizes_add_search_update_and_delete(services):
    book_service, _, _ = services
    book = book_service.add_book("  dune ", " Frank Herbert ", " fiction ")

    assert book.title == "DUNE"
    assert book.author_name == "Frank Herbert"
    assert book_service.search_by_title(" dune ") == [book]

    updated = book_service.update_book(book.id, " dune 2 ", "Frank Herbert", "fiction")
    assert updated.title == "DUNE 2"
    assert book_service.delete_book(book.id) == updated


def test_book_service_rejects_empty_fields_and_search(services):
    book_service, _, _ = services

    with pytest.raises(ValidationError):
        book_service.add_book(" ", "Author", "Category")
    with pytest.raises(ValidationError):
        book_service.search_by_title(" ")


def test_member_service_delegates_business_operations(services):
    _, member_service, _ = services
    from app.models.entities import Member

    member = Member("Alex", "555-0100")
    member_service.add_member(member)
    assert member_service.search_members("alex") == [member]
    member.name = "Jordan"
    member_service.update_member(member)
    assert member_service.get_all_members() == [member]
    member_service.delete_member(member.id)
    assert member_service.get_all_members() == []


def test_loan_service_borrow_changes_book_state(services):
    book_service, member_service, loan_service = services
    book = book_service.add_book("Dune", "Frank Herbert", "Fiction")
    from app.models.entities import Member

    member = Member("Alex", "555-0100")
    member_service.add_member(member)
    loan = loan_service.borrow_book(book.id, member.id)

    assert loan.book_id == book.id
    assert loan.member_id == member.id
    assert book_service.list_books()[0].state is State.BORROWED
    assert loan_service.get_active_loans() == [loan]


def test_loan_service_rejects_unavailable_book_and_invalid_ids(services):
    book_service, member_service, loan_service = services
    from app.models.entities import Member

    book = book_service.add_book("Dune", "Frank Herbert", "Fiction")
    member = Member("Alex", "555-0100")
    member_service.add_member(member)
    loan_service.borrow_book(book.id, member.id)

    with pytest.raises(ValidationError):
        loan_service.borrow_book(book.id, member.id)
    with pytest.raises(BookNotFoundError):
        loan_service.borrow_book("missing", member.id)
    available_book = book_service.add_book("Foundation", "Isaac Asimov", "Fiction")
    with pytest.raises(MemberNotFoundError):
        loan_service.borrow_book(available_book.id, "missing")


def test_loan_service_return_changes_book_state_and_rejects_repeat(services):
    book_service, member_service, loan_service = services
    from app.models.entities import Member

    book = book_service.add_book("Dune", "Frank Herbert", "Fiction")
    member = Member("Alex", "555-0100")
    member_service.add_member(member)
    loan = loan_service.borrow_book(book.id, member.id)

    returned = loan_service.return_book(loan.id)

    assert returned.return_date is not None
    assert book_service.list_books()[0].state is State.AVAILABLE
    with pytest.raises(ValidationError):
        loan_service.return_book(loan.id)
    with pytest.raises(LoanNotFoundError):
        loan_service.return_book("missing")
