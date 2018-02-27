import json

import discord
from discord.ext import commands

description = ""
startup_extentions = []

bot = commands.Bot(command_prefix=commands.when_mentioned_or("owo"), description=description)


@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Customer Service"))


def load_credentials():
    with(open("credentials.json")) as f:
        return json.load(f)


if __name__ == "__main__":
    credentials = load_credentials()
    bot.token = credentials["token"]
    bot.client_id = credentials["client_id"]

    for extention in startup_extentions:
        bot.load_extension(extention)

    bot.run(bot.token)
