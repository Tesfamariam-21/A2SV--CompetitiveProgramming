class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        start = 0
        
        for i in spaces:
            res+= s[start:i]+ " "
            start = i
            
        res += s[spaces[-1]:]
        # res = res[0:-1]
  
        return res
        