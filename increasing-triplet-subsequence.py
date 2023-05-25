class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first = second = 2**31

        for i in range(len(nums)):
            if first >= nums[i]:
                first = nums[i]
            elif second >= nums[i]:
                second = nums[i]
            else:
                return True


        return False