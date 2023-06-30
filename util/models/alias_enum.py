from enum import Enum
from functools import cache
from typing import Optional, Type, TypeVar

from fuzzywuzzy import fuzz

from util.standardize import standardize

T = TypeVar("T", bound="AliasEnum")


class AliasEnum(Enum):
    aliases: Optional[tuple[str]]

    def __new__(cls: Type[T], value: int, aliases: Optional[tuple[str]] = None):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.aliases = aliases
        return obj

    @classmethod
    @cache
    def fuzz_from_string(cls: Type[T], string: str) -> Type[T]:
        results: list[tuple[Type[T], int]] = list()
        for member in list(cls):
            for member_aliases in (member.name, *member.aliases):
                if (
                    score := fuzz.ratio(
                        standardize(member_aliases), standardize(string)
                    )
                ) >= 95:
                    return member
                results.append((member, score))
        return max(results, key=lambda value_pair: value_pair[-1])[0]
