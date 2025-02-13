class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        for i in range(9):
            set_ = set()
            set_2 = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in set_:
                        return False
                    
                    set_.add(board[i][j])
                
                if board[j][i] != ".":
                    if board[j][i] in set_2:
                        return False
                    set_2.add(board[j][i])
                    
        
        for k in range(0, 9, 3):
            for l in range(0, 9, 3):
                set_ = set()
                for i in range(k, k + 3):
                    for j in range(l, l + 3):
                        if board[i][j] != ".":
                            if board[i][j] in set_:
                                return False
                        set_.add(board[i][j]) 
                
        return True


        # ans = []

        # for i in range(9):
        #     for j in range(9):
        #         if board[i][j] == ".":
        #             continue

        #         item = board[i][j]
        #         ans += [(i, item), (item, j), (i//3, j//3, item)]

        # return len(ans) == len(set(ans))


