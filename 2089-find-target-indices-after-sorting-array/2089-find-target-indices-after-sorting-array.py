class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        # nums.sort()
        indices = []
        
        for i in range(len(nums)):
            for j in range(len(nums) - i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
       
        
        for i in range(len(nums)):
            if nums[i] == target:
                indices.append(i)
                
        return indices
                