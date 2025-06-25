class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        right = left = 0
        dict_ = {}
        length = len(s)
        longest_substring = 0

        while right < length:
            if s[right] in dict_:
                left = max(left, dict_[s[right]] + 1)
            
            dict_[s[right]] = right
            right +=1
            longest_substring = max(longest_substring, right - left)

        return longest_substring


        # longestSubstring = 0
        # length = len(s)
        # substring = set()
        # j = 0

        # for i in range(length):

        #     while s[i] in substring:
        #         substring.remove(s[j])
        #         j +=1


        #     substring.add(s[i])
        #     longestSubstring = max(longestSubstring, i - j + 1)
           

        # return longestSubstring










        
        # dict_ = {}
        # left = right = longest_substring= 0

        # while right < len(s):
        #     if s[right] in dict_:
        #         left = max(left, dict_[s[right]] + 1)

        #     dict_[s[right]] = right
        #     right +=1
        #     longest_substring = max(longest_substring, right - left)

        # return longest_substring

        # longest_substring = 0
        # left = right = 0
        # substrings = set()

        # while right < len(s):
        #     if s[right] in substrings:
        #         substrings.discard(s[left])
        #         left +=1
        #     else:
        #         substrings.add(s[right])
        #         right +=1
        #         longest_substring = max(longest_substring, right - left)

        # return longest_substring

