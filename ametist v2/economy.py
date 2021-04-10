import discord
from discord.ext import commands
import json
import random


colors=[0xeb4034,0x31e2e8,0x3e32e3,0xe332dd,0xe3e332]



mainshop=[{"name":"Watch","price":100,"description":"time"},
{"name":"laptop","price":1000,"description":"work"},
{"name":"tv","price":1400,"description":"watch"},
{"name":"pc","price":2000,"description":"gaming"}
]


@commands.command(aliases=["bal"])
async def balance(ctx):
	"""sends balance info"""
	await open_account(ctx.author)

	user= ctx.author
	users = await get_bank_data()

	wallet_amt= users[str(user.id)]["wallet"]
	bank_amt= users[str(user.id)]["bank"]

	emb= discord.Embed(title=f"{ctx.author.name}'s balance",color=random.choice(colors))
	emb.add_field(name="Wallet balance",value=wallet_amt)
	emb.add_field(name="Bank balance",value=bank_amt)
	await ctx.send(embed=emb)


@commands.command()
async def beg(ctx):
	"""you beg someone"""
	await open_account(ctx.author)

	users= await get_bank_data()

	user= ctx.author


	earnings = random.randrange(101)

	await ctx.send(f"Someone gave you {earnings} coins!")

	users[str(user.id)]["wallet"] += earnings

	with open("mainbank.json","w") as f:
		json.dump(users,f)



@commands.command(aliases=["wd"])
async def withdraw(ctx,amount=None):
	"""withdraws money from bank"""
	await open_account(ctx.author)

	if amount== None:
		await ctx.send("Please enter the amount")
		return
	
	bal= await update_bank(ctx.author)

	amount= int(amount)
	if amount>bal[1]:
		await ctx.send("You dont have enough money")
		return

	if amount<0:
		await ctx.send("Amount is must be positive!")
		return 

	await update_bank(ctx.author,amount)	
	await update_bank(ctx.author,-1*amount,"bank") 

	await ctx.send(f"You withdrew {amount} coins!")	



@commands.command(aliases=["dp"])
async def deposit(ctx,amount=None):
	"""deposits money in the bank """
	await open_account(ctx.author)

	if amount== None:
		await ctx.send("Please enter the amount")
		return
	
	bal= await update_bank(ctx.author)

	amount= int(amount)
	if amount>bal[0]:
		await ctx.send("You dont have enough money")
		return

	if amount<0:
		await ctx.send("Amount is must be positive!")
		return 

	await update_bank(ctx.author,-1*amount)	
	await update_bank(ctx.author,amount,"bank") 

	await ctx.send(f"You you deposited {amount} coins!")	



@commands.command()
async def send(ctx,member:discord.Member,amount=None):
	"""sends money to user"""
	await open_account(ctx.author)
	await open_account(member)


	if amount== None:
		await ctx.send("Please enter the amount")
		return
	
	bal= await update_bank(ctx.author)

	if amount=="all":
		amount=bal[0]

	amount= int(amount)
	if amount>bal[1]:
		await ctx.send("You dont have enough money")
		return

	if amount<0:
		await ctx.send("Amount is must be positive!")
		return 

	await update_bank(ctx.author,-1*amount,"bank")	
	await update_bank(member,amount,"bank") 
	await member.send(f"{ctx.author} gave you {amount} coins")
	await ctx.send(f"You gave {amount} coins!")	


@commands.command()
async def slot(ctx,amount=None): #düzenlenicek
	"""bets"""
	await open_account(ctx.author)

	if amount== None:
		await ctx.send("Please enter the amount")
		return

	bal= await update_bank(ctx.author)

	amount= int(amount)
	if amount>bal[0]:
		await ctx.send("You dont have enough money")
		return

	if amount<0:
		await ctx.send("Amount must be positive")
		return

	emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
	a = random.choice(emojis)
	b = random.choice(emojis)
	c = random.choice(emojis)

	slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"    

	if (a == b == c):    
		await ctx.send(f"{slotmachine} All matching, you won! 🎉")
		await update_bank(ctx.author,2*amount)    

	elif (a == b) or (a == c) or (b == c):
		await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
		await update_bank(ctx.author,1.5*amount)
	else:
		await ctx.send(f"{slotmachine} No match, you lost 😢")
		await update_bank(ctx.author,-1*amount)
            

@commands.command(aliases=["coin","flip"])
async def coinflip(ctx,amount=None,side=None):
	"""coinflips"""
	await open_account(ctx.author)
	if amount== None:
		await ctx.send("Please enter the amount")
		return
	if side==None:
		await ctx.send("Please enter the side")
		return
	bal= await update_bank(ctx.author)

	amount= int(amount)
	if amount>bal[0]:
		await ctx.send("You dont have enough money")
		return

	if amount<0:
		await ctx.send("Amount must be positive")
		return

	coinsides = ['head', 'tail']
	result=random.choice(coinsides)
	

	if side in coinsides:
		if side==result:
			await ctx.send("you win")
			await update_bank(ctx.author,1*amount)    

		else :
			await ctx.send("you lose")
			await update_bank(ctx.author,-1*amount)    

	else:
		await ctx.send("please sure to write trutly")
	

@commands.command()
async def rob(ctx,member:discord.Member):
	"""robs the user"""
	await open_account(ctx.author)
	await open_account(member)


	bal= await update_bank(member)

	
	if bal[0]<100:
		await ctx.send("It's not worth it!")
		return

	earnings = random.randrange(0,bal[0])

	await update_bank(ctx.author,earnings)	
	await update_bank(member,-1*earnings,"wallet") 

	await ctx.send(f"You robbed and got {earnings} coins!")	


@commands.command()
async def shop(ctx):
	"""sends market"""
	emb=discord.Embed(title="shop", color=random.choice(colors))
	for item in mainshop:
		name= item["name"]
		price=item["price"]
		desc=item["description"]
		emb.add_field(name=name,value=f"${price}| {desc}")

	await ctx.send(embed=emb)



@commands.command()
async def buy(ctx,item,amount=1):
	"""buys item"""
	await open_account(ctx.author)

	res = await buy_this(ctx.author,item,amount)

	if not res[0]:
		if res[1]==1:
			await ctx.send("That's object isn't there")
			return
		if res[1]==2:
			await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
			
	await ctx.send(f"You just bought {amount} {item}")



@commands.command()
async def bag(ctx):
	"""opens bag"""
	await open_account(ctx.author)
	user = ctx.author
	users= await get_bank_data()

	try:
		bag= users[str(user.id)]["bag"]
	except:
		bag=[]

	emb= discord.Embed(title="bag",color=random.choice(colors))
	for item in bag:
		name= item["item"]
		amount= item["amount"]

		emb.add_field(name=name,value=amount)

	await ctx.send(embed=emb)
	

@commands.command()
async def sell(ctx,item,amount = 1):
	"""sells item"""
	await open_account(ctx.author)

	res = await sell_this(ctx.author,item,amount)

	if not res[0]:
		if res[1]==1:
			await ctx.send("That Object isn't there!")
			return
		if res[1]==2:
			await ctx.send(f"You don't have {amount} {item} in your bag.")
			return
		if res[1]==3:
			await ctx.send(f"You don't have {item} in your bag.")
			return

	await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9* item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            return [False,3]
    except:
        return [False,3]    

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]



async def buy_this(user,item_name,amount):
	item_name= item_name.lower()

	name_=item_name 

	for item in mainshop:
		name= item["name"].lower()
		if name==item_name:
			name_==name
			price=item["price"]
			break

	if name_==None:
		return[False,1]

	cost=price*amount
	print(cost)
	users= await get_bank_data()	

	bal = await update_bank(user)

	if bal[0]<cost:
		return[False,2]

	try:
		index=0
		t=None
		for thing in users[str(user.id)]["bag"]:
			n= thing["item"]
			if n== item_name:
				old_amt=thing["amount"]
				new_amt=old_amt+amount
				users[str(user.id)]["bag"][index]["amount"]=new_amt
				t=1
				break
			index+=1
		if t== None:
			obj={"item":item_name,"amount":amount}
			users[str(user.id)]["bag"].append(obj)
	except:
		obj= {"item":item_name,"amount":amount}
		users[str(user.id)]["bag"]=[obj]	
	
	with open("mainbank.json","w")as f:
		json.dump(users,f)	

	await update_bank(user,cost*-1,"wallet")

	return[True,"Worked"]


async def open_account(user):
	with open("mainbank.json","r") as f:
		users = json.load(f)

	if str(user.id) in users:
		return False
	else:
		users[str(user.id)]={}
		users[str(user.id)]["wallet"] =0
		users[str(user.id)]["bank"]=0

	with open("mainbank.json","w") as f:
		json.dump(users,f)
	return True



async def get_bank_data():
	with open("mainbank.json","r") as f:
		users = json.load(f)

	return users



	
async def update_bank(user,change=0,mode="wallet"):
	users = await get_bank_data()

	users[str(user.id)][mode] += change

	with open("mainbank.json","w") as f:
		json.dump(users,f)
	
	bal= [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
	return bal



