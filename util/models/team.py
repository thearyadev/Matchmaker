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
