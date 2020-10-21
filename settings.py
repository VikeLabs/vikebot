import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print("ignoring dotenv file...")

# sample usage of loading environment variable from .env file
# KEY=VALUE
# print(os.environ["HELLO"]) 