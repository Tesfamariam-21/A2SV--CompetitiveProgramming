class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 2):
            a = nums[-3 - i]
            b = nums[-2 - i]
            c = nums[-1 - i]
            if(a + b > c):
                return a + b +c
        return 0
        
        