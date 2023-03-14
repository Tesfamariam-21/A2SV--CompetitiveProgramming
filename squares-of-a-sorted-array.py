class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted([x**2 for x in nums])
        # return sorted(list(map(lambda x: x**2, nums)))

        left = 0
        right = len(nums) -1
        ans = [0 for i in range(len(nums))]
        k = len(nums) - 1

        while k >= 0:
            if abs(nums[left]) <= abs(nums[right]):
                ans[k] = nums[right]**2
                right -=1
            else:
                ans[k] = nums[left]**2
                left +=1
            k -=1

        return ans