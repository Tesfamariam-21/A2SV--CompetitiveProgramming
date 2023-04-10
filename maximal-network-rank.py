class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        max_ = 0
        lenght1 = length2 = 0
        visited = set()

        for edge in roads:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])

        for i in range(n):
            length1 = len(graph[i])

            for j in range(i+1, n):
                if (i, j) in visited:
                    continue
                length2 = len(graph[j] - {i})
                max_ = max(max_, length1 + length2)
                visited.add((j, i))


        return max_