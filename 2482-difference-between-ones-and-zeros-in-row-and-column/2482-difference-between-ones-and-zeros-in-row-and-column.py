class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        onescol = []
        zerosRow = []
        zeroscol = []
        
        for item in grid:
            onesRow.append(item.count(1))
            zerosRow.append(item.count(0))
        
        column =list(zip(*grid))
        for item in column:
            zeroscol.append(item.count(0))
            onescol.append(item.count(1))
            
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = onesRow[i] + onescol[j] - zerosRow[i] - zeroscol[j]
            
        print(column)
        print(onesRow)
    
        return grid
        