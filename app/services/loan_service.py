from __future__ import annotations

from datetime import datetime, timezone

from app.core.exceptions import (
    BookNotFoundError,
    LoanNotFoundError,
    MemberNotFoundError,
    ValidationError,
)
from app.models.entities import Loan, State
from app.repositories.book_repository import BookRepository
from app.repositories.loan_repository import LoanRepository
from app.repositories.member_repository import MemberRepository


class LoanService:
    """Service for handling business operations related to loans."""

    def __init__(
        self,
        loan_repository: LoanRepository,
        book_repository: BookRepository,
        member_repository: MemberRepository,
    ) -> None:
        self._loan_repository = loan_repository
        self._book_repository = book_repository
        self._member_repository = member_repository

    def borrow_book(self, book_id: str, member_id: str) -> Loan:
        """Borrow a book for a member."""
        book = self._book_repository.get_by_id(book_id)
        if not book:
            raise BookNotFoundError(
                f"Book with ID '{book_id}' was not found."
            )

        if book.state != State.AVAILABLE:
            raise ValidationError("Book is not available for borrowing.")

        member = self._member_repository.get_by_id(member_id)
        if not member:
            raise MemberNotFoundError(
                f"Member with ID '{member_id}' was not found."
            )

        loan = Loan(
            book_id=book.id,
            member_id=member.id,
            borrow_date=datetime.now().isoformat(),
        )

        self._loan_repository.add(loan)

        book.state = State.BORROWED
        self._book_repository.save(book)

        return loan

    def return_book(self, loan_id: str) -> Loan:
        """Return a borrowed book."""
        loan = self._loan_repository.get_by_id(loan_id)
        if not loan:
            raise LoanNotFoundError(
                f"Loan with ID '{loan_id}' was not found."
            )

        if loan.return_date is not None:
            raise ValidationError("Book has already been returned.")

        loan.return_date = datetime.now().isoformat()
        self._loan_repository.update(loan)

        book = self._book_repository.get_by_id(loan.book_id)
        if book:
            book.state = State.AVAILABLE
            self._book_repository.save(book)

        return loan

    def get_active_loans(self) -> list[Loan]:
        """Return all active loans."""
        return self._loan_repository.get_active_loans()