class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def helperFunc(n, k, flip): 
            print(n, k, flip)
            if n == 1:
                return "1" if flip else "0"
            
            mid = 2**(n-1)
            if mid == k:
                return "0" if flip else "1" 
            elif k < mid:
                return helperFunc(n-1, k, flip)
            else: 
                return helperFunc(n-1, 2**n-k, 1-flip)  
            
        return helperFunc(n, k, 0)
        
