import discord
import datetime
import pytz
import json
from discord.ext import commands, tasks

file = json.load(open("setting.json", "r", encoding="utf-8"))

class Countdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.TIMEZONE = pytz.timezone('Asia/Shanghai')
        self.統測 = file["統測"]
        self.模考 = file["模考"]
        self.update_countdown_daily.start()

    async def countdown_daily(self):
        current_date = datetime.datetime.now(self.TIMEZONE).date()

        # 統測目標日期
        target_date_統測 = datetime.date(2025, 4, 26)
        days_統測 = (target_date_統測 - current_date).days

        # 模考目標日期（五模模擬考）
        target_date_模考 = datetime.date(2025, 4, 8)
        days_模考 = (target_date_模考 - current_date).days

        print('更改成功')
        print(datetime.datetime.now(self.TIMEZONE))
        print(f'統測剩餘{days_統測}天')
        print(f'五模剩餘{days_模考}天')

        # 統測 countdown
        統測_channel = self.bot.get_channel(self.統測)
        if days_統測 == 0:
            await 統測_channel.send("祝各位統測順利！")
            await 統測_channel.send("寫快！但不要粗心阿")
            await 統測_channel.edit(name="祝各位統測順利！")
        else:
            await 統測_channel.edit(name=f"統測倒數{days_統測}天")

        # 模考 countdown
        # 模考_channel = self.bot.get_channel(self.模考)
        # if days_模考 == 0:
        #     await 模考_channel.send("祝各位模考順利！")
        #     await 模考_channel.edit(name="祝各位模考順利！")
        # else:
        #     await 模考_channel.edit(name=f"五模倒數{days_模考}天")


    @tasks.loop(hours=24)
    async def update_countdown_daily(self):
        await self.countdown_daily()  # 每天 UTC+8 00:00 更新一次

    @update_countdown_daily.before_loop
    async def before_update_countdown_daily(self):
        now = datetime.datetime.now(self.TIMEZONE)
        tomorrow = now + datetime.timedelta(days=1)
        midnight = datetime.datetime.combine(tomorrow, datetime.time(0,1))
        print("現在", now)
        print("start")
        print("午夜", midnight)
        await discord.utils.sleep_until(midnight)

    @commands.Cog.listener()
    async def on_ready(self):
        await self.countdown_daily()
        await update_countdown_daily()
        print('Countdown cog is ready')

async def setup(bot):
    await bot.add_cog(Countdown(bot))