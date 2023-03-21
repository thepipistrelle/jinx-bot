#imports and stuff
import discord
import random
from discord.ext import commands

#set some variables
jinx = commands.Bot(command_prefix="*", intents = discord.Intents.all())

token = open("token.txt.", "r").read()

#commands
@jinx.command()
async def tarot(ctx, author, question):
    #read card file as lines and choose random line to output
    with open("jinx-bot\card.txt", "r") as file1:
        card_options = file1.read().splitlines()
        response_card = random.choice(card_options)
        card = str(response_card)
        print(card)
    #compare card to find corresponding description for the card chosen
    with open("jinx-bot\\upright.txt", "r") as file2, open("jinx-bot\\reversed.txt", "r") as file3:
        uprights=file2.readlines()
        reverseds=file3.readlines()

        for line in reverseds:
            if (card+" : ") in line:
                description = str(line)
                reading = (description.split(':', 1)[-1])
                print(reading)
            else:
                for line in uprights:
                    if (card+" : ") in line:
                        description = str(line)
                        reading = (description.split(':', 1)[-1])
                        print(reading)

        await ctx.send("your card : "+card+"\n"+"your card's reading : "+reading)

#start-up loads
@jinx.event
async def on_ready():
    print("jinx has entered the spectral wavelength")

#final run == do not put anything under here
jinx.run(token)