from app.core.exceptions import MemberNotFoundError
from app.models.entities import Member
from app.repositories.member_repository import MemberRepository


class MemberService:
    """Service for handling business operations related to members."""

    def __init__(self, repository: MemberRepository):
        self._repository = repository

    def get_all_members(self) -> list[Member]:
        """Return all members."""
        return self._repository.get_all()

    def search_members(self, name: str) -> list[Member]:
        """Search members by name."""
        return self._repository.search_by_name(name)

    def add_member(self, member: Member) -> None:
        """Add a new member."""
        self._repository.add(member)

    def update_member(self, member: Member) -> None:
        """Update an existing member."""
        try:
            self._repository.update(member)
        except ValueError as error:
            raise MemberNotFoundError(
                f"Member with ID '{member.id}' was not found."
            ) from error

    def delete_member(self, member_id: str) -> None:
        """Delete an existing member."""
        try:
            self._repository.delete(member_id)
        except ValueError as error:
            raise MemberNotFoundError(
                f"Member with ID '{member_id}' was not found."
            ) from error