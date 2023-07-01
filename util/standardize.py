from functools import cache


@cache
def standardize(string: str) -> str:
    return string.lower().replace("_", " ")
