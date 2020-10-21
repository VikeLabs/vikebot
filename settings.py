import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print("ignoring dotenv file...")

# sample usage of loading environment variable from .env file in the following syntax.
# KEY=VALUE
ADDRESS = os.environ["BOT_EMAIL"]
PASSWORD = os.environ["BOT_PASSWORD"]
