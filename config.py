## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "BQC0TJjR50U4in4eQmSHk2a7D5YDeYEdzuOZ5P4ae0DLzCOlNI7lWa6QMAIcTSxVlESJrKiT_fU7r5L1t5YeEmsvCM7XklQzdgNE_9hI1pNWm1te9OIXtpIgP9T-n7Fq71hU8y3IJORaB9DmZ-AmGlWS4gDY3BC4mGZZHq3lxXlEmvS1W2FB2vNob4nwj9ESqCgFE-oSYpoeA96X8VZ_bQHWrhUQkhsZDu_x2_jOrY1xmtDDNj5xAIPjiCEwysYpeYG9oZuZXGIbUJ8r3LCHa1RIb6lKINYGlWa_KRSvOObacu_vT7eG6FusjAQyWbvwvVQvJ2ajwZWFl2P7_b6l4LSxAAAAAUKVUL0A")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5430611324:AAGRuWb8BxK9Q_fWh5gQAwY0ZUsmhDc8AIY")
BOT_NAME = getenv("BOT_NAME", "˹ᴄᴀᴛ ✘ ᴍᴜsɪᴄ˼")

API_ID = int(getenv("API_ID", "26505340"))
API_HASH = getenv("API_HASH", "2c687333637c38602329de84aeb64baf")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://anon:anon@cluster0.7qv0pzk.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Opet")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Juliiannnnn")
ALIVE_NAME = getenv("ALIVE_NAME", "sal")
BOT_USERNAME = getenv("BOT_USERNAME", "kucinggtapibot")
OWNER_ID = getenv("OWNER_ID", "2061280554")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "˹ᴄᴀᴛ ꭙ ᴀssɪsᴛᴀɴᴛ˼")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "satpamhoeng")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "windtalkerr")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2061280554").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/55cbfea5917b66b686194.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
