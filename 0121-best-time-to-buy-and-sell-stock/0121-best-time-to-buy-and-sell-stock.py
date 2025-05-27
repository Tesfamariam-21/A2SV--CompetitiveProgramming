class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        min_ = [prices[0]]
        max_ = [0] * n
        max_[-1] = prices[-1]
        res = 0

        for i in range(1, n):
            min_.append(min(min_[-1], prices[i]))
            max_[n - 1 - i] = max(max_[-1], prices[n - 1 - i])

 
        for i in range(n):
            res = max(res, max_[i] - min_[i])

        return res

        