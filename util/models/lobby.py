from dataclasses import dataclass
from uuid import UUID
@dataclass
class Lobby:
    id: UUID
    players: set

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Lobby):
            return self.id == other.id
        return False