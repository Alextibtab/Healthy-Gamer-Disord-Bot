import os

import interactions
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = interactions.Client(token=TOKEN)

@client.event
async def on_ready():
    print(f'Client has connected to Discord!')


client.start()