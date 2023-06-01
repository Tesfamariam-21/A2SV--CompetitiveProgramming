class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0

        for i in range(len(nums)):
            temp = max(nums[i] + first, second)
            first = second
            second = temp
        return second