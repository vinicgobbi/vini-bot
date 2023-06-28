import discord
import json
import requests

async def docs(ctx, arg):
    if not arg:
        return
    else:
        dados = json.load(open("./langs.json"))
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

async def github(ctx, arg):
    github_json = requests.get(f"https://api.github.com/users/{arg}").json()
    if 'message' in github_json:
        await ctx.send("Perfil não encontrado")
    else:
        username = github_json['login']
        nome = github_json['name']
        url = github_json['html_url']
        avatar = github_json['avatar_url']
        bio = github_json['bio']
        seguindo = github_json['following']
        seguidores = github_json['followers']
        criado = github_json['created_at']
        repos = github_json['public_repos']
        gists = github_json['public_gists']
        embed = discord.Embed(
            title="Github User Info",
        )
        embed.set_thumbnail(url=avatar)
        embed.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.avatar)
        embed.add_field(name="--- Informações Básicas ---", value=f"""**Nome**: {nome}
**Nome de Usuário**: {username}
**Bio**: {bio}
""")
        embed.add_field(name="--- Informações técnicas ---", value=f"""**URL do perfil**: {url}
**Repositórios**: {repos}
**Gists**: {gists}
**Seguidores**: {seguidores}
**Seguindo**: {seguindo}
**Criado em**: {criado}""")
        await ctx.send(embed=embed)

async def cep(ctx, args):
    if not args:
        await ctx.send("Nenhum CEP inserido")
    else:
        arg = "".join(args)
        arg = str(arg).replace("-", "").replace(".", "")
        brasilapi = requests.get(f"https://brasilapi.com.br/api/cep/v2/{arg}").json()
        if "message" in brasilapi:
            await ctx.send("CEP inválido")
        else:
            cep = arg
            estado = brasilapi['state']
            cidade = brasilapi['city']
            servico = brasilapi['service']
            await ctx.send(f"**CEP**: {cep}\n**UF**: {estado}\n**Cidade**: {cidade}\nDisponbilizado por: {servico}")


async def repos(ctx, args):
    arg = "/".join(args).lower()
    github_repo = requests.get(f"https://api.github.com/repos/{arg}").json()
    if 'message' in github_repo:
        await ctx.send("Repositório não encontrado, verifique as informações!\nCertifique-se de ter colocado a seguinte estrutura `<nome-de-usuario> <nome-do-repo>` ou `<nome-de-usuario>/<nome-do-repo>`")
    else:
        repo_url = github_repo["html_url"]
        avatar = github_repo["owner"]["avatar_url"]
        nome = github_repo["name"]
        descricao = github_repo["description"]
        forks = github_repo["forks"]
        issues = github_repo["open_issues"]
        lang = github_repo["language"]
        is_fork = github_repo["fork"]
        if is_fork:
            is_fork = "Sim"
        else:
            is_fork = "Não"
        embed = discord.Embed(
            title="Github Repo Info"
        )
        embed.set_thumbnail(url=avatar)
        embed.set_footer(text=f"Solicitado por {ctx.author.name}", icon_url=ctx.author.avatar)
        embed.add_field(name="--- Repo Info ---", value=f"""**Repositório**: {nome}
**URL**: {repo_url}
**Descrição**: {descricao}
**Linguagem Principal**: {lang}
**É um Fork**? {is_fork}
**Forks**: {forks}
**Problemas(Issues)**: {issues}""")
        await ctx.send(embed=embed)