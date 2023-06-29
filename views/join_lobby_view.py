import nextcord

from modals.player_start_modal import PlayerStartModal
from util.models.lobby import Lobby
from util.models.player import Player


class JoinLobbyView(nextcord.ui.View):
    def __init__(self, lobby: Lobby):
        super().__init__(timeout=None)
        self.lobby = lobby

    @nextcord.ui.button(label="Join", style=nextcord.ButtonStyle.green)
    async def join_lobby_button_handler(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        modal = PlayerStartModal()
        await interaction.response.send_modal(modal=modal)
        await modal.wait()

        new_player = Player(
            user=interaction.user,
            role=modal.role,
            rank=modal.rank,
            total_games=0,
        )

        if new_player.rank is not None and new_player.role is not None:
            self.lobby.players.add(new_player)
            await self.lobby.update_player_count()
            await interaction.send(
                f"You've joined the lobby! Join {self.lobby.lobby_voice.mention} to get started.\n"
                f"Player Details: ```Name:{new_player.user.display_name}\nRank:{new_player.rank}\nRole:{new_player.role}```"
                "If something is wrong, click 'Join' again.",
                ephemeral=True,
            )
            return
        await interaction.followup.send(
            "Hmm. Something went wrong. Make sure you entered your rank and role correctly.",
            ephemeral=True,
        )

    @nextcord.ui.button(label="Close Lobby", style=nextcord.ButtonStyle.red)
    async def delete_lobby_button_handler(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        if interaction.user == self.lobby.owner:
            for channel in self.lobby.category.channels:
                await channel.delete()
            await self.lobby.category.delete()
