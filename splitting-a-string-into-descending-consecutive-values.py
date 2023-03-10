class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(substr, index):
            if len(substr):
                if len(substr) >= 2:
                    if substr[-2] - substr[-1] != 1:
                        return 
                    elif substr[-2] - substr[-1] == 1 and index == len(s):
                        return True

            for j in range(index+1, len(s)+1): 
                if backtrack(substr + [int(s[index:j])], j):
                    return True
        
        return backtrack([],0) or False