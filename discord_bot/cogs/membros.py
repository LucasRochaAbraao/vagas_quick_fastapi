import os
import datetime
import discord
from discord.ext import commands

class MembrosCog(commands.Cog, name = "Membros"):
    """Comandos disponíveis para todos membros do servidor."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["vaga", "perfil"], help='Exibe um cartão (embed) com \
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
            emb.add_field(name = 'titulo', value = vaga['titulo'])
        
        #emb.set_thumbnail(url = sujeito.avatar_url)
        emb.set_footer(text="QUICKFIBRA", icon_url="http://www.quick.com.br//images/logo-quick.png")
        await ctx.send(embed=emb)


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