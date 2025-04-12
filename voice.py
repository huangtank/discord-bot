import discord
from discord.ext import commands
import datetime

class Voice_publish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
        if before.channel is None and after.channel:
            embed_join = discord.Embed(description=f":inbox_tray:{member.display_name} 加入了{after.channel.name}語音", color=0x00ff1e)
            #temp = f"「{member.display_name}」加入「{after.channel.name}」語音頻道"
            await after.channel.send(embed=embed_join)
        elif before.channel and after.channel is None:
            embed_leave = discord.Embed(description=f":outbox_tray:{member.display_name} 離開了{before.channel.name}語音", color=0xff0000)
            #temp = f"「{member.display_name}」離開「{before.channel.name}」語音頻道"
            await before.channel.send(embed=embed_leave)
        elif before.channel != after.channel:
            embed_move = discord.Embed(description=f":airplane:{member.display_name} 移動{before.channel.name} -> {after.channel.name}語音", color=0x007bff)
            #temp = f"「{member.display_name}」移動「{before.channel.name} -> {after.channel.name}」語音頻道"
            await before.channel.send(embed=embed_move)

async def setup(bot):
    await bot.add_cog(Voice_publish(bot))