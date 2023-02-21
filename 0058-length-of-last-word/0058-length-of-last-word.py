class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        max_ = 0
        s = s.strip()
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                return max_
            else:
                max_ +=1
                       
        return max_
                
        