from discord.ext import commands

from decorators import is_registered
from models.user import User
from config import bot_token

is_registered = commands.check(is_registered)

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Bot is now online.')


@bot.command()
@is_registered
async def ballance(ctx):
    user = User(ctx.author.id)

    await ctx.send(f"Your money: {user.get_money()}")


bot.run(bot_token)
