import discord
from discord.ext import commands
import COVID19Py

@commands.command()
async def covid(ctx):
    """Sends global covid datas"""
    covid19 = COVID19Py.COVID19()

    datas=covid19.getLatest()

    confirmed=datas['confirmed']
    deaths=datas['deaths']
    recovered=datas['recovered']
    
    embed=discord.Embed(title="**COVID-19 stats**")
    embed.add_field(name=":microbe: Confirmed",value=confirmed)
    embed.add_field(name=":skull: Deaths",value=deaths)
    embed.add_field(name=":syringe: Recovered",value=recovered)
    embed.set_footer(text="These stats are not necessarily comprehensive, complete, accurate or up to date; none of this is professional or legal advice.")
    await ctx.send(embed=embed)