import os
import sys

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from util.models.rank import OverwatchRank


def test_fuzz_from_string_exact_match():
    assert OverwatchRank.fuzz_from_str("BRONZE_5") == OverwatchRank.BRONZE_5
    assert OverwatchRank.fuzz_from_str("SILVER_3") == OverwatchRank.SILVER_3
    assert OverwatchRank.fuzz_from_str("GM1") == OverwatchRank.GRANDMASTER_1
    assert OverwatchRank.fuzz_from_str("TOP_500") == OverwatchRank.TOP_500


def test_fuzz_from_string_fuzzy_match():
    assert OverwatchRank.fuzz_from_str("bronze 5") == OverwatchRank.BRONZE_5
    assert OverwatchRank.fuzz_from_str("b5") == OverwatchRank.BRONZE_5
    assert OverwatchRank.fuzz_from_str("silver 3") == OverwatchRank.SILVER_3
    assert OverwatchRank.fuzz_from_str("s3") == OverwatchRank.SILVER_3
    assert OverwatchRank.fuzz_from_str("grandmaster 1") == OverwatchRank.GRANDMASTER_1
    assert OverwatchRank.fuzz_from_str("grnd mstr 1") == OverwatchRank.GRANDMASTER_1
    assert (
        OverwatchRank.fuzz_from_str("grand master one") == OverwatchRank.GRANDMASTER_1
    )
    assert (
        OverwatchRank.fuzz_from_str("gwand mastwr owne") == OverwatchRank.GRANDMASTER_1
    )
    assert OverwatchRank.fuzz_from_str("top 500") == OverwatchRank.TOP_500
    assert OverwatchRank.fuzz_from_str("t500") == OverwatchRank.TOP_500
    assert OverwatchRank.fuzz_from_str("top five hundred") == OverwatchRank.TOP_500
    assert OverwatchRank.fuzz_from_str("top five hundwed") == OverwatchRank.TOP_500
