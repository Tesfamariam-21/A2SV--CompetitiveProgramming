class Solution:
    from collections import Counter
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        word = Counter(words[0])
        
        
        for i in range(1, len(words)):
            c = Counter(words[i])
            
            for j in word:
                word[j] = min(word[j], c[j])
                    

        return word.elements()
        
        