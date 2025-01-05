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
    # Search for the pattern in the suffix array
    result = []
    for i in suffix_array:
        if text[i:i+len(pattern)] == pattern:
            result.append(i)
    return result

# text = "bananana"
# pattern = "nan"

# # HENA F SEARCH THSB CHHAL TWL TANI
# indices = search_pattern_with_suffix_array(text, pattern)

# print(f"Indices où le motif {pattern} apparaît dans {text} : {indices}")

# # TSMA A LA FIN YKON FICHIER HKA {TEXT, PATTERN, TIME_SORT, TIME_CONS, TIME_SEARCH}

