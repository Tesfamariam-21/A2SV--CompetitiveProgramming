class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = defaultdict(int)

        for i in range(len(questions) - 1, -1, -1):
            dp[i] = max(questions[i][0] + dp[i + 1 + questions[i][1]], dp[i+1])


        return dp[0]



        # dp = {}

        # def dfs(i):
        #     if i >= len(questions):
        #         return 0

        #     if i in dp:
        #         return dp[i]

        #     adding = questions[i][0] + dfs(i + 1 + questions[i][1])
        #     skipping = dfs(i + 1)

        #     dp[i] = max(adding, skipping)

        #     return dp[i]
            

        # return dfs(0)