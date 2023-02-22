class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = 0
        leftSum = 0
        
        for i in nums:
            totalSum += i
            
        for i in range(len(nums)):
            if i != 0:
                leftSum += nums[i-1]
            if totalSum - leftSum - nums[i] == leftSum:
                return i
            
        return -1
            
            