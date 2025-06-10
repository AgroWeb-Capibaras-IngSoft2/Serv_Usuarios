from domain.entidades.user_model import user
#from ...domain.entidades.user_model import user
from domain.repositorio.user_repo import UserRepository
from dataclasses import dataclass
from typing import Dict,Optional
@dataclass
class GetUserEmailService:
    repo:UserRepository
    def execute(self,email):
        if(not(self.repo.getUserByEmail(email))):
            raise ValueError ("Email no encontrado en la base de datos")
        return self.repo.getUserByEmail(email)