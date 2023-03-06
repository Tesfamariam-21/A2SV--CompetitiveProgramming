class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0] = 1
        pSum = 0
        count = 0

        for num in nums:
            pSum += num
            if pSum - goal in prefixSum:
                count += prefixSum[pSum - goal]
                prefixSum[pSum] += 1
            else:
                prefixSum[pSum] += 1
        return count