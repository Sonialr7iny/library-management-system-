class LibraryException(Exception):
    """Base class for all library exceptions."""

class ValidationError(LibraryException):
    pass

class BookNotFoundError(LibraryException):
    pass

class MemberNotFoundError(LibraryException):
    pass

class BookUnavailableError(LibraryException):
    pass
class storageError(LibraryException):
    pass