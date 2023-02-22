class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_ = window_sum

        for end in range(k, len(nums)):
            window_sum += nums[end]
            window_sum -= nums[end-k]
            max_ = max(max_, window_sum)

        return max_/k
        
#         start= 0
#         end = k
#         max_ = 0.0
        
#         for i in range(k):
#             max_ += nums[i]
        
#         while end < len(nums):
#             max_ = max(max_,(max_ - nums[start] + nums[end]))
#             print(max_, nums[start], nums[end])
#             end +=1
#             start +=1
            
#         return max_/k
            
        