class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        d = { (1,0), (-1,0), (0,1), (0,-1), (-1,-1), (-1, 1), (1,-1), (1,1)}

        path = 1
        q = deque([(0,0)])

        def validatePath(r, c):
            return -1 < r < len(grid) and -1 < c < len(grid)

        while q:
            length = len(q)

            for i in range(length):
                r, c = q.popleft()    

                if r == n-1 and c == n-1:
                    return path

                for dr, dc in d:
                    if validatePath(r+dr, c + dc) and grid[r+dr][c+dc] == 0:
                        q.append((r+dr, c+dc))
                        grid[r+dr][c+dc] = 1
                
            path += 1
            

        return -1
