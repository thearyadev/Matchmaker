from enum import Enum
from util.models.alias_enum import AliasEnum


class Game(AliasEnum):
    OVERWATCH = 1, ("ow", "over watch")
    VALORANT = 2, ("val", "valor")
