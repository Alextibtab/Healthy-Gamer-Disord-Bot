import os

import interactions
from pymongo import MongoClient
from dotenv import load_dotenv

from .rpg.game import Game

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# GUILD = int(os.getenv("GUILD_ID"))

client = interactions.Client(token=TOKEN)

db_client = MongoClient(os.getenv("MONGO_URI"))
game = Game(db_client)

@client.event
async def on_ready():
    print(f"Client has connected to Discord!")


@client.command(name="stats", description="Get your player stats")
async def stats(ctx: interactions.CommandContext):
    player = game.get_player(ctx.member)
    stats_embed = interactions.Embed(
        title="Character Stats:",
        description=f"<@{ctx.member.id}> your stats are:",
        color=0xCD2323,
        fields=[
            interactions.EmbedField(
                name="Name", value=player.name, inline=True
            ),
            interactions.EmbedField(
                name="Level 🟢", value=player.get_level(), inline=True
            ),
            interactions.EmbedField(
                name="XP 🟡", value=player.get_xp(), inline=True
            ),
            interactions.EmbedField(
                name="\u200b", value="\u200b", inline=False
            ),
            interactions.EmbedField(
                name="Max HP", value=player.get_max_hp(), inline=False
            ),
            interactions.EmbedField(
                name="Current HP ❤️", value=player.health, inline=True
            ),
            interactions.EmbedField(
                name="Mana 🧙‍♂️", value=player.mana, inline=True
            ),
            interactions.EmbedField(
                name="\u200b", value="\u200b", inline=False
            ),
            interactions.EmbedField(
                name="Attack 🗡️", value=player.get_attack(), inline=True
            ),
            interactions.EmbedField(
                name="Defence 🛡️", value=player.get_defence(), inline=True
            ),
            interactions.EmbedField(
                name="Gold 💰", value=player.get_gold(), inline=False
            ),
            interactions.EmbedField(
                name="Items 🎒", value=player.get_items(), inline=False
            ),
        ],
        footer=interactions.EmbedFooter(text="RPG Bot"),
    )
    await ctx.send(embeds=stats_embed)


@client.command(name="fight", description="Battle a monster")
async def fight(ctx: interactions.CommandContext):
    result = game.encounter_action(ctx.member)
    await ctx.send(result)


@client.command(name="flee", description="Run from a battle")
async def flee(ctx: interactions.CommandContext):
    result = game.end_encounter(ctx.member)
    await ctx.send(result)


# reset player data
@client.command(name="reset", description="Reset your player data")
async def reset(ctx: interactions.CommandContext):
    result = game.reset_player(ctx.member)
    await ctx.send(result)


def start_bot():
    client.start()
