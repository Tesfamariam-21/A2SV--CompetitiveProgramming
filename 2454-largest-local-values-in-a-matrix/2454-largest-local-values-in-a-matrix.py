class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        arr = []


        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_ = 0
                for k in range(3):
                    for l in range(3):
                        if grid[i+k][j+l] > max_:
                            max_ = grid[i+k][j+l]
                        
                 
                row.append(max_)
                
            
            arr.append(row)

        return arr


        