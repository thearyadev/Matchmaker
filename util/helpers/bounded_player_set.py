from dataclasses import dataclass
from util.models.role import Role
from typing import TypeVar, Generic, Set

T = TypeVar("T")

class PlayerDoesntExist(Exception):
    pass

class TeamIsFull(Exception):
    pass

class BoundedPlayerSet(Generic[T], Set[T]):
    def __init__(self, size: int, role: Role, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_size = size
        self.role = role

    def add(self, player):
        if len(self) < self.max_size:
            super().add(player)
        else:
            raise TeamIsFull(f"Team role [{self.role}] is full")

    def remove(self, player):
        if player in self:
            super().remove(player)
        else:
            raise PlayerDoesntExist("Player not in set")