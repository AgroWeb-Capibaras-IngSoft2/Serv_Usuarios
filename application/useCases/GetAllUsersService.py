
"""
Servicio para obtener todos los usuarios
Maneja la lógica de negocio para consultar todos los usuarios
"""

from domain.entidades.user_model import user
from domain.repositorio.user_repo import UserRepository
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class GetAllUsersService:
    """
    Servicio para obtener todos los usuarios de la base de datos.
    """
    repo: UserRepository
    
    def execute(self) -> list:
        """
        Busca y retorna una lista de direcciones de usuarios.
        
        Args:
            
        Returns:
            List: Diccionario de todos los usuarios.
            
        Raises:
            ValueError: Si no existe ningún usuario en la base de datos
        """
        user_data = self.repo.getAllUsers()
        
        if not user_data:
            raise ValueError("Base de datos esta vacía.")
            
        return user_data
