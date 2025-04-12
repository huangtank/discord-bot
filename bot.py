import discord
#from keep_alive import keep_alive
import random
import asyncio
import time
import json
import datetime
from discord.ext import commands, tasks
import pytz
import os

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
file = json.load(open("setting.json", "r", encoding="utf-8"))
###############################################################################
# 載入指令程式檔案
@bot.event
async def on_ready():
    print('Bot is online')
    game = discord.Game('資三廉')
    #await countdown_daily()
    await bot.change_presence(status=discord.Status.idle, activity=game)
    await load_extensions()
    #await update_countdown_daily.start()
###############################################################################
# 載入指令程式檔案
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

# 卸載指令檔案
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

# 重新載入程式檔案
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")

# 一開始bot開機需載入全部程式檔案
s = []
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            s.append(filename[:-3])
            await bot.load_extension(f"cogs.{filename[:-3]}")
    print('Cog載入成功，載入了', s)
###############################################################################

# async def countdown_daily():
#     target_date = datetime.datetime(2025, 5, 3, 23, 59, 59, tzinfo=pytz.UTC)
#     current_date = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
#     time_difference = target_date - current_date
#     target_date_simulation = datetime.datetime(2024, 10, 21, 23, 59, 59, tzinfo=pytz.UTC)
#     time_difference_simulation = target_date_simulation - current_date
#     print('更改成功')
#     print(f'統測剩餘{time_difference.days}天')
#     print(f'一模剩餘{time_difference_simulation.days}天')
#     if time_difference.total_seconds() <= 0:
#         await bot.get_channel(統測).edit(name="目標日期已到達！")
#     else:
#         days = time_difference.days
#         await bot.get_channel(統測).edit(name=f"統測倒數{days}天")
    
#     if time_difference_simulation.total_seconds() <= 0:
#         await bot.get_channel(模考).edit(name="目標日期已到達！")
#     else:
#         days = time_difference_simulation.days
#         await bot.get_channel(模考).edit(name=f"一模倒數{days}天")

# @tasks.loop(hours=24)
# async def update_countdown_daily():
#     await countdown_daily()  # 每天 UTC+8 00:00 更新一次

# @update_countdown_daily.before_loop
# async def before_update_countdown_daily():
#     now = datetime.datetime.now(TIMEZONE)
#     tomorrow = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(days=1)
#     midnight = datetime.datetime.combine(tomorrow, datetime.time.min)
#     # 等待到 UTC+8 00:00
#     print("start")
#     await discord.utils.sleep_until(midnight)
##############################################################################
#keep_alive()
async def main():
    async with bot:
        await load_extensions()
        await bot.start(file["token"])

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())