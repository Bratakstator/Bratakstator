import discord
from discord.ext import commands, tasks
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)
bot_id = 713805374242816060

@client.event
async def on_ready():
    print('Bot ready')
    await client.change_presence(activity=discord.Game(name="shit"))


@client.command()
async def load(ctx, extension):
    channel = client.get_channel(ctx.channel)
    client.load_extension(f'cogs.{extension}')
    await channel.send(f"{extension} loaded")


@client.command()
async def unload(ctx, extension):
    channel = client.get_channel(ctx.channel)
    client.unload_extension(f'cogs.{extension}')
    await channel.send(f"{extension} unloaded")


@client.command()
async def clear(ctx):
    print(f'User {ctx.author} in the server "{ctx.guild.name}" requested clearing of {ctx.channel} chat')
    await ctx.channel.purge(limit=5)

@client.command()
async def RDC(ctx):
    print(f'User {ctx.author} in the server "{ctx.guild.name}" requested Code for Remote Desktop Control')
    await ctx.channel.send("569 149 781")


@client.event
async def on_message(message):
    channel = client.get_channel(message.channel.id)
    if message.author.id != bot_id:
        if 'godt brukt' in message.content:
            print(
                f'User {message.author} in the server "{message.guild.name}" wrote "{message.content}" in {message.channel}')
            await channel.send("Morra di er godt brukt")

        if 'flink bot' in message.content:
            print(
                f'User {message.author} in the server "{message.guild.name}" wrote "{message.content}" in {message.channel}')
            await channel.send("Takk")

        if 'bot, hva har du gjort i dag' in message.content:
            print(
                f'User {message.author} in the server "{message.guild.name}" wrote "{message.content}" in {message.channel}')
            await channel.send("Morra di")
            await channel.send(file=discord.File('megdinmor.png'))

    await client.process_commands(message)


@client.event
async def on_member_join(member):
    channel = client.get_channel(821843297743667214)
    await channel.send(f'oi {member}, fuck off')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzEzODA1Mzc0MjQyODE2MDYw.XsldDw.TC1gCRfngfDD9DmDEU3DZDS_CTk')
