class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sum_even = sum([n for n in nums if n % 2== 0])
        
        for [val, index] in queries:
            v = nums[index] + val
            
            if nums[index] % 2 == 0:
                sum_even -= nums[index]
                
            if v % 2 == 0:
                sum_even += v
            nums[index] = v
            
            res.append(sum_even)
        
        return res
        
        