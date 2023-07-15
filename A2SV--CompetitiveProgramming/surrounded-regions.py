class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r, c = len(board), len(board[0])
        if r == 1 and c == 1 and board[0][0] == "O":
            return 

        dir_ = {(1, 0), (0, 1), (-1, 0), (0, -1)}

        def dfs(i, j):
            if 0 <= i < r and 0 <= j < c and board[i][j] == "O":
                board[i][j] = "temp"
                for d in dir_:
                    dfs(i + d[0], j + d[1])

            return 

        for i in range(r):
            dfs(i, 0)
            dfs(i, c-1)
    
        for j in range(c):
            dfs(0, j)
            dfs(r-1, j)

        for i in range(r):
            for j in range(c):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "temp":
                    board[i][j] = "O"
