import asyncio
from discord import Game
from discord import Member
from discord.ext import commands
from Gura.config import Config


class User(commands.Cog, Config):
    """유저를 관리하는 클래스입니다."""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=Game("관리"))
        print("로딩완료")

    @commands.command("ban")
    async def ban(self, ctx, user : Member, *, reason):
        if ctx.author.id in self.mamager_list:
            return await user.ban(reason=reason)

    @commands.command("kick")
    async def kick(self, ctx, user : Member, *, reason):
        if ctx.author.id in self.mamager_list:
            return await user.kick(reason=reason)

    @commands.command("clear")
    async def clear(self, ctx, amount : int):
        if ctx.author.id in self.mamager_list:
            await ctx.channel.purge(limit=amount+1)
            msg = await ctx.send(f"{amount}개의 메세지 삭제완료")
            await asyncio.sleep(1.0)
            return await msg.delete()

def setup(bot):
    bot.add_cog(User(bot))
