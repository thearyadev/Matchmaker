import nextcord
from dataclasses import dataclass
from util.models.role import Role
from util.models.rank import OverwatchRank


@dataclass
class Player:
    user: nextcord.User
    role: Role
    total_games: int
    rank: OverwatchRank

    def __hash__(self):
        return hash(self.user)

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.user == other.user
        return False
