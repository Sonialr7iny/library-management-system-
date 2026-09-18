from pathlib import Path

from app.core.exceptions import MemberNotFoundError
from app.models.entities import Member
from app.repositories.json_repository import JsonRepository


class MemberRepository:

    def __init__(self, file_path: Path):
        self._repository = JsonRepository(
            file_path=file_path,
            collection="members",
        )

    def get_all(self) -> list[Member]:
        data = self._repository.get_all()
        return [Member.from_dict(item) for item in data]

    def get_by_id(self, member_id: str) -> Member | None:
        members = self.get_all()

        for member in members:
            if member.id == member_id:
                return member

        return None

    def search_by_name(self, name: str) -> list[Member]:
        search_term = name.strip().lower()

        return [
            member
            for member in self.get_all()
            if search_term in member.name.lower()
        ]

    def add(self, member: Member) -> None:
        if self.get_by_id(member.id) is not None:
            raise ValueError(f"Member with ID '{member.id}' already exists.")
        members = self.get_all()
        members.append(member)

        self._repository.replace_all(
            [item.to_dict() for item in members]
        )

    def update(self, member: Member) -> None:
        members = self.get_all()

        for index, existing_member in enumerate(members):
            if existing_member.id == member.id:
                members[index] = member

                self._repository.replace_all(
                    [item.to_dict() for item in members]
                )
                return

        raise MemberNotFoundError(f"Member with ID '{member.id}' not found.")

    def delete(self, member_id: str) -> None:
        members = self.get_all()

        updated_members = [
            member for member in members
            if member.id != member_id
        ]

        if len(updated_members) == len(members):
            raise MemberNotFoundError(f"Member with ID '{member_id}' not found.")

        self._repository.replace_all(
            [item.to_dict() for item in updated_members]
        )