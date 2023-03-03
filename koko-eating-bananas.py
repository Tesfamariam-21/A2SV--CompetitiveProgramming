class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        left = 1 
        right = max(piles)

        while left <= right:
            mid = (left + right) //2
            hr = 0

            for p in piles:
                hr += math.ceil(p/mid)

            if hr <= h:
                right = mid - 1
            else:
                left =mid +1

        return left