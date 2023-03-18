class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff +=1

        return diff == 2 and sorted(s1) == sorted(s2)