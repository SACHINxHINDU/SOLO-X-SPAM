## Copy Paster Must Give Credit...
## @JARVIS_V2

import logging
from telethon import TelegramClient
from os import getenv
from JARVIS.data import FRIDAY

# Set up logging configuration
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Constants required for JARVIS bots
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
#HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "solo-x-spammmm")
#HEROKU_API_KEY = getenv("HEROKU_API_KEY", "91f976ce-9ba3-4b3a-8e69-b8eb5c3a64e8")
BOT_TOKEN = getenv("BOT_TOKEN", default="7439140731:AAHk4e5ZmzdPiRt3LJ5p7rUt1nD2xwbF2UQ")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://SachinSanatani:SACHINxSANATANI@sanatani.bnmsfbd.mongodb.net/?retryWrites=true&w=majority&appName=Sanatani")
MONGO_DB_NAME = getenv("MONGO_DB_NAME", "SACHINxSANATANI")

CLONE_MODE = getenv("CLONE_MODE", True) # Set True or False
CLONE_MONGO_DB_URI = getenv("CLONE_MONGO_DB_URI", "mongodb+srv://SachinSanatani:SACHINxSANATANI@sanatani.bnmsfbd.mongodb.net/?retryWrites=true&w=majority&appName=Sanatani")
CLONE_MONGO_DB_NAME = getenv("CLONE_MONGO_DB_URI", "SACHINxSANATANI")

# Set up sudo users
SUDO_USERS = list(map(int, getenv("SUDO_USERS", default="5959548791").split()))
SUDO_USERS.extend(FRIDAY)

OWNER_ID = int(getenv("OWNER_ID", default="5959548791"))
SUDO_USERS.append(OWNER_ID)

# Initialize Telegram client
X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
