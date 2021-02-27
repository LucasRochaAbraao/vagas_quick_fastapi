import os
import asyncio
import datetime
import discord
from discord.ext import commands
from models import db, Vaga

class MembrosCog(commands.Cog, name = "Membros"):
    """Comandos disponíveis para todos membros do servidor."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["vaga"], help='Exibe um cartão (embed) com \
    informações de todas vagas, incluindo àquelas desativadas.')
    async def vagas(self, ctx):
        vagas_cursor = self.bot.collection.find()
        vagas = []
        if vagas_cursor:
            for vaga in vagas_cursor:
                vagas.append(vaga)
        else:
            await ctx.send("Não encontrei vagas anunciadas! Deseja criar uma vaga? Envie: !criar_vaga")

        emb = discord.Embed(
            title = 'vagas',
            description = 'Todas vagas no banco de dados',
            color = discord.Color.blue()
        )

        for vaga in vagas:
            if vaga['ativo']:
                ativo = 'sim'
            else:
                ativo = 'não'
            emb.add_field(name = vaga['titulo'], value = f"Atividades: {vaga['atividades']}\n\
                Requisitos: {vaga['requisitos']}\n\
                Destaques: {vaga['destaques']}\n\
                Ativo: {ativo}")
        
        #emb.set_thumbnail(url = sujeito.avatar_url)
        emb.set_footer(text="QUICKFIBRA", icon_url="http://www.quick.com.br//images/logo-quick.png")
        await ctx.send(embed=emb)

    @commands.command(help='Processo de criação de vaga')
    async def criar_vaga(self, ctx, vaga:Vaga):
        ret = db.vagas.insert_one(vaga.dict(by_alias=True))
        vaga.id = ret.inserted_id
        titulo_vaga = ctx.message.content.strip("$criar_vaga")
        await ctx.send("Quais atividades serão praticadas por essa vaga?")
        try:
            atividade = await self.bot.wait_for("message", check=lambda atividade: atividade.author == ctx.author, timeout=120.0)
        
        except asyncio.TimeoutError:
            await ctx.channel.send("Fui ignorado :(")
            return
        
        await ctx.send("Quais requisitos exigidos para essa vaga?")
        try:
            requisitos = await self.bot.wait_for("message", check=lambda requisitos: requisitos.author == ctx.author, timeout=120.0)
        
        except asyncio.TimeoutError:
            await ctx.channel.send("Fui ignorado :(")
            return

        await ctx.send("Quais destaques para essa vaga?")
        try:
            destaques = await self.bot.wait_for("message", check=lambda destaques: destaques.author == ctx.author, timeout=120.0)
        
        except asyncio.TimeoutError:
            await ctx.channel.send("Fui ignorado :(")
            return
        
        await ctx.send("Criar essa vaga habilitada vaga? (sim/não)")
        try:
            retorno = await self.bot.wait_for("message", check=lambda ativado: ativado.author == ctx.author, timeout=15.0)
            ativado = True if retorno.content.lower() == 'sim' else False
            if ativado:
                ativado_msg = 'sim'

        except asyncio.TimeoutError:
            await ctx.channel.send("Fui ignorado :(\nMas vou deixar a vaga habilitada!")
            ativado = True
            ativado_msg = 'sim'
        
        emb = discord.Embed(
            title = 'vaga',
            description = 'Nova vaga inserida no banco de dados!',
            color = discord.Color.blue()
        )
        emb.add_field(name = titulo_vaga, value = f"Atividades: {atividade.content}\n\
                Requisitos: {requisitos.content}\n\
                Destaques: {destaques.content}\n\
                Ativo: {ativado_msg}")

        await ctx.send(embed=emb)

        self.bot.collection.insert_one({"_id": sujeito.id, "username": sujeito.name, "xp": 0, "qbits": 25})

        """pesquisa = self.bot.collection.find_one({"_id": sujeito.id})
        if pesquisa:
            if amount > pesquisa["qbits"]:
                await ctx.send(f"@{sujeito.name} tem menos do que isso!")
                return
            if amount < 0:
                await ctx.send("Quantia precisa ser positiva!")
                return
            self.bot.collection.update_one({"_id": sujeito.id}, {"$inc": {"qbits": -amount}})
            await ctx.send(f"Você retirou {amount} qBits de @{sujeito.name}!")
            return

        self.bot.collection.insert_one({"_id": sujeito.id, "username": sujeito.name, "xp": 0, "qbits": 25})
        await ctx.send(f"@{sujeito.name} não possuía conta no banco. Acabamos de criar uma nova, com 25 qbits!")

        #emb.set_thumbnail(url = sujeito.avatar_url)
        emb.set_footer(text="QUICKFIBRA", icon_url="http://www.quick.com.br//images/logo-quick.png")
        await ctx.send(embed=emb)
"""
def setup(bot):
    bot.add_cog(MembrosCog(bot))

"""
######################################## MONGODB QUICK CHEATSHEET ######################################
import pymongo
from pymongo import MongoClient

cluster = MongoClient("url")

db = cluster['quickplay_db']

collection = db['discord']

usuario = {"_id": "12345", "xp": 0, "qbits": 25}

usuario_id = collection.insert_one(usuario).inserted_id

pesquisa = collection.find_one({"_id": usuario_id})

novo = 7
collection.update_one({"_id": usuario_id}, {"$inc": {"qbits": novo}})

"""