class Solution(object):
    def allPathsSourceTarget(self, graph):
        adjList = defaultdict(list)
        visited = set()
        ans = []
        n = len(graph)

        for i in range(len(graph)):
            adjList[i] = graph[i]

        def dfs(g, n, arr):
            if g == n-1:
                ans.append(arr + [g])
                return
            
            for path in graph[g]:
                dfs(path, n, arr + [g])
        

        dfs(0, n, [])
        return ans