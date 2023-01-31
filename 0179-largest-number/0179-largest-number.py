class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        
        def compare(str1, str2):
            if str1 + str2 > str2+str1:
                return -1
            else:
                return 1
            
        nums = sorted(nums, key= cmp_to_key(compare))
                
        return str(int("".join(nums)))