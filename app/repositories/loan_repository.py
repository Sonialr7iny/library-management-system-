from app.models.entities import Loan
from app.repositories.json_repository import JsonRepository


class LoanRepository:
    def __init__(self,repository:JsonRepository):
        self.repository=repository

    def get_all(self):
        return self.repository.get_all()

    def find_by_id(self,loan_id:str):
        loans=self.repository.get_all()

        for loan in loans:
            if loan["id"]==loan_id:
                return loan
        return None

    def git_active_loans(self):
        loans=self.repository.get_all()
        active_loans=[]

        for loan in loans:
            if loan["return_date"]is None:
                active_loans.append(loan)
        return active_loans

    def add_loan(self,loan:Loan) -> None:
        loans=self.repository.get_all()
        loans.append(loan.to_dict)
        self.repository.replace_all(loans)   

    def update_loan(self,loan_id:str,update_loan:Loan)-> None:
        loans=self.repository.get_all()

        for i,loan in enumerate(loans):
            if loan["loan_id"]==update_loan:
                loans[i]=update_loan.to_dict()
            self.repository.replace_all(loans)
            return            
        

