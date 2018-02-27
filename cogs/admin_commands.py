import discord
from discord.ext import commands
import checks

from util.colours import *


class AdminCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def log_out(self):
        await self.bot.logout()

    @commands.command()
    @checks.is_owner()
    async def say_channel(self, channel, *, message: str):
        await self.bot.send_message(self.bot.get_channel(channel), content=message)

    @commands.command()
    @checks.is_owner()
    async def say_channel_embed(self, channel, *, message: str):
        await self.bot.send_message(self.bot.get_channel(channel), embed=discord.Embed(description=message))

    @commands.command()
    @checks.is_owner()
    async def change_avatar(self, image):
        with open(image, "rb") as file:
            await self.bot.edit_profile(avatar=file.read())

    @commands.command()
    @checks.is_owner()
    async def change_game(self, ctx, *, game):
        await self.bot.change_presence(game=discord.Game(name=game))

    @commands.command()
    @checks.is_owner()
    async def reload_cog(self, cog):
        self.bot.unload_extension(cog)
        self.bot.load_extension(cog)

def setup(bot):
    bot.add_cog(AdminCommands(bot))