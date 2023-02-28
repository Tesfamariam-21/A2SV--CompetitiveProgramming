class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_ = res = 0
        count = Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            max_ = max(max_, count[s[i]])
            if res - max_ < k:
                res += 1
            else:
                count[s[i - res]] -= 1
        return res