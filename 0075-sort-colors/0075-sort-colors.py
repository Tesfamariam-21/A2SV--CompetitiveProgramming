class Solution:
    def sortColors(self, nums: List[int]) -> None:

        colors = [0, 0 ,0]
        
        for i in range(len(nums)):
            if nums[i] == 0:
                colors[0] +=1
            elif nums[i] == 1:
                colors[1] += 1
            elif nums[i] == 2:
                colors[2] += 1
        
        nums.clear()
        for i in range(3):
            for j in range(colors[i]):
                nums.append(i)
                
        return nums
        
        