class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(nums, i):
            if len(nums) > 2:
                if nums[-2] + nums[-3] != nums[-1]:
                    return
                else:
                    if i == len(num):
                        return True
            for j in range(i+1, len(num)+1):
                if j-i > 1 and num[i] == '0':
                    continue
                found = backtrack(nums + [int(num[i:j])], j)
                if found:
                    return True
        
        first = backtrack([], 0)
        if first:
            return True
        return False