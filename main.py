import discord
from discord.ext import commands
import random
import smtplib
import string
from discord.utils import get
import requests
from bs4 import BeautifulSoup

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
