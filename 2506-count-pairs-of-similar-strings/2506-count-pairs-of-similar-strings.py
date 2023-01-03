class Solution:
    def similarPairs(self, words: List[str]) -> int:
        pairs = 0
        
        for i in range(len(words)):
            for j in range(i):
                if set(words[i]) == set(words[j]):
                    pairs += 1
        return pairs
               
        