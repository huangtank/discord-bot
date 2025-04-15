'''
                               `-+syhddmmmddhyo+:`                              
                            .+hmmdddddddddddddddmmds/`      ``...`              
                         `/hmddddddddddddddddddddddddmy++osyhyyyhhs.            
                       `ommddddddddddddddddddddddddddddmmdys+++syhhh:           
           .`         /mmddddddddddddddddddddddddddddddddmmhyyyyyyyyh/          
       `:sdNy`      .ymddddddddddddddddddddddddddddddddddddmdhhhyyyyyh-         
   `.+hmmmddmo     -mmddddddddddddddddddddddddddddddddddddddmmhhhhhhhh+         
  odmmdddddddms` `+mmddddddddddddddddddddddddddddddddddddddddmmddhhhhh+         
  ymdmmmmmmmmdmmdmmdddddddddddddmmddddddddddddddddddddddddddddmd:ydhhd:         
  :Nmmmmmmmmmmmmmmddy+::+ydddms/:::/+osydmdddddddddddddddddddddN-`:+o:          
   ymmmmmmmmmmmmmmdo.`.``/hmm/+hdd/``````-+ydmdddddddddddddddddmy               
   .mmmmmmmmmmmmmmh:`-o+`:hm/`-o:.```````os/./ymddddddddddddddddN`              
    /Nmmmmmmmmmmmmh:..::-od/``dMs````````/hNm:`-ymddddddddddddddN-              
     sNmmmmmmmmmmmd+-:/-.`..`.hh:`...``:hh..:```:NdmmmmmmmdmddddN/              
  `::/dmmmmmmmmmmmmdo:```./d/````-..:`-mdd.````.dmdmmmmmmmmmmmdmmy              
./::-..+dmmmmmmmmmmh/````-dNms-```..``.+/`````-dmds/:-:ohmmmmmmmmN.             
-/.``--`/dmmmdysydmy.````omNd+.-::-...-:os:..`-hs-``.``./hmmmmmmmmd.       .os` 
/:---.`.`-/sy:```omy-````hddo` `s.``/NNNNo...`````-+o/``/dmmmmmmmmmms:..:+ymmN: 
:/.``.``````-``./dNh/````syyyhshd-``:mNmy.````````.```./hmmmmmmmmmmmmmmmmmmmmmd 
 .::-```...````+dNNNs-```//::/+ooosyhdds.``````-----:+ydmmmmmmmmmmmmmmmmmmmmmmN:
   `:/````..``-shhdmms-``./::/:::::::+/``````.+dmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd
     ./:-```.-oyyhyhhhy+.`.:/::::///:.````..:ymNNmmo:/ymmmmmmmmmmmmmmmmmmmmmmmmN
       `:y:./yyyyyyyyhh///:..--:--.````..-/ymNNNNNy.``-hNNNNNmmmmmmmmmmmmmmNmh+-
       `ymdyhyyyyyyhhy/---o+///:::::://oyhmNNNNNNNo```:osyho/---:ymmNNNNmho:`   
       `+hhhhhyyyyhhs-----y--o/------:+hhhhhhhddds.````````..-..-+dNds+-`       
         `.:+oossyyyy:---:ssoy:------+hyyyyhhyyys-``....```..--..//`            
                    syysyysssho:-----ohyyyyhyhhyy/`````..``````-o.              
                   `hssssssoyhhyo+++syyhhhhyyhyyh+:::-..-:::::::.               
                   :hysssyo/yhhssyysssssyhyhhhyhdmmy....`                       
                   shyyyyyyhhhhyyyyyyyyyyhh/-+syhdo`                            
                  `hhhhhhhhhhhhhhhhhhhhhhhhy`                                   
                   -:yhyyyysyhhyyyyyyyyyyyyh-                                   
                     -hysssssyydsyyssssssssyh.                                  
                      /hsysyyyyd-.+yyyssyyssyh-                                 
          -/+oo++/-`   +hhyhhhso`  .ohyyyyyyhho:`   `-:/++++/:.                 
       -+ooooooooooso+/ssss.yy:      `//+ds/oysss+ossoooooooo+os/.              
    `:o+:/oooooooooooooooossyh:          oyyssooooooooooooooo+/:os+`            
   -ssoooooooooooooooooosssssy+          .hyssssssooooooooooooooooss-           
   /syysssssssssssssssyyyyyyyh-           shyyyysyyysssssssssssssssyy           
     `-/+ossyyyysso+/:-./++//.             .---` `.-:/+oossssoo++/:-`           
'''

import discord
import datetime
import pytz
import json
from discord.ext import commands, tasks
import os

file = json.load(open(r"./setting.json", "r", encoding="utf-8"))

class Countdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.TIMEZONE = pytz.timezone('Asia/Shanghai')
        self.統測 = file["統測"]
        self.模考 = file["模考"]

    async def countdown_daily(self):
        current_date = datetime.datetime.now(self.TIMEZONE).date()

        # 統測目標日期
        target_date_統測 = datetime.date(2025, 4, 26)
        days_統測 = (target_date_統測 - current_date).days

        # 模考目標日期（五模模擬考）
        target_date_模考 = datetime.date(2025, 4, 8)
        days_模考 = (target_date_模考 - current_date).days

        print("⏰ 倒數任務執行時間：", datetime.datetime.now(self.TIMEZONE))
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
        
        # 取得 Asia/Shanghai 的「明天 00:01」
        tomorrow = now + datetime.timedelta(days=1)
        shanghai_midnight_001 = datetime.datetime.combine(tomorrow, datetime.time(0, 1))
        shanghai_midnight_001 = self.TIMEZONE.localize(shanghai_midnight_001)

        # 轉換成 UTC 給 sleep_until 用
        utc_target = shanghai_midnight_001.astimezone(pytz.UTC)

        print("現在時間：", now)
        print("等待到（UTC）：", utc_target)

        await discord.utils.sleep_until(utc_target)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.update_countdown_daily.is_running():
            print("✅ Bot 已上線，準備啟動每日倒數更新任務")
            await self.countdown_daily()
            self.update_countdown_daily.start()

async def setup(bot):
    await bot.add_cog(Countdown(bot))