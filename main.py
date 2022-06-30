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
    if ctx.author.bot:
        return
    else:
        pass
    timezone = datetime.timezone.utc
    time = datetime.datetime.now(tz=timezone)
    guild = bot.get_guild(920057625255747674)
    chn = guild.get_channel(991806371815243836)
    hour = chn.last_message.created_at + datetime.timedelta(hours=1)
    print(chn.last_message.content)
    print(time, hour.minute)
    if hour.hour == 0:
        return
    send = time.hour >= hour.hour and time.minute >= hour.minute
    if send:
        embed = discord.Embed(title="Come Chat!",
                              description="Aether is quiet,, it must be asleep :o Let's wake it up! Come talk to us!",
                              color=0xBEE0FA)
        await chn.send("<@&982394594727718938>",embed=embed)
    else:
        return

bot.run(token)
