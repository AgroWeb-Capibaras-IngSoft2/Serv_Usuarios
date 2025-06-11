from domain.entidades.user_model import user
#from ...domain.entidades.user_model import user
from domain.repositorio.user_repo import UserRepository
from dataclasses import dataclass
from typing import Dict,Optional
from datetime import datetime


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
                firstName=data["firstName"],
                middleName=data["middleName"],
                surName1=data["surName1"],
                surName2=data["surName2"],
                bornDate=datetime.strptime(data["bornDate"], "%Y-%m-%d").date(),
                department=data["department"],
                municipality=data["municipality"],
                email= data["email"],
                phoneNumber=data["phoneNumber"],
                typeDocument=data["typeDocument"],
                numberDocument=data["numberDocument"],
                trail=data["trail"],
                username=data["username"],
                age=0,
                hashPassword=data["hashPassword"]
            )
            self.repo.registerUser(new_user)
            print("error aca")
            return new_user
        except ValueError as e:
            raise ValueError(f"Error al crear usuario: {e}")
        

