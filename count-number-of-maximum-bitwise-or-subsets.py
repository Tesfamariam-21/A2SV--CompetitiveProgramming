class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        interval = 0
        count = 0
        max_ = 0
        n = len(nums)

        for i in range(n):
            interval ^=(1<<i)
        for i in range(0,interval+1):
            res = 0
            for j in range(20):
                if i &(1<<j) != 0:
                    res |= nums[j]
            if res > max_:
                max_ = res
                count = 1
            elif res == max_:
                count +=1  

        return count

        
        # count = 0
        # max_ = 0

        # def backtrack(i, arr):
        #     nonlocal count
        #     nonlocal max_
        #     res = 0
        #     for j in range(len(arr)):
        #         res |=arr[j]

        #     if res > max_:
        #         max_ = res
        #         count = 1
        #     elif res == max_:
        #         count +=1

        #     for j in range(i+1, len(nums)):
        #         backtrack(j, arr + [nums[j]])
    

        # backtrack(-1, [])
        # return count