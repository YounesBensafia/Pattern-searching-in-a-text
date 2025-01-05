import tracking_usage as tu
class Node:
    def __init__(self, leaf=False):
        self.children = {}
        self.suffix_link = None
        self.start = None
        self.end = None
        self.leaf = leaf
        self.suffix_index = None

class SuffixTree:
    def __init__(self, text):
        self.text = text + "$"
        self.root = Node()
        self.active_node = self.root
        self.active_edge = None
        self.active_length = 0
        self.remainder = 0
        self.current_end = -1
        self.nodes = []
        self.build_suffix_tree()

    def build_suffix_tree(self):
        global_end = [-1]  
        self.current_end = global_end
        
        for i in range(len(self.text)):
            self.current_end[0] += 1
            self.remainder += 1
            last_created_node = None

            while self.remainder > 0:
                if self.active_length == 0:
                    self.active_edge = i

                if (self.active_edge < len(self.text) and 
                    self.text[self.active_edge] in self.active_node.children):
                    
                    child_node, start, end = self.active_node.children[self.text[self.active_edge]]
                    length = min(end[0] if isinstance(end, list) else end, self.current_end[0] + 1) - start

                    if self.active_length >= length:
                        self.active_node = child_node
                        self.active_length -= length
                        self.active_edge += length
                        continue

                    if self.text[start + self.active_length] == self.text[i]:
                        self.active_length += 1
                        if last_created_node is not None:
                            last_created_node.suffix_link = self.active_node
                        break

                    split_node = Node()
                    self.active_node.children[self.text[self.active_edge]] = (
                        split_node,
                        start,
                        start + self.active_length
                    )
                    
                    leaf_node = Node(leaf=True)
                    leaf_node.suffix_index = i - self.remainder + 1
                    split_node.children[self.text[i]] = (
                        leaf_node,
                        i,
                        global_end
                    )
                    
                    split_node.children[self.text[start + self.active_length]] = (
                        child_node,
                        start + self.active_length,
                        end
                    )

                    if last_created_node is not None:
                        last_created_node.suffix_link = split_node
                    last_created_node = split_node

                else:
                    leaf_node = Node(leaf=True)
                    leaf_node.suffix_index = i - self.remainder + 1
                    self.active_node.children[self.text[self.active_edge]] = (
                        leaf_node,
                        i,
                        global_end
                    )

                    if last_created_node is not None:
                        last_created_node.suffix_link = self.active_node
                    last_created_node = self.active_node

                self.remainder -= 1
                
                if self.active_node == self.root and self.active_length > 0:
                    self.active_length -= 1
                    self.active_edge = i - self.remainder + 1
                elif self.active_node != self.root:
                    self.active_node = self.active_node.suffix_link or self.root

    def find_substring(self, pattern):
        node = self.root
        pattern_idx = 0
        
        while pattern_idx < len(pattern):
            if pattern[pattern_idx] not in node.children:
                return False
                
            child, start, end = node.children[pattern[pattern_idx]]
            edge_len = min(end[0] if isinstance(end, list) else end, self.current_end[0] + 1) - start
            
            match_len = 0
            while (match_len < edge_len and 
                   pattern_idx < len(pattern) and 
                   pattern[pattern_idx] == self.text[start + match_len]):
                pattern_idx += 1
                match_len += 1
                
            if match_len != edge_len and pattern_idx < len(pattern):
                return False
                
            node = child
            
        return True

    def find_all_occurrences(self, pattern):
        def _collect_positions(node, positions):
            if node.leaf:
                positions.append(node.suffix_index)
                return
            for child, _, _ in node.children.values():
                _collect_positions(child, positions)

        node = self.root
        pattern_idx = 0
        
        while pattern_idx < len(pattern):
            if pattern[pattern_idx] not in node.children:
                return []
                
            child, start, end = node.children[pattern[pattern_idx]]
            edge_len = min(end[0] if isinstance(end, list) else end, self.current_end[0] + 1) - start
            
            match_len = 0
            while (match_len < edge_len and 
                   pattern_idx < len(pattern) and 
                   pattern[pattern_idx] == self.text[start + match_len]):
                pattern_idx += 1
                match_len += 1
                
            if match_len != edge_len and pattern_idx < len(pattern):
                return []
                
            node = child
            
        positions = []
        _collect_positions(node, positions)
        return sorted(positions)


if __name__ == "__main__":
    text = "bananana" * 10
    pattern = "nan"

    suffix_tree = SuffixTree(text)

    memory1 = tu.track_memory(lambda: SuffixTree(text))
    memory2 = tu.track_memory(lambda: suffix_tree.find_all_occurrences(pattern))
    indices = suffix_tree.find_all_occurrences(pattern)
    total_memory = memory1 + memory2

    print(f"Indices où le motif {pattern} apparaît dans {text} : {indices}")
    print(f"Suffix tree construction memory: {memory1:.2f} KB")
    print(f"Pattern search memory: {memory2:.2f} KB")
    print(f"Total memory: {total_memory:.2f} KB")