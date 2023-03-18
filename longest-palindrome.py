class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        longest_palindrome = 0
        odd = 0

        for key, val in c.items():
            if val % 2 == 0:
                longest_palindrome +=val
            else:
                longest_palindrome += val - 1
                odd = 1

        return longest_palindrome + odd