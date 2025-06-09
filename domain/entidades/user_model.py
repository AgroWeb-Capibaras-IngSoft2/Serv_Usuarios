from dataclasses import dataclass
import datetime
from datetime import date
from email_validator import validate_email, EmailNotValidError
#Se crea el modelo de un usuario
@dataclass
class user:
    primerNombre:str
    primerNombre:str
    segundoNombre:str
    primerApellido:str
    segundoApellido:str
    fechaNacimiento:date
    departamento:str
    municipio:str
    email:str
    telefono:str
    tipoDocumento:str
    numeroDocumento:str
    edad:str=0

    #Validar despues de haber inicializado la informacion
    def __post_init__(self):
        self.calcularEdad()
        if(not self.validarEdad() or 
           not self.validarEmail() or 
           not self.validarTipoDocumento() or 
           not self.validarNumeroDocumento()):
            raise ValueError("Existen datos invalidos y no se puede crear el usuario")

    def calcularEdad(self):
        currentDate=datetime.date.today()
        diff=currentDate-self.fechaNacimiento
        self.edad=diff.days//365

    #Validamos la edad: TRUE: >=18 años
    def validarEdad(self)->bool:
        return self.edad>=18
    
    #Validamos el email
    def validarEmail(self)->bool:
        valido=True
        try:
            validate_email(self.email)  # Si el email es inválido, lanza una excepción
        except EmailNotValidError as e:
            valido=False
        finally:
            return valido
    #Validamos el tipo de documento
    def validarTipoDocumento(self)->bool:
        if self.tipoDocumento in ["CC","cc","Cc","cC"]:
            self.tipoDocumento=self.tipoDocumento.upper()
            return True
        return False
        
    #Validamos el numero de documento
    def validarNumeroDocumento(self)->bool:
        return self.numeroDocumento.isdigit()

    def toDictionary(self)->dict:
            return {
                "Num Documento": self.numeroDocumento,
                "Tipo Documento": self.tipoDocumento,
                "Primer Nombre": self.primerNombre,
                "Segundo Nombre": self.segundoNombre,
                "Primer Apellido": self.primerApellido,
                "Segundo Apellido": self.segundoApellido,
                "Fecha Nacimiento": self.fechaNacimiento.isoformat(),  # Formato 'YYYY-MM-DD'
                "Departamento": self.departamento,
                "Municipio": self.municipio,
                "email": self.email,
                "telefono": self.telefono,
                "edad": self.edad
            }



class seller(user):
    pass
    

class buyer(user):
    pass