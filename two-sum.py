class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = defaultdict(int)

        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in dict_:
                return [dict_[comp], i]
            
            dict_[nums[i]] = i