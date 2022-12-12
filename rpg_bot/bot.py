import os

import interactions
from pymongo import MongoClient
from dotenv import load_dotenv

from .rpg.game import Game

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = int(os.getenv("GUILD_ID"))

client = interactions.Client(token=TOKEN)

db_client = MongoClient(os.getenv("MONGO_URI"))
game = Game(db_client)

@client.event
async def on_ready():
    print(f"Client has connected to Discord!")


@client.command(name="stats", description="Get your player stats", scope=GUILD)
async def stats(ctx: interactions.CommandContext):
    player = game.get_player(ctx.member.id)
    await ctx.send(
        f"""{ctx.member.name} your stats are:
  
        Level: {player.get_level()}
        XP: {player.get_xp()}
        Attack: {player.get_attack()}
        Max HP: {player.get_max_hp()}
        Current HP: {player.current_hp}"""
    )


@client.command(name="fight", description="Battle a monster", scope=GUILD)
async def fight(ctx: interactions.CommandContext):
    result = game.encounter_action(ctx.member.id)
    await ctx.send(result)


@client.command(name="flee", description="Run from a battle", scope=GUILD)
async def flee(ctx: interactions.CommandContext):
    result = game.end_encounter(ctx.member.id)
    await ctx.send(result)


# reset player data
@client.command(name="reset", description="Reset your player data", scope=GUILD)
async def reset(ctx: interactions.CommandContext):
    result = game.reset_player(ctx.member.id)
    await ctx.send(result)


def start_bot():
    client.start()
