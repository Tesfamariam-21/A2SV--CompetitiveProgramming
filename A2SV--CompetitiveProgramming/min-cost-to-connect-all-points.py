class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))

        edges.sort()
        minCost = 0
        numEdges = 0
        parent = list(range(len(points)))

        for cost, u, v in edges:
            if find(u) != find(v):
                union(u, v)
                minCost += cost
                numEdges += 1
                if numEdges == len(points) - 1:
                    break

        return minCost
