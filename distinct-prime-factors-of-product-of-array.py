class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        n = 1
        s = set()

        for i in range(len(nums)):
            j = 2
            while j <= nums[i]:
                while nums[i]%j == 0:
                    s.add(j)
                    nums[i] = nums[i] //j
                j +=1

        return len(s)