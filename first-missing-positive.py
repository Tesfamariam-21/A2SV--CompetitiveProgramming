class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums):
            if 0 < nums[i] < len(nums)+1:
                index = nums[i] - 1

                if index != i:
                    if nums[i] == nums[index]:
                        nums[i] = -1
                    else:
                        nums[i], nums[index] = nums[index], nums[i]
                else:
                    i +=1
            else:
                nums[i] = -1
                i +=1


        for i, num in enumerate(nums):
            if num == -1:
                return i + 1
        
        return len(nums) + 1