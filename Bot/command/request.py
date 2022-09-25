from discord import Embed
from discord.ext import commands
from Gura.config import Config
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle

class Reqeust(commands.Cog, Config):
    """의뢰를 관리하는 클래스입니다."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command("의뢰알림")
    async def requests(self, ctx):
        embed = Embed(title="외주신청 안내", description = "버튼을 눌러 외주를 신청하실 수 있습니다.", color = 0xFF73FA)
        embed.add_field(name="⚠️주의사항", value="1. 최대한 구체적으로 생각한 후에 신청을 해주세요.\n2. 제발 장난으로 누르지 마세요.**(경고2회)**\n3. 기본적으로 가격은 **무료**입니다. 하지만 요청 기능에 따라 __가격이 추가__됩니다.", inline=False)
        buttons = [
            create_button(style=ButtonStyle.green, label="신청하기", custom_id = 'makebotplz', emoji="🛠️")
        ]
        action_row = create_actionrow(*buttons)
        return await ctx.send(embed = embed,components=[action_row])

                
def setup(bot):
    bot.add_cog(Reqeust(bot))
