import os
from dotenv import load_dotenv
load_dotenv()

# sample usage of loading environment variable from .env file in the following syntax.
# KEY=VALUE
ADDRESS = os.environ["BOT_EMAIL"]
PASSWORD = os.environ["BOT_PASSWORD"]