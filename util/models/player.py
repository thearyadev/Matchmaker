from dataclasses import dataclass
from typing import Optional

import nextcord

from util.models.rank import OverwatchRank
from util.models.role import Role


@dataclass(slots=True)
class Player:
    user: nextcord.User
    role: Optional[Role]
    total_games: int
    rank: OverwatchRank

    def __hash__(self):
        return hash(self.user)

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.user == other.user
        return False

    def rank_value(self) -> int:
        return self.rank.value
