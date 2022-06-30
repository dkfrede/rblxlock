from discord.ext import commands
from discord import Embed
import os
import sys; sys.path.append(".."); from user import tokenapi
def start():
    bot = commands.Bot(command_prefix='!')

    @bot.command(name='generate')
    async def fetchServerInfo(message,amount = 0):
        print("HEY")
        print(amount)
        if message.author.id == 734006395900264530:
            tokens = ''
            if int(amount) != 0:
                tokens = tokenapi.generateMultiTokens("user/tokens/",int(amount))
                print(tokens)
            else:
                tokens=tokenapi.generateNewToken('user/tokens/')
            embed = Embed(title="Generated new token!", description="You generated [a] new token(s):\n"+tokens+"", color=0x00ff00)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("Not allowed to do this!")
    bot.run('Nzc3MTUxNjYxNzYzOTg1NDE4.GvJzaY.EP8peeZ9Nmx_zEixU7TQ52s9VDP529UC-jwGtE')
