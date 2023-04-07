class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i, arr):
            nonlocal ans
            if len(arr) == len(nums):
                ans.append(arr)
                # return
            
            for j in range(len(nums)):
                if nums[j] not in arr:
                    backtrack(j, arr + [nums[j]])

        backtrack(-1, [])

        return ans