#imports and stuff
import discord
import random
from discord.ext import commands

#set some variables
salem = commands.Bot(command_prefix="*", intents = discord.Intents.all())

token = open("token.txt.", "r").read()

#commands
@salem.command()
async def tarot(ctx, author, question):
    #read card file as lines and choose random line to output
    with open("salem-bot\card.txt", "r") as file1:
        card_options = file1.read().splitlines()
        response_card = random.choice(card_options)
        card = str(response_card)
        print(card)
    #compare card to find corresponding description for the card chosen
    with open("salem-bot\description.txt", "r") as file2:
        descriptions = file2.readlines()
        for line in descriptions:
            if line.startswith(card):
                card_description = str(line)
                reading = (card_description.split(':', 1)[-1])
                print(reading)

                await ctx.send("your card : "+card+"\n"+"your card's reading : "+reading)

#start-up loads
@salem.event
async def on_ready():
    print("salem has entered the spectral wavelength")

#final run == do not put anything under here
salem.run(token)