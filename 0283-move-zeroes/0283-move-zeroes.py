class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                right += 1
                left += 1
            else:
                right+=1
        for i in range(left, len(nums)):
            nums[i] = 0
        return nums

                