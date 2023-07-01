from util.models.rank import OverwatchRank
import cProfile
import pstats

with cProfile.Profile() as pr:
    OverwatchRank.fuzz_from_str("GM1")
stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.TIME)
stats.print_stats()
stats.dump_stats("test2.prof")
