import os
import discord
from dotenv import load_dotenv
from discord.utils import get
import logging

# Load all env vars
load_dotenv()
token = os.getenv('Token')
channel1 = int(os.getenv('welcome_channel'))
channel2 = int(os.getenv('role_channel'))

# Enable intents
intents = discord.Intents.default()
intents.members = True
intents.reactions = True
client = discord.Client(intents=intents)

# Logging
logging.basicConfig(filename='Bot.log', level=logging.INFO, format='%(asctime)s %(message)s')


# Displays start-up
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    logging.info('{} has connected to Discord'.format(client.user.name))


# Displays a welcome message to member
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Lewis\'s Cyber Defense Club server!'
    )
    channel = client.get_channel(channel1)
    member_count = len(client.users)
    await channel.send(
        f'Hi there {member.mention}, welcome to Cyber Defense Club! Please read our #rules and check out '
        f'our #roles section to become a member. If you need any assistance please ask for an '
        f'admin. ({member_count} members!)')


# Display messages from users and look for commands
@client.event
async def on_message(message):
    if message.content[0] == '$':
        print(f'Attempting Command: {message.content}')
        logging.info('Attempting Command: {}'.format(message.content))
    if message.content == '$help':
        await message.channel.send('Here are the following commands {}:\n\n$help -Displays Commands'
                                   '\n$ping -Ping the bot\n\n More to come!'.format(message.author.mention))
    if message.content == '$ping':
        await message.channel.send('Pinging {}'.format(message.author.mention))
    if message.content == '$mute':
        print(f"Work in Progress")


# Adds role to user based of reaction
@client.event
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
@client.event
async def on_error(event, *args):
    if event == 'on_message':
        logging.info('\nUnhandled message: {}\n'.format(args[0]))
    else:
        raise


# Main
client.run(token)
