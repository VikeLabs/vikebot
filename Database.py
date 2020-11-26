import sqlite3
conn = sqlite3.connect('discord.db')

c = conn.cursor()

""""""
#c.execute('''CREATE TABLE userData
            #(discordID, userEmail, verified)''')

c.execute("INSERT INTO userData VALUES (userDiscordID, userEmail, userVerified)")

conn.commit()

conn.close()