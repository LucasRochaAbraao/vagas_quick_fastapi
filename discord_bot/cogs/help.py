import discord
from discord.ext import commands

class HelpCog(commands.Cog, name = "Ajuda"):
    """Comandos disponíveis para todos membros do servidor."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, aliases=["help"], help='Exibir um cartão (embed) com \
    informações dos comandos de ajuda.')
    async def ajuda(self, ctx):
        emb = discord.Embed(title = "Ajuda", description = "Use !ajuda <comando> para mais informações sobre algum comando específico.\nOBS: <obrigatório> e [opcional]", color = ctx.author.color)
        emb.add_field(name = "Membros", value = "vagas")
        await ctx.send(embed = emb)

    @ajuda.command(name="vagas")
    async def _vagas(self, ctx):
        emb = discord.Embed(title = "Vaga", description = "Exibe um cartão (embed) com \
    informações de todas vagas, incluindo àquelas desativadas.", color = ctx.author.color)
        emb.add_field(name = "**sintaxe**", value = "!vagas")
        await ctx.send(embed = emb)


def setup(bot):
    bot.add_cog(HelpCog(bot))
