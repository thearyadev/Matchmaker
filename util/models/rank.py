from typing import Optional, Type, TypeVar

from fuzzywuzzy import fuzz

from util.models.alias_enum import AliasEnum

T = TypeVar("T", bound="Rank")


class Rank(AliasEnum):
    ...


class OverwatchRank(Rank):
    BRONZE_5 = 1, ("b5", "bronze five")
    BRONZE_4 = 2, ("b4", "bronze four")
    BRONZE_3 = 3, ("b3", "bronze three")
    BRONZE_2 = 4, ("b2", "bronze two")
    BRONZE_1 = 5, ("b1", "bronze one")
    SILVER_5 = 6, ("s5", "silver five")
    SILVER_4 = 7, ("s4", "silver four")
    SILVER_3 = 8, ("s3", "silver three")
    SILVER_2 = 9, ("s2", "silver two")
    SILVER_1 = 10, ("s1", "silver one")
    GOLD_5 = 11, ("g5", "gold five")
    GOLD_4 = 12, ("g4", "gold four")
    GOLD_3 = 13, ("g3", "gold three")
    GOLD_2 = 14, ("g2", "gold two")
    GOLD_1 = 15, ("g1", "gold one")
    PLATINUM_5 = 16, ("p5", "platinum five")
    PLATINUM_4 = 17, ("p4", "platinum four")
    PLATINUM_3 = 18, ("p3", "platinum three")
    PLATINUM_2 = 19, ("p2", "platinum two")
    PLATINUM_1 = 20, ("p1", "platinum one")
    DIAMOND_5 = 21, ("d5", "diamond five")
    DIAMOND_4 = 22, ("d4", "diamond four")
    DIAMOND_3 = 23, ("d3", "diamond three")
    DIAMOND_2 = 24, ("d2", "diamond two")
    DIAMOND_1 = 25, ("d1", "diamond one")
    MASTER_5 = 26, ("m5", "master five")
    MASTER_4 = 27, ("m4", "master four")
    MASTER_3 = 28, ("m3", "master three")
    MASTER_2 = 29, ("m2", "master two")
    MASTER_1 = 30, ("m1", "master one")
    GRANDMASTER_5 = 31, ("gm5", "grandmaster five")
    GRANDMASTER_4 = 32, ("gm4", "grandmaster four")
    GRANDMASTER_3 = 33, ("gm3", "grandmaster three")
    GRANDMASTER_2 = 34, ("gm2", "grandmaster two")
    GRANDMASTER_1 = 35, ("gm1", "grandmaster one")
    TOP_500 = 36, ("t500", "top 500", "top500", "top five hundred", "top5OO")


class ValorantRank(Rank):
    IRON_1 = 1, ("i1", "iron one")
    IRON_2 = 2, ("i2", "iron two")
    IRON_3 = 3, ("i3", "iron three")
    BRONZE_1 = 4, ("b1", "bronze one")
    BRONZE_2 = 5, ("b2", "bronze two")
    BRONZE_3 = 6, ("b3", "bronze three")
    SILVER_1 = 7, ("s1", "silver one")
    SILVER_2 = 8, ("s2", "silver two")
    SILVER_3 = 9, ("s3", "silver three")
    GOLD_1 = 10, ("g1", "gold one")
    GOLD_2 = 11, ("g2", "gold two")
    GOLD_3 = 12, ("g3", "gold three")
    PLATINUM_1 = 13, ("p1", "platinum one")
    PLATINUM_2 = 14, ("p2", "platinum two")
    PLATINUM_3 = 15, ("p3", "platinum three")
    DIAMOND_1 = 16, ("d1", "diamond one")
    DIAMOND_2 = 17, ("d2", "diamond two")
    DIAMOND_3 = 18, ("d3", "diamond three")
    ASCENDANT_1 = 19, ("a1", "asc1", "ascendant one")
    ASCENDANT_2 = 20, ("a2", "asc2", "ascendant two")
    ASCENDANT_3 = 21, ("a3", "asc3", "ascendant three")
    IMMORTAL_1 = 22, ("im1", "immo1", "immortal one")
    IMMORTAL_2 = 23, ("im2", "immo2", "immortal two")
    IMMORTAL_3 = 24, ("im3", "immo3", "immortal three")
    RADIANT = 25, ("rad", "radiant")
