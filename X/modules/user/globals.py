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



from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message

from config import CMD_HANDLER
from config import SUDO_USERS
from X import *
from X.helpers.adminHelpers import DEVS, WHITELIST
from X.helpers.basic import edit_or_reply
from X.helpers.PyroHelpers import get_ub_chats
from X.utils import extract_user, extract_user_and_reason

from .help import *


def globals_init():
    try:
        global sql, sql2
        from importlib import import_module

        sql = import_module("X.helpers.SQL.gban_sql")
        sql2 = import_module("X.helpers.SQL.gmute_sql")
    except Exception as e:
        sql = None
        sql2 = None
        LOGS.warn("Unable to run GBan and GMute command, no SQL connection found")
        raise e


globals_init()


@Client.on_message(
    filters.command("menghilang", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(
    filters.command(["gban"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def gban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        X = await message.reply("`Gbanning...`")
    else:
        X = await message.edit("`Gbanning....`")
    if not user_id:
        return await X.edit("Who do you want to ban? Come on!!!!.")
    if user_id == client.me.id:
        return await X.edit("**Why Ban Yourself? Pepek**")
    if user_id in DEVS:
        return await X.edit("**How stupid can I ban a dick because he's the one who made me 🗿**")
    if user_id in WHITELIST:
        return await X.edit(
            "**You can't fuck him because he's an devil @xeno_kakarot 😡**"
        )
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await X.edit("`Please specify a valid user!`")

    if sql.is_gbanned(user.id):
        return await X.edit(
            f"[Jamet](tg://user?id={user.id}) **This is already on the gbanned list**"
        )
    f_chats = await get_ub_chats(client)
    if not f_chats:
        return await X.edit("**You don't have a GC that you admin 🥺**")
    er = 0
    done = 0
    for gokid in f_chats:
        try:
            await client.ban_chat_member(chat_id=gokid, user_id=int(user.id))
            done += 1
        except BaseException:
            er += 1
    sql.gban(user.id)
    msg = (
        r"**\\#GBanned_User//**"
        f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    msg += f"\n**Affected To:** `{done}` **Chats**"
    await X.edit(msg)


@Client.on_message(
    filters.command("cungban", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(
    filters.command(["ungban"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def ungban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        X = await message.reply("`UnGbanning...`")
    else:
        X = await message.edit("`UnGbanning....`")
    if not user_id:
        return await X.edit("I can't find that user.")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await X.edit("`Please specify a valid user!`")

    try:
        if user.id not in DEVS:
            await X.edit("Processing..")
            if not sql.is_gbanned(user.id):
                return await X.edit("`User already ungban`")
        ung_chats = await get_ub_chats(client)
        if not ung_chats:
            return await X.edit("**You don't have a GC that you admin 🥺**")
        er = 0
        done = 0
        for good_boi in ung_chats:
            try:
                await client.unban_chat_member(chat_id=good_boi, user_id=user.id)
                done += 1
            except BaseException:
                er += 1
        sql.ungban(user.id)
        msg = (
            r"**\\#UnGbanned_User//**"
            f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
            f"\n**User ID:** `{user.id}`"
        )
        if reason:
            msg += f"\n**Reason:** `{reason}`"
        msg += f"\n**Affected To:** `{done}` **Chats**"
        await X.edit(msg)
    except Exception as e:
        await X.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(
    filters.command(["listgban"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def gbanlist(client: Client, message: Message):
    users = sql.gbanned_users()
    Kazu = await edit_or_reply(message, "`Processing...`")
    if not users:
        return await X.edit("No User Has Been Banned Yet")
    gban_list = "**GBanned Users:**\n"
    count = 0
    for i in users:
        count += 1
        gban_list += f"**{count} -** `{i.sender}`\n"
    return await X.edit(gban_list)


@Client.on_message(
    filters.command(["gmute"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    X = await edit_or_reply(message, "`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await X.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await X.edit(f"`Please specify a valid user!`")
        return
    if user.id == client.me.id:
        return await X.edit("**Why mute yourself Pepek**")
    if user.id in DEVS:
        return await X.edit("**I can't mute my dick because he made me 🗿**")
    if user.id in WHITELIST:
        return await X.edit(
            "**Where Can Dogs Gmute Admin @xeno_kakarot 😡**"
        )
    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await X.edit("`Calm down anybob, you can't gmute yourself.`")
    except BaseException:
        pass

    try:
        if sql2.is_gmuted(user.id):
            return await X.edit("`User already gmuted`")
        sql2.gmute(user.id)
        await X.edit(f"[{user.first_name}](tg://user?id={user.id}) globally gmuted!")
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.restrict_member(user.id, ChatPermissions())
        except BaseException:
            pass
    except Exception as e:
        await X.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(
    filters.command(["ungmute"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def ungmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    X = await edit_or_reply(message, "`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await X.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await X.edit(f"`Please specify a valid user!`")
        return

    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await Man.edit("`Calm down anybob, you can't ungmute yourself.`")
    except BaseException:
        pass

    try:
        if not sql2.is_gmuted(user.id):
            return await X.edit("`User already ungmuted`")
        sql2.ungmute(user.id)
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.unban_member(user.id)
        except BaseException:
            pass
        await X.edit(
            f"[{user.first_name}](tg://user?id={user.id}) globally ungmuted!"
        )
    except Exception as e:
        await X.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(
    filters.command(["listgmute"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def gmutelist(client: Client, message: Message):
    users = sql2.gmuted_users()
    X = await edit_or_reply(message, "`Processing...`")
    if not users:
        return await X.edit("No Hair Has Been Muted Yet")
    gmute_list = "**GMuted Users:**\n"
    count = 0
    for i in users:
        count += 1
        gmute_list += f"**{count} -** `{i.sender}`\n"
    return await X.edit(gmute_list)


@Client.on_message(filters.incoming & filters.group)
async def globals_check(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id:
        return
    if sql.is_gbanned(user_id):
        try:
            await client.ban_chat_member(chat_id, user_id)
        except BaseException:
            pass

    if sql2.is_gmuted(user_id):
        try:
            await message.delete()
        except errors.RPCError:
            pass
        try:
            await client.restrict_chat_member(chat_id, user_id, ChatPermissions())
        except BaseException:
            pass

    message.continue_propagation()


add_command_help(
    "•─╼⃝𖠁 ɢʟᴏʙᴀʟꜱ",
    [
        [
            "gban <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>",
            "Gʟᴏʙᴀʟʟʏ Bᴀɴɴᴇᴅ Aʟʟ Gʀᴏᴜᴘꜱ Wʜᴇʀᴇ Yᴏᴜ Aʀᴇ Aᴅᴍɪɴ.",
        ],
        ["ungban <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Cᴀɴᴄᴇʟ Gʟᴏʙᴀʟ Bᴀɴɴᴇᴅ."],
        ["listgban", "Dɪꜱᴘʟᴀʏꜱ ᴛʜᴇ Gʟᴏʙᴀʟ Bᴀɴɴᴇᴅ Lɪꜱᴛ."],
    ],
     )
