class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        dict_ = {}

        while i < n:
            index = nums[i] - 1

            if index != i:
                if index > n - 1:
                    dict_[nums[i]] = i + 1
                    i +=1
                elif nums[i] == nums[index]:
                    dict_[nums[i]] = i + 1
                    i +=1
                else:
                    nums[i], nums[index] = nums[index], nums[i]
            else:
                i +=1

        return [list(dict_.keys())[0], list(dict_.values())[0]]