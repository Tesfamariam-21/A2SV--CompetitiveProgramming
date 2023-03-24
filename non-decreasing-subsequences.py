class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(arr, index):
            # print(arr)
            if index == len(nums):
                ans.append(arr)
                return
            
            if len(arr) >= 1:
                if arr[-1] <= nums[index]:
                    arr.append(nums[index])
                    if arr not in ans:
                        ans.append(arr)
                else:
                    return
            else:
                arr.append(nums[index])
            
            for i in range(index+1, len(nums)):
                backtrack(arr.copy(), i)

        for i in range(len(nums)):
            backtrack([], i)
        return ans