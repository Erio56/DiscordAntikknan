import os
import discord
import time
my_secret = os.environ['TOKEN']
intents = discord.Intents.default()
intents.members = True
intents.messages = True

miguel = "日日南Breast Apostle"
aiz = "Kurisu-tina / 日日南BreastNoble"

knanPJ = 日南
knan = Canan

kknanPj = 日日南
kknan = Cacanan

aizDesbasado = "Kurisu-tina / 日南BreastNoble"
miguelDesbasado = "日南Breast Apostle"

bot = discord.Client(intents=intents)
@bot.event
async def on_member_update(before, after):
    if(after.nick in knan):
        temp2 = after.nick.replace(knan,kknan)
        time.sleep(3)
        await after.edit(nick= temp2)

    if(after.nick in kknanPJ):
        temp =  after.nick.replace(knanPJ, kknanPj)
        time.sleep(3)   
        await after.edit(nick= temp)



bot.run(my_secret)