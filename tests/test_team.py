import os
import sys

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

from util.models.team import Team, mean_delta, shuffle
from util.models.player import Player
from util.models.rank import OverwatchRank
from util.models.role import Role


def test_initialization():
    team = Team(name="team_name")
    assert team.name == "team_name"
    assert isinstance(team.players, set)
    assert isinstance(team, set)


def test_add_player():
    team = Team(name="team_name")
    player = Player(
        user="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12
    )
    team.add(player)
    assert player in team.players


def test_remove():
    team = Team(name="team_name")
    player = Player(
        user="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12
    )
    team.add(player)
    assert player in team.players
    team.remove(player)
    assert player not in team.players


def test_iterable():
    team = Team(name="team_name")
    player = Player(
        user="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12
    )
    team.add(player)
    for player in team:
        assert player in team.players


def test_len():
    team = Team(name="team_name")
    player = Player(
        user="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12
    )
    team.add(player)
    assert len(team) == 1


def test_mean_delta():
    team1 = Team(name="team_name")
    team2 = Team(name="team_name")
    player1 = Player(
        user="player1", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12
    )
    player2 = Player(
        user="player2", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12
    )
    team1.add(player1)
    team2.add(player2)
    assert mean_delta(team1, team2) == 0

    player3 = Player(
        user="player3",
        role=Role.SUPPORT,
        rank=OverwatchRank.GRANDMASTER_2,
        total_games=12,
    )
    player4 = Player(
        user="player4",
        role=Role.SUPPORT,
        rank=OverwatchRank.GRANDMASTER_2,
        total_games=12,
    )
    team1.add(player3)
    team2.add(player4)
    assert mean_delta(team1, team2) == 0
    player5 = Player(
        user="player5",
        role=Role.DAMAGE,
        rank=OverwatchRank.GRANDMASTER_1,
        total_games=12,
    )
    player6 = Player(
        user="player6", role=Role.DAMAGE, rank=OverwatchRank.BRONZE_5, total_games=12
    )
    team1.add(player5)
    team2.add(player6)
    assert mean_delta(team1, team2) == 11.333333333333332


def test_shuffle():
    team1 = Team(name="team1")
    team2 = Team(name="team2")

    # Add players to the teams
    player1 = Player(
        user="player1", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_2, total_games=12
    )
    player2 = Player(
        user="player2", role=Role.SUPPORT, rank=OverwatchRank.BRONZE_5, total_games=12
    )
    player3 = Player(
        user="player3", role=Role.DAMAGE, rank=OverwatchRank.SILVER_4, total_games=12
    )
    player4 = Player(
        user="player4", role=Role.TANK, rank=OverwatchRank.DIAMOND_5, total_games=12
    )
    player5 = Player(
        user="player5", role=Role.SUPPORT, rank=OverwatchRank.MASTER_2, total_games=12
    )
    player6 = Player(
        user="player6",
        role=Role.DAMAGE,
        rank=OverwatchRank.GRANDMASTER_5,
        total_games=12,
    )
    team1.add(player1)
    team1.add(player2)
    team1.add(player3)
    team2.add(player4)
    team2.add(player5)
    team2.add(player6)
    old_rank_delta = mean_delta(team1, team2)
    shuffle(team1, team2)
    new_rank_delta = mean_delta(team1, team2)
    assert len(team1) == len(team2)
    assert old_rank_delta != new_rank_delta

    assert set(
        [player1, player2, player3, player4, player5, player6]
    ) == team1.players.union(team2.players)
