import os
import discord
import time
my_secret = os.environ['TOKEN']
intents = discord.Intents.default()
intents.members = True
intents.messages = True

listaDesbasadaM = ["日南Breast Apostle", "Kurisu-tina / 日 南BreastNoble"]
ListaDesbasadaA = ["Kurisu-tina / 日南BreastNoble", "Kurisu-tina / 日 南BreastNoble",]

miguel = "日日南Breast Apostle"
aiz = "Kurisu-tina / 日日南BreastNoble"

#aizDesbasado = "Kurisu-tina / 日南BreastNoble"
#miguelDesbasado = "日南Breast Apostle"

bot = discord.Client(intents=intents)
@bot.event
async def on_member_update(before, after):
    for i in range (len(ListaDesbasadaA)):
        if(after.nick == ListaDesbasadaA[i]):
            time.sleep(3)
            await after.edit(nick= aiz)
    for e in range(len(listaDesbasadaM)):
        if(after.nick == listaDesbasadaM[e]):
            time.sleep(3)
            await after.edit(nick= miguel)


bot.run(my_secret)