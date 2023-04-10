class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()

        def dfs(index):
            for i in range(len(isConnected[index])):
                if isConnected[index][i] == 1 and i not in visited:
                    visited.add(i)
                    dfs(i)

            
        for i in range(len(isConnected)):
            if i in visited:
                continue
            visited.add(i)
            provinces += 1
            dfs(i)

        return provinces