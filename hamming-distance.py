class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0

        for i in range(32):
            if (x & (1<<i))^(y & (1<<i)) != 0:
                count +=1
            
        return count