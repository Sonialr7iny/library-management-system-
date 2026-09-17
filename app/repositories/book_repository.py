from app.core.config import settings
from app.core.exceptions import NotFoundError
from app.models import Book
from app.repositories.json_repository import JsonRepository


class BookRepository:
    def __init__(self):
        self._repo = JsonRepository[Book](settings.data_file, "book")

    def list(self) -> list[Book]:
        return [Book.from_dict(item) for item in self._repo.get_all()]

    def get(self, book_id: str) -> Book:
        for book in self.list():
            if book.id == book_id:
                return book
        raise NotFoundError(f"book not found: {book_id}")

    def get_by_author(self, author: str) -> list[Book]:
        return [book for book in self.list() if book.author_name == author]

    def get_by_title(self, title: str) -> list[Book]:
            return [book for book in self.list() if book.title == title]
    
    def get_by_category(self, category: str) -> list[Book]:
            return [book for book in self.list() if book.category == category]
    
    def get_by_state(self, state: str) -> list[Book]:
            return [book for book in self.list() if book.state == state]

    def get_by_state(self, state: str) -> list[Book]:
         return [book for book in self.list() if book.state == state]    
    
    def save(self, book: Book) -> Book:
        items = [b for b in self.list() if b.id != book.id]
        items.append(book)
        self._repo.replace_all([b.to_dict() for b in items])
        return book
    
    def delete(self, book_id: str) -> Book:
        book = self.get(book_id)
        items = [item for item in self.list() if item.id != book_id]
        self._repo.replace_all([item.to_dict() for item in items])
        return book
