class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        i = 0
        temp = 0

        while i < n:
            index = nums[i]

            if index != i:
                if index > len(nums) - 1:
                    temp = index
                    i +=1
                else:
                    nums[i], nums[index] = nums[index], nums[i]
        
            else:
                i +=1

        
        return len(nums) if temp == 0 else nums.index(temp)