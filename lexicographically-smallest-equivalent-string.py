class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {}
        ans = []

        for i in range(len(s1)):
            rep[s1[i]] = s1[i]
            rep[s2[i]] = s2[i]

        def find(char):
            if char == rep[char]:
                return char

            rep[char] = find(rep[char])
            return rep[char]

        def union(char1, char2):
            c1 = find(char1)
            c2 = find(char2)

            if c1 != c2:
                if c1 < c2:
                    rep[c2] = c1
                else:
                    rep[c1] = c2

        for i in range(len(s1)):
            union(s1[i], s2[i])


        for i in range(len(baseStr)):
            if baseStr[i] not in rep:
                ans.append(baseStr[i])
                continue
            ans.append(find(baseStr[i]))

        return "".join(ans)