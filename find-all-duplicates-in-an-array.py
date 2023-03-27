class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = set()
        i = 0

        while i < n:
            index = nums[i] - 1

            if index != i:
                if nums[index] == nums[i]:
                    ans.add(nums[i])
                    i +=1
                else:
                    nums[index], nums[i] = nums[i], nums[index]
                    # i +=1
            else:
                i +=1

        return ans