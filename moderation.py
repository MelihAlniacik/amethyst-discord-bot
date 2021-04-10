import discord
from discord.ext import commands 
import random


colors=[0xeb4034,0x31e2e8,0x3e32e3,0xe332dd,0xe3e332]


@commands.command()#mute
@commands.has_permissions(manage_messages=True)
async def mute(ctx,member: discord.Member,*,reason=None):
    """mutes the user"""
    guild= ctx.guild
    mutedRole= discord.utils.get(guild.roles,name="Muted")
    
    if not mutedRole:
        mutedRole= await guild.create_role(name="Muted")
        
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False , send_messages=False, read_message_history=True, read_messages=True)
    
    await member.add_roles(mutedRole,reason=reason)
    await ctx.send(f"{member.mention} is Muted for {reason}")        
    await member.send(f"you were muted in this server {guild.name} for {reason} ")

@commands.command()#unmute
@commands.has_permissions(manage_messages=True)
async def unmute(ctx,member:discord.Member):
    """unmutes the user"""
    mutedRole = discord.utils.get(ctx.guild.roles,name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"{member.mention} is Unmuted ") 
    await member.send(f"you were Unmuted in this server {guild.name} ")

@commands.command()
@commands.has_permissions(manage_messages=True)
async def clean(ctx, limit: int):
    """deletes messages"""
    await ctx.channel.purge(limit=limit)
    await ctx.send('Cleared by {}'.format(ctx.author.mention))
    await ctx.message.delete()





@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
    """Kicks user"""
    await user.kick(reason=reason)
    kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.channel.send(embed=kick)
    await user.send(embed=kick)






@commands.command()
@commands.has_permissions(kick_members=True)
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
    """Bans user"""
    await user.ban(reason=reason)
    ban = discord.Embed(title=f":boot: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
    await ctx.channel.send(embed=ban)
    await user.send(embed=ban)


@commands.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,user:discord.Member,*,reason="No reason provided"):
    """Unbans User"""
    banned_users= await ctx.guild.ban()
    member_name,member_disc= member.split("#")

    for banned_entry in banned_users:
        user= banned_entry.user

        if (user.name, user.discriminator)==(member_name,member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member.name+" has been unbaned")
            return
    await ctx.send(member+" was not found")


    


