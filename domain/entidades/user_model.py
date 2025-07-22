"""
Modelo de dominio para usuarios del sistema Agroweb
Define la estructura y validaciones para entidades de usuario
"""

from dataclasses import dataclass
import datetime
from datetime import date
from email_validator import validate_email, EmailNotValidError

@dataclass
class user:
    """
    Modelo de usuario para la plataforma Agroweb
    Incluye validaciones automáticas para datos críticos como edad, email y documento
    """
    firstName: str
    middleName: str
    surName1: str
    surName2: str
    userType: str
    bornDate: date
    department: str
    municipality: str
    trail: str
    email: str
    typeDocument: str
    numberDocument: str
    phoneNumber: str
    hashPassword: str
    username: str
    age: str = 0

    def __post_init__(self):
        """
        Validaciones automáticas después de la inicialización
        Calcula la edad y valida datos críticos del usuario
        
        Raises:
            ValueError: Si alguna validación falla
        """
        self.calcularEdad()
        if (not self.validarEdad() or 
           not self.validarEmail() or 
           not self.validarTipoDocumento() or 
           not self.validarNumeroDocumento()):
            raise ValueError("Existen datos inválidos y no se puede crear el usuario")

    def calcularEdad(self):
        """
        Calcula la edad del usuario basada en su fecha de nacimiento
        Actualiza el campo age automáticamente
        """
        currentDate = datetime.date.today()
        diff = currentDate - self.bornDate
        self.age = diff.days // 365

    def validarEdad(self) -> bool:
        """
        Valida que el usuario sea mayor de edad (>=18 años)
        
        Returns:
            bool: True si el usuario es mayor de edad
        """
        return self.age >= 18
    
    def validarEmail(self) -> bool:
        """
        Valida el formato del email usando la librería email-validator
        
        Returns:
            bool: True si el email tiene un formato válido
        """
        valido = True
        try:
            validate_email(self.email)  # Lanza excepción si el email es inválido
        except EmailNotValidError as e:
            valido = False
        finally:
            return valido
    def validarTipoDocumento(self) -> bool:
        """
        Valida que el tipo de documento sea cédula de ciudadanía (CC)
        Normaliza el formato a mayúsculas
        
        Returns:
            bool: True si es un tipo de documento válido
        """
        if self.typeDocument in ["CC", "cc", "Cc", "cC", "C.C"]:
            self.typeDocument = self.typeDocument.upper()
            return True
        return False
        
    def validarNumeroDocumento(self) -> bool:
        """
        Valida que el número de documento contenga solo dígitos
        
        Returns:
            bool: True si el número de documento es válido (solo números)
        """
        return self.numberDocument.isdigit()

    def toDictionary(self) -> dict:
        """
        Convierte la instancia de usuario a un diccionario
        Útil para serialización y almacenamiento en base de datos
        
        Returns:
            dict: Representación en diccionario del usuario
        """
        return {
           "numberDocument": self.numberDocument,
            "typeDocument": self.typeDocument,
            "firstName": self.firstName,
            "middleName": self.middleName,
            "surName1": self.surName1,
            "surName2": self.surName2,
            "userType": self.userType,
            "username": self.username,
            "bornDate": self.bornDate.isoformat(),  # Formato 'YYYY-MM-DD'
            "department": self.department,
            "municipality": self.municipality,
            "trail": self.trail,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "age": self.age,
            "hashPassword": self.hashPassword,
        }


class seller(user):
    """
    Clase especializada para usuarios vendedores
    Hereda todas las propiedades y validaciones de user
    """
    pass
    

class shopper(user):
    """
    Clase especializada para usuarios compradores
    Hereda todas las propiedades y validaciones de user
    """
    pass