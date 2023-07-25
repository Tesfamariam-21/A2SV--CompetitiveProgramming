class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        row, col = click
        
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        
        def dfs(r, c):
            num = 0
            for i in range(r-1, r+2):
                for j in range(c-1, c+2):
                    if 0 <= i < m and 0 <= j < n and board[i][j] == 'M':
                        num += 1
            
            if num > 0:
                board[r][c] = str(num)
            else:
                board[r][c] = 'B'
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if 0 <= i < m and 0 <= j < n and board[i][j] == 'E':
                            dfs(i, j)
        
        dfs(row, col)
        return board