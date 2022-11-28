
from discord.ext import commands     
from discord.ext.commands import Bot 
from os import system               
from os import name                 
from colorama import *               
import discord                       
import aiohttp                       
import random    
import datetime
import requests               
#Put your buyer, admin and owner ids in this also add bot token.
buyers  = [0000000, 0000000,0000000 ]              
admins  = [0000000, 0000000, 0000000]              
owners  = [0000000, 0000000, 0000000]              
token   = 'bot token here'                 
bot     = commands.Bot(command_prefix='.')
# here is where to enter the placeholders that people may enter when using the bot.
methods = ['ADDUSER', 'REMOVEUSER', 'CREATESERVER', 'DELETESERVER']            

api_data = [
    {
        'api_url':'https://vanish.sh/Endpoints/apistart.php?key=', 
        'api_key':'ihsdfih298BGD',              
                      
    }
]

async def random_color():
    number_lol = random.randint(1, 999999)

    while len(str(number_lol)) != 6:
        number_lol = int(str(f'{random.randint(1, 9)}{number_lol}'))

    return number_lol

@bot.command()
async def add_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif buyer in buyers:
        await ctx.send(f'{buyer} has already bought a spot!')

    elif buyer is None:
        await ctx.send('Please provide a buyer!!')

    else:
        buyers.append(buyer)
        await ctx.send('Added them!!')

@bot.command()
async def del_buyer(ctx, buyer : int = None):
    if ctx.author.id not in admins:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an admin!')

    elif buyer not in buyers:
        await ctx.send(f'{buyer} did not buy a spot!')

    elif buyer is None:
        await ctx.send('Please give a buyer!!')

    else:
        buyers.remove(buyer)
        await ctx.send('Removed them!!')
        
@bot.command()
async def add_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')

    elif admin in admins:
        await ctx.send(f'{admin} is already an admin!')

    elif admin is None:
        await ctx.send('Please give an admin!!')

    else:
        admins.append(admin)
        await ctx.send('Added him/her!!')

@bot.command()
async def del_admin(ctx, admin : int = None):
    if ctx.author.id not in owners:
        await ctx.send(f'Sorry, {ctx.author}, but you aren\'t an owner!')

    elif admin not in admins:
        await ctx.send(f'{admin} is not an admin')

    elif admin is None:
        await ctx.send('Please give an admin!!')

    else:
        admins.remove(admin)
        await ctx.send('Removed him/her!!')

    

@bot.command()
async def send(ctx, method : str = None, host1 : str = None, port : str = None, time : str = None):
    if ctx.author.id not in buyers: # They didn't buy the bot!!
        await ctx.send('Sorry, but you need to buy a spot!')

    else:
        if method is None or method.upper() == 'Help':
            methodstr = ''

            for m in methods:
                methodstr = f'{methodstr}{m}\n'

         

            embed = discord.Embed(title="HELP", description="Help Menu", color=await random_color())
            embed.add_field(name="Syntax:", value=".send <variable> <target> <port> ")
            embed.add_field(name="METHODS:", value=f"{methodstr}")
          

            await ctx.send(embed=embed)

        # There was no method
        elif method is None:
            await ctx.send('You need a method!')
            
        # The method was invalid!
        elif method.upper() not in methods:
            await ctx.send(f'Invalid Variable!!')

        # There was no host
        elif host1 is None:
            await ctx.send('You need a target!')

        # There was no port
        elif port is None:
            await ctx.send('You need a port!')

        # Everything is correct!
        else:
            for i in api_data:
                try:
                    api_url = i["api_url"]
                    api_key = i["api_key"]

                   

                    async with aiohttp.ClientSession() as session:
                        #You can edit this to whichever format your link is in.
                        await session.get(f"{api_url}{api_key}&host={host1}&port={port}&method={method}&username=")

                        #print(f'{api_url}{api_key}&host={host1}&time={time2}&port={[port]}&method={method.upper()}')

                except Exception as e:
                    #print(e)
                    pass

            embed = discord.Embed(
                title = 'API Request Sent                ',
                color = await random_color()
            )
            embed.set_footer(text='Vanish Services',
            icon_url = 'https://media.discordapp.net/attachments/975792833862717450/976619016984592434/c3.jpg')
            embed.set_image(url ='https://cdn.discordapp.com/attachments/975792833862717450/976336821942382622/28FD5650-F231-458B-BDA8-EC2D4A2CBC27.jpg')
            embed.add_field(name='Field', value=f'{victim}', inline=False)
            embed.add_field(name='Field', value=f'{port}', inline=False)
            embed.add_field(name='Field', value=f'{time}', inline=False)
            embed.add_field(name='Field', value=f'{method}', inline=False)
            

            

            await ctx.send(embed=embed)

    if name == 'nt':
        system('cls')

    else:
        system('clear')

    print(f'{Fore.RED}Logged in on {Fore.YELLOW}{bot.user.name}{Fore.GREEN}! My ID is {Fore.BLUE}{bot.user.id}{Fore.MAGENTA}, I believe!{Fore.RESET}\n')
    
    if str(len(bot.guilds)) == 1:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} server!"))
        
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(bot.guilds)} servers!"))

if __name__ == '__main__':
    init(convert=True)
    bot.run(token)
