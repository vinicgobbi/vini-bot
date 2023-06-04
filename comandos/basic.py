import discord
import random

async def ola(ctx, bot):
    await ctx.send(f"Olá do {bot.user.name} 👋")

async def dados(ctx):
    numero = random.randint(0, 6)
    await ctx.send(f"O dado caiu o numero {numero}")

async def ping(ctx, bot):
    await ctx.send(f"Pong! 🏓 {round(bot.latency, 2)} ms")