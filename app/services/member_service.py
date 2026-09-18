from app.models.entities import Member
from app.repositories.member_repository import MemberRepository


class MemberService:
    """Service for handling business operations related to members."""

    def __init__(self, member_repository: MemberRepository):
        self._member_repository = member_repository

    def get_all_members(self) -> list[Member]:
        """Return all members."""
        return self._member_repository.get_all()

    def search_members(self, name: str) -> list[Member]:
        """Search members by name."""
        return self._member_repository.search_by_name(name)

    def add_member(self, member: Member) -> None:
        """Add a new member."""
        self._member_repository.add(member)

    def update_member(self, member: Member) -> None:
        """Update an existing member."""
        self._member_repository.update(member)

    def delete_member(self, member_id: str) -> None:
        """Delete an existing member."""
        self._member_repository.delete(member_id)