import discord
from discord.ext import commands
import random
import os
import smtplib
import string
from discord.utils import get
import requests
from bs4 import BeautifulSoup
from database import DiscordUserModel

TOKEN = os.environ.get("BOT_TOKEN")

# Prefix
client = commands.Bot(command_prefix=".")
# client.remove_command('help')

@client.event
async def on_ready():
    print("Bot is ready.")

# Ping Pong command
@client.command()
async def ping(ctx):
    await ctx.send('pong')

# Store user's Github username
@client.command(breif="Let us know your Github username so we can connect you with your team!", description="Use '.usergit' followed by your Github username")
async def set_user_github(ctx: commands.Context, username):
    user = None
    try:
        user = DiscordUserModel.get(ctx.author.id)
    except DiscordUserModel.DoesNotExist:
        user = DiscordUserModel(ctx.author.id)
    
    user.github = username
    user.save()
    await ctx.send(f'Github username saved as https://github.com/{username}')

@client.command(breif="Let us know your Github username so we can connect you with your team!", description="Use '.usergit' followed by your Github username")
async def get_user_github(ctx: commands.Context):
    try:
        user = DiscordUserModel.get(ctx.author.id)
        #user either has or hasnt set value
        if user.github:
            await ctx.send(f'Github username is saved as https://github.com/{user.github}')
        else:
             await ctx.send('You have not set this information yet')
    except DiscordUserModel.DoesNotExist:
        await ctx.send('You have not set any information yet')
        return
    
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

# Code must be above this line
client.run(TOKEN)

s.quit()
