class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        dict_ = defaultdict(set)

        for i in range(rows):
            for j in range(cols):
                key = i - j
                dict_[key].add(matrix[i][j])
                if len(dict_[key]) > 1:
                    return False
                
        
        return True

        # rows, cols = len(matrix), len(matrix[0])

        # for i in range(rows - 1):
        #     for j in range(cols - 1):
        #         print(i - j)
        #         if matrix[i][j] != matrix[i + 1][j + 1]:
        #             return False
        # return True

                