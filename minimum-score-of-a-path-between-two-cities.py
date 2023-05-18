class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep= {}
        distance =[1000000 for _ in range(n+1)]
        rank = [1] * (n + 1)

        for i in range(1, n+1):
            rep[i] = i
        
        def find(char):
            if char == rep[char]:
                return rep[char]

            rep[char] = find(rep[char])
            return rep[char]

        def union(char1, char2, dist):
            c1 = find(char1)
            c2 = find(char2)

            if rank[c1] < rank[c2]:
                rep[c1] = c2
                rank[c2] += rank[c1]
                distance[c2] = min(distance[c2], distance[c1], dist)
            else:
                rep[c2] = c1
                rank[c1] += rank[c2]
                distance[c1] = min(distance[c1], distance[c2], dist)

        for i in range(len(roads)):
            union(roads[i][0], roads[i][1], roads[i][2])


        return distance[find(1)]