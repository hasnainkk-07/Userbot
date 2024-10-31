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


#REMAKE BY : NOBITA XD AND TRYTOLIVEALONE
#DON'T KANG FUCKING COWARD
#BSDKE KANG KIYA TOH SOCH LIYO
#AAG LAGA DUNGA TERE ANDAR 
#SAMJHA ? 


import asyncio
import os
import time
from platform import python_version

from pyrogram import Client
from pyrogram import __version__ as versipyro
from pyrogram import filters
from pyrogram.types import Message
from telegraph import exceptions, upload_file

from config import BOT_VER, CHANNEL
from config import CMD_HANDLER
from config import SUDO_USERS
from config import GROUP, OWNER_ID
from X import CMD_HELP, StartTime
from X.helpers.basic import edit_or_reply
from X.helpers.PyroHelpers import ReplyCheck
from X.helpers.SQL.globals import gvarstatus
from X.helpers.tools import convert_to_image
from X.utils import get_readable_time
from X.utils.misc import restart

from .help import *

modules = CMD_HELP
alivemodules = CMD_HELP
alive_logo = (
    gvarstatus("ALIVE_LOGO") or ""
)
emoji = gvarstatus("ALIVE_EMOJI") or "✧"
alive_text = gvarstatus("ALIVE_TEKS_CUSTOM") or "✧✧ Goku-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 ✧✧"


@Client.on_message(
    filters.command(["alive"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def alip(client: Client, message: Message):
    X = await edit_or_reply(message, "🌸")
    await asyncio.sleep(2)
    sad = client.send_video if alive_logo.endswith(".mp4") else client.send_photo
    uptime = await get_readable_time((time.time() - StartTime))
    man = (
        f"<b>{alive_text}</b>\n\n"
        f"<b>•─╼⃝𖠁 𝐒ʏꜱᴛᴇ𝐌 𝐒ᴛᴀᴛᴜ𝐒 </b>\n\n"
        f"{emoji} <b>𝐌ʏ 𝐌ᴀꜱᴛᴇ𝐑:</b> [{client.me.mention}](tg://user?id={OWNER_ID}) \n\n"
        f"{emoji} <b>𝐏ʏʀᴏɢʀᴀ𝐌 𝐕ᴇʀꜱɪᴏ𝐍:</b> <code>{versipyro}</code>\n\n"
        f"{emoji} <b>𝐁ᴏᴛ 𝐔ᴘᴛɪᴍ𝐄:</b> <code>{uptime}</code> \n\n"
        f"{emoji} <b>𝐕ᴇʀꜱɪᴏ𝐍:</b> <code>{BOT_VER}</code> \n\n"
        f"{emoji} <b>𝐌ᴏᴅᴜʟᴇ𝐒:</b> <code>{len(modules)} 𝐌ᴏᴅᴜʟᴇ𝐒</code> \n\n"
        f"{emoji} <b>𝐏ʏᴛʜᴏ𝐍 𝐕ᴇʀꜱɪᴏ𝐍:</b> <code>{python_version()}</code> \n\n"
        f"{emoji} <b>𝐆ʀᴏᴜ𝐏 :</b> [𝐒ᴜᴘᴘᴏʀ𝐓](https://t.me/lolpagalokigc)** \n\n"
        f"{emoji} <b>𝐂ʜᴀɴɴᴇʟ:<b> [𝐔ᴘᴅᴀᴛᴇ𝐒](https://t.me/mlohvdryj)** \n\n"
        f"{emoji} <b>[𝐃ᴇᴘʟᴏʏ](http://dashboard.heroku.com/new?template=https://github.com/Gokukhan1/userbot) 𝐘ᴏᴜʀ 𝐎ᴡɴ [Goku-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓](http://github.com/Gokukhan1/userbot) ✧\n\n"
        
    )
    try:
      await sad(
                message.chat.id,
                alive_logo,
                caption=man,
                reply_to_message_id=ReplyCheck(message),
            )
      await X.delete()
    except:
      await X.edit(man, disable_web_page_preview=True)


@Client.on_message(
    filters.command(["setalivepic"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def setalivelogo(client: Client, message: Message):
    try:
        import X.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    X = await edit_or_reply(message, "`Processing...`")
    link = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await X.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        link = f"https://telegra.ph/{media_url[0]}"
        os.remove(m_d)
    sql.addgvar("ALIVE_LOGO", link)
    await X.edit(
        f"**Successfully Customized ALIVE LOGO Become {link}**",
        disable_web_page_preview=True,
    )
    restart()


@Client.on_message(
    filters.command(["setalivetext"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def setalivetext(client: Client, message: Message):
    try:
        import X.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    X = await edit_or_reply(message, "`Processing...`")
    if not text:
        return await edit_or_reply(
            message, "**Give a text or reply to a text**"
        )
    sql.addgvar("ALIVE_TEKS_CUSTOM", text)
    await X.edit(f"**Successfully Customized ALIVE TEXT Become** `{text}`")
    restart()


@Client.on_message(
    filters.command(["setaliveemoji"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def setemoji(client: Client, message: Message):
    try:
        import X.helpers.SQL.globals as sql
    except AttributeError:
        await message.edit("**Running on Non-SQL mode!**")
        return
    emoji = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    X = await edit_or_reply(message, "`Processing...`")
    if not emoji:
        return await edit_or_reply(message, "**Give A Emoji**")
    sql.addgvar("ALIVE_EMOJI", emoji)
    await X.edit(f"**Successfully Customize ALIVE EMOJI Becomes** {emoji}")
    restart()
