import discord
import time
from decouple import config

intents = discord.Intents.default()
intents.members = True
intents.messages = True

miguel = "日日南Breast Apostle"
aiz = "Kurisu-tina / 日日南BreastNoble"

bot = discord.Client(intents=intents)
@bot.event
async def on_member_update(before, after):
    if(after.nick == "Kurisu-tina / 日南BreastNoble" ):
        time.sleep(10)
        await after.edit(nick= aiz)

    if(after.nick == "日南Breast Apostle"):
        time.sleep(10)
        await after.edit(nick= miguel)



bot.run(config('TOKEN'))