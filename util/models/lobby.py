from dataclasses import dataclass
from uuid import UUID
import nextcord
from util.models.game import Game
from util.models.player import Player


@dataclass
class Lobby:
    id: UUID
    name: str

    owner: nextcord.User

    players: set[Player]
    guild: nextcord.Guild
    game: Game

    category: nextcord.CategoryChannel = None

    lobby_text: nextcord.TextChannel = None
    lobby_voice: nextcord.VoiceChannel = None
    team1_voice: nextcord.VoiceChannel = None
    team2_voice: nextcord.VoiceChannel = None

    join_text: nextcord.TextChannel = None
    match_text: nextcord.TextChannel = None
    tools_text: nextcord.TextChannel = None

    join_message: nextcord.Message = None

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Lobby):
            return self.id == other.id
        return False

    async def create_channels(self):
        if self.category is None:
            self.category = await self.guild.create_category(
                f"{self.name} [{self.game.name}] [{self.id.hex[:4]}]"
            )

        if self.lobby_voice is None:
            self.lobby_voice = await self.category.create_voice_channel(name="lobby")

        if self.lobby_text is None:
            self.lobby_text = await self.category.create_text_channel("lobby")

        if self.team1_voice is None:
            self.team1_voice = await self.category.create_voice_channel("team-one")

        if self.team2_voice is None:
            self.team2_voice = await self.category.create_voice_channel("team-two")

        if self.join_text is None:
            self.join_text = await self.category.create_text_channel("join")

        if self.match_text is None:
            self.match_text = await self.category.create_text_channel("match")

        if self.tools_text is None:
            self.tools_text = await self.category.create_text_channel("tools")

    async def update_player_count(self):
        await self.join_message.edit(
            embed=nextcord.Embed(
                title="Welcome to the lobby!",
                description="Click the 'Join' button to join the lobby!",
                color=nextcord.Color.green(),
            )
            .add_field(name="Game", value=self.game.name)
            .add_field(name="Owner", value=self.owner.mention)
            .add_field(name="Lobby ID", value=self.id.hex[:4])
            .add_field(name="Number of Players", value=len(self.players))
        )
