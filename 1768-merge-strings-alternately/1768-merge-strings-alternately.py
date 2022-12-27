class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1 = 0
        pointer2 = 0
        string = ""
        
        size = len(word1) if len(word1) > len(word2) else len(word2)
        
        for _ in range(size):
            if(pointer1 < len(word1)):
                string += word1[pointer1]
                pointer1 += 1
            if(pointer2 < len(word2)):
                string += word2[pointer2]
                pointer2 += 1
                
        return string
            
            
            
            
        