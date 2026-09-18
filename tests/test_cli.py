from app.cli import cli
from app.models.entities import Book


def test_main_menu_navigates_to_each_menu_and_exits(monkeypatch, capsys):
    choices = iter(["1", "0", "2", "0", "3", "0", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(choices))
    service = object()

    cli.main_menu(service, service, service)

    output = capsys.readouterr().out
    assert "Manage Books:" in output
    assert "Manage Members:" in output
    assert "Manage Loans:" in output
    assert "Exiting" in output


def test_menus_report_invalid_choices(monkeypatch, capsys):
    choices = iter(["x", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choices))

    cli.manage_books(object())

    assert "Invalid choice. Please try again." in capsys.readouterr().out


def test_book_menu_add_and_view(capsys, monkeypatch):
    class BookService:
        def add_book(self, title, author, category):
            return Book(title.upper(), author, category)

        def list_books(self):
            return [Book("DUNE", "Frank Herbert", "Fiction", id="book-1")]

    choices = iter(["3", "Dune", "Frank Herbert", "Fiction", "1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choices))

    cli.manage_books(BookService())

    output = capsys.readouterr().out
    assert "Book added successfully" in output
    assert "DUNE" in output


def test_member_and_loan_menu_error_handling(capsys, monkeypatch):
    class FailingMemberService:
        def add_member(self, member):
            from app.core.exceptions import ValidationError

            raise ValidationError("invalid member")

    choices = iter(["3", "Alex", "555-0100", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choices))
    cli.manage_members(FailingMemberService())
    assert "invalid member" in capsys.readouterr().out

    class LoanService:
        def borrow_book(self, book_id, member_id):
            from app.core.exceptions import BookNotFoundError

            raise BookNotFoundError("missing book")

    choices = iter(["1", "missing", "member", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(choices))
    cli.manage_loans(LoanService())
    assert "missing book" in capsys.readouterr().out
