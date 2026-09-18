from app.cli.formatting import show_spinner, show_success, show_error


def cli_run():
    print("Welcome to the Library Management System CLI!")
    main_menu()
    
    
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Manage Books")
        print("2. Manage Members")
        print("3. Manage Loans")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # print("Manage Books selected.")
            manage_books()
        elif choice == "2":
            print("Manage Members selected.")
            # manage_members()
        elif choice == "3":
            print("Manage Loans selected.")
            # manage_loans()
        elif choice == "4":
            print("Exiting the Library Management System CLI.")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
def manage_books():
    while True:
        print("\nManage Books:")
        print("1. View All Books")
        print("2. Search Book")
        print("3. Add Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("View All Books selected.")
            show_spinner("Fetching all books")
            show_success("All books fetched successfully.")
            # view_all_books()
        elif choice == "2":
            print("Search Book selected.")
            show_spinner("Searching for book")
            show_success("Book found successfully.")
            # search_book()
        elif choice == "3":
            print("Add Book selected.")
            # add_book()
        elif choice == "4":
            print("Update Book selected.")
            # update_book()
        elif choice == "5":
            print("Delete Book selected.")
            # delete_book() 
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
            
def manage_members():
    while True:
        print("\nManage Members:")
        print("1. View All Members")
        print("2. Search Member")
        print("3. Add Member")
        print("4. Update Member")
        print("5. Delete Member")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print("View All Members selected.")
            # view_all_members()
        elif choice == "2":
            print("Search Member selected.")
            # search_member()
        elif choice == "3":
            print("Add Member selected.")
            # add_member()
        elif choice == "4":
            print("Update Member selected.")
            # update_member()
        elif choice == "5":
            print("Delete Member selected.")
            # delete_member()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
            
def manage_loans():
    while True:
        print("\nManage Loans:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. View All Loans")
        print("0. Back to Main Menu")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("Borrow a Book selected.")
            # borrow_book()
        elif choice == "2":
            print("Return a Book selected.")
            # return_book()
        elif choice == "3":
            print("View All Loans selected.")
            # view_all_loans()
        elif choice == "4":
            print("View Active Loans selected.")
            # view_active_loans()   
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")