class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        color = [-1] * (n+1)

        for d in dislikes:
            adjList[d[0]].append(d[1])
            adjList[d[1]].append(d[0])


        def dfs(d, c):            
            color[d] = c
            for val in adjList[d]:
                if color[val] != -1:
                    
                    if c^1 == color[val]:
                        continue
                    else:
                        print(color[val], c^1)
                        return False
                if not dfs(val, c^1):
                    return False
            
            return True

        for adj in adjList:
            if color[adj] != -1:
                continue
            if not dfs(adj, 0):
                return False
            
        
        return True