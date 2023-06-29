import os
from uuid import uuid4

import nextcord
from dotenv import load_dotenv
from nextcord.ext import commands
from rich import print

from modals.create_lobby_modal import CreateLobbyModal
from modals.player_start_modal import PlayerStartModal
from util.models.lobby import Lobby
from views.join_lobby_view import JoinLobbyView

load_dotenv()
TESTING_GUILD_ID = 1042253802507616337  # Replace with your guild ID

bot = commands.Bot()


class Matchmaker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lobbies = set()

    @nextcord.slash_command(
        name="play", description="Join the lobby!", guild_ids=[TESTING_GUILD_ID]
    )
    async def play(self, interaction: nextcord.Interaction):
        # modal = PlayerStartModal()
        # await interaction.response.send_modal(modal)
        await interaction.response.send_message("Joining lobby...")

    @nextcord.slash_command(
        name="purge",
        description="Purge all lobbies",
        guild_ids=[TESTING_GUILD_ID],
    )
    async def purge(self, interaction: nextcord.Interaction):
        for channel in interaction.guild.channels:
            try:
                await channel.delete()
            except:
                pass

    @nextcord.slash_command(
        name="createlobby",
        description="Create a new lobby",
        guild_ids=[TESTING_GUILD_ID],
    )
    async def createlobby(self, interaction: nextcord.Interaction):
        createLobbyModal = CreateLobbyModal()
        await interaction.response.send_modal(createLobbyModal)
        await createLobbyModal.wait()
        if createLobbyModal.game is not None:
            lobby: Lobby = Lobby(
                id=uuid4(),
                players=set(),
                name=createLobbyModal.lobby_name,
                guild=interaction.guild,
                game=createLobbyModal.game,
                owner=interaction.user,
            )
            await lobby.create_channels()

            self.lobbies.add(lobby)
            lobby.join_message = await lobby.join_text.send(
                view=JoinLobbyView(lobby=lobby),
                embed=nextcord.Embed(
                    title="Welcome to the lobby!",
                    description="Click the 'Join' button to join the lobby!",
                    color=nextcord.Color.green(),
                )
                .add_field(name="Game", value=lobby.game.name)
                .add_field(name="Owner", value=lobby.owner.mention)
                .add_field(name="Lobby ID", value=lobby.id.hex[:4])
                .add_field(name="Number of Players", value=len(lobby.players)),
            )


bot.add_cog(Matchmaker(bot))
bot.run(os.getenv("TOKEN"))
