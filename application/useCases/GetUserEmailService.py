"""
Servicio para obtener usuario por email
Maneja la lógica de negocio para consultar usuarios por dirección de email
"""

from domain.entidades.user_model import user
from domain.repositorio.user_repo import UserRepository
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class GetUserEmailService:
    """
    Servicio para obtener un usuario por su dirección de email
    """
    repo: UserRepository
    
    def execute(self, email: str) -> Dict:
        """
        Busca y retorna un usuario por su dirección de email
        
        Args:
            email (str): Dirección de email del usuario
            
        Returns:
            Dict: Datos del usuario encontrado
            
        Raises:
            ValueError: Si no existe ningún usuario con ese email
        """
        user_data = self.repo.getUserByEmail(email)
        
        if not user_data:
            raise ValueError("Email no encontrado en la base de datos")
            
        return user_data