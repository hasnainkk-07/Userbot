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


# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team


#REMAKE BY NOBITA XD AND TRYTOLIVEALONE 



import random
from X import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import OWNER_ID as owner 

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = owner
    message = "A Pᴏᴡᴇʀғᴜʟ Assɪᴛᴀɴᴛ GOKU 𝐗 𝐔𝐒𝐄𝐑𝐁𝐎𝐓!!!!"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

logoX = [
    "https://files.catbox.moe/edeh8k.jpg"
]

alive_logo = random.choice(logoX)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "Hello, Mʏ Mᴀsᴛᴇʀ!!\nNice To Meet You 🤗 !!\nI guess, that you know me, Uhh you don't, np..\nWell.\n\nA Pᴏᴡᴇʀғᴜʟ Assɪᴛᴀɴᴛ \n\n Pᴏᴡᴇʀᴇᴅ Bʏ [Goku 𝐗 𝐔𝐒𝐄𝐑𝐁𝐎𝐓](t.me/xeno_kakarot)\n\nYᴏᴜ Cᴀɴ Cʜᴀᴛ Wɪᴛʜ Mʏ Mᴀsᴛᴇʀ Tʜʀᴏᴜɢʜ Tʜɪs Bᴏᴛ.\nIғ Yᴏᴜ Wᴀɴᴛ Yᴏᴜʀ Oᴡɴ Assɪᴛᴀɴᴛ Yᴏᴜ Cᴀɴ Dᴇᴘʟᴏʏ Fʀᴏᴍ Bᴜᴛᴛᴏɴ Bᴇʟᴏᴡ."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="https://t.me/lolpagalokigc"),
            InlineKeyboardButton("𝐂𝐡𝐚𝐧𝐧𝐞𝐥", url="https://t.me/Hindi_new_Animes"),
            InlineKeyboardButton("𝐎𝐰𝐧𝐞𝐫", url="https://t.me/xeno_kakarot"),
            InlineKeyboardButton("𝐑𝐞𝐩𝐨", url="https://github.com/Gokukhan1/userbot"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
