class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dict_ = {}
        maxLength = 0
        
        for right in range(len(s)):
            if s[right] in dict_:
                left =max(left, dict_[s[right]] + 1)

            maxLength = max(maxLength, (right - left + 1))
            dict_[s[right]] = right
         
        return maxLength