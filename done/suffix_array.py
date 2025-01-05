import tracking_usage as tu
def suffix_array_construction(text):
    n = len(text)
    suffixes = [(text[i:], i) for i in range(n)]    
    # HENA F SORT THSB CHHAL TWL
    suffixes.sort()    
    suffix_array = [suffix[1] for suffix in suffixes]
    return suffix_array

def search_pattern_with_suffix_array(text, pattern):
    suffix_array = suffix_array_construction(text)
    n = len(text)
    result = []
    for i in suffix_array:
        if text[i:i+len(pattern)] == pattern:
            result.append(i)
    return result

# text = "bananana"*10  
# pattern = "nan"

# # HENA F SEARCH THSB CHHAL TWL TANI
# indices = search_pattern_with_suffix_array(text, pattern)

# memory1 = tu.track_memory(lambda: suffix_array_construction(text))
# memory2 = tu.track_memory(lambda: search_pattern_with_suffix_array(text, pattern))
# total_memory = memory1 + memory2
# print(f"Indices où le motif {pattern} apparaît dans {text} : {indices}")
# print(f"Suffix array construction memory usage: {memory1:.10f} KB")
# print(f"Pattern search memory usage: {memory2:.10f} KB")
# print(f"Total memory usage: {total_memory:.10f} KB")



