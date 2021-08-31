import asyncio
import os
import subprocess
import time

from telethon import events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights

import psutil
from pyrogram import filters
from pyrogram import Client
from pyrogram.errors import FloodWait
from config import SUDO_USERS

@Client.on_message(
    filters.command("gcast")
    & filters.user(SUDO_USERS)
    & ~filters.edited
)
async def gcast(event):
    
    to_send = update.effective_message.text.split(None, 1)
    if len(to_send) >= 2:
        chats = sql.get_all_chats() or []
        failed = 0
        for chat in chats:
            try:
                bot.sendMessage(int(chat.chat_id), to_send[1])
                sleep(0.1)
            except TelegramError:
                failed += 1
                LOGGER.warning("Couldn't send broadcast to %s, group name %s", str(chat.chat_id), str(chat.chat_name))

        update.effective_message.reply_text("Broadcast complete. {} groups failed to receive the message, probably "
