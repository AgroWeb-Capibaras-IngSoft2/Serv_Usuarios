#Se necesita definir una interfaz que especifique como se interactúa con usuarios, 
#sin importar la base de datos que se use.
from abc import ABC, abstractmethod
from typing import Optional
from domain.entidades.user_model import user

class UserRepository(ABC):
    @abstractmethod
    def getAllUsers(self) -> Optional[list]:
        pass

    @abstractmethod
    def getUserByDocument(self, usuario_id: str) -> Optional[user]:
        pass

    @abstractmethod
    def getUserByEmail(self,usuario_email:str)->Optional[user]:
        pass

    @abstractmethod
    def deleteUserById(self,usuario_id:str)->bool:
        pass

    @abstractmethod
    def updateUser(self,usuario:user)->bool:
        pass

    @abstractmethod
    def registerUser(self,usuario:user)->Optional[user]:
        pass
