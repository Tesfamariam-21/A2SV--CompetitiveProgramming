class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        op = 0
        nums.sort()
        
        while left < right:
            if nums[left] + nums[right] == k:
                op += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            
            
        return op
            
#         c = Counter(nums)
#         output = 0
#         counted = set()
        
#         for x in c:
#             if x not in counted and (k-x) in c:
#                 if x == (k-x):
#                     output += c[x]//2
#                 else:
#                     output += min(c[x], c[k-x])
#                     counted.add(x)
#                     counted.add(k-x)
                
#         return output