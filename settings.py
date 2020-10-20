import os
from dotenv import load_dotenv
load_dotenv()

# sample usage of loading environment variable from .env file
# KEY=VALUE
print(os.environ["HELLO"])