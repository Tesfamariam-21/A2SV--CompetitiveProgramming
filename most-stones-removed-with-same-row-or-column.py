class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = {}

        def find(x):
            if x!= rep[x]:
                rep[x] = find(rep[x])

            return rep[x]

        def union(x, y):
            rep.setdefault(x, x)
            rep.setdefault(y, y)

            r = find(x)
            c = find(y)
            
            if r != c:
                rep[c] = r

        for i, j in stones:
            union(i, ~j)

        group = set()

        for k in rep:
            g = find(k)
            group.add(g)

        return len(stones) - len(group)
            
        # visited = set()
        # graph = defaultdict(list)
        # group = 0

        # for i, j in stones:
        #     graph[i].append((i, j))
        #     graph[~j].append((i, j))

        # def dfs(r, c):

        #     for i, j in graph[r]:
        #         if (i, j) not in visited:
        #             visited.add((i, j))
        #             dfs(i, j)

        #     for i, j in graph[~c]:
        #         if (i, j) not in visited:
        #             visited.add((i, j))
        #             dfs(i, j)


        # for i, j in stones:
        #     if (i, j) not in visited:
        #         group +=1
        #         visited.add((i, j))
        #         dfs(i, j)
        
        
        # return len(stones) - group