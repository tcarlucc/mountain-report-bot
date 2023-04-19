import discord
from discord.ext import commands
import secrets  # Seperate python file to not expose private token for bot login

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())
intents = discord.Intents.all()

client.run(secrets.token)
