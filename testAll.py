import random
import string
from done.AlgoTree import SuffixTree
from done.FmIndex import FMIndex
from done.suffix_array import search_pattern_with_suffix_array
from tracking_usage import track_time, track_memory
import csv


with open('csv/testData.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    data = list(reader)

with open('csv/results.csv', mode='w') as file:
    file.write(f"length,time_suffix_array,time_suffix_tree,time_fm,memory_suffix_array,memory_suffix_tree,memory_fm\n")


for row in data:
    length = row[0]
    text = row[1]  # Assuming the text is in the first column
    pattern = row[2]  # Assuming the pattern is in the second column

    time_suffix_array = track_time(lambda: search_pattern_with_suffix_array(text, pattern))
    memory_suffix_array = track_memory(lambda: search_pattern_with_suffix_array(text, pattern))

    indices = search_pattern_with_suffix_array(text, pattern)

    suffix_tree = SuffixTree(text)
    time_exists = track_time(lambda: suffix_tree.find_substring(pattern))
    exists = suffix_tree.find_substring(pattern)
    memory_exists = track_memory(lambda: suffix_tree.find_substring(pattern))

    time_positions = track_time(lambda: suffix_tree.find_all_occurrences(pattern))
    positions = suffix_tree.find_all_occurrences(pattern)
    memory_positions = track_memory(lambda: suffix_tree.find_all_occurrences(pattern))

    total_time = time_exists + time_positions
    total_memory = memory_exists + memory_positions

    fm = FMIndex(text)

    time = track_time(lambda: fm.count(pattern))
    count = fm.count(pattern)
    memory = track_memory(lambda: fm.count(pattern))

    time = time + track_time(lambda: fm.locate(pattern))
    positions = fm.locate(pattern)
    memory = memory + track_memory(lambda: fm.locate(pattern))

    # Convert times and memory to string without exponential notation
    time_suffix_array_str = f"{time_suffix_array:.10f}"
    memory_suffix_array_str = f"{memory_suffix_array:.10f}"
    total_time_str = f"{total_time:.10f}"
    total_memory_str = f"{total_memory:.10f}"
    time_str = f"{time:.10f}"
    memory_str = f"{memory:.10f}"

    with open('csv/results.csv', mode='a') as file:
        file.write(f"{length},{time_suffix_array_str},{total_time_str},{time_str},{memory_suffix_array_str},{total_memory_str},{memory_str}\n")

 