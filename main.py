import platform
import time

import discord
from discord.ext import tasks, commands
import os
from dotenv import load_dotenv
from colorama import Back, Fore, Style

load_dotenv("settings.env")

my_guild = discord.Object(id=os.getenv("GUILD-ID"))

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=discord.Intents().all())

    async def setup_hook(self):
        for fileName in os.listdir('./cogs'):
            if fileName.endswith('.py'):
                await self.load_extension(f'cogs.{fileName[:-3]}')

        await self.tree.sync(guild=my_guild)

async def on_ready(self):
    prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC",
                                                    time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
    print(f"{prfx} Logged in as {Fore.YELLOW + self.user.name}")
    print(f"{prfx} Bot ID: {Fore.YELLOW + str(self.user.id)}")
    print(f"{prfx} Discord Version: {Fore.YELLOW + discord.__version__}")
    print(f"{prfx} Python Version: {Fore.YELLOW + str(platform.python_version())}")
    print(
        f"{prfx} Slash CMDs Synced: {Fore.YELLOW + str(len(await self.tree.fetch_commands(guild=my_guild)))} Commands")
    print(f"{prfx} Connected to: {Fore.YELLOW + str(len(self.guilds))} Guilds")


if __name__ == '__main__':
    client = Client()
    client.run(os.getenv("TOKEN"))