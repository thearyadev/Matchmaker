

import nextcord
from nextcord.ext import commands
from modals.player_start_modal import PlayerStartModal
from dotenv import load_dotenv
import os
from views.join_lobby_view import JoinLobbyView
from util.models.lobby import Lobby
from rich import print
from uuid import uuid4

load_dotenv()
TESTING_GUILD_ID = 1042253802507616337  # Replace with your guild ID

bot = commands.Bot()


class Matchmaker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lobbies = set()
        
    @nextcord.slash_command(name="play", description="Join the lobby!", guild_ids=[TESTING_GUILD_ID])
    async def play(self, interaction: nextcord.Interaction):
        # modal = PlayerStartModal()
        # await interaction.response.send_modal(modal)
        print(self.lobbies)
        await interaction.response.send_message("Joining lobby...")
    
    @nextcord.slash_command(name="createlobby", description="Create a new lobby", guild_ids=[TESTING_GUILD_ID])
    async def createlobby(self, interaction: nextcord.Interaction):
        lobby: Lobby = Lobby(id=uuid4(), players=set())
        self.lobbies.add(lobby)
        view = JoinLobbyView(lobby=lobby)
        await interaction.response.send_message("Lobby created!", view=view)

bot.add_cog(Matchmaker(bot))
bot.run(os.getenv("TOKEN"))
