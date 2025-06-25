class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        length = len(prices)
        max_array = [0] * length
        max_array[-1] = prices[-1]

        for i in range(length - 2, -1, -1):
            max_array[i] =max(max_array[i + 1], prices[i])


        for i in range(length):
            profit = max(profit, max_array[i] - prices[i])

        return profit

        # profit = 0
        # length = len(prices)

        # for i in range(length):
        #     for j in range(i, length):
        #         profit = max(profit, prices[j] - prices[i])

        # return profit

        # # 7 6 6 6 6 4


        # n = len(prices)
        # min_ = [prices[0]]
        # max_ = [0] * n
        # max_[-1] = prices[-1]
        # res = 0

        # for i in range(1, n):
        #     min_.append(min(min_[-1], prices[i]))
        #     max_[n - 1 - i] = max(max_[-1], prices[n - 1 - i])

        # for i in range(n):
        #     res = max(res, max_[i] - min_[i])

        # # 0 5 
        # return res

        