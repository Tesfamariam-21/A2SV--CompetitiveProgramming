class Solution:
    def isHappy(self, n: int) -> bool:
        while n > 9:
            n = str(n)
            summ = 0

            for i in range(len(n)):
                summ += int(n[i])**2

            n = summ

        return True if n == 1 else False