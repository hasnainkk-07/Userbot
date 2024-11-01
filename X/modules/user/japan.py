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

# CREDIT  : NOBITA XD AND TRYTOLIVEALONE
# Copyright (C) 2024 JAPANESE X USERBOT
#DON'T KANG FUCKING COWARD
#BSDKE KANG KIYA TOH SOCH LIYO
#AAG LAGA DUNGA TERE ANDAR 
#SAMJHA ? 




import json
from aiohttp.client_exceptions import ClientError
from pyrogram import filters, Client
from pyrogram.types import Message
from X.helpers.aiohttp_helper import AioHttp
from .help import *

cf_apii_data = {
    "japan": {
        "url": "https://expressional-leaper.000webhostapp.com/image.php?random-data",
        "help": "see my country's beauty !",
    }
}

texit_api_commands = []
for x in cf_apii_data:
    texit_api_commands.append(x)
    if "alts" in cf_apii_data[x]:
        for y in cf_apii_data[x]["alts"]:
            texit_api_commands.append(y)

@Client.on_message(filters.command(texit_api_commands, ".") & filters.me)
async def japan_api(bot: Client, message: Message):
    cmd = message.command
    api_key = cmd[0]
    api = cf_apii_data.get(api_key)

    if not api:
        await message.reply("Invalid command")
        return

    try:
        data = await AioHttp().get_json(api["url"])

        # Extract URL and Caption from the JSON response
        content_url = data.get('url', '').replace('\\', '')
        caption = data.get('caption', None)

        if not content_url:
            await message.reply("Failed to fetch content")
            return

        # Add your developer's name and link
        developer_info = "ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴍʏ [Dᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/lolpagalokigc)"

        # Combine facts from caption (if available), fetched caption, and developer info
        final_caption = f"ғᴀᴄᴛ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴜɴᴛʀʏ ✨\n\n{caption}\n\n{developer_info}" if caption else developer_info

        # don't try to take credit otherwise mai services and api dono banf karke bhag jaunga samjhe bsdk walo 
        await bot.send_photo(message.chat.id, content_url, caption=final_caption)
    except Exception as e:
        print(f"Error: {e}")
        await message.reply("An error occurred while processing the request")

    await message.delete()

for x in cf_apii_data:
    add_command_help(
        "•─╼⃝𖠁 Jᴀᴘᴀɴ",
        [
            [f"{x}", cf_apii_data[x]["help"]],
        ],
        )


