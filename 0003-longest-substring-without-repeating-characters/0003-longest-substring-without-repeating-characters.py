class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        dict_ = {}
        max_ = 0
        
        while right < len(s):
            if s[right] in dict_:
                left = max(left,dict_[s[right]]+1)
                

            
            dict_[s[right]] = right
            max_ = max(max_, right - left + 1)
            right +=1
        print(left, right)
        return max_
        
        
#         left = 0
#         dict_ = {}
#         maxLength = 0
        
#         for right in range(len(s)):
#             if s[right] in dict_:
#                 left =max(left, dict_[s[right]] + 1)

#             maxLength = max(maxLength, (right - left + 1))
#             dict_[s[right]] = right
         
#         return maxLength