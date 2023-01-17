class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag = {}
        index = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    flag[index] = [i, j]
                    index += 1
                    
        for dict_ in flag.values():
              
            for col in range(len(matrix[0])):
                matrix[dict_[0]][col] = 0
                
            for row in range(len(matrix)):
                matrix[row][dict_[1]] = 0
                    
        return matrix
        
        
        
        