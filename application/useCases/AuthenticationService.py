from domain.repositorio.user_repo import UserRepository
from dataclasses import dataclass
from typing import Dict,Optional
@dataclass
class AuthenticationService:
    repo:UserRepository
    def execute(self,email:str,password:str):
        user=self.repo.getUserByEmail(email)
        if not user:
            raise Exception("El usuario no existe")
        print(user)
        if(user["hashPassword"]==password):
            return True
        raise ValueError("La contraseña es incorrecta")