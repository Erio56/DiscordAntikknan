import os
import discord
import time
import string
my_secret = os.environ['TOKEN']
intents = discord.Intents.default()
intents.members = True
intents.messages = True

#listaDesbasadaM = ["日南BreastApostle","日 南Breast Apostle", "日'南BreastApostle", "日-南BreastApostle", "日''南Breast Apostle", "Hí南BreastApostle", "Hi南Breast Apostle"]
#ListaDesbasadaA = ["Kurisu-tina/日南BreastNoble", "Kurisu-tina / 日 南BreastNoble"]

miguel = "KK南Breast Apostle"
aiz = "Kurisu-tina / KK南BreastNoble"

#aizDesbasado = "Kurisu-tina / 日南BreastNoble"
#miguelDesbasado = "日南Breast Apostle"

bot = discord.Client(intents=intents)
@bot.event
async def on_member_update(before, after):
    #temp = after.nick
    #trimed = temp.translate(str.maketrans("", "",string.whitespace))
    #trimed = trimed.translate(str.maketrans("", "","'"))
    #trimed = trimed.translate(str.maketrans("", "",'*'))
    #print(trimed)

    #miguel

    if(after.id == 219659069244309505):
        if(after.nick != miguel):
            await after.edit(nick= miguel)
    #aiz
    if(after.id == 321036956589096960):
        if(after.nick != aiz):
            await after.edit(nick= aiz)


bot.run(my_secret)