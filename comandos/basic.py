import discord
import random


async def ola(ctx, bot):
    await ctx.send(f"Olá do {bot.user.name} 👋")

async def dados(ctx):
    numero = random.randint(0, 6)
    await ctx.send(f"O dado caiu o numero {numero}")

async def ping(ctx, bot):
    await ctx.send(f"Pong! 🏓 {round(bot.latency, 2)} ms")

async def ajuda(ctx, bot, prefix):
    embed = discord.Embed(
        title="Ajuda",
        description="Vamos ver do que o bot é capaz?",
        color=0x8110cc
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar)
    embed.add_field(name="----- Básicos -----", value=f"""**{prefix}ola**
Nada melhor que um cumprimento a qualquer hora do dia certo?
**{prefix}dados**
Que tal testar sua sorte jogando os dados?
**{prefix}ping**
O bot está lento para responder? Teste a latencia dele""")
    embed.add_field(name="----- Dev -----", value=f"""**{prefix}docs**
Que tal aprender a programar usando a documentação oficial da linguagem?
**{prefix}quotes**
Frases aleatória de Half-Life""")
    embed.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)