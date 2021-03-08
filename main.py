import discord
from discord.ext import commands
import random
import os
import smtplib
import string
from discord.utils import get
import requests
from bs4 import BeautifulSoup
from database import *

TOKEN = os.environ.get("BOT_TOKEN")

# Prefix
client = commands.Bot(command_prefix=".")
# client.remove_command('help')

# Will be replaced with connecting to actual database when we have one
DiscordUserModel()



# On bot start
@client.event
async def on_ready():
    print("Bot is ready.")



# Ping Pong command
@client.command()
async def ping(ctx):
    await ctx.send('pong')

# Stack Overflow searcher
@client.command(brief="Search Stack Overflow", description="Use '.stack' followed by comma separated search terms "
                                                           "to search Stack Overflow. (e.g. '.stack python,string,split')")
async def stack(ctx, entry):
    final_entry = str(entry).replace(',', "+")
    result = requests.get("https://stackoverflow.com/search?q=" + final_entry)
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    div_tag = soup.find('div', class_="result-link")
    h3_tag = div_tag.find('h3')
    a_tag = h3_tag.find('a')
    temp_url = str(a_tag)
    temp2_url = temp_url[50:]
    url = str(temp2_url).split(';')
    finalurl = "https://stackoverflow.com" + str(url[0])
    await ctx.send(finalurl)

# Database Interface - Need to implement verified check
@client.command()
async def add_info(ctx, arg1, arg2, arg3, user: discord.user):
    author = ctx.message.author
    # Checks for missing data
    if not arg1 or arg2 or arg3:
        await ctx.send('The information you have entered is incomplete')
    # Saves to database
    NoSQL = DiscordUserModel(author, first_name=arg1, last_name=arg2, email=arg3)
    NoSQL.save()
    # Attempts to PM user and verify message content - NOT COMPLETE
    message = "The information you submitted is..."
    await client.send_message(user, message)


# Code must be above this line
client.run(TOKEN)

#s.quit()
