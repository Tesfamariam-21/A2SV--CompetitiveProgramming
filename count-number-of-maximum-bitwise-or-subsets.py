class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        max_ = 0

        def backtrack(i, arr):
            nonlocal count
            nonlocal max_
            res = 0
            for j in range(len(arr)):
                res |=arr[j]

            if res > max_:
                max_ = res
                count = 1
            elif res == max_:
                count +=1
            
            if len(arr) == len(nums):
                return

            for j in range(i+1, len(nums)):
                backtrack(j, arr + [nums[j]])


            

        backtrack(-1, [])
        return count