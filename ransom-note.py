class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)

        for key, val in c1.items():
            if c2[key] < val:
                return False

        return True

        # st1, st2 = Counter(ransomNote), Counter(magazine)
        #     return st1 & st2 == st1