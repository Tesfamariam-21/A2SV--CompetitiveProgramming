class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return 1 if (product :=math.prod(nums)) > 0 else -1 if product < 0 else 0
        
        # res = 1

        # for num in nums:
        #     if res == 0:
        #         return 0
        #     res *= num

        # return 1 if res > 0 else -1