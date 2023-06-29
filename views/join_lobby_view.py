import nextcord
from util.models.lobby import Lobby


class JoinLobbyView(nextcord.ui.View):
    def __init__(self, lobby: Lobby):
        super().__init__(timeout=None)
        self.lobby = lobby

    @nextcord.ui.button(label="Join", style=nextcord.ButtonStyle.green)
    async def join_lobby_button_handler(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        self.lobby.players.add(interaction.user)
        await self.lobby.update_player_count()
        await interaction.response.send_message(
            f"You've joined the lobby! Join {self.lobby.lobby_voice.mention} to get started.",
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
