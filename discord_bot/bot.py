import os
import traceback

import discord
from discord.ext import commands

import pymongo
from pymongo import MongoClient

# TODO:
# - para adicionar novo comando;
#   - adicionar comando no cogs correto
#   - lógica com @bcommands.command()
#   - adicionar o sintaxe na cogs Ajuda
#   - Colocar no README.md
#
# - comandos em desenvolvimento:
#   - criar vaga no db
#
# - member poster
#   - colaborador of the month
#

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix=('$'), description="QUICKFIBRA Bot", intents=intents, case_insensitive=True)
bot.remove_command("help") # eu faço um melhor nos cogs

bot.cluster = MongoClient(os.environ["DB_URI"])
bot.db = bot.cluster['vagas_quick']
bot.collection = bot.db["vagas"]

for extension in os.listdir("./discord_bot/cogs"):
    if extension.endswith(".py"):
        try:
            bot.load_extension(f'cogs.{extension[:-3]}')
            print(f"Loaded extension: {extension}")
        except Exception as e:
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

bot.run(TOKEN)

# ========================= COMANDOS EM DESENVOLVIMENTO ========================= #

"""
# por enquanto, não vejo necessidade disso, mais fácil fazer manual msm...
@bot.command(name='criar-canal', help='criar canal com nome personalizado.')
@commands.has_role('Admin')
async def create_channel(ctx, channel_name='canal-sem-nome'):
    existing_channel = discord.utils.get(ctx.guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Criando o canal "{channel_name}".')
        await ctx.guild.create_text_channel(name=channel_name)

@bot.command(name='deletar-canal', help='deleta o canal especificado')
@commands.has_role('Admin')
async def delete_channel(ctx, channel_name):
   # check if the channel exists
   existing_channel = discord.utils.get(ctx.guild.channels, name=channel_name)
   # if the channel exists
   if existing_channel is not None:
      await existing_channel.delete()
   # if the channel does not exist, inform the user
   else:
      await ctx.send(f'Nenhum canal "{channel_name}" foi encontrado')

# desnecessário...
@bot.command(name='socorro', help='Enviar pergunta destacada para os Administradores.')
async def socorro(ctx, mensagem):
    await ctx.send(f"Admins, ele disse: {mensagem}")
"""
"""
# será implementado futuramente...
@bot.command(name='cor', help='Troca a cor do cartão (embed) do membro que tem\
essa função liberada.')
async def cor(ctx, cor_escolhida):
    await ctx.send(f"Nova cor do cartão: {cor_escolhida}")

import random
@bot.command(aliases=[""]) # esse veio do canal do swastik no youtube
async def meme(ctx):
    emb = discord.Embed(color = discord.Color.red())
    random_link = random.choice(memes_img)
    emb.set_image(url = random_link)
    await ctx.send(embed=emb)

@bot.command(name='piada', help='Com esse comando liberado, o membro pode\
solicitar 3 piadas a cada 10 minutos.')
async def piada(ctx):
    await ctx.send("Alguma piada")

@bot.command(name='conselho', help='Com esse comando liberado, o membro pode\
solicitar 3 conselhos a cada 10 minutos.')
async def conselho(ctx):
    await ctx.send("Algum conselho")

@bot.command(name='contar-piada', help='Com esse comando liberado, o membro\
pode contar piadas ilimitada no canal aberto do servidor.')
async def contar_piada(ctx, piada):
    await ctx.send(piada)

@bot.command(name='aconselhar', help='Com esse comando liberado, o membro\
pode dar conselhos ilimitados no canal aberto do servidor.')
async def aconselhar(ctx, **kwargs):
    await ctx.send(kwags)

@bot.command(name='quick-tech', help='Gasta 100 q-bits para liberar o canal\
Quick-Tech, que contém conteúdo mensal sobre a internet, games e tecnologia.\
Esse custo serve para separá-lo do canal aberto, promovendo bate papo mais\
focado e sem spam.')
async def quick_tech(ctx):
    await ctx.send("Acesso liberado")
"""
"""
# comandos para campeonatos. À ser implementados.
@bot.command(name='registrar', help='Inicia o processo de se registrar\
em uma equipe.')
async def registrar(ctx):
    await ctx.send(f"Beleza {ctx.author.name}, vou te chamar no dm!")
    await ctx.author.send(f'Fala {ctx.author.name}, bora registrar sua equipe!\n\
\n\
Preciso que me envie a informação de cada jogador no seguinte formato:\n\
---!registrar_integrante "equipe" "nome real" "nickname" "data de nascimento" \
"endereço" "email" "telefone de contato"\n\
\n\
Por exemplo: "!registrar_player "equipe" "Quick Fibra" "QuickPlay" \
"01/01/1998" "Rua Almirante Adalberto de barros Nunes 629, Vila Mury, VR, RJ" \
"suporte@quick.com.br" "(24) 3512 3312"')
# nome real
# nickname
# data de nascimento
# endereço
# email
# telefone de contato

import json

@bot.command(name='registrar_integrante', help='Inscriçao de cada integrante da equipe.')
async def registrar_integrante(ctx, equipe, nome, nickname, dob, address, email, telefone):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        print(f"Equipe: {equipe}\nNome: {nome}\nNickname: {nickname}\n\
Data de nascimento: {dob}\nEndereço: {address}\nEmail: {email}\nTelefone: {telefone}")
        # json
        data = {equipe:{
            "nome completo": nome,
            "nickname": nickname,
            "data de nascimento": dob,
            "endereço": address,
            "email": email,
            "telefone": telefone
        }}
        print("criando arquivo json")
        with open(f"equipes/equipe_{equipe}_{nickname}.json", "w") as equipe_db:
            json.dump(data, equipe_db)
        print("pronto")

        await ctx.send("Jogador registrado!\nObs: para verificar os integrantes\
da sua equipe, use o comando: !minha_equipe.\nFaça a inscrição também no Battlefy: <link>")
    else:
        await ctx.send("Este comando funciona apenas no DM!")

@bot.command(name='minha_equipe', help='Inscriçao de cada integrante da equipe.')
async def minha_equipe(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        await ctx.send(f"Info da equipe:\n-")
"""

"""
@bot.command(name='disregistrar', help='Remove sua inscrição de uma equipe.')
async def disregistrar(ctx):
    await ctx.send("De qual equipe?")

@bot.command(name='rodada', help='Informação sobre as partidas da rodada atual.')
async def rodada(ctx):
    await ctx.send("Partidas:")

@bot.command(name='equipe', help='Informação sobre sua equipe.')
async def equipe(ctx):
    await ctx.send("Cartão embed")

@bot.command(name='resultado', help='Resumo dos resultados dessa equipe.')
async def disregistrar(ctx, equipe):
    await ctx.send(f"Resultados da equipe {equipe}")

@bot.command(name='premio', help='Informação sobre a premiação.')
async def premio(ctx):
    await ctx.send("Regras de premiação:\n")

@bot.command(name='ping', help='Consultar status de saúde do bot.')
async def ping(ctx):
    await ctx.send("Bot ok! :D")

@bot.command(name='placar', help='Inicia o processo de registro de placar.')
async def placar(ctx, equipe_a, equipe_b):
    await ctx.send(f"Equipe {equipe_a[0]}: {equipe_a[1]}\nEquipe {equipe_b[0]}: {equipe_b[1]}")

@bot.command(name='nova_rodada', help='Inicia o processo de configuração\
da próxima rodada.')
async def nova_rodada(ctx):
    await ctx.send("Primeira partida?")

@bot.command(name='atribuir', help='Forma manual de atribuir q-bits ou troféis.')
async def atribuir(ctx, ativo, membro: discord.Member):
    await ctx.send(f"{ativo} entregue ao {membro.name}")

@bot.command(name='ban', help='Banir <membro>. OBS: comando de permissão ADMIN.')
async def ban(ctx, member : discord.Member = None, days = " ", reason = " "):
    '''Bans specified member from the server.'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await bot.say("Você não tem a role: Admin")
    pass

    try:
        if member == None:
            await bot.say(ctx.message.author.mention + ", Favor especificar um membro para banir!")
            return

        if member.id == ctx.message.author.id:
            await bot.say(ctx.message.author.mention + ", Você não pode se banir!")
            return
        else:
            await bot.ban(member, days)
            if reason == ".":
                await bot.say(member.mention + " Foi banido(a) do servidor!")
            else:
                await bot.say(member.mention + " Foi banido(a) do servidor! Razão: " + reason + ".")
            return
    except Forbidden:
        await bot.say("Você não tem as permissõe necessárias para banir alguém!")
        return
    except HTTPException:
        await bot.say("Algo deu errado, tente novamente mais tarde.")

@bot.command(name='kick', help='Retirar <membro>. OBS: comando de permissão ADMIN.')
async def kick(ctx, *, member : discord.Member = None):
    '''Kicks A User From The Server'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await bot.say("Você não tem a role: Admin")
    pass

    if not member:
        return await bot.say(ctx.message.author.mention + "Favor especificar um membro para kick!")
    try:
        await bot.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await bot.say(":x: Privilégio muito baixo!")
 
    embed = discord.Embed(description = f"**{member.name}** foi retirado.", color = 0xF00000)
    embed.set_footer(text="QUICK GAMES", icon_url="https://is4-ssl.mzstatic.com/image/thumb/Purple113/v4/48/cd/fc/48cdfc22-cce0-9231-dfd9-2cc8c5661940/source/512x512bb.jpg")
    await bot.say(embed = embed)

#Mutes a Member From The server

@bot.command(name='silenciar', help='Silenciar <membro>. OBS: comando de permissão ADMIN.')
async def mute(ctx, *, member : discord.Member):
    '''Mutes A Memeber'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await bot.say("Você não tem a role: Admin")
    pass

    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)

    await bot.say(f"**{member.mention}** foi silenciado! Aguarde até ser liberado...")

#Unmutes a member

@bot.command(name='disilenciar', help='Tirar o silencio de <membro>. OBS: comando de permissão ADMIN.')
async def unmute(ctx, *, member : discord.Member):
    '''Unmutes The Muted Memeber'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await bot.say("Você não tem a role: Admin")
    pass

    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await bot.edit_channel_permissions(ctx.message.channel, member, overwrite)

    await bot.say(f"**{member.mention}** Pronto... Foi retirado do silêncio!")
"""
