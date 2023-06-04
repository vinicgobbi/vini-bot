import json
import requests

async def docs(ctx, arg):
    if not arg:
        return
    else:
        file = open("./langs.json")
        dados = json.load(file)
        lang = ' '.join(arg).lower()
        if lang not in dados:
            await ctx.send(f"Linguagem {lang} não encontrada, aguarde que ela pode ser adicionada no futuro")
            await ctx.send(f"Se quiser pode colaborar adicionando novas linguagens e comandos ao bot Aqui: https://github.com/vinicgobbi/vini-bot-py")
        else:
            link = dados[lang]
            await ctx.send(f"Estude a linguagem {lang} pelo site {link}")

async def quotes(ctx):
    quote_api = requests.get("https://hl-api.fly.dev/").json()
    frase = quote_api[0]['quote']
    autor = quote_api[0]['author']

    await ctx.send(f'"{frase}", {autor}')
