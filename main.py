import discord
from discord.ext import commands
from moderation import *
from fun import *
from economy import *   
import random as rndm
import json
from hash import*
import pyshorteners
from covid import*




colors=[0xeb4034,0x31e2e8,0x3e32e3,0xe332dd,0xe3e332]



bot = commands.Bot(command_prefix = "!",help_command=None)




@bot.command()
async def help(ctx,arg=None):
	"""I think you are already know this"""
	command_names_list = [x.name for x in bot.commands]
	embed= discord.Embed(title="amethyst bot's help")
	general_commands="`avatar`,`serverinfo`,`userinfo`,`ping`,`invite`,`covid`"
	fun_commands="`meme`,`say`,`f`,`thiscommanddoesfuckingnothing`,`reverse`,`encodemorse`,`cowsay`,`cows`,`hotcalc`,`encode_md5`,`encode_sha256`,`hug`,`kiss`,`subreddit`"
	economy_commands="`balance`,`beg`,`deposit`,`withdraw`,`rob`,`slot`,`send`,`shop`,`bag`,`buy`,`sell`,`coinflip`"
	moderation_commands="`mute`,`unmute`,`ban`,`unban`,`kick`"

	if arg==None:
		embed.add_field(name="general commands",value=general_commands,inline=False)
		embed.add_field(name="fun commands",value=fun_commands,inline=False)
		embed.add_field(name="economy commands",value=economy_commands,inline=False)
		embed.add_field(name="moderation commands",value=moderation_commands,inline=False)

		await ctx.send(embed=embed)
	elif arg in command_names_list:
		embed.add_field(
			name=f"!{arg}",
			value=bot.get_command(arg).help)
		await ctx.send(embed=embed)
	else:
		embed.add_field(
			name="Nope.",
			value="Don't think I got that command!"
		)
		await ctx.send(embed=embed)



@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Game(name="| !help to help"))
	print("bot is ready")



@bot.command()
async def ping(ctx):
    """sends ping"""
    await ctx.send(f"pong! {round(bot.latency * 1000)}ms")


@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member=None):
	"""Sends avatar"""
	if member is None:
		member = ctx.author
	await ctx.send("{}".format(member.avatar_url))


@bot.command()
async def invite(ctx):
	"""sends invite link"""
	emb=discord.Embed(title="invite link" ,description=f"Add me with this [link]({discord.utils.oauth_url(bot.user.id)})!")
	await ctx.send(embed=emb)
      

@bot.command()
async def bruh(ctx):
	"""sends bruh gif"""
	await ctx.send("https://tenor.com/6ruK.gif")


@bot.command()
async def welcome(ctx):
	"""sends welcome gifs"""
	gifs=["https://media1.tenor.com/images/f898731211184dca06f52005d7d0a166/tenor.gif?itemid=8846380",
		"https://media.tenor.com/images/578d96612b002bd7dc9096536efcee56/tenor.gif",
		"https://media.tenor.com/images/eba043bd8859df792aaec7a185ec6cdb/tenor.gif",
		"https://media.tenor.com/images/4f276e8211aac2be5f33000e42cfa1d1/tenor.gif",
		"https://media.tenor.com/images/7ab5c8247e639abe8a5bb6de0f2bcf76/tenor.gif",
		"https://media.tenor.com/images/aef6732e83b229e0a7b80f5a177c3aee/tenor.gif"]
	await ctx.send(rndm.choice(gifs))

@bot.command()
async def shorturl(ctx,link):
	"""shortens link"""
	s = pyshorteners.Shortener(api_key="API KEY")
	await ctx.send(s.bitly.short(link))
	
@bot.command()
async def serverinfo(ctx):
	"""sends server's info"""
	icon = str(ctx.guild.icon_url)
	name= ctx.guild.name
	region= ctx.guild.region
	verification= ctx.guild.verification_level	
	premiums=ctx.guild.premium_subscription_count
	channelnumber=len(ctx.guild.channels)
	voicenumber=len(ctx.guild.voice_channels)
	memberCount = str(ctx.guild.member_count)
	rolenumber=len(ctx.guild.roles)
	created=str(ctx.guild.created_at).split(".")[0]
	

	embed = discord.Embed(
      title=name + " Server Information",
      color=rndm.choice(colors)
    )

	embed.set_thumbnail(url=icon)
	embed.add_field(name="name", value=name, inline=True)
	embed.add_field(name="region", value=region, inline=True)	
	embed.add_field(name="verification", value=verification, inline=True)
	embed.add_field(name="premiums", value=premiums, inline=True)
	embed.add_field(name="text channels",value=channelnumber,inline=True)
	embed.add_field(name="voice channels",value=voicenumber,inline=True)
	embed.add_field(name="members",value=memberCount,inline=True)
	embed.add_field(name="roles",value=rolenumber,inline=True)
	embed.add_field(name="created at",value=created,inline=True)


	await ctx.send(embed=embed)


@bot.command()
async def userinfo(ctx, *, user: discord.Member = None):
	"""sends user's info"""
	if user is None:
		user = ctx.author      
	
	date_format = "%a, %d %b %Y %I:%M %p"
    
	joined_at=user.joined_at.strftime(date_format)
	created_at=user.created_at.strftime(date_format)
	
	embed = discord.Embed(color=rndm.choice(colors), description=user.mention)
	embed.set_author(name=str(user), icon_url=user.avatar_url)
	embed.set_thumbnail(url=user.avatar_url)
	embed.add_field(name="Joined", value=joined_at)
	members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
	embed.add_field(name="Registered", value=created_at)
	if len(user.roles) > 1:
		role_string = ' '.join([r.mention for r in user.roles][1:])
		embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
	perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
	embed.add_field(name="Guild permissions", value=perm_string, inline=False)
	embed.set_footer(text='ID: ' + str(user.id))
	return await ctx.send(embed=embed)


@bot.command()
async def servers(ctx):
	if ctx.author.id==735886435978182657:
		server_list=[]

		for i in range(0, len(bot.guilds), 10):
			embed = discord.Embed(title='Guilds', colour=0x7289DA)
			guilds = bot.guilds[i:i + 10]

		for guild in guilds:
			server_list.append(guild.name)

		embed.add_field(name="servers",value=server_list)
			

		await ctx.send(embed=embed)
	




bot.add_command(mute)
bot.add_command(unmute)
bot.add_command(subreddit)
bot.add_command(balance)
bot.add_command(beg)
bot.add_command(deposit)
bot.add_command(withdraw)
bot.add_command(rob)
bot.add_command(slot)
bot.add_command(clean)
bot.add_command(send)
bot.add_command(shop)
bot.add_command(bag)
bot.add_command(buy)
bot.add_command(sell)
bot.add_command(meme)
bot.add_command(encode_md5)
bot.add_command(encode_sha256)
bot.add_command(say)
bot.add_command(f)
bot.add_command(coinflip)
bot.add_command(kick)
bot.add_command(thiscommanddoesfuckingnothing)
bot.add_command(reverse)
bot.add_command(encodemorse)
bot.add_command(cowsay)
bot.add_command(cows)
bot.add_command(hotcalc)
bot.add_command(ban)
bot.add_command(unban)
bot.add_command(covid)
bot.add_command(hug)
bot.add_command(kiss)




bot.run("Token Here") 
