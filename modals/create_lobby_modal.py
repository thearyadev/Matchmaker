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
            min_length=3,
            max_length=10,
            label="Lobby Name",
        )
        self.game_input = nextcord.ui.TextInput(label="Game")

        self.add_item(self.lobby_name_input)
        self.add_item(self.game_input)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        self.lobby_name = self.lobby_name_input.value
        self.game = Game.fuzz_from_string(self.game_input.value)
        self.stop()
