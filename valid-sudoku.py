class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ans = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                item = board[i][j]
                ans += [(i, item), (item, j), (i//3, j//3, item)]

        return len(ans) == len(set(ans))