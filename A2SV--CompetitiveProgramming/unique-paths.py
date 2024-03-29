class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1: 
            return 1
        N = n + m - 2
        K = min(n - 1, m - 1)
        ans = 1
        for i in range(N,N-K, -1):
            ans *=i
        for i in range(1, K+1):
            ans //=i   
                
        return ans 