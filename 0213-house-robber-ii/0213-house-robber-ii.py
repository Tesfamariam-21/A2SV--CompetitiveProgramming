class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        first = second = one= two = 0

        for i in range(len(nums)-1):
            temp = max(nums[i] + first, second)
            first = second
            second = temp
        for i in range(len(nums)-1, 0, -1):
            temp = max(nums[i] + one, two)
            one = two
            two = temp

        return max(second, two)