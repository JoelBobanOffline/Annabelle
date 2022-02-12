from userbot import Annabelle
from pyrogram import filters as vrn
from pyrogram.types import ChatPermissions
from config import HANDLER

import logging
logging = logging.getLogger(__name__)

@Annabelle.on_message(vrn.command('mute', HANDLER) & vrn.group & vrn.outgoing)
async def mute(Annabelle, message):
  mem = await Annabelle.get_chat_member(message.chat.id, message.from_user.id)
  if mem.status in ['administrator', 'creator']:
    if message.reply_to_message:
      await message.edit('muting...')
      args = message.text.split(None, 1)
      if len(args) >= 2:
        reason = args[1]
      else:
        reason = ''
      try:
        await Annabelle.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions())
        await message.edit(MUTE.TXT.format(message.reply_to_message.from_user.mention, message.chat.title, reason))
      except Exception as e:
        await message.edit("`Failed to mute that user! Check app logs for more..`")
        print(e)
    else:
      await message.edit("`Whom to mute dude? Reply to the message of the user to mute`")
  else:
    await message.edit("`We are not admin here to do that!`")
