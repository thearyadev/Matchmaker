from dataclasses import dataclass

from util.models.player import Player


@dataclass
class Team:
    name: str
    players: set[Player]
