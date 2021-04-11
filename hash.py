import discord
from discord.ext import commands
import hashlib
import random

#encode şifrele
#decode çöz
colors=[0xeb4034,0x31e2e8,0x3e32e3,0xe332dd,0xe3e332]


@commands.command(aliases=["encode-md5"])
async def encode_md5(ctx,*args):
	"""encodes text with md5"""
	original_text="".join(args)
	hash_obj = hashlib.md5(original_text.encode())
	emb= discord.Embed(title="md5 encryption",description=f"original text is: {original_text} \nresult is: {hash_obj.hexdigest()}" ,color=random.choice(colors))
	await ctx.send(embed=emb)



@commands.command(aliases=["encode-sha256"])
async def encode_sha256(ctx,*args):
	"""encodes text with sha256 """
	original_text="".join(args)
	hash_obj = hashlib.sha256(original_text.encode())
	emb= discord.Embed(title="sha256 encryption",description=f"original text is: {original_text} \nresult is: {hash_obj.hexdigest()}",color=random.choice(colors))
	await ctx.send(embed=emb)


