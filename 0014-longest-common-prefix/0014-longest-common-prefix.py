class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        size = len(strs)
  
    # if size is 0, return empty string 
        if size == 0:
            return ""
        
        s = 100000
        for i in range(size):
            s = min(s, len(strs[i]))
        
            
        if s == 0:
            return ""
        for i in range(s):
            ch = strs[0][i]
            for letter in strs:
                if letter[i] != ch:
                    return strs[0][:i]
        return strs[0][:i+1]
        
        