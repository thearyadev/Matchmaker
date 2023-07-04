from dataclasses import dataclass
from typing import Generic, Set, TypeVar

from util.models.role import Role

T = TypeVar("T")


class PlayerDoesntExist(Exception):
    pass


class TeamIsFull(Exception):
    pass


class BoundedPlayerSet(Generic[T], Set[T]):
    def __init__(self, size: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_size = size

    def add(self, player):
        if len(self) < self.max_size:
            super().add(player)
        else:
            raise TeamIsFull(f"Team is full")

    def remove(self, player):
        if player in self:
            super().remove(player)
        else:
            raise PlayerDoesntExist("Player not in set")
