import os
import sys
import time
from telethon import TelegramClient, events, utils

botName = ''

# https://my.telegram.org/apps
api_id = 00000
api_hash = ''

session = os.environ.get('TG_SESSION', 'printer')
proxy = None

client = TelegramClient(session, api_id, api_hash, proxy=proxy).start()

@client.on(events.NewMessage())
async def handler(event):
  sender = await event.get_sender()
  name = utils.get_display_name(sender)
  if(name == botName):
    print(name, ' ', event.text)
    cmd = 1
    execute(cmd)

try:
    print('Server running')
    print('Ctrl+C to stop')
    client.run_until_disconnected()
finally:
    client.disconnect()

def execute(cmd):
  # ...
  pass