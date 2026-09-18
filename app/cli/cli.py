from app.cli.formatting import (
    format_books,
    show_error,
    # show_spinner,
    show_success,
)
from app.core.config import settings
from app.core.exceptions import LibraryException
from app.models.entities import Member
from app.repositories.book_repository import BookRepository
from app.repositories.json_repository import JsonRepository
from app.repositories.loan_repository import LoanRepository
from app.repositories.member_repository import MemberRepository
from app.services.book_service import BookService
from app.services.loan_service import LoanService
from app.services.member_service import MemberService


def cli_run():
    print("=================================================")
    print("""Welcome to the Library Management System CLI!""")
    print("=================================================")
    
    book_service, member_service, loan_service=create_services()
    main_menu(
        book_service=book_service,
        member_service=member_service, 
        loan_service=loan_service
    )
    
    
def main_menu( book_service, member_service, loan_service):
    while True:
        print("Main Menu:")
        print("1. Manage Books")
        print("2. Manage Members")
        print("3. Manage Loans")
        print("4. Exit")
        print("=================================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            manage_books(book_service)
        elif choice == "2":
            manage_members(member_service)
        elif choice == "3":
            manage_loans(loan_service)
        elif choice == "4":
            print("Exiting the Library Management System CLI.")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
def manage_books(book_service):
    while True:
        print("=================================================")
        print("\nManage Books:")
        print("1. View All Books")
        print("2. Search Book")
        print("3. Add Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("0. Back to Main Menu")
        print("=================================================")

        choice = input("Enter your choice (0-5): ")

        if choice == "1":
            # print("View All Books selected.")
            # show_spinner("Fetching all books")
            # show_success("All books fetched successfully.")
            view_all_books(book_service)
        elif choice == "2":
            search_book(book_service)
        elif choice == "3":
            add_book(book_service)
        elif choice == "4":
            update_book(book_service)
        elif choice == "5":
            delete_book(book_service)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
            
def manage_members(member_service):
    while True:
        print("\nManage Members:")
        print("1. View All Members")
        print("2. Search Member")
        print("3. Add Member")
        print("4. Update Member")
        print("5. Delete Member")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-5): ")

        if choice == "1":
            view_all_members(member_service)
        elif choice == "2":
            search_member(member_service)
        elif choice == "3":
            add_member(member_service)
        elif choice == "4":
            update_member(member_service)
        elif choice == "5":
            delete_member(member_service)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
            
def manage_loans(loan_service):
    while True:
        print("\nManage Loans:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. View Active Loans")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (0-3): ")

        if choice == "1":
            borrow_book(loan_service)
        elif choice == "2":
            return_book(loan_service)
        elif choice == "3":
            view_active_loans(loan_service)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
            
#---------------- Books Operations ------------------   
def view_all_books(book_service):
    try:
        books = book_service.list_books()
        print(format_books(books))
        show_success("Books fetched successfully.")
    except LibraryException as error:
        show_error(str(error))


def search_book(book_service):
    try:
        print("\nSearch Book:")
        print("1. By Title")
        print("2. By Author")
        print("3. By Category")

        choice = input("Choose search type (1-3): ")
        value = input("Enter search value: ")

        if choice == "1":
            books = book_service.search_by_title(value)
        elif choice == "2":
            books = book_service.search_by_author(value)
        elif choice == "3":
            books = book_service.search_by_category(value)
        else:
            print("Invalid choice.")
            return

        print(format_books(books))
    except LibraryException as error:
        show_error(str(error))


def add_book(book_service):
    try:
        title = input("Enter book title: ")
        author_name = input("Enter author name: ")
        category = input("Enter category: ")

        book = book_service.add_book(
            title,
            author_name,
            category,
        )

        show_success(f"Book added successfully. ID: {book.id}")
    except LibraryException as error:
        show_error(str(error))


def update_book(book_service):
    try:
        book_id = input("Enter book ID: ")
        title = input("Enter new title: ")
        author_name = input("Enter new author name: ")
        category = input("Enter new category: ")

        book = book_service.update_book(
            book_id,
            title,
            author_name,
            category,
        )

        show_success(f"Book updated successfully. ID: {book.id}")
    except LibraryException as error:
        show_error(str(error))


def delete_book(book_service):
    try:
        book_id = input("Enter book ID: ")

        book = book_service.delete_book(book_id)

        show_success(f"Book '{book.title}' deleted successfully.")
    except LibraryException as error:
        show_error(str(error))     


#------------------- Members OPerations -------------------# 
def view_all_members(member_service):
    try:
        members = member_service.get_all_members()

        if not members:
            print("No members found.")
            return

        for index, member in enumerate(members, start=1):
            print(
                f"\n{index}. {member.name}\n"
                f"   Phone: {member.phone_number}\n"
                f"   ID: {member.id}"
            )
    except LibraryException as error:
        show_error(str(error))


def search_member(member_service):
    try:
        name = input("Enter member name: ")
        members = member_service.search_members(name)

        if not members:
            print("No members found.")
            return

        for index, member in enumerate(members, start=1):
            print(
                f"\n{index}. {member.name}\n"
                f"   Phone: {member.phone_number}\n"
                f"   ID: {member.id}"
            )
    except LibraryException as error:
        show_error(str(error))


def add_member(member_service):
    try:
        name = input("Enter member name: ")
        phone_number = input("Enter phone number: ")

        member = Member(
            name=name,
            phone_number=phone_number,
        )

        member_service.add_member(member)

        show_success(f"Member added successfully. ID: {member.id}")
    except LibraryException as error:
        show_error(str(error))


def update_member(member_service):
    try:
        member_id = input("Enter member ID: ")
        name = input("Enter new name: ")
        phone_number = input("Enter new phone number: ")

        member = Member(
            id=member_id,
            name=name,
            phone_number=phone_number,
        )

        member_service.update_member(member)

        show_success("Member updated successfully.")
    except LibraryException as error:
        show_error(str(error))


def delete_member(member_service):
    try:
        member_id = input("Enter member ID: ")

        member_service.delete_member(member_id)

        show_success("Member deleted successfully.")
    except LibraryException as error:
        show_error(str(error))
#------------------- Loans OPerations -------------------#

def borrow_book(loan_service):
    try:
        book_id = input("Enter book ID: ")
        member_id = input("Enter member ID: ")

        loan = loan_service.borrow_book(
            book_id=book_id,
            member_id=member_id,
        )

        show_success(
            f"Book borrowed successfully. Loan ID: {loan.id}"
        )
    except LibraryException as error:
        show_error(str(error))


def return_book(loan_service):
    try:
        loan_id = input("Enter loan ID: ")

        loan = loan_service.return_book(loan_id)

        show_success(
            f"Book returned successfully. Loan ID: {loan.id}"
        )
    except LibraryException as error:
        show_error(str(error))


def view_active_loans(loan_service):
    try:
        loans = loan_service.get_active_loans()

        if not loans:
            print("No active loans.")
            return

        for index, loan in enumerate(loans, start=1):
            print(
                f"\n{index}. Loan ID: {loan.id}\n"
                f"   Book ID: {loan.book_id}\n"
                f"   Member ID: {loan.member_id}\n"
                f"   Borrow Date: {loan.borrow_date}"
            )
    except LibraryException as error:
        show_error(str(error))

def create_services():
    book_repository=BookRepository()
    member_repository=MemberRepository(settings.data_file)
    loan_repository=LoanRepository(JsonRepository(settings.data_file, "loans"))
    book_service=BookService(book_repository)
    member_service=MemberService(member_repository)
    loan_service=LoanService(loan_repository=loan_repository, book_repository=book_repository, member_repository=member_repository)
    
    return book_service, member_service, loan_service