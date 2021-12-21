"""

    Jorge E. Campos II
    Cyber Defense Club Discord BOT
    Date: 12.20.21

"""

import logging
import os
from DiscordBot.botApis.googleApi import _googleApiClient, gSearch
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv


# python3 -m pip install -U discord.py[voice]

# Load all env vars
load_dotenv()
token = os.getenv('Token')
channel1 = int(os.getenv('welcome_channel'))
channel2 = int(os.getenv('role_channel'))

# Enable intents
intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# Logging
logging.basicConfig(filename='Bot.log', level=logging.INFO, format='%(asctime)s %(message)s')


# Displays start-up
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    logging.info('{} has connected to Discord'.format(bot.user.name))


# Displays a welcome message to member
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Lewis\'s Cyber Defense Club server!'
    )
    channel = bot.get_channel(channel1)
    member_count = len(bot.users)
    await channel.send(
        f'Hi there {member.mention}, welcome to Cyber Defense Club! Please read our #rules and check out '
        f'our #roles section to become a member. If you need any assistance please ask for an '
        f'admin. ({member_count} members!)')


# Display messages from users and look for commands


# Adds role to user based of reaction
@bot.event
async def on_raw_reaction_add(payload):
    channel = channel2
    if payload.channel_id != channel:
        return
    else:
        if str(payload.emoji) == '👾':
            role = 'Member'
            member = payload.member
            await member.add_roles(get(member.guild.roles, name=role))
            print(f'[+] Adding {member.nick} to member role!')
            logging.info('[+] Adding {} to member role!'.format(member.nick))
            await member.create_dm()
            await member.dm_channel.send(
                f'Hi {member.name}, thanks for becoming a member of the Cyber Defense Club!'
            )
        if str(payload.emoji) == '<:hackerman:882796534272516136>':
            role = 'Red Team'
            member = payload.member
            await member.add_roles(get(member.guild.roles, name=role))
            print(f'[+] Adding {member.nick} to red team role!')
            logging.info('[+] Adding {} to red team role!'.format(member.nick))
        if str(payload.emoji) == '🛡️':
            role = 'Blue Team'
            member = payload.member
            await member.add_roles(get(member.guild.roles, name=role))
            print(f'[+] Adding {member.nick} to blue team role!')
            logging.info('[+] Adding {} to blue team role!'.format(member.nick))
        if str(payload.emoji) == '📚':
            role = 'Law and Governance'
            member = payload.member
            await member.add_roles(get(member.guild.roles, name=role))
            print(f'[+] Adding {member.nick} to Law and Governance role!')
            logging.info('[+] Adding {} to Law and Governance role!'.format(member.nick))
        if str(payload.emoji) == '<:iusearchbtw:882799034077704192>':
            role = 'Architecture'
            member = payload.member
            await member.add_roles(get(member.guild.roles, name=role))
            print(f'[+] Adding {member.nick} to Architecture role!')
            logging.info('[+] Adding {} to Architecture role!'.format(member.nick))
        if str(payload.emoji) == '⌨':
            role = 'Software'
            member = payload.member
            await member.add_roles(get(member.guild.roles, name=role))
            print(f'[+] Adding {member.nick} to Software role!')
            logging.info('[+] Adding {} to Software role!'.format(member.nick))
        if str(payload.emoji) == '🐸':
            role = 'Management'
            member = payload.member
            await member.add_roles(get(member.guild.roles, name=role))
            print(f'[+] Adding {member.nick} to Management role!')
            logging.info('[+] Adding {} to Management role!'.format(member.nick))
        if str(payload.emoji) == '👴':
            role = 'Alumni'
            member = payload.member
            await member.add_roles(get(member.guild.roles, name=role))
            print(f'[+] Adding {member.nick} to Alumni role!')
            logging.info('[+] Adding {} to Alumni role!'.format(member.nick))
            await member.create_dm()
            await member.dm_channel.send(
                f'Hi {member.name}, thank you and welcome alumni!'
            )
        if str(payload.emoji) == '🦩':
            role = 'Order of The Purple Flamingo'
            member = payload.member
            await member.add_roles(get(member.guild.roles, name=role))
            print(f'[+] Adding {member.nick} to the Order of the Purple Flamingo!')
            logging.info('[+] Adding {} to the Order of the Purple Flamingo!'.format(member.nick))


# Errors are bad
@bot.event
async def on_error(event, *args):
    if event == 'on_message':
        logging.info('\nUnhandled message: {}\n'.format(args[0]))
    else:
        raise


@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")


@bot.command()
async def search(ctx, *args):
    query = ""
    for arg in args:
        query = query + " " + arg

    search_term = gSearch.FilterStopWords(query)
    await ctx.channel.send("\nSearching: {}".format(search_term))

    resp = _googleApiClient.google_search(search_term)

    del resp[3:]
    for title, link, snippet in resp:
        await ctx.channel.send("\nTitle: {}\nLink: {}\nSum: {}\n\n".format(title, link, snippet))


bot.run(token)
