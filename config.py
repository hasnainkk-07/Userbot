#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os
from distutils.util import strtobool
from XDB.data import MASTERS
from os import getenv
from X.helpers.cmd import cmd
from dotenv import load_dotenv

load_dotenv("config.env")

ALIVE_EMOJI = getenv("ALIVE_EMOJI", "😘")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://files.catbox.moe/noj77k.jpg")
PM_PIC = getenv("PM_PIC", "https://files.catbox.moe/sq0gsn.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = getenv("API_HASH", "f8f993acb1d5f51c950ba873404d9af5")
API_ID = getenv("API_ID", "22731333")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "4.0.0@main"
BRANCH = getenv("BRANCH", "main") #don't change this line 
CMD_HNDLR = cmd
BOT_TOKEN = getenv("BOT_TOKEN", "none")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
CHANNEL = getenv("CHANNEL", "Hindi_new_Animes")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "lolpagalokigc")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/Gokukhan1/userbot")
MONGO_URL = getenv("MONGO_URL", "")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDOS = os.getenv("SUDO_USERS", None)
SUDO_USERS = []

if SUDOS:
    sudos = str(SUDOS).split(" ")
    for sudo_id in sudos:
        try:
            SUDO_USERS.append(int(sudo_id))
        except ValueError:
            print(f"Warning: Invalid user ID '{sudo_id}' in SUDO_USERS environment variable.")
            continue
            
OWNER_ID = os.getenv("OWNER_ID", "")

SUDO_USERS.append(OWNER_ID)
SUDO_USERS.extend(MASTERS)

BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001608701614, -1001675459127, -1001473548283, -1001608701614]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
