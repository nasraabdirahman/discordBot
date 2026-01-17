import discord 
from discord.ext import commands # so the bot can have commands
import logging # logs to fix stuff
import os #so it runs on every os
from dotenv import loard_dotenv

#loads the env file
loard_dotenv()
#creates a permission set with basic disc bot permissions
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = command.Bot(command_prefix='!', intents =intents)

#handles user logging
@bot.event # funtion that runs once when bot sccessfully connects to discord
async def on_ready(): #listens to events
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.mention}!") #runs whenever someone joins the server

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if "shit" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} watch ur language!", delete_after = 5) 
        return # sends warning to same channel, mentions the user, auto-deletes after 5 seconds
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Gamer")
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f":white_check_mark: {ctx.author.mention} now has {role.name}")



@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Gamer")
    if role:
        await ctx.author.remove_roles(role) #pings/mentions the user who ran the command
        await ctx.send(f":white_check_mark: Removed {role.name}") #sends response message to same channel where command was used

@bot.command()
async def poll(ctx, *, question):
    msg = await ctx.send(f":bar_chart: **{question}**")
    await msg.add_reaction(":thumbsup:")
    await msg.add_reaction(":thumbsdown:")

@bot.command()
@commands.has_role("Gamer")
async def secret(ctx):
    await ctx.send("Welcome to the club!")


@secret.error #catches errors from that command only
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole): 
        await ctx.send("You need the Gamer role!")

bot.run(os.getenv('DISCORD_TOKEN')) #starts the bot using token from ENV variables  soo keeps bot running and listening for events/commands

