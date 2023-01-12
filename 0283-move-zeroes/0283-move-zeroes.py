class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        read = 0
        while read < len(nums):
            if nums[read] != 0:
                temp = nums[read]
                nums[read] = nums[write]
                nums[write] = temp
                write = write + 1

            read = read + 1
            
        return nums

                