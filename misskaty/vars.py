import requests
import sys
from logging import getLogger
from os import environ

import dotenv

LOGGER = getLogger("MissKaty")

dotenv.load_dotenv("config.env", override=True)

if YT_COOKIES := environ.get("YT_COOKIES"):
    response = requests.get(YT_COOKIES)
    if response.status_code == 200:
        with open('cookies.txt', 'w') as file:
            file.write(response.text)
            LOGGER.info("Success download YT Cookies")
    else:
        LOGGER.info("Failed download YT Cookies")

if API_ID := environ.get("API_ID", "20457610"):
    API_ID = int(API_ID)
else:
    LOGGER.error("API_ID variable is missing! Exiting now")
    sys.exit(1)
API_HASH = environ.get("API_HASH", "b7de0dfecd19375d3f84dbedaeb92537")
if not API_HASH:
    LOGGER.error("API_HASH variable is missing! Exiting now")
    sys.exit(1)
BOT_TOKEN = environ.get("BOT_TOKEN", "7951809508:AAHjLuVJfgq_xJDgDMxxv_I1xyXWDjJRy6M")
if not BOT_TOKEN:
    LOGGER.error("BOT_TOKEN variable is missing! Exiting now")
    sys.exit(1)
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://hrx:nx@hnx.l8spp2n.mongodb.net/?retryWrites=true&w=majority&appName=hnx")
if not DATABASE_URI:
    LOGGER.error("DATABASE_URI variable is missing! Exiting now")
    sys.exit(1)
if LOG_CHANNEL := environ.get("LOG_CHANNEL", "-1002071541675"):
    LOG_CHANNEL = int(LOG_CHANNEL)

else:
    LOGGER.error("LOG_CHANNEL variable is missing! Exiting now")
    sys.exit(1)
# Optional ENV
LOG_GROUP_ID = environ.get("-1002071541675")
DATABASE_NAME = environ.get("DATABASE_NAME", "erza")
USER_SESSION = environ.get("BQE4KIoAusSpKkUDSCEj2z8Lf2ovqOHgEG_FdD32qejk4WGpf__NsJO3LJdHdCQzDa9eFqxQKDCuQtzgS9T_Wj3q8il9tUYEMGqMqBOlcyiS2o1B8HXeb7CX_xdzfxL-vNFpXqbcv3wpOPlQ62Q10lWfTDTW7XPWBWulEvogc2T8_RNQF9pYEwsdoy8XDsFzj_EO6irBIq7WyNu3n4v7jqP-HTS2KP5VEzbEY8L-ZkieDWNhgdlle5qXmm_2E1-UA77ZsoAgy6S_-pfrom49aOuQImhp090vfWTaIMxq5pLdYiojKjaskZqBA7Pxpc-c9DinqPE8xt-J4IYhsGU5QNzAzJ7hkgAAAAHZDnmkAA")
TZ = environ.get("TZ", "Asia/Jakarta")
PORT = environ.get("PORT", 80)
COMMAND_HANDLER = environ.get("COMMAND_HANDLER", "! /").split()
SUDO = list(
    {
        int(x)
        for x in environ.get(
            "SUDO",
            "6710921938",
        ).split()
    }
)
OWNER_ID = int(environ.get("OWNER_ID", 6710921938))
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "Soldier_071")
AUTO_RESTART = environ.get("AUTO_RESTART", False)
OPENAI_KEY = environ.get("OPENAI_KEY")
GOOGLEAI_KEY = environ.get("GOOGLEAI_KEY")
PAYDISINI_KEY = environ.get("PAYDISINI_KEY")
PAYDISINI_CHANNEL_ID = environ.get("PAYDISINI_CHANNEL_ID", "17")

## Config For AUtoForwarder
# Forward From Chat ID
FORWARD_FROM_CHAT_ID = list(
    {
        int(x)
        for x in environ.get(
            "FORWARD_FROM_CHAT_ID",
            "-1001128045651 -1001455886928 -1001686184174",
        ).split()
    }
)
# Forward To Chat ID
FORWARD_TO_CHAT_ID = list(
    {int(x) for x in environ.get("FORWARD_TO_CHAT_ID", "-1001210537567").split()}
)
FORWARD_FILTERS = list(set(environ.get("FORWARD_FILTERS", "video document").split()))
BLOCK_FILES_WITHOUT_EXTENSIONS = bool(
    environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", True)
)
BLOCKED_EXTENSIONS = list(
    set(
        environ.get(
            "BLOCKED_EXTENSIONS",
            "html htm json txt php gif png ink torrent url nfo xml xhtml jpg",
        ).split()
    )
)
MINIMUM_FILE_SIZE = environ.get("MINIMUM_FILE_SIZE")
CURRENCY_API = environ.get("CURRENCY_API")
