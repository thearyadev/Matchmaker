import os
import sys

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from util.models.game import Game


def test_fuzz_from_string():
    assert Game.fuzz_from_str("OVERWATCH") == Game.OVERWATCH
    assert Game.fuzz_from_str("OVER") == Game.OVERWATCH
    assert Game.fuzz_from_str("OVERW") == Game.OVERWATCH
    assert Game.fuzz_from_str("OVERWA") == Game.OVERWATCH
    assert Game.fuzz_from_str("OW") == Game.OVERWATCH
    assert Game.fuzz_from_str("VALORANT") == Game.VALORANT
    assert Game.fuzz_from_str("VAL") == Game.VALORANT
    assert Game.fuzz_from_str("VALOR") == Game.VALORANT
    assert Game.fuzz_from_str("VALORRANT") == Game.VALORANT
    assert Game.fuzz_from_str("VALORR") == Game.VALORANT
    assert Game.fuzz_from_str("VALORRAN") == Game.VALORANT
    assert Game.fuzz_from_str("VALORRANT") == Game.VALORANT
