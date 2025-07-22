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
            print("olaa")
            return {"Success":True,"message":"Ingreso exitoso","user":{"userdocument":user["numberDocument"],
                                           "doctype":user["typeDocument"]}}
        raise ValueError("La contraseña es incorrecta")