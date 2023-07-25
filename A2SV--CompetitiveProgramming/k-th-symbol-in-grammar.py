class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(N,K):
            if N==1 and K == 1 :
                return 0
            mid = 2**(N-2)
            if K <= mid:
                return helper(N-1,K)
            
            if K > mid:
                return 1-helper(N-1,K-mid)
        
        return helper(n,k)