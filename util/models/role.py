from typing import Optional, Type, TypeVar

from fuzzywuzzy import fuzz

from util.helpers.alias_enum import AliasEnum

T = TypeVar("T", bound="Role")


class Role(AliasEnum):
    DAMAGE = 1, ("dps", "offense")
    TANK = 2, ("main tank", "off tank")
    SUPPORT = 3, ("healer", "main support", "flex support", "fs", "ms")
