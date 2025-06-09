from domain.entidades.user_model import user
#from ...domain.entidades.user_model import user
from domain.repositorio.user_repo import UserRepository
from dataclasses import dataclass
from typing import Dict,Optional
@dataclass
class GetUserIdService:
    repo:UserRepository
    def execute(self,id):
        return self.repo.getUserByDocument(id)