class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        Toeplitz = False
        
        dict_ = defaultdict(set)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dict_[j-i].add(matrix[i][j])
                if(len(dict_[j-i]) > 1):
                    return False
        
        return True