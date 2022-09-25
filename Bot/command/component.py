import discord
from discord.ext import commands
from discord import Embed
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from Gura.config import Config
import asyncio

class Component(commands.Cog, Config):
    """모든 Component를 관리하는 클래스입니다."""

    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_component(self, ctx):
        """초대버튼"""
        if ctx.custom_id == 'invite':
            role = discord.utils.get(ctx.guild.roles, name="Member")
            await ctx.author.add_roles(role)
            return await ctx.reply('역할이 부여되었습니다!\n<#963404825998020668>를 필독해주세요!', hidden = True)

        
        """봇제작"""
        if ctx.custom_id == 'makebotplz':
            category = discord.utils.get(ctx.guild.categories, name="상담")
            guild = ctx.guild
            m = await guild.create_text_channel(
                f"{ctx.author.name}님의 외주문의", category = category
            )
            await m.set_permissions(
                ctx.author,
                speak=True,
                send_messages=True,
                read_message_history=True,
                read_messages=True
            )
            #채널 생성
            
            buttons = [
                create_button(
                    style=ButtonStyle.green,
                    label="채널 닫기", 
                    custom_id = "close", 
                    emoji="🔒"
                )
            ]
            action_row = create_actionrow(*buttons)
            
            embed = Embed(
                title="신청이 완료되었습니다!", 
                description = "<@&963402343460782130>또는 <@&963402759275700234>가 곧 연락이 갈 예정입니다."
            )
            embed.add_field(
                name="미리 준비해주세요!", 
                value="```\n1. 봇의 기능\n2. 호스팅유무(y/n)\n```", 
                inline=False
            )
            await m.send(f'{ctx.author.mention}',embed=embed,components=[action_row])
            
            chan = self.bot.get_channel(963404522527535104)
            await chan.send(f"<@&963402343460782130> <@&963402759275700234>님 의뢰가 들어왔어요!\n<#{m.id}>")
            return await ctx.send(f"외주문의채널이 생성되었습니다! <#{m.id}>", hidden = True)

        
        """봇제작"""    
        if ctx.custom_id == 'close':
            if ctx.author.id in self.mamager_list:
                await ctx.send('3초후에 채널이 삭제됩니다...')
                await asyncio.sleep(3)
                channel = self.bot.get_channel(ctx.channel.id)
                return await channel.delete()
  
            else:
                return await ctx.send("티켓닫기는 처리자만 가능합니다.", hidden = True)

        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        """#역할부여"""
        if str(reaction.message_id) == '1023592021614657627':
            if str(reaction.emoji) == '📢':
                user = reaction.member
                role = discord.utils.get(user.guild.roles, id=963434539059916850)
                return await user.add_roles(role)
            elif str(reaction.emoji) == '🔧':
                user = reaction.member
                role = discord.utils.get(user.guild.roles, id=966014424156602399)
                return await user.add_roles(role)

    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, reaction):
        """#역할제거"""
        if str(reaction.message_id) == '1023592021614657627':
            if str(reaction.emoji) == '📢':
                guild = self.bot.get_guild(reaction.guild_id)
                member = guild.get_member(reaction.user_id)
                role = discord.utils.get(guild.roles, id=963434539059916850)
                return await member.remove_roles(role)
            elif str(reaction.emoji) == '🔧':
                guild = self.bot.get_guild(reaction.guild_id)
                member = guild.get_member(reaction.user_id)
                role = discord.utils.get(guild.roles, id=966014424156602399)
                return await member.remove_roles(role)
                
def setup(bot):
    bot.add_cog(Component(bot))
