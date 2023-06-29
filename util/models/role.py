from typing import Optional, Type, TypeVar

from fuzzywuzzy import fuzz

from util.models.alias_enum import AliasEnum

T = TypeVar("T", bound="Role")


class Role(AliasEnum):
    aliases: list[str]
    DAMAGE = 1, ["dps", "offense"]
    TANK = 2, ["main tank", "off tank"]
    SUPPORT = 3, ["healer", "main support", "flex support", "fs", "ms"]
