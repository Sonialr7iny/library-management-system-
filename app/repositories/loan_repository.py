from app.models.entities import Loan
from app.repositories.json_repository import JsonRepository


class LoanRepository:
    def __init__(self,repository:JsonRepository):
        self.repository=repository

    def get_all(self) -> list[Loan]:
        data=self.repository.get_all()
        return [Loan.from_dict(item) for item in data]

    def get_by_id(self, loan_id: str) -> Loan | None:
        for loan in self.get_all():
            if loan.id == loan_id:
                return loan
        return None

    def get_active_loans(self) -> list[Loan]:
        return [loan for loan in self.get_all() if loan.return_date is None]

    def add(self, loan: Loan) -> Loan:
        loans=self.repository.get_all()
        loans.append(loan.to_dict())
        self.repository.replace_all(loans)   
        return loan

    def update(self, loan: Loan)-> None:
        loans=self.repository.get_all()

        for index, existing_loan in enumerate(loans):
            if existing_loan["id"] == loan.id:
                loans[index] = loan.to_dict()
                self.repository.replace_all(loans)
                return            
        

