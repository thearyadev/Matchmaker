from enum import Enum
from typing import Optional, TypeVar, Type
from fuzzywuzzy import fuzz

T = TypeVar("T", bound="AliasEnum")

class AliasEnum(Enum):
    aliases: list[str]
    def __new__(cls: Type[T], value: int, aliases: Optional[list[str]] = None):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.aliases = aliases
        return obj

    @classmethod
    def fuzz_from_string(cls: Type[T], string: str) -> Type[T]:
        """Returns the enum member that best matches the given string."""
        standardised_string = cls.standardize(string) # standardize the user input
        members = list(cls) # get members as list

        best_match = None # best match found so far
        best_score = 0 # score of best match found so far
        for member in members: # iter members
            score = fuzz.ratio( # fuzz on the member name
                cls.standardize(member.name), standardised_string
            )
            if member.aliases: # if the member has aliases
                for alias in member.aliases: # iter aliases
                    alias_score = fuzz.ratio(cls.standardize(alias), standardised_string)
                    if alias_score > score: # if the score is better
                        score = alias_score

            if score > best_score: # if the score is better
                best_match = member
                best_score = score

        return best_match # return the best match
    
    @staticmethod
    def standardize(string: str) -> str:
        return string.upper().strip().replace(" ", "_")