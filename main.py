from pyrogram import Client, filters

API_ID = "14516015"
API_HASH = "61653dd713fdb95f10de8f4bf6407b30"
BOT_TOKEN = "5728995132:AAG_LI2dmHUvPtX1SyATgEfp9-mx32oP8iQ"

NAGEHX = Client(
  name="PyrogramBot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

print("Bot Started")

NAGEHX.run()
