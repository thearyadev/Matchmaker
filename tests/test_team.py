import os
import sys

# Get the parent directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to sys.path
sys.path.append(parent_dir)

import random

from util.helpers.bounded_player_set import BoundedPlayerSet
from util.models.player import Player
from util.models.rank import OverwatchRank, ValorantRank
from util.models.role import Role
from util.models.team import (
    OverwatchTeam,
    ValorantTeam,
    balance_teams,
    mean_delta,
    shuffle,
)


def test_overwatch_team_initialization():
    team = OverwatchTeam(name="team_name")
    assert team.name == "team_name"
    assert isinstance(team.tank, BoundedPlayerSet)
    assert isinstance(team.damage, BoundedPlayerSet)
    assert isinstance(team.support, BoundedPlayerSet)
    assert team.tank.max_size == 1
    assert team.damage.max_size == 2
    assert team.support.max_size == 2


def test_valorant_team_initialization():
    team = ValorantTeam(name="team_name")
    assert team.name == "team_name"
    assert isinstance(team.players, BoundedPlayerSet)
    assert team.players.max_size == 5


def test_overwatch_add_player():
    team = OverwatchTeam(name="team_name")
    player = Player(
        user="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12
    )
    team.add(player)
    assert player in team


def test_valorant_add_player():
    team = ValorantTeam(name="team_name")
    player = Player(
        user="player", role=None, rank=ValorantRank.ASCENDANT_1, total_games=12
    )
    team.add(player)
    assert player in team


def test_overwatch_remove():
    team = OverwatchTeam(name="team_name")
    player = Player(
        user="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12
    )
    team.add(player)
    assert player in team
    team.remove(player)
    assert player not in team


def test_valorant_remove():
    team = ValorantTeam(name="team_name")
    player = Player(
        user="player", role=None, rank=ValorantRank.ASCENDANT_1, total_games=12
    )
    team.add(player)
    assert player in team
    team.remove(player)
    assert player not in team


def test_overwatch_iterable():
    team = OverwatchTeam(name="team_name")
    player = Player(
        user="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12
    )
    team.add(player)
    for player in team:
        assert player in team


def test_valorant_iterable():
    team = ValorantTeam(name="team_name")
    player = Player(
        user="player", role=None, rank=ValorantRank.ASCENDANT_1, total_games=12
    )
    team.add(player)
    for player in team:
        assert player in team


def test_overwatch_len():
    team = OverwatchTeam(name="team_name")
    player = Player(
        user="player", role=Role.TANK, rank=OverwatchRank.GRANDMASTER_1, total_games=12
    )
    team.add(player)
    assert len(team) == 1


def test_valorant_len():
    team = ValorantTeam(name="team_name")
    player = Player(
        user="player", role=None, rank=ValorantRank.ASCENDANT_1, total_games=12
    )
    team.add(player)
    assert len(team) == 1


def test_overwatch_mean_delta():
    team1 = OverwatchTeam(name="team_name")
    team2 = OverwatchTeam(name="team_name")
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


def test_valorant_mean_delta():
    team1 = ValorantTeam(name="team_name")
    team2 = ValorantTeam(name="team_name")
    player1 = Player(
        user="player1", role=None, rank=ValorantRank.ASCENDANT_1, total_games=12
    )
    player2 = Player(
        user="player2", role=None, rank=ValorantRank.ASCENDANT_1, total_games=12
    )
    team1.add(player1)
    team2.add(player2)
    assert mean_delta(team1, team2) == 0

    player3 = Player(
        user="player3",
        role=None,
        rank=ValorantRank.ASCENDANT_3,
        total_games=12,
    )
    player4 = Player(
        user="player4",
        role=None,
        rank=ValorantRank.ASCENDANT_3,
        total_games=12,
    )
    team1.add(player3)
    team2.add(player4)
    assert mean_delta(team1, team2) == 0
    player5 = Player(
        user="player5",
        role=None,
        rank=ValorantRank.DIAMOND_3,
        total_games=12,
    )
    player6 = Player(
        user="player6", role=None, rank=ValorantRank.BRONZE_3, total_games=12
    )
    team1.add(player5)
    team2.add(player6)
    assert mean_delta(team1, team2) == 3.9999999999999982


def test_overwatch_shuffle():
    team1 = OverwatchTeam(name="team1")
    team2 = OverwatchTeam(name="team2")

    for i in range(1, 100):
        player = Player(
            user=f"player{i}",
            role=Role(random.randint(1, 3)),
            rank=OverwatchRank(random.randint(1, 36)),
            total_games=12,
        )
        if i % 2 == 0:
            team1.add(player)
        else:
            team2.add(player)

    old_rank_delta = mean_delta(team1, team2)
    shuffle(team1, team2)
    new_rank_delta = mean_delta(team1, team2)
    assert len(team1) == len(team2)
    assert old_rank_delta != new_rank_delta # THIS IS RANDOM, SO IT CAN FAIL. 
    # RE-RUN THE TEST IF IT FAILS


def test_valorant_shuffle():
    team1 = ValorantTeam(name="team1")
    team2 = ValorantTeam(name="team2")

    for i in range(1, 100):
        player = Player(
            user=f"player{i}",
            role=None,
            rank=ValorantRank(random.randint(1, 25)),
            total_games=12,
        )
        if i % 2 == 0:
            team1.add(player)
        else:
            team2.add(player)

    old_rank_delta = mean_delta(team1, team2)
    shuffle(team1, team2)
    new_rank_delta = mean_delta(team1, team2)
    assert len(team1) == len(team2)
    assert old_rank_delta != new_rank_delta


def test_overwatch_balance():
    team1 = OverwatchTeam(name="team1")
    team2 = OverwatchTeam(name="team2")

    for i in range(1, 100):
        player = Player(
            user=f"player{i}",
            role=Role(random.randint(1, 3)),
            rank=OverwatchRank(random.randint(1, 36)),
            total_games=12,
        )
        if i % 2 == 0:
            team1.add(player)
        else:
            team2.add(player)

    balance_teams(team1, team2)
    assert len(team1) == len(team2)


def test_valorant_balance():
    team1 = ValorantTeam(name="team1")
    team2 = ValorantTeam(name="team2")

    for i in range(1, 100):
        player = Player(
            user=f"player{i}",
            role=None,
            rank=ValorantRank(random.randint(1, 25)),
            total_games=12,
        )
        if i % 2 == 0:
            team1.add(player)
        else:
            team2.add(player)

    balance_teams(team1, team2)
    assert len(team1) == len(team2)


def test_player_add_overflow_void():
    team1 = OverwatchTeam(name="team1")
    team2 = OverwatchTeam(name="team2")

    for i in range(1, 100):
        player = Player(
            user=f"player{i}",
            role=Role(random.randint(1, 3)),
            rank=OverwatchRank(random.randint(1, 36)),
            total_games=12,
        )
        if i % 2 == 0:
            team1.add(player)
        else:
            team2.add(player)

    assert len(team1) == len(team2)
