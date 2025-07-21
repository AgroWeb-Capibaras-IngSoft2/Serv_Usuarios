"""
Servicio de registro de usuarios
Maneja la lógica de negocio para registrar nuevos usuarios en el sistema
"""

from domain.entidades.user_model import user
from domain.repositorio.user_repo import UserRepository
from dataclasses import dataclass
from typing import Dict
from datetime import datetime

@dataclass 
class RegisterUserService:
    """
    Servicio para registrar nuevos usuarios
    Valida los datos y crea una nueva instancia de usuario
    """
    repo: UserRepository
    
    def execute(self, data: Dict) -> user:
        """
        Ejecuta el registro de un nuevo usuario
        
        Args:
            data (Dict): Datos del usuario a registrar
            
        Returns:
            user: Usuario creado exitosamente
            
        Raises:
            ValueError: Si hay errores en la validación o creación del usuario
        """
        try:
            # Crear nueva instancia de usuario con validaciones automáticas
            new_user = user(
                firstName=data["firstName"],
                middleName=data["middleName"],
                surName1=data["surName1"],
                surName2=data["surName2"],
                bornDate=datetime.strptime(data["bornDate"], "%Y-%m-%d").date(),
                department=data["department"],
                municipality=data["municipality"],
                email=data["email"],
                phoneNumber=data["phoneNumber"],
                typeDocument=data["typeDocument"],
                numberDocument=data["numberDocument"],
                trail=data["trail"],
                username=data["username"],
                age=0,  # Se calcula automáticamente en __post_init__
                hashPassword=data["hashPassword"]
            )
            
            # Registrar usuario en la base de datos
            self.repo.registerUser(new_user)
            return new_user
            
        except ValueError as e:
            raise ValueError(f"Error al crear usuario: {e}")
        except KeyError as e:
            raise ValueError(f"Campo requerido faltante: {e}")

