import random
from dataclasses import dataclass, field

from util.models.player import Player
from util.helpers.bounded_player_set import BoundedPlayerSet, TeamIsFull, PlayerDoesntExist
from util.models.role import Role
from typing import Iterator


@dataclass
class Team:
    name: str
    tank: BoundedPlayerSet[Player] = field(default_factory=lambda: BoundedPlayerSet(size=1, role=Role.TANK))
    damage: BoundedPlayerSet[Player] = field(default_factory=lambda: BoundedPlayerSet(size=2, role=Role.DAMAGE))
    support: BoundedPlayerSet[Player] = field(default_factory=lambda: BoundedPlayerSet(size=2, role=Role.SUPPORT))

    def __contains__(self, player: Player) -> bool:
        return player in self.tank or player in self.damage or player in self.support

    def __iter__(self) -> Iterator[Player]:
        return iter(self.tank | self.damage | self.support)

    def __len__(self) -> int:
        return len(self.tank | self.damage | self.support)

    def __getitem__(self, index) -> Player:
        return list(self.tank | self.damage | self.support)[index]  # this is used for random.choice()

    def __repr__(self) -> str:
        return f"Team({self.name}, {self.tank | self.damage | self.support})"

    def add(self, player: Player) -> bool:
        try:
            match (player.role):
                case Role.TANK:
                    self.tank.add(player)
                case Role.DAMAGE:
                    self.damage.add(player)
                case Role.SUPPORT:
                    self.support.add(player)
            
            return True
        except TeamIsFull:
            return False


    def remove(self, player: Player) -> bool:
        try:
            match (player.role):
                case Role.TANK:
                    self.tank.remove(player)
                case Role.DAMAGE:
                    self.damage.remove(player)
                case Role.SUPPORT:
                    self.support.remove(player)
            return True
        except PlayerDoesntExist:
            return False

    def clear(self):
        self.tank.clear()
        self.damage.clear()
        self.support.clear()


    def rank_mean(self) -> float:
        return sum([player.rank_value() for player in self]) / len(self)

    def is_full(self):
        return len(self) == 5


def mean_delta(team_1: Team, team_2: Team) -> float:
    return abs(team_1.rank_mean() - team_2.rank_mean())


def shuffle(team1: Team, team2: Team):
    """Swaps one player from team1 with one player from team2 with the same role."""

    if (not team1.is_full()) and (not team2.is_full()):
        raise ValueError("Both teams must be full to shuffle.")
    
    player1: Player = random.choice(team1)
    team1.remove(player1)
    for p in team2:
        if p.role == player1.role:
            team2.remove(p)
            team2.add(player1)
            team1.add(p)
            return
