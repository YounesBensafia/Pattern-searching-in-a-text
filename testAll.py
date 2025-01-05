from done.AlgoTree import SuffixTree
from done.FmIndex import FMIndex
from done.suffix_array import search_pattern_with_suffix_array
from tracking_usage import track_time, track_memory


text = "bananananananabananabanananaannnnnnnnnnnnnnnnnnnnnnhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
pattern = "na"




time_suffix_array = track_time(lambda: search_pattern_with_suffix_array(text, pattern))
memory_suffix_array = track_memory(lambda: search_pattern_with_suffix_array(text, pattern))

indices = search_pattern_with_suffix_array(text, pattern)

print("\n================== Suffix Array ==================\n")
print(f"Time taken to search using Suffix Array: {time_suffix_array} seconds")
print(f"Pattern found at positions: {indices}")
print(f"Memory used for Suffix Array search: {memory_suffix_array} KB")



suffix_tree = SuffixTree(text)
time_exists = track_time(lambda: suffix_tree.find_substring(pattern))
exists = suffix_tree.find_substring(pattern)
memory_exists = track_memory(lambda: suffix_tree.find_substring(pattern))

time_positions = track_time(lambda: suffix_tree.find_all_occurrences(pattern))
positions = suffix_tree.find_all_occurrences(pattern)
memory_positions = track_memory(lambda: suffix_tree.find_all_occurrences(pattern))

total_time = time_exists + time_positions
total_memory = memory_exists + memory_positions

print("\n================== Suffix Tree ==================\n")
print(f"Time taken to search using Suffix Tree: {total_time} seconds")
print(f"Pattern found at positions: {positions}")
print(f"Memory used for Suffix Tree search: {total_memory} KB")

# ===========================================================

fm = FMIndex(text)

time = track_time(lambda: fm.count(pattern))
count = fm.count(pattern)
memory = track_memory(lambda: fm.count(pattern))

time = time + track_time(lambda: fm.locate(pattern))
positions = fm.locate(pattern)
memory = memory + track_memory(lambda: fm.locate(pattern))

print("\n================== FM Index ==================\n")

print(f"Time taken to search using FM Index: {time} seconds")
print(f"Pattern found at positions: {positions}")
print(f"Memory used for FM Index search: {memory} KB")


length = len(text)


with open('csv/results.csv', mode='w+') as file:
    file.write(f"length,time_suffix_array,time_suffix_tree,time_fm,memory_suffix_array,memory_suffix_tree,memory_fm\n")
    file.write(f"{length},{time_suffix_array},{total_time},{time},{memory_suffix_array},{total_memory},{memory}\n")


# SUFFIX ARRAY > SUFFIX TREE > FM_INDEX





