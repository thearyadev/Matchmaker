import copy
import random
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass, field
from typing import Iterator, Self, Type, TypeVar

from util.helpers.bounded_player_set import (
    BoundedPlayerSet,
    PlayerDoesntExist,
    TeamIsFull,
)
from util.models.player import Player
from util.models.role import Role

T = TypeVar("T")


@dataclass
class Team(ABC):
    @abstractproperty
    def name(self) -> str:
        pass

    @abstractmethod
    def __contains__(self, player: Player) -> bool:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[Player]:
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> Player:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def add(self, player: Player) -> bool:
        """Adds a player to the team."""
        pass

    @abstractmethod
    def remove(self, player: Player) -> bool:
        """Removes a player from the team."""
        pass

    @abstractmethod
    def clear(self):
        """Removes all players from the team."""
        pass

    @abstractmethod
    def rank_mean(self) -> float:
        """Returns the mean rank of the team."""
        pass

    @abstractmethod
    def is_full(self) -> bool:
        """Returns True if the team is full, False otherwise."""
        pass

    @abstractmethod
    def demo_clone(self: T) -> T:
        """Returns a copy of the team with the same players."""
        pass

    def get_player_name_array_by_role(self) -> list[str]:
        result: list[str] = list()
        player: Player
        for player in sorted(self, key=lambda player: player.role):
            result.append(player.user.name)
        return result

@dataclass(slots=True)
class OverwatchTeam(Team):
    name: str

    tank: BoundedPlayerSet[Player] = field(
        default_factory=lambda: BoundedPlayerSet(size=1)
    )
    damage: BoundedPlayerSet[Player] = field(
        default_factory=lambda: BoundedPlayerSet(size=2)
    )
    support: BoundedPlayerSet[Player] = field(
        default_factory=lambda: BoundedPlayerSet(size=2)
    )
    cloned: bool = field(default=False)

    @property
    def name(self) -> str:
        return self.name

    def __contains__(self, player: Player) -> bool:
        return player in self.tank or player in self.damage or player in self.support

    def __iter__(self) -> Iterator[Player]:
        return iter(self.tank | self.damage | self.support)

    def __len__(self) -> int:
        return len(self.tank | self.damage | self.support)

    def __getitem__(self, index) -> Player:
        return list(self.tank | self.damage | self.support)[
            index
        ]  # this is used for random.choice()

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

    def is_full(self) -> bool:
        return len(self) == 5

    def demo_clone(self: T) -> T:
        team = type(self)(copy.copy(self.name))

        team.cloned = True
        team.tank = BoundedPlayerSet(size=1)
        team.damage = BoundedPlayerSet(size=2)
        team.support = BoundedPlayerSet(size=2)
        for player in self:
            team.add(player)
        return team

@dataclass(slots=True)
class ValorantTeam(Team):
    name: str
    players: BoundedPlayerSet[Player] = field(
        default_factory=lambda: BoundedPlayerSet(size=5)
    )
    cloned: bool = field(default=False)

    @property
    def name(self) -> str:
        return self.name

    def __contains__(self, player: Player) -> bool:
        return player in self.players

    def __iter__(self) -> Iterator[Player]:
        return iter(self.players)

    def __len__(self) -> int:
        return len(self.players)

    def __getitem__(self, index) -> Player:
        return list(self.players)[index]

    def __repr__(self) -> str:
        return f"Team({self.name}, {self.players})"

    def add(self, player: Player) -> bool:
        try:
            self.players.add(player)
            return True
        except TeamIsFull:
            return False

    def remove(self, player: Player) -> bool:
        try:
            self.players.remove(player)
            return True
        except PlayerDoesntExist:
            return False

    def clear(self):
        self.players.clear()

    def rank_mean(self) -> float:
        return sum([player.rank_value() for player in self]) / len(self)

    def is_full(self) -> bool:
        return len(self) == 5

    def demo_clone(self: T) -> T:
        team = type(self)(copy.copy(self.name))

        team.cloned = True
        team.players = BoundedPlayerSet(size=5)
        for player in self:
            team.add(player)
        return team


def mean_delta(team_1: Team, team_2: Team) -> float:
    return abs(team_1.rank_mean() - team_2.rank_mean())


def shuffle(team1: Team, team2: Team):
    """Swaps one player from team1 with one player from team2 with the same role."""

    if (not team1.is_full()) and (not team2.is_full()):
        raise ValueError("Both teams must be full to shuffle.")

    player1: Player = random.choice(team1)
    team1.remove(player1)
    for p in team2:
        if (
            p.role == player1.role
        ):  # no special case needs to be made. Valorant roles should be set to NONE.
            # in the future if we want to add more games, we can add a special case for each game.
            team2.remove(p)
            team2.add(player1)
            team1.add(p)
            return


def balance_teams(team1: Team, team2: Team, iterations: int = 60):
    if (not team1.is_full()) and (not team2.is_full()):
        raise ValueError("Both teams must be full to shuffle.")

    cloned_team1 = team1.demo_clone()
    cloned_team2 = team2.demo_clone()

    best_result: tuple[float, OverwatchTeam, OverwatchTeam] = (
        float("inf"),
        cloned_team1,
        cloned_team2,
    )  # store best results
    # init values are (inf, team1 (cloned), team2 (cloned))

    for _ in range(iterations):
        shuffle(cloned_team1, cloned_team2)

        if mean_delta(cloned_team1, cloned_team2) < best_result[0]:
            best_result = (
                mean_delta(cloned_team1, cloned_team2),
                cloned_team1.demo_clone(),
                cloned_team2.demo_clone(),
            )

    team1.clear()
    team2.clear()
    for player in best_result[1]:
        team1.add(player)
    for player in best_result[2]:
        team2.add(player)
