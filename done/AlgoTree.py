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

# text = "jejeje"
# suffix_tree = SuffixTree(text)

# pattern = "je"
# exists = suffix_tree.find_substring(pattern)
# positions = suffix_tree.find_all_occurrences(pattern)

# print(f"Le motif '{pattern}' existe dans le texte: {exists}")
# print(f"Positions: {positions}")

# class Node:
#     def __init__(self, leaf=False):
#         self.children = {}  # {char: (node, start, end)}
#         self.suffix_link = None
#         self.start = None
#         self.end = None
#         self.leaf = leaf
#         self.suffix_index = None

# class SuffixTree:
#     def __init__(self, text):
#         self.text = text + "$"
#         self.root = Node()
#         self.active_node = self.root
#         self.active_edge = None
#         self.active_length = 0
#         self.remainder = 0
#         self.current_end = [-1] 
#         self.build_suffix_tree()

#     def build_suffix_tree(self):
#         for i in range(len(self.text)):
#             self.current_end[0] += 1
#             self.remainder += 1
#             last_created_node = None

#             while self.remainder > 0:
#                 if self.active_length == 0:
#                     self.active_edge = i

#                 if (self.active_edge < len(self.text) and 
#                     self.text[self.active_edge] in self.active_node.children):
                    
#                     child_node, start, end = self.active_node.children[self.text[self.active_edge]]
#                     length = min(end[0] if isinstance(end, list) else end, self.current_end[0] + 1) - start

#                     if self.active_length >= length:
#                         self.active_node = child_node
#                         self.active_length -= length
#                         self.active_edge += length
#                         continue

#                     if self.text[start + self.active_length] == self.text[i]:
#                         self.active_length += 1
#                         if last_created_node is not None:
#                             last_created_node.suffix_link = self.active_node
#                         break

#                     split_node = Node()
#                     self.active_node.children[self.text[self.active_edge]] = (
#                         split_node,
#                         start,
#                         start + self.active_length
#                     )
                    
#                     leaf_node = Node(leaf=True)
#                     leaf_node.suffix_index = i - self.remainder + 1
#                     split_node.children[self.text[i]] = (
#                         leaf_node,
#                         i,
#                         self.current_end
#                     )
                    
#                     split_node.children[self.text[start + self.active_length]] = (
#                         child_node,
#                         start + self.active_length,
#                         end
#                     )

#                     if last_created_node is not None:
#                         last_created_node.suffix_link = split_node
#                     last_created_node = split_node

#                 else:
#                     leaf_node = Node(leaf=True)
#                     leaf_node.suffix_index = i - self.remainder + 1
#                     self.active_node.children[self.text[self.active_edge]] = (
#                         leaf_node,
#                         i,
#                         self.current_end
#                     )

#                     if last_created_node is not None:
#                         last_created_node.suffix_link = self.active_node
#                     last_created_node = self.active_node

#                 self.remainder -= 1
                
#                 if self.active_node == self.root and self.active_length > 0:
#                     self.active_length -= 1
#                     self.active_edge = i - self.remainder + 1
#                 elif self.active_node != self.root:
#                     self.active_node = self.active_node.suffix_link or self.root

#     def get_edge_string(self, start, end):
#         """Récupère la chaîne de caractères sur une arête"""
#         end_val = end[0] if isinstance(end, list) else end
#         return self.text[start:min(end_val + 1, len(self.text))]

#     def print_tree(self, node=None, prefix="", is_last=True, depth=0):
#         """Affiche l'arbre des suffixes avec une structure visuelle"""
#         if node is None:
#             node = self.root
#             print("Arbre des suffixes pour le texte:", self.text)
#             print("Root")
            
#         # Trier les enfants par caractère pour un affichage cohérent
#         children = sorted(node.children.items())
        
#         for i, (char, (child, start, end)) in enumerate(children):
#             is_last_child = i == len(children) - 1
            
#             # Créer le préfixe pour les lignes actuelles
#             current_prefix = prefix + ("└── " if is_last_child else "├── ")
            
#             # Obtenir la chaîne de l'arête
#             edge_string = self.get_edge_string(start, end)
            
#             # Afficher l'arête avec son contenu
#             suffix_info = f" [suffixe: {child.suffix_index}]" if child.leaf else ""
#             print(f"{current_prefix}{edge_string}{suffix_info}")
            
#             # Préfixe pour les enfants
#             new_prefix = prefix + ("    " if is_last_child else "│   ")
            
#             # Récursion pour les enfants
#             self.print_tree(child, new_prefix, is_last_child, depth + 1)

# # Test avec le texte "banana"
# text = "banana"
# suffix_tree = SuffixTree(text)

# # Afficher l'arbre
# suffix_tree.print_tree()