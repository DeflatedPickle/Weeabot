import json

from discord.ext import commands
import discord.utils

from Weeabot import load_credentials

def is_owner_check(message):
    return message.author.id == load_credentials()["owner_id"]

def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))
