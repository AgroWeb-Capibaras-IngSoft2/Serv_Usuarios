"""
Conexión y operaciones con base de datos MongoDB
Maneja todas las operaciones CRUD para usuarios en MongoDB
"""

from pymongo import MongoClient
from domain.entidades.user_model import user

class DB:
    """
    Clase para manejar conexiones y operaciones con MongoDB
    Base de datos: Serv_Usuarios, Colección: Usuarios
    """

    def __init__(self):
        """Inicializa la conexión al cliente MongoDB"""
        self.open_client()

    def open_client(self):
        """
        Establece conexión con MongoDB
        Conecta a localhost:27017 y selecciona la base de datos Serv_Usuarios
        """
        try:
            self.client = MongoClient('localhost', 27017)
            self.db = self.client['Serv_Usuarios']
            self.collection = self.db['Usuarios']
        except Exception as e:
            raise Exception(f"Error conectando a MongoDB: {e}")

    def close_client(self):
        """Cierra la conexión con MongoDB"""
        if hasattr(self, 'client') and self.client:
            self.client.close()

    def add_user(self, user: user) -> bool:
        """
        Agrega un nuevo usuario a la base de datos
        Valida que no existan duplicados de email, documento o username
        
        Args:
            user: Instancia del modelo user a insertar
            
        Returns:
            bool: True si la inserción fue exitosa
            
        Raises:
            ValueError: Si ya existe un usuario con el mismo email, documento o username
        """
        try:
            # Validar duplicados antes de insertar
            if self.get_user_by_email(user.email) is not None:
                print(f"Email duplicado encontrado: {self.get_user_by_email(user.email)}")
                raise ValueError("Email ya registrado")
            
            if self.get_user_by_document(user.numberDocument) is not None:
                raise ValueError("Documento ya registrado")
            
            if self.get_user_by_username(user.username) is not None:
                raise ValueError("Username no disponible")
            
            # Insertar usuario
            result = self.collection.insert_one(user.toDictionary())
            return result.acknowledged
        except Exception as e:
            print(f"Error en add_user: {e}")
            raise

    def get_user_by_email(self, email: str) -> dict:
        """
        Busca un usuario por su dirección de email
        
        Args:
            email (str): Email del usuario a buscar
            
        Returns:
            dict: Datos del usuario o None si no existe
        """
        try:
            result = self.collection.find_one({"email": email})
            if result:
                result['_id'] = str(result['_id'])  # Convertir ObjectId a string
                return dict(result)
            return None
        except Exception as e:
            print(f"Error en get_user_by_email: {e}")
            return None

    def get_user_by_document(self, numero_documento: str) -> dict:
        """
        Busca un usuario por su número de documento
        
        Args:
            numero_documento (str): Número de documento del usuario
            
        Returns:
            dict: Datos del usuario o None si no existe
        """
        try:
            result = self.collection.find_one({"numberDocument": numero_documento})
            if result:
                result['_id'] = str(result['_id'])  # Convertir ObjectId a string
                return dict(result)
            return None
        except Exception as e:
            print(f"Error en get_user_by_document: {e}")
            return None

    def get_user_by_username(self, username: str) -> dict:
        """
        Busca un usuario por su username
        
        Args:
            username (str): Username del usuario a buscar
            
        Returns:
            dict: Datos del usuario o None si no existe
        """
        try:
            result = self.collection.find_one({"username": username})
            if result:
                result['_id'] = str(result['_id'])  # Convertir ObjectId a string
                return dict(result)
            return None
        except Exception as e:
            print(f"Error en get_user_by_username: {e}")
            return None

    def delete_user_by_id(self, username: str) -> int:
        """
        Elimina un usuario por su username
        
        Args:
            username (str): Username del usuario a eliminar
            
        Returns:
            int: Número de documentos eliminados
        """
        try:
            result = self.collection.delete_one({"username": username})
            return result.deleted_count
        except Exception as e:
            print(f"Error en delete_user_by_id: {e}")
            return 0

  