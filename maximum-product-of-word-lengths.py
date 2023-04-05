class Solution:
    def maxProduct(self, words: List[str]) -> int:
        arr = []
        Max = 0

        for i in range(len(words)):
            chars = 0
            for j in range(len(words[i])):
                chars |= (1 << ord(words[i][j]) - 97)
                
            arr.append(chars)
        
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                if arr[i] & arr[j] == 0:
                    Max = max(Max, len(words[i]) * len(words[j]))
        return Max