from dataclasses import dataclass
import datetime
from datetime import date
from email_validator import validate_email, EmailNotValidError
#Se crea el modelo de un usuario
@dataclass
class user:
    firstName:str
    middleName:str
    surName1:str
    surName2:str
    bornDate:date
    department:str
    municipality:str
    trail:str
    email:str
    typeDocument:str
    numberDocument:str
    phoneNumber:str
    hashPassword:str
    username:str
    age:str=0

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
        diff=currentDate-self.bornDate
        self.age=diff.days//365

    #Validamos la edad: TRUE: >=18 años
    def validarEdad(self)->bool:
        return self.age>=18
    
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
        if self.typeDocument in ["CC","cc","Cc","cC","C.C"]:
            self.typeDocument=self.typeDocument.upper()
            return True
        return False
        
    #Validamos el numero de documento
    def validarNumeroDocumento(self)->bool:
        return self.numberDocument.isdigit()

    def toDictionary(self)->dict:
            return {
               "numberDocument": self.numberDocument,
                "typeDocument": self.typeDocument,
                "firstName": self.firstName,
                "middleName": self.middleName,
                "surName1": self.surName1,
                "surName2": self.surName2,
                "username":self.username,
                "bornDate": self.bornDate.isoformat(),  # Formato 'YYYY-MM-DD'
                "department": self.department,
                "municipality": self.municipality,
                "trail":self.trail,
                "email": self.email,
                "phoneNumber": self.phoneNumber,
                "age": self.age,
                "hashPassword":self.hashPassword,
            }
    


class seller(user):
    pass
    

class shopper(user):
    pass