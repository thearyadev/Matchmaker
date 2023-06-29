import nextcord


class PlayerStartModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Welcome to the lobby!",
            timeout=5 * 60,  # 5 minutes
        )

        self.tank = nextcord.ui.TextInput(
            placeholder="Enter your favourite pet's name...",
            min_length=3,
            max_length=25,
            label="Pet's name",
        )
        self.add_item(self.tank)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        response = (
            f"{interaction.user.mention}'s favourite pet's name is {self.tank.value}."
        )
        await interaction.send(response)
