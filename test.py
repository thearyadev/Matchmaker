from util.models.rank import OverwatchRank
from util.models.team import Team, shuffle
from util.models.player import Player
from util.models.role import Role

import random

team1 = Team("Team 1")
team2 = Team("Team 2")

team1.add(Player(user="gnome", role=Role.TANK, total_games=0, rank=OverwatchRank.BRONZE_5))
team1.add(Player(user="gnome2", role=Role.SUPPORT, total_games=0, rank=OverwatchRank.BRONZE_5))

team2.add(Player(user="gnome3", role=Role.SUPPORT, total_games=0, rank=OverwatchRank.BRONZE_5))
team2.add(Player(user="gnome4", role=Role.DAMAGE, total_games=0, rank=OverwatchRank.BRONZE_5))

shuffle(team1, team2)
print(team1)
print(team2)
