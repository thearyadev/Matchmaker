from enum import Enum
from functools import cache
from typing import Any, Optional, Type, TypeVar

from fuzzywuzzy import fuzz

from util.standardize import standardize

T = TypeVar("T", bound="AliasEnum")


class AliasEnum(Enum):
    __slots__ = ()
    _aliases: Optional[tuple[str]]

    def __new__(cls: Type[T], value: int, aliases: Optional[tuple[str]] = None):
        obj = object.__new__(cls)
        obj._value_ = value
        obj._aliases = aliases
        return obj

    @classmethod
    @cache
    def fuzz_from_str(cls: Type[T], string: str) -> Type[T]:
        """Return the member of the enum that is most similar to the given string."""
        standardized_string: str = standardize(string)
        results: list[tuple[Type[T], int]] = (
            # iterate through all members of the enum
            # and fuzzy compare the string to the member and its aliases
            (member, fuzz.ratio(member_alias, standardized_string))
            for member in cls  # members
            for member_alias in {
                standardize(member.name),
                *member.aliases,
            }  # members and aliases
        )
        return max(results, key=lambda value_pair: value_pair[-1])[
            0
        ]  # most similar member

    @classmethod
    def closest_by_value(cls: Type[T], value: int | float) -> Type[T]:
        """Return the member of the enum with the closest value to the given value."""
        return min(cls, key=lambda member: abs(member.value - value))

    @classmethod
    def members(cls: Type[T]) -> list[Type[T]]:
        """Return a list of all members of the enum."""
        return list(cls)

    @property
    def aliases(self) -> tuple[str]:
        """Return the aliases of the member."""
        return self.name, *(self._aliases or tuple())
