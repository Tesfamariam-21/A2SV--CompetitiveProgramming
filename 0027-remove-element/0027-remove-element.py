class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        count = 0
        
        for i in range(len(nums)):
            if(nums[index] != val):
                index = index+1
            else:
                nums.append(nums.pop(index))
                count = count + 1
                
        return len(nums)-count