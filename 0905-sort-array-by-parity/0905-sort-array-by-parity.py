class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pointer = 0
        size = len(nums)
        even = []
        odd = []
        
        while pointer < size:
            if(nums[pointer] % 2 == 0):
                even.append(nums[pointer])
            else:
                odd.append(nums[pointer])
            pointer +=1
            
         
        return even + odd
                
        
        