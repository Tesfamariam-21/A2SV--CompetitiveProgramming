class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)-1
        
        for _ in range(k):
            nums.insert(0,nums.pop())

            
        return nums
        