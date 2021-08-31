from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""Cᴏᴍᴍᴀɴᴅs ᴏғ 𝗠𝗿 𝗗 𝗘 𝗩 𝗶 𝗟🕊️⃝🦋</ 𝗣 𝗥 𝗶 𝗡 𝗖 𝗘 [ 🇮🇳 ] Vᴄ Bᴏᴛ 🔥🛠
**For all in group**

- `/play <song name> - play song you requested 
- `/song <song name> - download songs you want quickly

 
** Admin only**🔥😏

- `/pause - pause song play
- `/resume - resume song play
- `/skip - play the next song
- `/end - end song""")

