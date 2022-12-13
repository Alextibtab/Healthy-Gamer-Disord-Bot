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
    player = game.get_player(str(ctx.member.id))
    player.current_hp
    stats_embed = interactions.Embed(
        title="Character Stats:",
        description=f"<@{ctx.member.id}> your stats are:",
        color=0xCD2323,
        fields=[
            interactions.EmbedField(
                name="Level", value=player.get_level(), inline=True
            ),
            interactions.EmbedField(
                name="XP 🟢", value=player.get_xp(), inline=True
            ),

            interactions.EmbedField(
                name="Max HP", value=player.get_max_hp(), inline=True
            ),
            interactions.EmbedField(
                name="Current HP ❤️", value=player.current_hp, inline=True
            ),
            interactions.EmbedField(
                name="Attack 🗡️", value=player.get_attack(), inline=False
            ),
        ],
        footer=interactions.EmbedFooter(text="RPG Bot"),
    )
    await ctx.send(embeds=stats_embed)


@client.command(name="fight", description="Battle a monster", scope=GUILD)
async def fight(ctx: interactions.CommandContext):
    result = game.encounter_action(str(ctx.member.id))
    await ctx.send(result)


@client.command(name="flee", description="Run from a battle", scope=GUILD)
async def flee(ctx: interactions.CommandContext):
    result = game.end_encounter(str(ctx.member.id))
    await ctx.send(result)


# reset player data
@client.command(name="reset", description="Reset your player data", scope=GUILD)
async def reset(ctx: interactions.CommandContext):
    result = game.reset_player(str(ctx.member.id))
    await ctx.send(result)


def start_bot():
    client.start()
