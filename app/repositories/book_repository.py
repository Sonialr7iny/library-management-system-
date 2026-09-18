from app.core.config import settings
from app.core.exceptions import BookNotFoundError
from app.models import Book
from app.repositories.json_repository import JsonRepository


class BookRepository:
    def __init__(self):
        self._repo = JsonRepository(settings.data_file, "books")

    def get_all(self) -> list[Book]:
        return [Book.from_dict(item) for item in self._repo.get_all()]

    def get_by_id(self, book_id: str) -> Book:
        for book in self.get_all():
            if book.id == book_id:
                return book
        raise BookNotFoundError(f"book not found: {book_id}")

    def get_by_author(self, author: str) -> list[Book]:
        return [book for book in self.get_all() if book.author_name == author]

    def get_by_title(self, title: str) -> list[Book]:
            return [book for book in self.get_all() if book.title == title]
    
    def get_by_category(self, category: str) -> list[Book]:
            return [book for book in self.get_all() if book.category == category]
    
    def get_by_state(self, state: str) -> list[Book]:
            return [book for book in self.get_all() if book.state == state]  
    
    def save(self, book: Book) -> Book:
        items = [b for b in self.get_all() if b.id != book.id]
        items.append(book)
        self._repo.replace_all([b.to_dict() for b in items])
        return book
    
    def delete(self, book_id: str) -> Book:
        book = self.get_by_id(book_id)
        items = [item for item in self.get_all() if item.id != book_id]
        self._repo.replace_all([item.to_dict() for item in items])
        return book
    
    
