# VikeBot
Documentation is work in progress!

## Pycord
Discord.py is now deprecated so we're moving to an alternative ~ Pycord. Pycord is a fork of Discord.py being maintained from v1.7.3 onwards. 
The documentation to get started with Pycord can be found [Here!](https://docs.pycord.dev/en/master/#getting-started)

## Development

### .env file
1. Create a `.env` file in the root directory.
2. Add the `.env` file to `.gitignore`


### Pipenv
1. Use [pipenv](https://github.com/pypa/pipenv) to manage dependencies etc.
2. Execute `pipenv install` to install dependecies.
2. Run `main.py` using `pipenv run python main.py`
    - **Note**: The bot expects either the `BOT_TOKEN` passed in as an environement variable or within a `.env` file in the project root directory. 

### Discord Bot Token    
1. Login to/Create your [Discord Developer](https://discord.com/developers) account. 
2. Create a `New Application` from the dashboard, give the app a name to match the use. Eg: test-bot.
3. In the Application, click on `Bot` from the menu to the left.
4. Create a new bot on the Build-A-Bot page by clicking on the `New Bot` button. 
5. Once the bot is created, you'll see a `Copy` button under Token on the bot page. 
6. Paste the copied Token into the `.env` file in the project root directory.

### Database
VikeBot uses DynamoDB, which is a NoSQL database by Amazon. Below provides some brief instructions on how to setup a local instance of DynamoDB as well as a visual tool to interact with the database.

1. Install a local DynamoDB instance.
    - This can be anything but for the same of simplificty, we'll be using the [AWS-provided Java version](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html).
    - For those who have Docker installed, that will probably be easier.
    - Unzip the contents of the `zip` or `tar.gz` file into a folder called `tmp` in the repository root folder.
    - `unzip dynamodb_local_latest.zip -d tmp`
2. Start the local DynamoDB instance.
    - `java -Djava.library.path=./tmp/DynamoDBLocal_lib -jar ./tmp/DynamoDBLocal.jar -sharedDb` from the repository directory.
    - This will start the instance on port `8000`. Please read the AWS documentation for changing the port.
    - Congrats, you have a local DynamoDB instance!

**Optional**: If you wish to have a visual interface to interfact with DynamoDB, follow these steps!

[dynamodb-admin](https://github.com/aaronshaf/dynamodb-admin) is a Node.js based tool. You'll need to have Node.js and npm installed.
```
# For Windows:
set DYNAMO_ENDPOINT=http://localhost:8000
npx dynamodb-admin

# For Mac/Linux:
DYNAMO_ENDPOINT=http://localhost:8000 npx dynamodb-admin
```

Once the all of the above is setup, try playing around using the Python interrupter.
```
$ pipenv run python
Python 3.9.1 (default, Jan 20 2021, 00:00:00)
>>> from database import *
# let's create a document
u = DiscordUserModel(100)
# save the document
u.save()
```

