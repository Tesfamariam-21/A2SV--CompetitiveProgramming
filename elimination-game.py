class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        
        ans =  2*(1 + n//2 - self.lastRemaining(n//2))

        return ans