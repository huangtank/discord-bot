import discord
from discord.ext import commands

trigger_responses = {
    "ewe": "ewe",
    "不知道": "https://i.imgur.com/MfyFFux.jpg",
    "@1049693945145348116": "tag銃三小啦幹",
    "":"",
    "":"",
}
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def 網站(self, ctx: commands.Context):
        await ctx.send('https://huangtank.github.io')
    
    @commands.command()
    async def 擲骰子(self, ctx: commands.Context):
        n = random.randint(0,1001)
        await ctx.send(n)
    @commands.command()
    async def 指令是啥(self, ctx):
        embed = discord.Embed()
        embed = discord.Embed(title="機器人指令大全", description="在不會我就會笑你")
        embed.set_author(name="點擊此處即可發現人生大道理", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        embed.add_field(name="回覆系統", value="就...回覆", inline=False)
        embed.add_field(name=".", value="ewe", inline=True)
        embed.add_field(name=".", value="偶不知道", inline=True)
        embed.set_footer(text="有沒有人贊助阿QQ")
        await ctx.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return  # 避免機器人自己觸發自己的事件
        content = message.content.lower()  # 將消息轉換為小寫，以便進行比較
        # 檢查消息是否包含觸發詞
        for trigger_word, response in trigger_responses.items():
            if trigger_word in content:
                if trigger_word == "@1049693945145348116" and message.author.name == "ice.____06":
                    print(message.author)
                    await message.channel.send("怎麼了寶")
                else:
                    await message.channel.send(response) #回覆消息
                print(message.author.name == "ice.____06")
                break  # 找到觸發詞後停止迴圈

async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))