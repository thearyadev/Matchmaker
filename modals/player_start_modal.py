import nextcord
from util.models.rank import OverwatchRank
from util.models.role import Role


class PlayerStartModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Welcome to the lobby!",
            timeout=5 * 60,  # 5 minutes
        )
        self.role: Role = None
        self.rank: OverwatchRank = None

        self.role_input = nextcord.ui.TextInput(
            min_length=4,
            label="What role would you like to play?",
            placeholder="TANK, DAMAGE, or SUPPORT",
            required=True,
        )
        self.rank_input = nextcord.ui.TextInput(
            min_length=4, label="What is your rank? (Example: DIAMOND 5)", required=True
        )
        self.add_item(self.role_input)
        self.add_item(self.rank_input)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        self.role = Role.__members__.get(self.role_input.value.upper().strip())
        self.rank = OverwatchRank.__members__.get(
            "_".join(self.rank_input.value.upper().strip().split(" "))
        )
        self.stop()
