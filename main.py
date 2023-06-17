import discord
from discord.ext import commands
import comandos.basic as basic
import comandos.dev as dev
import json

config = json.load(open("./config.json"))

prefix = config["prefix"]

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix=prefix, help_command=None)

@bot.event
async def on_ready():
    print(f"Logado no bot {bot.user} com sucesso!")
    print(f"Prefixo do bot '{prefix}'")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
        await bot.process_commands(message)

@bot.command(name="ola")
async def ola(message):
    await basic.ola(message, bot)
    
@bot.command(name="dado", aliases=["dados"])
async def dado(message):
    await basic.dados(message)

@bot.command(name="ping")
async def ping(message):
    await basic.ping(message, bot)

@bot.command(name="sabio", aliases=["genio", "pergunta"])
async def sabio(message, args):
    await basic.sabio(message, args)

@bot.command(name="docs")
async def docs(message, *args):
    await dev.docs(message, args)

@bot.command(name="hlquotes", aliases=["half-life", "quotes", "halflife"])
async def quotes(message):
    await dev.quotes(message)

@bot.command(name="ajuda", aliases=["help"])
async def ajuda(message):
    await basic.ajuda(message, bot, prefix)

@bot.command(name="github", aliases=["git"])
async def github(message, arg):
    await dev.github(message, arg)

@bot.command(name="cep")
async def cep(message, arg):
    await dev.cep(message, arg)
      
if __name__ == "__main__":
    bot.run(config["token"])