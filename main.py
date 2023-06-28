

import nextcord
from nextcord.ext import commands
from modals.player_start_modal import PlayerStartModal
from dotenv import load_dotenv
import os

load_dotenv()
TESTING_GUILD_ID = 1042253802507616337  # Replace with your guild ID

bot = commands.Bot()


class Matchmaker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @nextcord.slash_command(name="play", description="Join the lobby!", guild_ids=[TESTING_GUILD_ID])
    async def play(self, interaction: nextcord.Interaction):
        modal = PlayerStartModal()
        await interaction.response.send_modal(modal)

bot.add_cog(Matchmaker(bot))

bot.run(os.getenv("TOKEN"))
