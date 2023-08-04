class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = delete = window = max_ = 0

        while r < len(nums):
            if nums[r] == 0:
                if delete == 0:
                    delete = 1
                else:
                    while l < r and nums[l] != 0:
                        l += 1
                    l += 1
            r += 1
            window = r - l
            max_ = max(max_, window)

        return max_ - 1