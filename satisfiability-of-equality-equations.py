class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {}
        rank = [1 for _ in range(26)]


        for i in range(len(equations)):
            rep[equations[i][0]] = equations[i][0]
            rep[equations[i][3]] = equations[i][3]


        def find(char):
            if char == rep[char]:
                return char
            
            rep[char] = find(rep[char])
            return rep[char]

        def union(char1, char2, equality):
            c1 = find(char1)
            c2 = find(char2)
          
            if c1 != c2:
                c1 = ord(c1) - 97
                c2 = ord(c2) - 97

                if rank[c1] <= rank[c2]:
                    rep[chr(c1 + 97)] = chr(c2 + 97)
                    rank[c2] += rank[c1]
                else:
                    rep[chr(c2 + 97)] = chr(c1 + 97)
                    rank[c1] += rank[c2]


        for item in equations:
            if item[1] == "=":
                union(item[0], item[3], item[1])


        for i in range(len(equations)):            
            if equations[i][1] == "!" and find(equations[i][0]) == find(equations[i][3]):
                return False


        return True