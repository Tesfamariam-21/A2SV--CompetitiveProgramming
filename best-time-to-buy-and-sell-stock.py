class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # base case not to go to the algo even though it works
        if len(prices) == 1:
            return 0

        min_ = prices[0]
        max_ = 0

        for p in prices:
            min_ = min(min_, p)
            max_ = max(max_, p - min_)

        return max_