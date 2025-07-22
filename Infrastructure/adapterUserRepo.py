"""
Adaptador del repositorio de usuarios
Implementa la interfaz UserRepository utilizando MongoDB como base de datos
"""

from domain.repositorio.user_repo import UserRepository
from Infrastructure.mongoDB import DB

class AdapterUserRepo(UserRepository):
    """
    Adaptador que conecta la lógica de negocio con la base de datos MongoDB
    Implementa el patrón Adapter para la persistencia de usuarios
    """
    
    def __init__(self):
        """Inicializa la conexión a la base de datos MongoDB"""
        self.database: DB = DB()

    def getAllUsers(self) -> list:
        """
        Obtiene todos los usuarios de la base de datos
        
        Args:
            
        Returns:
            List: Lista de diccionario de usuarios
          
        """
        return self.database.get_all_users()

    def getUserByDocument(self, usuario_id: str) -> dict:
        """
        Obtiene un usuario por su número de documento
        
        Args:
            usuario_id (str): Número de documento del usuario
            
        Returns:
            dict: Datos del usuario o None si no existe
        """
        return self.database.get_user_by_document(usuario_id)
    
    def getUserByEmail(self, usuario_email: str) -> dict:
        """
        Obtiene un usuario por su email
        
        Args:
            usuario_email (str): Email del usuario
            
        Returns:
            dict: Datos del usuario o None si no existe
        """
        return self.database.get_user_by_email(usuario_email)
    
    def registerUser(self, usuario) -> bool:
        """
        Registra un nuevo usuario en la base de datos
        
        Args:
            usuario: Instancia del modelo user a registrar
            
        Returns:
            bool: True si el registro fue exitoso
        """
        return self.database.add_user(usuario)
    
    def updateUser(self, usuario):
        """
        Actualiza los datos de un usuario existente
        Método heredado del repositorio base
        """
        return super().updateUser(usuario)
    
    def deleteUserById(self, usuario_id: str) -> int:
        """
        Elimina un usuario por su ID
        
        Args:
            usuario_id (str): ID del usuario a eliminar
            
        Returns:
            int: Número de documentos eliminados
        """
        return self.database.delete_user_by_id(usuario_id)
    
