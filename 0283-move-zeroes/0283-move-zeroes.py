class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums.append(nums.pop(i))
        
        for num in nums:
            if num == 0:
                nums.append(nums.pop(nums.index(num)))
                