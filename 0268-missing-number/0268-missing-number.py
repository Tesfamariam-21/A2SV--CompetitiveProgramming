class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        sumTotal = size*(size+1)/2
        
        return int(sumTotal - sum(nums))
        