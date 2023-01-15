class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        ans = []
        
        for i in range(len(grid)-2):
            li = []
            for j in range(len(grid[0])-2):
                max_ = 0
                for k in range(3):
                    for l in range(3):
                        max_ = max(max_, grid[i+k][j+l])
                
                li.append(max_)
        
            ans.append(li)
        
        return ans
                
        