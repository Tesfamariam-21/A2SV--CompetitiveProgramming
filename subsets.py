class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(index, subset):
            ans.append(subset)
            # to optimaize the time
            if len(ans) == 2**len(nums):
                return
            
            for i in range(index, len(nums)):
                backtrack(i+1, subset + [nums[i]])

        backtrack(0, [])
        return ans