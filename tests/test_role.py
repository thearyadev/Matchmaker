import os
import sys

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from util.models.role import Role


def test_fuzz_from_string():
    assert Role.fuzz_from_string("DPS") == Role.DAMAGE
    assert Role.fuzz_from_string("DAMAGE") == Role.DAMAGE
    assert Role.fuzz_from_string("Damg") == Role.DAMAGE
    assert Role.fuzz_from_string("TANK") == Role.TANK
    assert Role.fuzz_from_string("HEALER") == Role.SUPPORT
    assert Role.fuzz_from_string("SUPPORT") == Role.SUPPORT
    assert Role.fuzz_from_string("MAIN SUPPORT") == Role.SUPPORT
    assert Role.fuzz_from_string("FLEX SUPPORT") == Role.SUPPORT
    assert Role.fuzz_from_string("FS") == Role.SUPPORT
    assert Role.fuzz_from_string("MS") == Role.SUPPORT
    assert Role.fuzz_from_string("OFF TANK") == Role.TANK
    assert Role.fuzz_from_string("MAIN TANK") == Role.TANK
    assert Role.fuzz_from_string("OFFENSE") == Role.DAMAGE
