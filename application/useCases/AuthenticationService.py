"""
Servicio de autenticación de usuarios
Maneja la lógica de negocio para autenticar usuarios en el sistema
"""

from domain.repositorio.user_repo import UserRepository
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class AuthenticationService:
    """
    Servicio para autenticar usuarios mediante email y contraseña
    """
    repo: UserRepository
    
    def execute(self, email: str, password: str) -> bool:
        """
        Autentica un usuario verificando sus credenciales
        
        Args:
            email (str): Email del usuario
            password (str): Contraseña hasheada del usuario
            
        Returns:
            bool: True si la autenticación es exitosa
            
        Raises:
            Exception: Si el usuario no existe
            ValueError: Si la contraseña es incorrecta
        """
        # Buscar usuario por email
        user_data = self.repo.getUserByEmail(email)
        
        if not user_data:
            raise Exception("El usuario no existe")
        print(user_data)
        if(user_data["hashPassword"]==password):
            print("olaa")
            return {"Success":True,"message":"Ingreso exitoso","user":{"userdocument":user_data["numberDocument"],
                                           "doctype":user_data["typeDocument"], "usertype":user_data["userType"]}}
        raise ValueError("La contraseña es incorrecta")