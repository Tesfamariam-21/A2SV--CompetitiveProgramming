class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dict_ = defaultdict(int)
        odd_counts, ans = 0, 0
        dict_[0] = 1
        
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                odd_counts+=1
            ans += dict_[odd_counts-k]
            dict_[odd_counts]+=1
            
        return ans