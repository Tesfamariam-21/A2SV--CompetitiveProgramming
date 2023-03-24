class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_ = 0
        sett = set()

        def backtrack(sett, i):
            nonlocal max_
            l = len(arr[i])
            
            s = sett.union(set(arr[i]))
            
            if len(s) != l + len(sett):
                return

            max_ = max(max_, len(s))

            for j in range(i+1, len(arr)):
                backtrack(s, j)

        
        for i in range(len(arr)):
            backtrack(sett, i)
        return max_