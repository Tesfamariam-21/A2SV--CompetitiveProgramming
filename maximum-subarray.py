class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]
        summ = 0

        for n in nums:  
            if summ < 0:
                summ = 0
            summ += n
            max_ = max(max_, summ)

        return max_