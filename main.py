import os
from dotenv import load_dotenv
import discord


load_dotenv()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Lewis\'s Cyber Defense Club server!'
    )

    channel = client.get_channel(872376054612906014)
    member_count = len(client.users)
    await channel.send(
        f'Hi there {member.mention}, welcome to Cyber Defense Club! Please read our #rules and check out '
        f'our #roles section to become a member. If you need any assistance please ask for an '
        f'admin. ({member_count} members!)')


@client.event
async def on_message(message):
    print('Message from {0.author}: {0.content}'.format(message))
    if message.content[0] == '$':
        print(f'Attempting Command: {message.content}')


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


token = os.getenv('Token')
client.run(token)
bot.run(token)