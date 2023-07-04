import os
import sys

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)


from util.helpers.alias_enum import AliasEnum


def test_alias_enum_init():
    class TestEnum(AliasEnum):
        ONE = 1, ("one", "1")
        TWO = 2, ("two", "2")

    assert TestEnum.ONE.value == 1
    assert TestEnum.TWO.value == 2
    assert TestEnum.ONE.name == "ONE"
    assert TestEnum.TWO.name == "TWO"
    assert TestEnum.ONE.aliases == ("ONE", "one", "1")
    assert TestEnum.TWO.aliases == ("TWO", "two", "2")


def test_fuzz_from_string():
    class TestEnum(AliasEnum):
        ONE = 1, ("one", "1")
        TWO = 2, ("two", "2")

    assert TestEnum.fuzz_from_str("one") == TestEnum.ONE
    assert TestEnum.fuzz_from_str("1") == TestEnum.ONE
    assert TestEnum.fuzz_from_str("two") == TestEnum.TWO
    assert TestEnum.fuzz_from_str("2") == TestEnum.TWO

    assert TestEnum.fuzz_from_str("on") == TestEnum.ONE
    assert TestEnum.fuzz_from_str("o") == TestEnum.ONE
    assert TestEnum.fuzz_from_str("t") == TestEnum.TWO
    assert TestEnum.fuzz_from_str("tw") == TestEnum.TWO
    assert TestEnum.fuzz_from_str("")
