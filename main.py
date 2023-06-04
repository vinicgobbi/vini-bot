import discord
from discord.ext import commands
import comandos.basic as basic
import comandos.dev as dev
import dotenv
import openai
from os import getenv

dotenv.load_dotenv()

intents = discord.Intents.all()

bot = commands.Bot(intents=intents, command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logado no bot {bot.user} com sucesso!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        print(f"Mensagem de {message.author}")
        await bot.process_commands(message)

@bot.command(name="ola")
async def ola(message):
    await basic.ola(message, bot)
    
@bot.command(name="dado")
async def dado(message):
    await basic.dados(message)

@bot.command(name="ping")
async def ping(message):
    await basic.ping(message, bot)

@bot.command(name="docs")
async def docs(message, *args):
    await dev.docs(message, args)

@bot.command(name="hlquotes")
async def quotes(message):
    await dev.quotes(message)


if __name__ == "__main__":
    bot.run(getenv("TOKEN"))