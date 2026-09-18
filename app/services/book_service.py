from __future__ import annotations

from app.core.exceptions import ValidationError
from app.models import Book, State
from app.repositories import BookRepository


class BookService:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def add_book(self, title: str, author_name: str, category: str, /,
        *, state: State = State.AVAILABLE) -> Book:
        title = title.strip().upper()
        author_name = author_name.strip()
        category = category.strip()
        self._validate_book_fields(title, author_name, category)
        return self.book_repository.save(Book(title, author_name, category, state))

    def list_books(self) -> list[Book]:
        return sorted(self.book_repository.list(), key=lambda book: book.id)

    def search_by_title(self, title: str) -> list[Book]:
        title = title.strip().upper()
        self._validate_search_value(title)
        return self.book_repository.get_by_title(title)

    def search_by_author(self, author_name: str) -> list[Book]:
        author_name = author_name.strip()
        self._validate_search_value(author_name)
        return self.book_repository.get_by_author(author_name)

    def search_by_category(self, category: str) -> list[Book]:
        category = category.strip()
        self._validate_search_value(category)
        return self.book_repository.get_by_category(category)

    def update_book(
        self,
        book_id: str,
        title: str,
        author_name: str,
        category: str,
        *,
        state: State | None = None,
    ) -> Book:
        current_book = self.book_repository.get(book_id)
        title = title.strip().upper()
        author_name = author_name.strip()
        category = category.strip()
        self._validate_book_fields(title, author_name, category)
        updated_book = Book(
            title,
            author_name,
            category,
            current_book.state if state is None else state,
            current_book.id,
        )
        return self.book_repository.save(updated_book)

    def delete_book(self, book_id: str) -> Book:
        return self.book_repository.delete(book_id)

    @staticmethod
    def _validate_book_fields(title: str, author_name: str, category: str) -> None:
        if not title or not author_name or not category:
            raise ValidationError(
                "Book title, author name, and category are required"
            )

    @staticmethod
    def _validate_search_value(value: str) -> None:
        if not value:
            raise ValidationError("Search value cannot be empty")
