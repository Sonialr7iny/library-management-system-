import sys
import time


def show_spinner(message: str, duration: float = 2.0) -> None:
    """Display a simple terminal spinner while an operation is running."""
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    end_time = time.time() + duration
    index = 0

    while time.time() < end_time:
        frame = frames[index % len(frames)]
        sys.stdout.write(f"\r{message}... {frame}")
        sys.stdout.flush()

        time.sleep(0.1)
        index += 1

    sys.stdout.write("\r" + " " * (len(message) + 8) + "\r")
    sys.stdout.flush()


def show_success(message: str) -> None:
    """Display a success message."""
    print(f"✓ {message}")


def show_error(message: str) -> None:
    """Display an error message."""
    print(f"✗ {message}")
    

# def format_books(books) -> str:
#     if not books:
#         return "No books found."

#     lines = []

#     for index, book in enumerate(books, start=1):
#         lines.append(
#             f"{index}. {book.title}\n"
#             f"   Author: {book.author_name}\n"
#             f"   Category: {book.category}\n"
#             f"   State: {book.state.value}\n"
#             f"   ID: {book.id}"
#         )

#     return "\n\n".join(lines)

def format_books(books) -> str:
    if not books:
        return "No books found."

    lines = []

    for index, book in enumerate(books, start=1):
        lines.append(
            f"{index}. {book.title}\n"
            f"   Author: {book.author_name}\n"
            f"   Category: {book.category}\n"
            f"   State: {book.state.value}\n"
            f"   ID: {book.id}"
        )

    return "\n\n".join(lines)