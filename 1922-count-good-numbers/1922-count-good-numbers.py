class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        
        even = math.ceil(n/2)
        odd = n//2
        
        val1 = pow(5, even, mod)
        val2 = pow(4, odd, mod)
        
        return (val1 * val2)%mod