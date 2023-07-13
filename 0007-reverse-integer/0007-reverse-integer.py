class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x *= -1
        else:
            sign = 1
            
        reversed_str = str(x)[::-1]
        reversed_int = int(reversed_str) * sign
        
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        
        return reversed_int