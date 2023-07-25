class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s) 
        left = 0
        length = len(s)//4 
        res =  inf
        for right in range(len(s)):
            count[s[right]] -= 1
            while left < len(s) and count['W'] <= length and count['Q'] <= length and count['E'] <= length and count['R'] <= length:
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1
        return res