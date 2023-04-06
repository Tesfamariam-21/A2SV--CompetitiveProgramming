class Solution:
    def minSteps(self, n: int) -> int:
        count = 0
        primeFactor = 2

        while n > 1:
            if n % primeFactor == 0:
                count += primeFactor
                n //= primeFactor
                continue
            primeFactor +=1

        return count