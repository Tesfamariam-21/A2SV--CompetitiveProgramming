class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        c = 0
        for i in range(len(nums)):
            if nums[i] < 0:
                c +=1

        for i in range(32):
            count = 0
            for n in nums:
                if n < 0:
                    n = abs(n)
                if n & (1 << i) != 0:
                    count +=1
                
            if count % 3 != 0:
                ans |= (1<<i)
            
        return ans if c % 3 == 0 else -1 * ans


        # return Counter(nums).most_common()[-1][0]

        # nums.sort()
        # found = False
        # for i in range(len(nums)-1):
        #     if nums[i] ^ nums[i+1] == 0:
        #         if found:
        #             found = False 
        #         continue
        #     else:
        #         if i == 0:
        #             return nums[0]
        #         if found:
        #             return nums[i]
        #         found = True
        
        # return nums[-1]