import discord
from discord.ext import commands, tasks
import os
import math
from lottery.lotteryStats import LotteryStatistics

LOTTERY_HANDLE = '$llc.lottery'

TOKEN = os.getenv('TOKEN')
client = discord.Client(intents=discord.Intents(messages=True, message_content=True))


@client.event
async def on_ready():
    lottery_stats = LotteryStatistics(wallet_identifier=LOTTERY_HANDLE)
    update_status.start(lottery_stats)
    print("bot started")

@tasks.loop(seconds=300)
async def update_status(lottery_stats: LotteryStatistics):
    lottery_stats.wallet.update_balance()
    lottery_stats.tickets.update_tickets_minted()
    lottery_stats.set_prize_breakdown()
    jackpot = lottery_stats.breakdown['Match first 6']
    per_mask = lottery_stats.get_payout_per_mask()

    await client.change_presence(activity=discord.Activity(name=f'Total: {math.ceil(lottery_stats.wallet.get_balance())} \ Jackpot: {jackpot}\ Payout/Mask: {per_mask}', type=0))

@update_status.before_loop
async def before_update_status():
    await client.wait_until_ready()

@client.event
async def on_message(message):
    lottery_stats = LotteryStatistics()
    if message.author == client.user:
        return

    if message.content.startswith('$lotteryStats'):
        await message.channel.send('```\n' + repr(lottery_stats) + '\n```')


client.run(TOKEN)