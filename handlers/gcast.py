import asyncio
import regex
from pyrogram import Client, filters
from pyrogram.types import Message

from pyrogram.types import Dialog
from pyrogram.types import Chat
from aiohttp import ClientSession
from config import SUDO_USERS, BOT_TOKEN
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as USER
from config import SUDO_USERS

@client.on_message(
    filters.command("broadcast")
    & filters.user(SUDO_USERS)
    & ~filters.edited
)
@capture_err
async def broadcast_message(_, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "**Usage**:\n/broadcast [MESSAGE]"
        )
    sleep_time = 0.1
    text = message.text.split(None, 1)[1]
    sent = 0
    schats = await get_served_chats()
    chats = [int(chat["chat_id"]) for chat in schats]
    m = await message.reply_text(
        f"Broadcast in progress, will take {len(chats) * sleep_time} seconds."
    )
    for i in chats:
        try:
            await app.send_message(i, text=text)
            await asyncio.sleep(sleep_time)
            sent += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await m.edit(f"**Broadcasted Message In {sent} Chats.**")
