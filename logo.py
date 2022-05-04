from pyrogram import filters, Client
from pyrogram.types import Message
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

logo = Client("logo Bot", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)


caption = """
✍️ 𝐋𝐨𝐠𝐨 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐒𝐮𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 ✅
◇───────────────◇

🚀 **𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮** : **[𝐋𝐨𝐠𝐨 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐞 𝐁𝐨𝐭 🧑‍💻](https://t.me/LogoGeneratorRymBot)**

🌺 **𝙍𝙚𝙦𝙪𝙚𝙨𝙩𝙚𝙧** : ** {} **

🍀 **𝙋𝙤𝙬𝙚𝙧𝙙 𝘽𝙮**  : **[🔥 𝐑𝐲𝐦 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 🔥](https://t.me/RymOfficial)**
◇───────────────◇️  
    """
#◇───────────────────────────────────────◇ 

#◇───────────────────────────────────────◇ 

@logo.on_message(filters.command("start"))
async def start(client,message):
    await message.reply_chat_action("typing")
    await message.reply_photo(photo="https://telegra.ph/file/859bfec6a5ba66df9d64b.jpg", caption="🔐 𝙃𝙞 𝙞 𝘼𝙢 𝙍𝙮𝙢 𝙇𝙤𝙜𝙤 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧 𝘽𝙤𝙩 𝙁𝙤𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 \n𝘽𝙮 @RymOfficial 𝙖𝙣𝙙 @RymBots 𝘾𝙧𝙚𝙖𝙩𝙚𝙙 𝘽𝙮 @TumaraBaap...\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨 - /logo, /logohq, /wall, /write")


#◇───────────────────────────────────────◇ 

@logo.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/logo?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 𝐎𝐩𝐞𝐧 𝐈𝐧 𝐆𝐨𝐨𝐠𝐥𝐞 🍀", url=f"{photo}"
                    ),
                    InlineKeyboardButton(
                        "🍀 𝐉𝐨𝐢𝐧 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🍀", url="https://t.me/RymOfficial"
                    )
                ]
            ]
          ),
    )

#◇────────────────────────────────────◇ 
  
@logo.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/logohq?name={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 𝐎𝐩𝐞𝐧 𝐈𝐧 𝐆𝐨𝐨𝐠𝐥𝐞 🍀", url=f"{photo}"
                    ),
                    InlineKeyboardButton(
                        "🍀 𝐉𝐨𝐢𝐧 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🍀", url="https://t.me/RymOfficial"
                    )
                ]
            ]
          ),
    )

#◇──────────────────────────────────────◇ 


@logo.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/wallpaper?search={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 𝐎𝐩𝐞𝐧 𝐈𝐧 𝐆𝐨𝐨𝐠𝐥𝐞 🍀", url=f"{photo}"
                    ),
                    InlineKeyboardButton(
                        "🍀 𝐉𝐨𝐢𝐧 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🍀", url="https://t.me/RymOfficial"
                    )
                ]
            ]
          ),
    )

#◇──────────────────────────────────────◇ 


@logo.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"http://single-developers.up.railway.app/write?write={text}").history[1].url
    await message.reply_chat_action("upload_photo")
    await logo.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🍀 𝐎𝐩𝐞𝐧 𝐈𝐧 𝐆𝐨𝐨𝐠𝐥𝐞 🍀", url=f"{photo}"
                    ),
                    InlineKeyboardButton(
                        "🍀 𝐉𝐨𝐢𝐧 𝐎𝐟𝐟𝐢𝐜𝐢𝐚𝐥 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 🍀", url="https://t.me/RymOfficial"
                    )
                ]
            ]
          ),
    )


logo.run()

app.start()
LOGGER.info("© @TumaraBaap")
idle()
