import pyowm
import discord
from  discord.ext import commands
from discord.ext.commands import Bot
owm = pyowm.OWM('cd1ce42897e0ce128723e6f7d8c20864')
observation = owm.weather_at_place('Ekaterinburg, RU')
w = observation.get_weather()

Bot = commands.Bot(command_prefix= '!')

@Bot.event
async def on_ready():
        print("Bot online")

@Bot.command(pass_context= True)
async def weather(ctx):
    await ctx.send(w)

Bot.run('NjA2NDAyOTYwMzk3OTU5MTY4.XUfoWw.VLnjeSZhnByygTakTTni51o2lcI')
