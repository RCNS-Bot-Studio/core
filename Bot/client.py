import discord
from discord.ext import commands
from discord_slash import SlashCommand
from Gura.config import Config

class Gura(Config):

    def run(self) -> None:
        """봇을 작동 시킵니다."""
        bot = commands.Bot(
            command_prefix=self.prefix, intents=discord.Intents.all()
        )
        for command in self.command_list:
            bot.load_extension(f"Gura.command.{command}")
            
        slash = SlashCommand(bot, sync_commands=True)
        bot.run(self.token)
