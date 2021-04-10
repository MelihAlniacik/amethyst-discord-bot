import discord
from discord.ext import commands
import praw
import random
from utils.tools import *

colors=[0xeb4034,0x31e2e8,0x3e32e3,0xe332dd,0xe3e332]

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='')

@commands.command()
async def subreddit(ctx,subreddit):
    """sends images from subreddit"""
    if ctx.channel.is_nsfw():
        subreddit=reddit.subreddit(subreddit)
        all_subs=[]
        top= subreddit.hot(limit=30)
        for submission in top:
            all_subs.append(submission)
    
        random_sub = random.choice(all_subs)
        name= random_sub.title
        url=random_sub.url

        emb= discord.Embed(title=name,color=random.choice(colors))
        emb.set_image(url=url)
        await ctx.send(embed=emb)
    else:
        await ctx.send(":x: You need to use this command in a nsfw channel!")

@commands.command()
async def meme(ctx):
    """sends meme from r/memes"""
    subreddit=reddit.subreddit("memes")
    all_subs=[]
    top= subreddit.hot(limit=30)
    for submission in top:
        all_subs.append(submission)
    
    random_sub = random.choice(all_subs)
    name= random_sub.title
    url=random_sub.url

    emb= discord.Embed(title=name,color=random.choice(colors))
    emb.set_image(url=url)
    await ctx.send(embed=emb)





@commands.command()
async def avatar(self, ctx, *,  avamember:discord.Member):
    """sends users avatar"""
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUr)


@commands.command()
async def say(ctx, *, message:str):
    """Make the bot say whatever you want it to say"""
    try:
        await ctx.message.delete()
    except:
        pass
    await ctx.send(message)


@commands.command()
async def f(ctx, *, text: commands.clean_content = None):
    """ Press F to pay respect """
    hearts = ['❤', '💛', '💚', '💙', '💜']
    reason = f"for **{text}** " if text else ""
    await ctx.send(f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")

@commands.command()
async def thiscommanddoesfuckingnothing(ctx):
    """It doesn't do a fucking thing (or does it? OwO)"""
    await ctx.send("Ha?")

@commands.command()
async def reverse(ctx, *, msg:str):
        """ffuts esreveR"""
        await ctx.send(msg[::-1])

@commands.command()
async def encodemorse(ctx, *, msg:str):
    """Encode something into morse code"""
    encoded_message = ""
    for char in list(msg.upper()):
        encoded_message += encode_morse[char] + " "
        await ctx.send(encoded_message)


@commands.command()
async def cowsay(ctx, type:str, *, message:str):
    """moo"""
    try:
        cow = cowList[type.lower()]
    except KeyError:
        await ctx.send("`{}` is not a usable character type. Run **{}cows** for a list of cows.".format(type, ctx.prefix))
        return
    msg = "```{}```".format(cow.milk(message))
    if len(msg) > 2000:
        await ctx.send("Sorry, the message length with the cow in it has a total character length of {}. Discord only allows 2000 characters per message.".format(len(msg)))
        return
    await ctx.send(msg)

@commands.command()
async def cows(ctx):
    """Cow list for the cowsay command"""
    await ctx.send("Current list of cows:```{}```".format(", ".join(cowList.keys())))



@commands.command(aliases=['howhot', 'hot'])
async def hotcalc(ctx, *, user: discord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")

@commands.command()
async def hug(ctx,member=None,*, reason=None):
    """Hug someone"""
    if member==None or member== ctx.author:
        await ctx.send("You are too lonely right? \n nevermind I am here for you dude let me hug you")
    else:
        if reason==None:
            embed=discord.Embed(title=f"{ctx.author} hugged {member}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} hugged you")            

        else:
            embed=discord.Embed(title=f"{ctx.author} hugged {member} for {reason}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} hugged you for {reason}")


@commands.command()
async def kiss(ctx,member=None,*, reason=None):
    """kiss someone"""
    if member==None or member== ctx.author:
        await ctx.send("You are too lonely right? \n nevermind I am here for you dude let me kiss you")
    else:
        if reason==None:
            embed=discord.Embed(title=f"{ctx.author} kissed {member}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} kissed you")            
            
        else:
            embed=discord.Embed(title=f"{ctx.author} kissed {member} for {reason}")
            await ctx.send(embed=embed)
            await member.send(f"{ctx.author} kissed you for {reason}")   




  


    