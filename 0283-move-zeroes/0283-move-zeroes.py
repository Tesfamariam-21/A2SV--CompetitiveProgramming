class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for num in nums:
            if num == 0:
                nums.append(nums.pop(nums.index(num)))
                