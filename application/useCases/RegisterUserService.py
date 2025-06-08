from domain.entidades.user_model import user
from domain.repositorio.user_repo import UserRepository
from dataclasses import dataclass
from typing import Dict,Optional
import re

@dataclass 
class RegisterUserService:
    repo:UserRepository
    def execute(self,data:Dict)->user:
        documentExist= self.repo.getUserByDocument("documento")
        emailExist=self.repo.getUserByEmail("email")
        if(emailExist):
            raise ValueError("Email ya registrado")
        if(documentExist):
            raise ValueError("Documento ya registrado")
        try:
            new_user=user(
                primerNombre=data["primerNombre"],
                segundoNombre=data["segundoNombre"],
                primerApellido=data["primerApellido"],
                segundoApellido=data["segundoApellido"],
                fechaNacimiento=data["fechaNacimiento"],
                departamento=data["departamento"],
                municipio=data["municipio"],
                email= data["email"],
                telefono=data["telefono"],
                tipoDocumento=data["tipoDocumento"],
                numeroDocumento=data["numeroDocumento"],
                edad=0
            )
            self.repo.registerUser(new_user)
            return new_user
        except ValueError as e:
            raise ValueError(f"Error al crear usuario: {e}")
        

