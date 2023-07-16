class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_ = 0
        prevMax = values[0] + 0

        for j in range(1, len(values)):
            score = values[j] + prevMax - j
            max_ = max(max_, score)
            prevMax = max(prevMax, values[j] + j)

        return max_
