from pydantic import BaseModel
import json
from fastapi.encoders import jsonable_encoder
from typing import List
import discord

TOKEN = ''


        
client = discord.Client()


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
def rankPlayers():
    first = {}
   
    second = {}
   
    third = {}
   
    with open("names" + '.txt', 'r') as f:
        for line in f.readlines():
            
            if line.strip() != "\n":
                print(line)
                with open(line.strip() + '.json', 'r') as f:
                    user = json.load(f)
                    try:
                        if user["points"] > first["points"]:
                            first = user
                            
                    except:
                        first = user
                    try:
                        if user["points"] > second["points"]:
                            if first != user:
                                second = user
                            
                    except:
                        if first != user:
                            second = user
                    try:
                        if user["points"] > third["points"]:
                             if second != user and first != user:
                               
                                third = user
                            
                    except:
                        if second != user and first != user:
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
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '!L' in message.content:
        
        ranks = rankPlayers()
        embed=discord.Embed(title= f"{ranks[0]['name']}" , url="", description="", color=0x1CEEEE)
        embed.set_thumbnail(url="https://github.com/UNF-AIRO/AIRO-Discord-Bot/blob/master/Images/Gold.png?raw=true")
        embed.add_field(name= "1st Place", value= f"{ranks[0]['points']}" + " Points", inline=False)
        try:
            await message.channel.send(embed=embed)
            embed=discord.Embed(title= f"{ranks[1]['name']}", url="", description="", color=0x1CEEEE)
            embed.set_thumbnail(url="https://github.com/UNF-AIRO/AIRO-Discord-Bot/blob/master/Images/Silver.png?raw=true")
            embed.add_field(name= "2nd Place", value= f"{ranks[1]['points']}" + " Points", inline=False)
            await message.channel.send(embed=embed)
        except:
            print("No 2nd Player")
        try:
            embed=discord.Embed(title=f"{ranks[2]['name']}", url="", description="", color=0x1CEEEE)
            embed.set_thumbnail(url="https://github.com/UNF-AIRO/AIRO-Discord-Bot/blob/master/Images/Bronze.png?raw=true")
            embed.add_field(name= "3rd Place", value= "Points" + f"{ranks[2]['points']}" + " Points", inline=False)
            await message.channel.send(embed=embed)
        except:
            print("No 3rd Player")
        

client.run(TOKEN)