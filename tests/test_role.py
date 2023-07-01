import os
import sys

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from util.models.role import Role


def test_fuzz_from_string():
    assert Role.fuzz_from_str("DPS") == Role.DAMAGE
    assert Role.fuzz_from_str("DAMAGE") == Role.DAMAGE
    assert Role.fuzz_from_str("Damg") == Role.DAMAGE
    assert Role.fuzz_from_str("TANK") == Role.TANK
    assert Role.fuzz_from_str("HEALER") == Role.SUPPORT
    assert Role.fuzz_from_str("SUPPORT") == Role.SUPPORT
    assert Role.fuzz_from_str("MAIN SUPPORT") == Role.SUPPORT
    assert Role.fuzz_from_str("FLEX SUPPORT") == Role.SUPPORT
    assert Role.fuzz_from_str("FS") == Role.SUPPORT
    assert Role.fuzz_from_str("MS") == Role.SUPPORT
    assert Role.fuzz_from_str("OFF TANK") == Role.TANK
    assert Role.fuzz_from_str("MAIN TANK") == Role.TANK
    assert Role.fuzz_from_str("OFFENSE") == Role.DAMAGE
