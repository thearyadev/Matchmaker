import nextcord

from util.models.rank import OverwatchRank, ValorantRank
from util.models.role import Role


class OverwatchPlayerStartModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Welcome to the lobby!",
            timeout=None,  # 5 minutes
        )
        self.role: Role = None
        self.rank: OverwatchRank = None

        self.role_input = nextcord.ui.TextInput(
            min_length=4,
            label="What role would you like to play?",
            required=True,
        )
        self.rank_input = nextcord.ui.TextInput(
            label="What is your rank?", required=True
        )
        self.add_item(self.role_input)
        self.add_item(self.rank_input)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        self.role = Role.fuzz_from_str(self.role_input.value)
        self.rank = OverwatchRank.fuzz_from_str(self.rank_input.value)
        self.stop()


class ValorantPlayerStartModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Welcome to the lobby!",
            timeout=None,  # 5 minutes
        )
        self.rank: ValorantRank = None

        self.rank_input = nextcord.ui.TextInput(
            label="What is your rank?", required=True
        )
        self.add_item(self.rank_input)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        self.rank = ValorantRank.fuzz_from_str(self.rank_input.value)
        self.stop()
