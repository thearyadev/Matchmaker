import random
from dataclasses import dataclass

from util.models.player import Player


@dataclass
class Team(set):
    def __init__(self, name: str, *args, **kwargs):
        self.players: set[Player] = set()
        self.name: str = name

        super().__init__(*args, **kwargs)

    def __contains__(self, player):
        return player in self.players

    def __iter__(self):
        return iter(self.players)

    def __len__(self):
        return len(self.players)

    def __getitem__(self, index):
        return list(self.players)[index]  # this is used for random.choice()

    def __repr__(self):
        return f"Team({self.name}, {self.players})"

    def add(self, player: Player):
        self.players.add(player)

    def remove(self, player: Player):
        self.players.remove(player)

    def clear(self):
        self.players.clear()

    def rank_mean(self):
        return sum([player.rank_value() for player in self.players]) / len(self.players)


def mean_delta(team_1: Team, team_2: Team) -> float:
    return abs(team_1.rank_mean() - team_2.rank_mean())


def shuffle(team1: Team, team2: Team):
    """Swaps one player from team1 with one player from team2 with the same role."""
    player1: Player = random.choice(team1)
    team1.remove(player1)
    for p in team2:
        if p.role == player1.role:
            team2.remove(p)
            team2.add(player1)
            team1.add(p)
            return
