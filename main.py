# <--------------------Imports-------------------->
import discord
from discord.ext import commands
import random
import asyncio
from asyncio import shield
from tokens import token
import datetime

# <--------------------Bot------------------------>
intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.watching, name='over Aether')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), case_insensitive=True, activity=activity, intents=intents, help_command=None)


@bot.event
async def on_message(ctx):
    timezone = datetime.timezone.utc
    time = datetime.datetime.now(tz=timezone)
    guild = bot.get_guild(982394594677358682)
    chn = guild.get_channel(982394595478478906)
    hour = chn.last_message.created_at + datetime.timedelta(hours=1)
    send = time.hour >= hour.hour
    if send:
        embed = discord.Embed(title="Come Chat!",
                              description="Aether is quiet,, it must be asleep :o Let's wake it up! Come talk to us!",
                              color=0xBEE0FA)
        await chn.send("<@&982394594727718938>",embed=embed)
    else:
        return

bot.run(token)
