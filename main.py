import os
import discord
import time
my_secret = os.environ['TOKEN']
intents = discord.Intents.default()
intents.members = True
intents.messages = True

miguel = "日日南Breast Apostle"
aiz = "Kurisu-tina / 日日南BreastNoble"

aizDesbasado = "Kurisu-tina / 日南BreastNoble"
miguelDesbasado = "日南Breast Apostle"

bot = discord.Client(intents=intents)
@bot.event
async def on_member_update(before, after):
    if(after.nick == aizDesbasado ):
        time.sleep(3)
        await after.edit(nick= aiz)

    if(after.nick == miguelDesbasado):
        time.sleep(3)
        await after.edit(nick= miguel)



bot.run(my_secret)