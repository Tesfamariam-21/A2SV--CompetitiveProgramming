class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True for _ in range(right +1)]
        isPrime[0], isPrime[1] = False, False

        i = 2

        while i*i < right+1:
            if isPrime[i]:
                j = i*i

                while j <right+1:
                    isPrime[j] = False
                    j +=i
            i+=1

        diff = float("inf")
        ans = [-1, -1]
        p = []
        
        for i in range(left, right+1):
            if isPrime[i]:
                p.append(i)
            if len(p) == 2:
                if p[1] - p[0] < diff:
                    diff = p[1] - p[0]
                    ans = [p[0], p[1]]
                p.pop(0)

        return ans