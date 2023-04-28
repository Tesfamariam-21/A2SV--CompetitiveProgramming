class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direction = { (1,0), (-1,0), (0,1), (0,-1) }
        q = deque()
        visited = set()

        def validatePath(r, c):
            return -1 < r < len(mat) and -1 < c < len(mat[0])


        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i,j))

        while q:
            r, c, distance = q.popleft()

            mat[r][c] = distance

            for dr, dc in direction:
                if (r+dr, c + dc) not in visited and validatePath(r+dr, c + dc):
                    q.append((r+dr, c+dc, distance + 1))
                    visited.add((r+dr, c+dc))
       
        return mat