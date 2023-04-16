import discord
from discord import app_commands
from discord.ext import commands

class initiate(commands.Cog):

    def __init__(self, bot = commands.Bot):
        self.bot = bot


    @app_commands.command(name="colorpicker", description="Start the colorpicker.")
    async def start_colorpicker(self, interaction: discord.Interaction):
        await interaction.response.send_message("colorpicker")


async def setup(bot):
    await bot.add_cog(initiate(bot))