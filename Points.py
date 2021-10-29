from pydantic import BaseModel
import json
from fastapi.encoders import jsonable_encoder
from typing import List

class User(BaseModel):
    id: int = 0
    name: str = ""
    points: int = 0
    level: int = 0

class Users(BaseModel):
    __root__: List[User]
def addPoints(user):
    
    with open(user["name"] + '.json', 'w') as f:
        user["points"] += 1
        json.dump(user, f)
def rankPlayer():
    first = {}
   
    second = {}
   
    third = {}
   
    with open("names" + '.txt', 'r') as f:
        for line in f.readlines():
            with open(line + '.json', 'r') as f:
                user = json.load(f)
                try:
                    if user["points"] > first["points"]:
                        first = user
                    elif user["points"] > second["points"]:
                        second = user
                    elif user["points"] > third["points"]:
                        third = user
                except:
                    first = user
                    second = user
                    third = user
    return [first, second, third]

                

        

def checkForLevelUp(points):
   if points > 0 and points < 2:
       return 1
   if points > 2 and points < 5:
       return 2
   if points > 5 and points < 15:
       return 3
   if points > 15 and points < 35:
       return 4
   if points > 35 and points < 50:
       return 5
       

        

#addPoints(user= User(id=0, name="a", points=0))