from pymongo import MongoClient
from domain.entidades.user_model import user

class DB:

  def __init__(self):
    self.open_client()

  def open_client(self):
    try:
      self.client = MongoClient('localhost', 27017)
      self.db = self.client['Serv_Usuarios']
      self.collection = self.db['Usuarios']
    except Exception as e:
      raise Exception("error:", e)

  def close_client(self):
     self.client.close  

  def add_user(self, user:user):
    self.open_client()
    if self.get_user_by_email(user.email) != None:
        print(self.get_user_by_email(user.email))
        raise ValueError("Email ya registrado")
    if self.get_user_by_document(user.numberDocument) != None:
        raise ValueError("Documento ya registrado")
    if self.get_user_by_username(user.username) != None:
        raise ValueError ("Username no disponible")
    result = self.collection.insert_one(user.toDictionary())
    self.close_client()
    return result.acknowledged

  def get_user_by_email(self, email: str):
    self.open_client()
    result = self.collection.find_one({"email": email})
    self.close_client()
    if result:
      result['_id'] = str(result['_id'])  # Convert ObjectId to string
      print(result)
      return dict(result)

  def get_user_by_document(self, numero_documento: str):
    self.open_client()
    result = self.collection.find_one({"numberDocument": numero_documento})
    self.close_client()
    if result:
      result['_id'] = str(result['_id'])  
      return dict(result)

  def get_user_by_username(self, username: str):
    self.open_client()
    result = self.collection.find_one({"username": username})
    self.close_client()
    if result:
      result['_id'] = str(result['_id'])  
      return dict(result)

  def delete_user_by_id(self, username):
    self.open_client()
    result = self.collection.delete_one({"username": username})
    self.close_client()
    return result.deleted_count

  