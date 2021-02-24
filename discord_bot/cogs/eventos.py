import os
import random
import discord
from discord.ext import commands

class EventsCog(commands.Cog, name = "Eventos"):
    """ Docstrings (Cog Description) """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} se conectou ao servidor!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Você não tem permissão para isso espertinho!")
            #await ctx.message.delete()
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Por favor, coloque todos parâmetros.")
            #await ctx.message.delete()
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("Não entendi esse comando. :/\n!ajuda para comandos disponíveis.")
            #await ctx.message.delete()
        else:
            raise error

    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return

    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        ''' Mensagem no canal ao detectar uma mensagem deletada.'''
        print(f"{msg.author.name} apagou: {msg.content}") #debug no console, ainda não testei
        # futuramente, caso seja necessário, posso criar um log com mensagens deletadas (autor, data, etc)
        await msg.channel.send(content=f"@{msg.author.name}", file=discord.File("resources/msg_on_delete.png"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        #caso queira mensagem privada:
        #''' Mensagem de boas vindas privada.'''
        #await member.send('Olá! Seja bem vindo[a] ao servidor discord QUICKFIBRA!')
        
        channel = member.guild.system_channel # Esse canal é setado nas configurações dentro do servidor
        if channel is not None:
            await channel.send(f'Muito boas vindas {member.mention}!')


def setup(bot):
    bot.add_cog(EventsCog(bot))
