class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        dict_ = defaultdict(int)
        max_ = 0

        while right < len(s):
            if s[right] in dict_:
                left = max(left,dict_[s[right]]+1)

            dict_[s[right]] = right
            right +=1
            max_= max(max_, right - left)

        return max_