import os
import sys

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from util.models.game import Game


def test_fuzz_from_string():
    assert Game.fuzz_from_string("OVERWATCH") == Game.OVERWATCH
    assert Game.fuzz_from_string("OVER") == Game.OVERWATCH
    assert Game.fuzz_from_string("OVERW") == Game.OVERWATCH
    assert Game.fuzz_from_string("OVERWA") == Game.OVERWATCH
    assert Game.fuzz_from_string("OW") == Game.OVERWATCH
    assert Game.fuzz_from_string("VALORANT") == Game.VALORANT
    assert Game.fuzz_from_string("VAL") == Game.VALORANT
    assert Game.fuzz_from_string("VALOR") == Game.VALORANT
    assert Game.fuzz_from_string("VALORRANT") == Game.VALORANT
    assert Game.fuzz_from_string("VALORR") == Game.VALORANT
    assert Game.fuzz_from_string("VALORRAN") == Game.VALORANT
    assert Game.fuzz_from_string("VALORRANT") == Game.VALORANT
