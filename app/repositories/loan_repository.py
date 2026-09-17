from app.repositories.json_repository import JsonRepository

class LoanRepository:
    def __init__(self,repository:JsonRepository):
        self.repository=repository

    def get_all(self):
        return self.repository.get_all()

         
        

