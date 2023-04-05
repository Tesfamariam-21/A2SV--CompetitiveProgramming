class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # return Counter(nums).most_common()[-1][0]

        nums.sort()
        found = False
        for i in range(len(nums)-1):
            if nums[i] ^ nums[i+1] == 0:
                if found:
                    found = False 
                continue
            else:
                if i == 0:
                    return nums[0]
                if found:
                    return nums[i]
                found = True
        
        return nums[-1]