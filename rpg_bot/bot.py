import os

import interactions
from dotenv import load_dotenv

from .rpg.game import Game

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = int(os.getenv("GUILD_ID"))

client = interactions.Client(token=TOKEN)
game = Game()


@client.event
async def on_ready():
    print(f"Client has connected to Discord!")


@client.command(name="getstats", description="Get your player stats", scope=GUILD)
async def get_stats(ctx: interactions.CommandContext):
    player = game.get_player(ctx.member.id)
    await ctx.send(
        f"""{ctx.member.name} your stats are:
  
        Level: {player.get_level()}
        XP: {player.get_xp()}
        Attack: {player.get_attack()}
        Max HP: {player.get_max_hp()}
        Current HP: {player.current_hp}"""
    )


@client.command(name="attack", description="Battle a monster", scope=GUILD)
async def attack(ctx: interactions.CommandContext):
    result = game.encounter_action(ctx.member.id)
    await ctx.send(result)


@client.command(name="run", description="Run from a battle", scope=GUILD)
async def run(ctx: interactions.CommandContext):
    result = game.end_encounter(ctx.member.id)
    await ctx.send(result)


def start_bot():
    client.start()
