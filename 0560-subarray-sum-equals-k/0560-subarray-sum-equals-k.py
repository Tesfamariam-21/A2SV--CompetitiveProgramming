class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
                    
        dict_ = defaultdict(int)
        # defaultdict(def_value)
        subarray = 0
        curSum_ = 0
        remainder = 0
        dict_[0] = 1
        
        for i in range(len(nums)):
            curSum_ += nums[i]
            remainder = curSum_ - k
            
            if remainder in dict_:
                subarray +=dict_[remainder]
            
            dict_[curSum_] +=1
           
        return subarray
        
        
        
#         right = 1
#         left = 0
#         sum_ = nums[0]
#         subarray = 0
        
#         if sum_ == k:
#             subarray +=1
        
#         for i in range(1,len(nums)):
#             sum_ += nums[i]
#             # print(sum_)
#             if sum_ > k:
#                 sum_ -= nums[left]
#                 left +=1
#             if sum_ < k and nums[left] < 0:
#                 sum_ -= nums[left]
#                 left +=1
#             if sum_ == k:
#                 subarray +=1
#                 sum_ -= nums[left]                
#                 left +=1
#             # if nums[len(nums)-1] == k:
#             #     subarray +=1
#                 # sum_ += nums[right]

            
#             right +=1
        
#         return subarray

        
        
        
        
        
        
        
        
        
        
        