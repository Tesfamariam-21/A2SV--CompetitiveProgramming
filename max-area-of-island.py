class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        dict_ = [(1,0), (-1,0), (0,1), (0,-1)]
        max_ = 0

        def validatePath(r,c):
            return -1 < r < len(grid) and -1 < c < len(grid[0]) 

        def dfs(r,c):
            if not validatePath(r,c):
                return 0   
            if (r, c) in visited or grid[r][c] != 1:
                return 0
  

            visited.add((r,c))
            area = 1
            for d in dict_:
                area += dfs(r + d[0], c + d[1])

            return area 



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    area =dfs(i,j)
                    max_ = max(max_, area)
                
        return max_