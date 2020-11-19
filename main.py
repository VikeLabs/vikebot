import discord
from discord.ext import commands
import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from discord.utils import get
import requests
from bs4 import BeautifulSoup
import settings

# Prefix
client = commands.Bot(command_prefix=".")
# client.remove_command('help')


@client.event
async def on_ready():
    print("Bot is ready.")
    for server in client.guilds:
        for channel in server.text_channels:
            if channel.name == 'general':
                await client.get_channel(channel.id).send("Greetings! To complete my set up, "
                                                          "please type: '.setup (your desired email suffix here e.g. uvic.ca)'")

# On member join, set visibility of all channels to false, except "verify-channel" and send an explanatory msg


@client.event
async def on_server_join(member):
    for channel in member.guild.channels:
        if channel.name != 'verify-channel':
            await channel.set_permissions(member, view_channel=False)

    for channel in member.server.channels:
        if channel.name == 'verify-channel':
            message = 'Hello {}, welcome to {}'.format(member.mention, server.name) + \
                "In order to gain access to the other channels in this server, please verify " \
                "that you are a UVic student, by responding with the following command: " \
                "'.email NetlinkID@uvic.ca', using your own Netlink ID."
            await client.send_message(default_channel, message)

# Ping Pong command


@client.command()
async def ping(ctx):
    await ctx.send('pong')

verify_code = 'J4B97H' #Initialized to random value

# Creates and sends email


def send_email(sender, recipient, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)


# Logs into the Bot's email account
if __name__ == '__main__':
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(ADDRESS, PASSWORD)

# Email command


@client.command()
async def email(ctx, address):
    run = True
    for role in ctx.author.roles:
        if role == 'Verified':
            run = False

    if run:
        global DOMAIN
        if is_right_address(address, DOMAIN):
            code = create_code()
            send_email(ADDRESS, address, 'Email Verification - Discord', 'Here is your code: '+code + '\n\nSincerely,\n'
                       + 'UVic Email Verification Bot')
            await ctx.send("Your verification email has been sent. Please respond with '.code xxxxxx', "
                           "replacing the x's with the digits found in the email.")
        else:
            await ctx.send("My apologies, it appears you have not read my instructions correctly. Please try again, "
                           "using the following command: '.email NetlinkID@uvic.ca', with your own Netlink ID.")

# Checks last 8 characters of given email address
# Input: add - email address
# Output: True if last 8 characters = "@uvic.ca", return False otherwise


def is_right_address(add, domain):
    l = add.split('@')
    if l[-1] == domain:
        return True
    else:
        return False

# Creates randomized code
# Input: n/a
# Output: a random 6 character string


def create_code():
    length = 6
    letters = string.ascii_lowercase
    code = ''.join(random.choice(letters) for i in range(length))
    global verify_code
    verify_code = code
    return code

# Code command


@client.command()
async def code(ctx, entry):
    if entry == verify_code:
        await ctx.send('Code accepted. Welcome to the server!')
    else:
        await ctx.send('Invalid code.')


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

# Sets up 'verify-channel' and the role 'Verified'
DOMAIN = ''


@client.command(brief="Set up the bot", description="'.setup (your desired email suffix here e.g. uvic.ca)'")
async def setup(ctx, domain):
    global DOMAIN
    domain = DOMAIN

    guild = ctx.guild
    role_exists = False
    channel_exists = False

    await guild.role[0].edit(read_messages=False, view_channel=False)

    for role in guild.roles:
        if role.name == 'Verified':
            role_exists = True
    if not role_exists:
        role = await guild.create_role('Verified')

    for channel in guild.text_channels:
        if channel.name == 'verify-channel':
            channel_exists = True
    if not channel_exists:
        verified_role = get(guild.roles, name="Verified")
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=True, read_message_history=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            verified_role: discord.PermissionOverwrite(view_channel=False)
        }
        channel = await guild.create_text_channel('verify-channel', overwrites=overwrites)

# Code must be above this line
client.run(TOKEN)

s.quit()
