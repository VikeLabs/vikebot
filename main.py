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
@client.command(breif="Let us know your Github username so we can connect you with your team!", description="Use '.set_user_github' followed by a ping of the desired discord user and then their Linkedin username all space seperated")
async def set_user_github(ctx: commands.Context, discorduser=None, gitusername=None):
    if discorduser == None or discorduser[:-1][0] != '<':
        return await ctx.send('No user was specified, make sure to ping the desired user after the command')
    if gitusername == None:
        return await ctx.send('No Github username was specified')
    discordid = discorduser.replace("<","").replace("@","").replace("!","").replace(">","")
    discordid = int(discordid)
    user = None
    try:
        user = DiscordUserModel.get(discordid)
    except DiscordUserModel.DoesNotExist:
        user = DiscordUserModel(discordid)
    
    user.github = gitusername
    user.save()
    await ctx.send(f'Github username saved as https://github.com/{gitusername}')

@client.command(breif="Check which Github username you have stored", description="Use '.get_user_github', then a space, then ping the desird user")
async def get_user_github(ctx: commands.Context, discorduser=None):
    if discorduser == None or discorduser[:-1][0] != '<':
        return await ctx.send('No user was specified, make sure to ping the desired user after the command')
    discordid = discorduser.replace("<","").replace("@","").replace("!","").replace(">","")
    discordid = int(discordid)
    try:
        user = DiscordUserModel.get(discordid)
        #user either has or hasnt set value
        if user.github:
            await ctx.send(f'Github username is saved as https://github.com/{user.github}')
        else:
             await ctx.send('You have not set this information yet')
    except DiscordUserModel.DoesNotExist:
        await ctx.send('You have not set any information yet')
        return

# Store user's Linkedin username
@client.command(breif="Let us know your Linkedin username", description="Use '.set_user_linkedin' followed by a ping of the desired discord user and then their Linkedin username all space seperated")
async def set_user_linkedin(ctx: commands.Context, discorduser=None, *args):
    if discorduser == None or discorduser[:-1][0] != '<':
        return await ctx.send('No user was specified. Make sure to ping the desired user after the command')
    if len(args) < 1:
        return await ctx.send('No Linkedin username was specified')
    discordid = discorduser.replace("<","").replace("@","").replace("!","").replace(">","")
    discordid = int(discordid)
    user = None
    try:
        user = DiscordUserModel.get(discordid)
    except DiscordUserModel.DoesNotExist:
        user = DiscordUserModel(discordid)
    
    username = ""
    for arg in args:
        username = username+" "+arg
    username = username[1:]
    user.linkedin = username
    user.save()
    await ctx.send(f'Linkedin username saved as {username}')

@client.command(breif="Check which Linkedin username is associated with a certain user", description="Use '.get_user_linkedin' then a space, then ping the desird user")
async def get_user_linkedin(ctx: commands.Context, discorduser=None):
    if discorduser == None or discorduser[:-1][0] != '<':
        return await ctx.send('No user was specified. Make sure to ping the desired user after the command')
    discordid = discorduser.replace("<","").replace("@","").replace("!","").replace(">","")
    discordid = int(discordid)
    try:
        user = DiscordUserModel.get(discordid)
        #user either has or hasnt set value
        if user.linkedin:
            await ctx.send(f'Linkedin username is saved as {user.linkedin}')
        else:
             await ctx.send('This user has not set this information yet')
    except DiscordUserModel.DoesNotExist:
        await ctx.send('This user has not set any information yet')
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
