class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        sett = set()
        dict_ = {}

        while i < n:
            index = nums[i] - 1

            if index != i:
                if index > len(nums) -1:
                    sett.add(i)
                    dict_[nums[i]] = i + 1
                    i +=1
                elif nums[i] == nums[index]:
                    sett.add(i)
                    dict_[nums[i]] = i + 1
                    i +=1
                else:
                    nums[i], nums[index] = nums[index], nums[i]
                    # i +=1
            else:
                i +=1

        return dict_.values()