import chatbot as cb
import streamlit as st
import discord

TOKEN = ''


        
client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '901193670970179637' in message.channel:
        cbResponse = cb.chatbot_response(message.content)
        await message.channel.send(cbResponse)

client.run(TOKEN)