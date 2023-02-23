class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        sum_ = 0
        min_ = float("inf")
        
        
        
        while right < len(nums) and left <= right:
            sum_ += nums[right]
            if sum_ >= target:
                min_ = min(min_, right - left+1)
                sum_ -= nums[left]
                sum_ -= nums[right] 
                left +=1
            
            else:
                right +=1
        
        return 0 if min_ == float("inf") else min_
                