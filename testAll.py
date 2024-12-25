from done.AlgoTree import SuffixTree
from done.FmIndex import FMIndex
from done.suffix_array import search_pattern_with_suffix_array
from tracking_usage import track_time


text = "bananananananabananabanananaannnnnnnnnnnnnnnnnnnnnnhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
pattern = "na"




time_suffix_array = track_time(lambda: search_pattern_with_suffix_array(text, pattern))
indices = search_pattern_with_suffix_array(text, pattern)
print("TIME IS: ", time_suffix_array)
print(f"Positions: {indices}")


print("===========================================================")

suffix_tree = SuffixTree(text)
time_exists = track_time(lambda: suffix_tree.find_substring(pattern))
exists = suffix_tree.find_substring(pattern)

time_positions = track_time(lambda: suffix_tree.find_all_occurrences(pattern))
positions = suffix_tree.find_all_occurrences(pattern)

total_time = time_exists + time_positions
print("TIME IS: ", total_time)

print(f"Positions: {positions}")
print("===========================================================")

# ===========================================================

fm = FMIndex(text)

time = track_time(lambda: fm.count(pattern))
count = fm.count(pattern)

time = time + track_time(lambda: fm.locate(pattern))
positions = fm.locate(pattern)

print("TIME IS: ", time)

print(f"Positions : {positions}")

print("===========================================================")




