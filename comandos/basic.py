import discord
import random

async def ola(ctx, bot):
    await ctx.send(f"Olá do {bot.user.name} 👋")

async def avatar(ctx, member):
    if not member:
        embed = discord.Embed(
            title=f"Avatar de {ctx.author.name}"
        )
        embed.set_image(url=ctx.author.avatar)
        embed.set_footer(text=f"Solicitado por: {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f"Avatar de {member.name}"
        )
        embed.set_image(url=member.avatar)
        embed.set_footer(text=f"Solicitado por: {ctx.author.name}", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed)

async def dados(ctx):
    numero = random.randint(0, 6)
    await ctx.send(f"O dado caiu o numero {numero}")

async def ping(ctx, bot):
    await ctx.send(f"Pong! 🏓 {round(bot.latency, 2)} ms")

async def sabio(ctx, arg):
    ask = ' '.join(arg).lower()
    if ask[-1] == "?":
        respostas = ["Sim", "Não", "Talvez", "Claro que sim","Claro que não", "Boa pergunta", "Obviamente não", "Obviamente Sim", "Claramente Sim", "Claramente não", "Me poupe", "Mano, me deixa quieto", "Me recuso a responder"]
        numero = random.randint(0, len(respostas)-1)
        await ctx.send(respostas[numero])
    else:
        await ctx.send("Faça uma pergunta por favor")

async def ajuda(ctx, bot, prefix):
    embed = discord.Embed(
        title="Ajuda",
        description="Vamos ver do que o bot é capaz?",
        color=0x8110cc
    )
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar)
    embed.add_field(name="----- Básicos -----", value=f"""**{prefix}ola**
Nada melhor que um cumprimento a qualquer hora do dia certo?
**{prefix}avatar**
Procurando pelo avatar de alguém? Encontre aqui!
**{prefix}dado [dados]**
Que tal testar sua sorte jogando os dados?
**{prefix}ping**
O bot está lento para responder? Teste a latencia dele
**{prefix}help [ajuda]**
Mostra essa tela
**{prefix}sabio [genio, pergunta]**
Pergunte ao sábio que ele te dará uma resposta""")
    embed.add_field(name="----- Dev -----", value=f"""**{prefix}docs**
Que tal aprender a programar usando a documentação oficial da linguagem?
**{prefix}hlquotes [half-life, quotes, halflife]**
Frases aleatória de Half-Life
**{prefix}github [git]**
Procurar informações de um perfil no github
**{prefix}repo [repos]**
Procurar informações de um repositório do github
**{prefix}cep**
Mostrar informações básicas de um local baseado em seu CEP""")
    embed.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.avatar)
    await ctx.send(embed=embed)