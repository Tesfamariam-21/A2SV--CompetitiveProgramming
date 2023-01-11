class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        row, col = len(mat), len(mat[0])
        
        curRow = curCol = 0
        ans = []
        up = True
        
        while len(ans) < row*col:
            if up:
                while curRow >=0 and curCol < col:
                    ans.append(mat[curRow][curCol])
                    curRow -= 1
                    curCol += 1
                
                if curCol == col:
                    curCol -= 1
                    curRow += 2
                else:
                    curRow +=1                
                up = False
            
            else:
                while curRow < row and curCol >=0:
                    ans.append(mat[curRow][curCol])
                    curRow += 1
                    curCol -= 1
                if curRow == row:
                    curRow -= 1
                    curCol += 2
                else:
                    curCol += 1
                up = True
        
        return ans
                
                