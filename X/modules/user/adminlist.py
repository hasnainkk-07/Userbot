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



import html

from pyrogram import Client, enums, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply
from X.helpers.parser import mention_html, mention_markdown
from .help import *


@Client.on_message(
    filters.command(["admins"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def adminlist(client: Client, message: Message):
    replyid = None
    toolong = False
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.id
    creator = []
    admin = []
    badmin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        try:
            name = a.user.first_name + " " + a.user.last_name
        except:
            name = a.user.first_name
        if name is None:
            name = "☠️ 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭"
        if a.status == enums.ChatMemberStatus.ADMINISTRATOR:
            if a.user.is_bot:
                badmin.append(mention_markdown(a.user.id, name))
            else:
                admin.append(mention_markdown(a.user.id, name))
        elif a.status == enums.ChatMemberStatus.OWNER:
            creator.append(mention_markdown(a.user.id, name))
    admin.sort()
    badmin.sort()
    totaladmins = len(creator) + len(admin) + len(badmin)
    teks = "**Admins in {}**\n".format(grup.title)
    teks += "╒═══「 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 」\n"
    for x in creator:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╞══「 {} 𝐇𝐮𝐦𝐚𝐧 𝐀𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐭𝐨𝐫 」\n".format(len(admin))
    for x in admin:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╞══「 {} 𝐁𝐨𝐭 𝐀𝐝𝐦𝐢𝐧𝐢𝐬𝐭𝐫𝐚𝐭𝐨𝐫 」\n".format(len(badmin))
    for x in badmin:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╘══「 𝐓𝐨𝐭𝐚𝐥 {} 𝐀𝐝𝐦𝐢𝐧𝐬 」".format(totaladmins)
    if toolong:
        await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)


@Client.on_message(
    filters.command(["zombies"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def kickdel_cmd(client: Client, message: Message):
    Man = await edit_or_reply(message, "<b>𝐊𝐢𝐜𝐤𝐢𝐧𝐠 𝐝𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭𝐬...</b>")
    # noinspection PyTypeChecker
    values = [
        await message.chat.ban_member(user.user.id, int(time()) + 31)
        for member in await message.chat.get_members()
        if member.user.is_deleted
    ]
    await Man.edit(f"<b>𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐤𝐢𝐜𝐤𝐞𝐝 {len(values)} 𝐝𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭(s)</b>")


@Client.on_message(
    filters.command(["report"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def report_admin(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = None
    grup = await client.get_chat(message.chat.id)
    admin = []
    async for a in client.get_chat_members(
        message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS
    ):
        if (
            a.status == enums.ChatMemberStatus.ADMINISTRATOR
            or a.status == enums.ChatMemberStatus.OWNER
        ):
            if not a.user.is_bot:
                admin.append(mention_html(a.user.id, "\u200b"))
    if message.reply_to_message:
        if text:
            teks = "{}".format(text)
        else:
            teks = "{} reported to admins.".format(
                mention_html(
                    message.reply_to_message.from_user.id,
                    message.reply_to_message.from_user.first_name,
                )
            )
    else:
        if text:
            teks = "{}".format(html.escape(text))
        else:
            teks = "𝐂𝐚𝐥𝐥𝐢𝐧𝐠 𝐚𝐝𝐦𝐢𝐧𝐬 𝐢𝐧 {}.".format(grup.title)
    teks += "".join(admin)
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            teks,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, teks, parse_mode=enums.ParseMode.HTML
        )


@Client.on_message(
    filters.command(["tagall"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def tag_all_users(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = "𝐇𝐞𝐥𝐥𝐨 every one 😊"
    kek = client.get_chat_members(message.chat.id)
    async for a in kek:
        if not a.user.is_bot:
            text += mention_html(a.user.id, "\u200b")
    if message.reply_to_message:
        await client.send_message(
            message.chat.id,
            text,
            reply_to_message_id=message.reply_to_message.id,
            parse_mode=enums.ParseMode.HTML,
        )
    else:
        await client.send_message(
            message.chat.id, text, parse_mode=enums.ParseMode.HTML
        )


@Client.on_message(
    filters.command(["bots"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def get_list_bots(client: Client, message: Message):
    replyid = None
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.id
    getbots = client.get_chat_members(chat)
    bots = []
    async for a in getbots:
        try:
            name = a.user.first_name + " " + a.user.last_name
        except:
            name = a.user.first_name
        if name is None:
            name = "☠️ 𝐃𝐞𝐥𝐞𝐭𝐞𝐝 𝐚𝐜𝐜𝐨𝐮𝐧𝐭"
        if a.user.is_bot:
            bots.append(mention_markdown(a.user.id, name))
    teks = "**𝐀𝐥𝐥 𝐛𝐨𝐭𝐬 𝐢𝐧 𝐠𝐫𝐨𝐮𝐩 {}**\n".format(grup.title)
    teks += "╒═══「 𝐁𝐨𝐭𝐬 」\n"
    for x in bots:
        teks += "│ • {}\n".format(x)
    teks += "╘══「 𝐓𝐨𝐭𝐚𝐥 {} 𝐁𝐨𝐭𝐬 」".format(len(bots))
    if replyid:
        await client.send_message(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)


add_command_help(
    "•─╼⃝𖠁 ᴛᴀɢ",
    [
        [f"{cmd}admins", "Gᴇᴛ Cʜᴀᴛꜱ ᴀᴅᴍɪɴ ʟɪꜱᴛ ."],
        [f"{cmd}zombies", "Tᴏ ᴋɪᴄᴋ ᴅᴇʟᴇᴛᴇᴅ Aᴄᴄᴏᴜɴᴛ ."],
        [
            f"{cmd}everyone `or` {cmd}tagall",
            "Tᴏ ᴍᴇɴᴛɪᴏɴ ᴇᴠᴇʀʏᴏɴᴇ",
        ],
        [
            f"{cmd}bots",
            "ᴛᴏ ɢᴇᴛ ᴄʜᴀᴛꜱ ʙᴏᴛ ʟɪꜱᴛ",
        ],
    ],
) 
