class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        prev = nums[1] - nums[0]
        count = 2 if prev != 0 else 1

        for i in range(2, len(nums)):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prev <= 0) or (diff < 0 and prev >= 0):
                count += 1
                prev = diff

        return count
