class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i: [] for i in range(n)}
        for p, c in edges:
            adj[p].append(c)
            adj[c].append(p)

        def dfs(c, parent):
            t = 0

            for child in adj[c]:
                if child == parent:
                    continue
                childTime = dfs(child, c)
                if childTime or hasApple[child]:
                    t += (2 + childTime)

            return t

        return dfs(0, -1)

        