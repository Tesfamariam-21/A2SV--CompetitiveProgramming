class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            gcf = nums[i]
            for j in range(i,len(nums)):
                temp = math.gcd(gcf,nums[j])
                if temp == k:
                    count +=1
                elif temp < k:
                    break
                gcf = math.gcd(gcf, nums[j])

        return count