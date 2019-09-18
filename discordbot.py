from discord.ext import commands
import os
import traceback
import random

from typing import List

bot = commands.Bot(command_prefix=';')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pongpongpong')


@bot.command()
async def houka(ctx):
    await ctx.send(':fire:')


@bot.command()
async def r1d100(ctx):
    dice_count: int = 1
    dice_men: int = 100
    dice_results: List[int] = []
    result_sum: int = 0

    result_sum = await roll(dice_count, dice_men, dice_results, result_sum)
    await ctx.send(result_sum)


async def roll(dice_count, dice_men, dice_results, result_sum):

    for i in range(dice_count):
        print('i:', i)
        result: int = random.randint(1, dice_men)
        dice_results.append(result)
        result_sum += dice_results[i]

    return result_sum


bot.run(token)
