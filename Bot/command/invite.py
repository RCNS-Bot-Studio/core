from discord.ext import commands
from discord import Embed
from Gura.config import Config
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle


class Invite(commands.Cog, Config):
    """서버인증, 역할을 관리하는 클래스입니다."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command("인증")
    async def get_role(self, ctx):
        if ctx.author.id in self.mamager_list:
            embed = Embed(title="입장버튼", description = "버튼을 눌러 <@&963402929690267708>역할을 받으세요!")
            buttons = [
                create_button(style=ButtonStyle.green, label="버튼", custom_id = 'invite')
            ]
            action_row = create_actionrow(*buttons)
            return await ctx.send(embed = embed, components=[action_row])


    @commands.command("역할부여")
    async def get_role(self, ctx):
        if ctx.author.id in self.mamager_list:
            embed = Embed(title="알림역할 안내", description = "공지알림 : 📢\n업데이트 알림 : 🔧", color=0xff8dc9)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("📢")
            await msg.add_reaction("🔧")

    

def setup(bot):
    bot.add_cog(Invite(bot))
