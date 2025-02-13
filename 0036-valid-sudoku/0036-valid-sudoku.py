class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        for i in range(9):
            set_ = set()
            set_2 = set()
            set_3 = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in set_:
                        return False
                    
                    set_.add(board[i][j])
                
                if board[j][i] != ".":
                    if board[j][i] in set_2:
                        return False
                    set_2.add(board[j][i])

                row_index = (i // 3) * 3 + (j // 3)
                col_index = (i % 3) * 3 + (j % 3)

                if board[row_index][col_index] != ".":
                    if board[row_index][col_index] in set_3:
                        return False
                    set_3.add(board[row_index][col_index])
                    
                
        return True
        


        # ans = []

        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] == ".":
        #             continue

        #         item = board[i][j]
        #         ans += [(i, item), (item, j), (i//3, j//3, item)]

        # return len(ans) == len(set(ans))


