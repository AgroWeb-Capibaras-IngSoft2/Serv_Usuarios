"""
Servicio para obtener usuario por documento
Maneja la lógica de negocio para consultar usuarios por número de documento
"""

from domain.entidades.user_model import user
from domain.repositorio.user_repo import UserRepository
from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class GetUserIdService:
    """
    Servicio para obtener un usuario por su número de documento
    """
    repo: UserRepository
    
    def execute(self, document_id: str) -> Dict:
        """
        Busca y retorna un usuario por su número de documento
        
        Args:
            document_id (str): Número de documento del usuario
            
        Returns:
            Dict: Datos del usuario encontrado
            
        Raises:
            ValueError: Si no existe ningún usuario con ese documento
        """
        user_data = self.repo.getUserByDocument(document_id)
        
        if not user_data:
            raise ValueError("No existe ningún usuario con este documento")
            
        return user_data