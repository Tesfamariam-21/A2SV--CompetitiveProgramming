class Solution:
    def divElements(self, nums, divisor):
        summ = 0
        for num in nums:
            summ += math.ceil(num/divisor)
        return summ

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low  = 1
        high = max(nums)

        while low < high:
            mid = (low + high)// 2
            elements = self.divElements(nums, mid)

            if elements <= threshold:
                high = mid 
            elif elements > threshold:
                low = mid + 1    
        
        return high