import nextcord
from util.models.lobby import Lobby


class JoinLobbyView(nextcord.ui.View):
    def __init__(self, lobby: Lobby):
        super().__init__(timeout=None)
        self.lobby = lobby
    @nextcord.ui.button(label="Join", style=nextcord.ButtonStyle.green)
    async def join_lobby_button_handler(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.lobby.players.add(interaction.user)
        await interaction.response.send_message("nice")
