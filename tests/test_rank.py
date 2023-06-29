import sys
import os

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)
from util.models.rank import OverwatchRank

def test_fuzz_from_string_exact_match():
    assert OverwatchRank.fuzz_from_string("BRONZE_5") == OverwatchRank.BRONZE_5
    assert OverwatchRank.fuzz_from_string("SILVER_3") == OverwatchRank.SILVER_3
    assert OverwatchRank.fuzz_from_string("GM1") == OverwatchRank.GRANDMASTER_1

def test_fuzz_from_string_fuzzy_match():
    assert OverwatchRank.fuzz_from_string("bronze 5") == OverwatchRank.BRONZE_5
    assert OverwatchRank.fuzz_from_string("b5") == OverwatchRank.BRONZE_5
    assert OverwatchRank.fuzz_from_string("silver 3") == OverwatchRank.SILVER_3
    assert OverwatchRank.fuzz_from_string("s3") == OverwatchRank.SILVER_3
    assert OverwatchRank.fuzz_from_string("grandmaster 1") == OverwatchRank.GRANDMASTER_1
    assert OverwatchRank.fuzz_from_string("grnd mstr 1") == OverwatchRank.GRANDMASTER_1
