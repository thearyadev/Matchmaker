from dataclasses import dataclass
from uuid import UUID

import nextcord

from util.models.game import Game
from util.models.player import Player
from util.models.team import Team, balance_teams


@dataclass(slots=True)
class Lobby:
    id: UUID
    name: str

    owner: nextcord.User

    players: set[Player]

    team_one: Team
    team_two: Team

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
    rosters_message: nextcord.Message = None

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

    @staticmethod
    def sort_players(players: set[Player]) -> list:
        return sorted(players, key=lambda player: player.total_games, reverse=True)

    def flood(self):
        sorted_players: list[Player] = self.sort_players(
            self.players
        )  # sort players by total games played

        for player in sorted_players:  # add players to team one
            self.team_one.add(player)
            self.players.remove(player)  # remove player from lobby

        sorted_players: list[Player] = self.sort_players(self.players)

        for player in sorted_players:
            self.team_two.add(player)  #
            self.players.remove(player)  # remove player from lobby

        # remaining players were not selected, and are likely prime candiates for next round.

    def balance(self):
        balance_teams(self.team_one, self.team_two)

    def return_(self, player: Player):
        for player in self.team_one:
            self.players.add(player)
            self.team_one.remove(player)

        for player in self.team_two:
            self.players.add(player)
            self.team_two.remove(player)
