class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        if len(bombs)==1:
            return 1
        
        adjList= defaultdict(list)
        visited = set()
        res = 0
       

        for i in range(len(bombs)):
            x, y, r = bombs[i]
            for j in range(len(bombs)):
                if i == j:
                    continue
                
                x2, y2, r2 = bombs[j]

                if r**2 >= ((x- x2)**2 + (y- y2)**2):
                    adjList[i].append(j)


        def dfs(node, v):
            v.add(node)

            for child in adjList[node]:
                if child not in v:
                    dfs(child, v)

            return v

        

        for i in range(len(bombs)):
            res = max(res, len(dfs(i, set())))

        return res