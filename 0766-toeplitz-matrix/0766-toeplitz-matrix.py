class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        Toeplitz = False
        
        dict_ = defaultdict(set)
        li = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dict_[j-i].add(matrix[i][j])
                li = dict_[j-i]
                if(len(li) > 1):
                    return False
        
        return True