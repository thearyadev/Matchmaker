import os
import sys

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from util.models.player import Player
from util.models.rank import OverwatchRank
from util.models.role import Role


def test_rank_value():
    player = Player(
        user="player",
        role=Role.DAMAGE,
        rank=OverwatchRank.GRANDMASTER_1,
        total_games=12,
    )
    assert isinstance(player.rank_value(), int)
    assert player.rank_value() == OverwatchRank.GRANDMASTER_1.value
