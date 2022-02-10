import discord 
from discord.ext import commands 
import tokens 

intents = discord.Intents.default()
intents.members = True 
bot = commands.Bot(command_prefix='/', intents = intents)  

@bot.command() 
async def info(context):
    server_name = str(context.guild.name) 
    description = str(context.guild.description) 
    owner_name = str(context.guild.owner) 
    id = str(context.guild.id) 
    icon = str(context.guild.icon_url) 
    members = str(context.guild.member_count) 

    embed = discord.Embed(
        title = server_name, 
        description = description, 
        color = discord.Color.dark_green() 
    )

    embed.set_thumbnail(url = icon) 
    embed.add_field(name="Owner Name", value=owner_name) 
    embed.add_field(name="ID", value=id) 
    embed.add_field(name="Member Count", value=members)

    await context.send(embed = embed)

token = tokens.TOKEN
bot.run(token)