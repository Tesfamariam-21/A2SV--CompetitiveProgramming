class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        write, read = 0, 0

        while read < len(nums):
            if nums[write] != 0:
                write +=1
                read +=1
            elif nums[read] == 0:
                read +=1
            else: 
                nums[read], nums[write] = nums[write], nums[read]
                
        return nums
        