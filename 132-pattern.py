class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_ = nums[0]

        for i in nums[1:]:
            while stack and stack[-1][0] <= i:
                stack.pop()
            
            if stack and stack[-1][1] < i:
                return True

            stack.append([i, min_])
            min_ = min(min_, i)

        return False