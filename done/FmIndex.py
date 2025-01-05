class FMIndex:
    def __init__(self, text):
        self.text = text + '$'  
        self.n = len(self.text)
        
        self.sa, self.bwt = self.build_sa_and_bwt()
        
        self.occ = self.build_occ_array()
        self.c = self.build_c_array()

    def build_sa_and_bwt(self):

        suffixes = [(self.text[i:], i) for i in range(self.n)]
        suffixes.sort()
        
        sa = [idx for _, idx in suffixes]
        bwt = ''.join(self.text[(idx - 1) % self.n] for idx in sa)
        
        return sa, bwt

    def build_occ_array(self):
        chars = sorted(set(self.text))
        occ = {char: [0] for char in chars}
        
        for i, c in enumerate(self.bwt):
            for char in chars:
                occ[char].append(occ[char][i] + (1 if c == char else 0))
                
        return occ

    def build_c_array(self):

        c = {}
        curr_count = 0
        
        for char in sorted(set(self.text)):
            c[char] = curr_count
            curr_count += self.bwt.count(char)
            
        return c

    def count(self, pattern):
        if not pattern:
            return 0
            
        char = pattern[-1]
        if char not in self.c:
            return 0
            
        start = self.c[char]
        end = start + self.bwt.count(char)
        
        for char in reversed(pattern[:-1]):
            if char not in self.c:
                return 0
                
            start = self.c[char] + self.occ[char][start]
            end = self.c[char] + self.occ[char][end]
            
            if start >= end:
                return 0
                
        return end - start

    def locate(self, pattern):

        if not pattern:
            return []
            
        char = pattern[-1]
        if char not in self.c:
            return []
            
        start = self.c[char]
        end = start + self.bwt.count(char)
        
        for char in reversed(pattern[:-1]):
            if char not in self.c:
                return []
                
            start = self.c[char] + self.occ[char][start]
            end = self.c[char] + self.occ[char][end]
            
            if start >= end:
                return []
        
        return sorted([self.sa[i] for i in range(start, end)])

# Exemple d'utilisation
# text = "younessenyou"
# fm = FMIndex(text)

# # Test de recherche
# pattern = "you"
# count = fm.count(pattern)
# positions = fm.locate(pattern)

# print(f"Le motif '{pattern}' apparaît {count} fois dans le {text}.")
# print(f"Positions : {positions}")