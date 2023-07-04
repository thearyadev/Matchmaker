import nextcord

from modals.player_start_modal import (
    OverwatchPlayerStartModal,
    ValorantPlayerStartModal,
)
from util.models.game import Game
from util.models.lobby import Lobby
from util.models.player import Player


class TeamsLobbyOptionsView(nextcord.ui.View):
    def __init__(self, lobby: Lobby):
        super().__init__(timeout=None)
        self.lobby = lobby

    @nextcord.ui.button(label="Start Match", style=nextcord.ButtonStyle.green)
    async def join_lobby_button_handler(
        self, button: nextcord.ui.Button, interaction: nextcord.Interaction
    ):
        if len(self.lobby.players) > 10:
            await interaction.response.send_message(
                f"You need at least 10 players to start the match! (Current: {len(self.lobby.players)})",
                ephemeral=True,
            )
        self.lobby.flood()
        # self.lobby.balance()
        # show match info
        await self.lobby.rosters_message.edit(
            view=self,
            embed=nextcord.Embed(
                title="Welcome to the match!",
                description="The match has started!",
                color=nextcord.Color.green(),
            ).add_field(
                name="Team 1",
                value="\n".join(self.lobby.team_one.get_player_name_array_by_role()),
            ).add_field(
                name="Team 1",
                value="\n".join(self.lobby.team_one.get_player_name_array_by_role()),
            ),
        ),

        # move players
        for player in self.lobby.team_one:
            await player.user.move_to(self.lobby.team1_voice)
        for player in self.lobby.team_two:
            await player.user.move_to(self.lobby.team2_voice)
