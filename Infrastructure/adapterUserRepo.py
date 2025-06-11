from domain.repositorio.user_repo import UserRepository
from Infrastructure.DB import db
class AdapterUserRepo(UserRepository):
    def __init__(self):
        self.database:db=db()

    def getUserByDocument(self, usuario_id):
        return self.database.get_user_by_document(usuario_id)
    
    def getUserByEmail(self, usuario_email):
        return self.database.get_user_by_email(usuario_email)
    
    def registerUser(self, usuario):
        return self.database.add_user(usuario)
    
    def updateUser(self, usuario):
        return super().updateUser(usuario)
    
    def deleteUserById(self, usuario_id):
        return super().deleteUserById(usuario_id)
    