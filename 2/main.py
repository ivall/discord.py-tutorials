import config

from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType


bot = commands.Bot(command_prefix='$')
components = DiscordComponents(bot)


@bot.command()
async def test(ctx):
    await ctx.send("Przyciski", components=[Button(style=ButtonStyle.blue, label="test1", disabled=True),
                                            Button(style=ButtonStyle.red, label="test2")])
    res = await bot.wait_for("button_click")
    await res.respond(
        type=InteractionType.ChannelMessageWithSource,
        content=res.component.label
    )


bot.run(config.bot_token)