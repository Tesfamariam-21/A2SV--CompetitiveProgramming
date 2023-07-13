class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        x, y = -1, -1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                    break
        
        
        bfs_queue = [(x, y)]
        second_bfs_queue = [(x, y)]
        grid[x][y] = 2

        while bfs_queue:
            new_bfs = []
            for x, y in bfs_queue:
                for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n and grid[cur_x][cur_y] == 1:
                        new_bfs.append((cur_x, cur_y))
                        second_bfs_queue.append((cur_x, cur_y))
                        grid[cur_x][cur_y] = 2
            bfs_queue = new_bfs

        distance = 0
        while second_bfs_queue:
            new_bfs = []
            for x, y in second_bfs_queue:
                for cur_x, cur_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= cur_x < n and 0 <= cur_y < n:
                        if grid[cur_x][cur_y] == 1:
                            return distance
                        elif grid[cur_x][cur_y] == 0:
                            new_bfs.append((cur_x, cur_y))
                            grid[cur_x][cur_y] = -1
                            
            second_bfs_queue = new_bfs
            distance += 1