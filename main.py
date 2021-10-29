#############################################################################                                                  
#                                                                           #
#                                                                           #
#                                   .ss` os:                                #
#                                `` .ys.`oy: .--` .-/++/:-`                 #
#                            -oyhhm/:hhddhh-+myydhdys++oshdo.               #
#                          .yms-..Ms```yM`` sM` -My      `-smo              #
#                          dm.   `My   yM   sM+:oMh`        /Ns             #
#                         .Ms    `My`  yM   sNsso:Nh         hM             #
#                          dm-    MNyhohM   sM`  .Ny        `mm             #
#                          `sdyooyd+.oMNM:::hm`  oM/...--:/odh.             #
#                            `://:.  hsssssss-   `oysyyyyso/-               #
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
############################################################################# 


import os

import discord
from dotenv import load_dotenv

from bs4 import BeautifulSoup

import requests

import xml.dom.minidom

from gitMain import autoMaintain
#from cairosvg import svg2png
import time
import json

import Points as pts
load_dotenv()
TOKEN = ''


        
client = discord.Client()



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    before = ""
    channel = client.get_channel(901193670970179637)
    while True:
        commit = autoMaintain()
        if before != str(commit):
            print(commit[0])
            print(commit[1])
            await channel.send(f"{commit[0]} just commited with the message, {commit[1]}")
            try:
                with open(commit[0] + '.json', 'r') as f:
                
                    user = json.load(f)
                  
                    if pts.checkForLevelUp(user["points"]) != user["level"]:
                        embed=discord.Embed(title="", url="", description="", color=0x1CEEEE)
                        #embed.set_thumbnail(url="https://github.com/AndreasInk/HyperDashDiscordBot/blob/main/trophy.png?raw=true")
                        user["level"] = pts.checkForLevelUp(user["points"])
                        embed.add_field(name= "Level", value= f"{user['name']} reached level {user['level']}", inline=False)
                        await channel.send(embed=embed)
                        
                    pts.addPoints(user=user)


            except:
                    user = {}
                    user["id"] =  0
                    user["name"] =  commit[0]
                    user["points"] = 0
                    user["level"] = 0
                    with open("names" + '.txt', 'w') as f:
                        try:
                            f.write(f.read() + user["name"])
                        except:
                            f.write(user["name"])
                    pts.addPoints(user= user)
           
            
        before = str(commit)
        time.sleep(10)
        
        ranks = pts.rankPlayer()
        embed=discord.Embed(title="", url="", description="", color=0x1CEEEE)
        embed.set_thumbnail(url="https://github.com/UNF-AIRO/AIRO-Discord-Bot/blob/master/Images/Gold.png?raw=true")
        embed.add_field(name= "1st Place", value= f"{ranks[0]['name']}", inline=False)
        await channel.send(embed=embed)
        time.sleep(10)
client.run(TOKEN)
