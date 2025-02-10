class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_ = float(inf)

        for num in nums:
            if abs(num) == abs(min_):
                min_ = max(num, min_)
            elif abs(num) < abs(min_):
                min_ = num

        return min_
        