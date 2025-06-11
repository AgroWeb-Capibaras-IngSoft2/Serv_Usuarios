import pandas as pd
from domain.entidades.user_model import user
class db:
    def __init__(self):
        self.dataBase=pd.DataFrame(columns=["numberDocument",
                                       "typeDocument",
                                       "firstName",
                                       "middleName",
                                       "username",
                                       "bornDate",
                                       "deparment",
                                       "municipality",
                                       "trail",
                                       "email",
                                       "phoneNumber",
                                       "age",
                                       "hashPassword"]
                                       )
    
    def add_user(self, user: user):
        if self.exists_by_email(user.email):
            raise ValueError("Email ya registrado")
        if self.exists_by_document(user.numeroDocumento):
            raise ValueError("Documento ya registrado")
        
        self.dataBase = pd.concat([
            self.dataBase,
            pd.DataFrame([user.toDictionary()])
        ], ignore_index=True)
        print(user.toDictionary())

    def get_user_by_email(self, email: str):
        result = self.dataBase[self.dataBase["email"] == email]
        return result.iloc[0].to_dict() if not result.empty else None

    def get_user_by_document(self, numero_documento: str):
        result = self.dataBase[self.dataBase["numeroDocumento"] == numero_documento]
        return result.iloc[0].to_dict() if not result.empty else None

    def exists_by_email(self, email: str) -> bool:
        return not self.dataBase[self.dataBase["email"] == email].empty

    def exists_by_document(self, numero_documento: str) -> bool:
        return not self.dataBase[self.dataBase["numeroDocumento"] == numero_documento].empty
