from typing import Optional, Type, TypeVar

from fuzzywuzzy import fuzz

from util.models.alias_enum import AliasEnum

T = TypeVar("T", bound="Rank")


class Rank(AliasEnum):
    ...


class OverwatchRank(Rank):
    BRONZE_5 = 1, ["b5"]
    BRONZE_4 = 2, ["b4"]
    BRONZE_3 = 3, ["b3"]
    BRONZE_2 = 4, ["b2"]
    BRONZE_1 = 5, ["b1"]
    SILVER_5 = 6, ["s5"]
    SILVER_4 = 7, ["s4"]
    SILVER_3 = 8, ["s3"]
    SILVER_2 = 9, ["s2"]
    SILVER_1 = 10, ["s1"]
    GOLD_5 = 11, ["g5"]
    GOLD_4 = 12, ["g4"]
    GOLD_3 = 13, ["g3"]
    GOLD_2 = 14, ["g2"]
    GOLD_1 = 15, ["g1"]
    PLATINUM_5 = 16, ["p5"]
    PLATINUM_4 = 17, ["p4"]
    PLATINUM_3 = 18, ["p3"]
    PLATINUM_2 = 19, ["p2"]
    PLATINUM_1 = 20, ["p1"]
    DIAMOND_5 = 21, ["d5"]
    DIAMOND_4 = 22, ["d4"]
    DIAMOND_3 = 23, ["d3"]
    DIAMOND_2 = 24, ["d2"]
    DIAMOND_1 = 25, ["d1"]
    MASTER_5 = 26, ["m5"]
    MASTER_4 = 27, ["m4"]
    MASTER_3 = 28, ["m3"]
    MASTER_2 = 29, ["m2"]
    MASTER_1 = 30, ["m1"]
    GRANDMASTER_5 = 31, ["gm5"]
    GRANDMASTER_4 = 32, ["gm4"]
    GRANDMASTER_3 = 33, ["gm3"]
    GRANDMASTER_2 = 34, ["gm2"]
    GRANDMASTER_1 = 35, ["gm1"]
