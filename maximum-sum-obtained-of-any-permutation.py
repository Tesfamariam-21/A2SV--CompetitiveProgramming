class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefixSum = [0]*(len(nums)+1)
        ans = 0

        for start, end in requests:
            prefixSum[start] += 1
            prefixSum[end + 1] -= 1
        
        for i in range(len(prefixSum) -1):
            prefixSum[i+1] += prefixSum[i]

        prefixSum = sorted(prefixSum, reverse=True)
        nums = sorted(nums, reverse=True)

        for i in range(len(nums)):
            ans += (nums[i]*prefixSum[i])
        
        return ans % (10**9 + 7)