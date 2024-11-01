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

# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

#REMAKE BY NOBITA XD AND TRYTOLIVEALONE



import sys
from os import environ, execle, remove

from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS

from config import CMD_HANDLER
from X import BOTLOG_CHATID, LOGGER
from X.helpers.adminHelpers import DEVS
from X.helpers.basic import edit_or_reply

from .help import *

HAPP = None


@Client.on_message(filters.command("restc", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("restart", cmd) & filters.me)
@Client.on_message(
    filters.command(["restart"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def restart_bot(_, message: Message):
    try:
        msg = await edit_or_reply(message, "`Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ Bot has restarted !\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "X"]
        execle(sys.executable, *args, environ)


@Client.on_message(filters.command("shutdown", cmd) & filters.me)
@Client.on_message(
    filters.command(["shutdown"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def shutdown_bot(client: Client, message: Message):
    if BOTLOG_CHATID:
        await client.send_message(
            BOTLOG_CHATID,
            "**#SHUTDOWN** \n"
            "**GOKU X USERBOT** has been turned off!\If you want to turn it back on, please open it heroku",
        )
    await edit_or_reply(message, "**GOKU X USERBOT Successfully turned it off!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@Client.on_message(filters.command("logs", cmd) & filters.me)
@Client.on_message(
    filters.command(["logs"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def logs_ubot(client: Client, message: Message):
    if HAPP is None:
        return await edit_or_reply(
            message,
            "Make sure `HEROKU_API_KEY` and `HEROKU_APP_NAME` you are configured correctly in config vars heroku",
        )
    Man = await edit_or_reply(message, "**Currently Taking Logs Heroku**")
    with open("Logs-Heroku.txt", "w") as log:
        log.write(HAPP.get_log())
    await client.send_document(
        message.chat.id,
        "Logs-Heroku.txt",
        thumb="X/resources/logo.jpg",
        caption="**This is your Heroku Logs**",
    )
    await Man.delete()
    remove("Logs-Heroku.txt")


add_command_help(
    "•─╼⃝𖠁 ꜱʏꜱᴛᴇᴍ",
    [
        ["restart", "Tᴏ ʀᴇꜱᴛᴀʀᴛ ᴜꜱᴇʀʙᴏᴛ."],
        ["shutdown", "Tᴏ ᴛᴜʀɴ ᴏғғ ᴜꜱᴇʀʙᴏᴛ."],
        ["logs", "Tᴏ ꜱᴇᴇ ʟᴏɢꜱ ᴜꜱᴇʀʙᴏᴛ."],
    ],
) 
