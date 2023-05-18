class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = {1: [(0, 1), (0, -1)],
                2: [(1, 0), (-1, 0)],
                3: [(0, -1), (1, 0)],
                4: [(0, 1), (1, 0)],
                5: [(0, -1), (-1, 0)],
                6: [(0, 1), (-1, 0)]}
        rep = {(i, j): (i, j) for i in range(m) for j in range(n)}
        size = {element: 1 for element in rep}

        def validatePath(r, c):
            return 0 <= r < m and 0 <= c < n

        def find(element):
            if element == rep[element]:
                return element
            rep[element] = find(rep[element])
            return rep[element]


        def union(coord1, coord2):
            rep1 = find(coord1)
            rep2 = find(coord2)

            if size[rep1] < size[rep2]:
                rep[rep1] = rep2
                size[rep2] += size[rep1]
            else:
                rep[rep2] = rep1
                size[rep1] += size[rep2]

        for i in range(m):
            for j in range(n):
                curr = grid[i][j]
                for dx, dy in dirs[curr]:
                    ni, nj = i + dx, j + dy
                    if validatePath(ni, nj):
                        if (-dx, -dy) in dirs[grid[ni][nj]]:
                            union((i, j), (ni, nj))


        return find((0, 0)) == find((m - 1, n - 1))





        # m, n = len(grid), len(grid[0])
        # dirs = {1: [(0, 1), (0, -1)],
        #         2: [(1, 0), (-1, 0)],
        #         3: [(0, -1), (1, 0)],
        #         4: [(0, 1), (1, 0)],
        #         5: [(0, -1), (-1, 0)],
        #         6: [(0, 1), (-1, 0)]}
        # queue = [(0, 0)]
        # visited = set()
        
        # while queue:
        #     x, y = queue.pop(0)
        #     if (x, y) == (m-1, n-1):
        #         return True
        #     visited.add((x, y))
        #     for dx, dy in dirs[grid[x][y]]:
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
        #             for dx2, dy2 in dirs[grid[nx][ny]]:
        #                 if (dx2, dy2) == (-dx, -dy):
        #                     queue.append((nx, ny))
        #                     break
        # return False