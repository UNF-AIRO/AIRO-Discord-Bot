from pydantic import BaseModel
import json
from fastapi.encoders import jsonable_encoder
from typing import List

class User(BaseModel):
    id: int = 0
    name: str = ""
    points: int = 0

class Users(BaseModel):
    __root__: List[User]
def addPoints(user):
    
    with open(user.name + '.txt', 'w') as f:
        user.points += 1
        f.write(str(user.dict()))
        

addPoints(user= User(id=0, name="a", points=0))