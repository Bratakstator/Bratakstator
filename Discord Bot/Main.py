import discord
from discord.ext import commands, tasks
import os

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents)

@client.event
async def on_ready():
    print('Bot ready')
    await client.change_presence(activity=discord.Game(name="a game"))

@client.command()
async def load(ctx, extension): # Command for loading cogs
    channel = client.get_channel(ctx.channel)
    client.load_extension(f'cogs.{extension}')
    await channel.send(f"{extension} loaded")

@client.command()
async def unload(ctx, extension): # Command for unloading cogs
    channel = client.get_channel(ctx.channel)
    client.unload_extension(f'cogs.{extension}')
    await channel.send(f"{extension} unloaded")

@client.command()
async def clear(ctx): # when .clear is called in discord chat the bot will remove the last 5 messages.
    print(f'User {ctx.author} in the server "{ctx.guild.name}" requested clearing of {ctx.channel} chat') # Prints out that the command has been called in the terminal.
    await ctx.channel.purge(limit=5)

@client.event
async def on_message(message): # Bot will look for key-words on the server and respond to them.
    bot_id = 713805374242816060 # The id of this discord bot.
    channel = client.get_channel(message.channel.id)
    if message.author.id != bot_id: # Checks if the message sent in the discord server is from the bot or another user.
        if 'godt brukt' in message.content: # Checks if message contains the words 'godt brukt'
            print(
                f'User {message.author} in the server "{message.guild.name}" wrote "{message.content}" in {message.channel}')
            await channel.send("Morra di er godt brukt") # If the message contains 'godt brukt' it will be logged in the terminal and the respons will be sent to the discord server

        if 'flink bot' in message.content:
            print(
                f'User {message.author} in the server "{message.guild.name}" wrote "{message.content}" in {message.channel}')
            await channel.send("Takk")

        if 'bot, hva har du gjort i dag' in message.content:
            print(
                f'User {message.author} in the server "{message.guild.name}" wrote "{message.content}" in {message.channel}')
            await channel.send("Morra di")
            await channel.send(file=discord.File('megdinmor.png'))

    await client.process_commands(message) # processes the command so that the infinite loop will not stop the rest of the bot from working.

for filename in os.listdir('./cogs'): # Automatically loads cogs when the bot starts up.
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
client.run('TOKEN_HERE')
