class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n= len(mat)
        m = len(mat[0])
        if r*c != n*m:
            return mat
        
        li = []
        res = [[0]*c for i in range(r)]
        
        for i in range(n):
            for j in range(m):
                li.append(mat[i][j])
         
        k = 0
        
        for i in range(r):
            for j in range(c):
                res[i][j] = li[k]
                k +=1
        
        return res
        
        
        
        
        
