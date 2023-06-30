import os
import sys

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from util.models.team import Team
from util.models.player import Player
from util.models.rank import OverwatchRank
from util.models.role import Role

def test_initialization():
    team = Team("team_name")
    assert team.name == "team_name"
    assert isinstance(team.players, set)
    assert isinstance(team, set)

def test_add_player():
    team = Team("team_name")
    player = Player(name="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12)
    team.add_player(player)
    assert player in team.players

def test_remove():
    team = Team("team_name")
    player = Player(name="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12)
    team.add_player(player)
    assert player in team.players
    team.remove(player)
    assert player not in team.players

def test_iterable():
    team = Team("team_name")
    player = Player(name="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12)
    team.add_player(player)
    for player in team:
        assert player in team.players
    
def test_shuffle():
    """to be implemented"""
    ...

