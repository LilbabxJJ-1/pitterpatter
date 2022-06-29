# <--------------------Imports-------------------->
import discord
from discord.ext import commands
import random
import asyncio
from tokens import token

# <--------------------Bot------------------------>
intents = discord.Intents.all()
activity = discord.Activity(type=discord.ActivityType.watching, name='over Aether')
bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'), case_insensitive=True, activity=activity, intents=intents, help_command=None)


@bot.event
async def on_message(ctx):
    if ctx.channel.id == 982394595478478906:
        pass
    else:
        pass
    if ctx.author.id != bot.user.id:
        pass
    if not ctx.author.bot:
        pass
    else:
        return

    times = [10, 5, 15]
    try:
        ll = await bot.wait_for("message", timeout=3600)
    except:
        async with ctx.channel.typing():
            await asyncio.sleep(random.choice(times))
        embed = discord.Embed(title="Come Chat!",
                              description="Aether is quiet,, it must be asleep :o Let's wake it up! Come talk to us!",
                              color=0xBEE0FA)
        await ctx.channel.send("<@&982394594727718938>", embed=embed)

bot.run(token)
