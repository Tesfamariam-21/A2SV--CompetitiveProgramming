class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjList = defaultdict(list)

        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])

        visited = set()

        def dfs(s, visited):
            nonlocal adjList

            if s == destination:
                return True

            visited.add(s)

            for child in adjList[s]:
                if child not in visited:
                    if dfs(child, visited):
                        return True

            return False

        return dfs(source, visited)