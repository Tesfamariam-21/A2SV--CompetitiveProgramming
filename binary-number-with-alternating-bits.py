class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = -1

        while n > 0:
            if bit == n & ( 1<<0):
                return False
            bit = n & (1<<0)
            n = n>>1

        return True