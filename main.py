import os
import discord
import time
import string
my_secret = os.environ['TOKEN']
intents = discord.Intents.default()
intents.members = True
intents.messages = True

listaDesbasadaM = ["日南BreastApostle","日 南Breast Apostle", "日'南BreastApostle", "日-南BreastApostle", "日''南Breast Apostle" ]
ListaDesbasadaA = ["Kurisu-tina/日南BreastNoble", "Kurisu-tina / 日 南BreastNoble"]

miguel = "日日南Breast Apostle"
aiz = "Kurisu-tina / 日日南BreastNoble"

#aizDesbasado = "Kurisu-tina / 日南BreastNoble"
#miguelDesbasado = "日南Breast Apostle"

bot = discord.Client(intents=intents)
@bot.event
async def on_member_update(before, after):
    temp = after.nick
    trimed = temp.translate(str.maketrans("", "",string.whitespace))
    trimed = trimed.translate(str.maketrans("", "","'"))
    trimed = trimed.translate(str.maketrans("", "",'*'))
    print(trimed)
    for i in range (len(ListaDesbasadaA)):
        if(trimed == ListaDesbasadaA[i]):
            print(ListaDesbasadaA[i])
            await after.edit(nick= aiz)
    for e in range(len(listaDesbasadaM)):
        if(trimed == listaDesbasadaM[e]):
            print(listaDesbasadaM[e])
            await after.edit(nick= miguel)


bot.run(my_secret)