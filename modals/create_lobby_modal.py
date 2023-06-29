import nextcord
from util.models.game import Game


class CreateLobbyModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Create New Lobby",
            timeout=5 * 60,  # 5 minutes
        )

        self.lobby_name: str = None
        self.game: Game = None

        self.lobby_name_input = nextcord.ui.TextInput(
            placeholder="Enter your lobby name...",
            min_length=3,
            max_length=25,
            label="Lobby Name",
        )
        self.game_input = nextcord.ui.TextInput(
            min_length=3, label="Game", placeholder="OVERWATCH or VALORANT"
        )

        self.add_item(self.lobby_name_input)
        self.add_item(self.game_input)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        self.lobby_name = self.lobby_name_input.value
        self.game = Game.__members__.get(self.game_input.value.upper())
        self.stop()
