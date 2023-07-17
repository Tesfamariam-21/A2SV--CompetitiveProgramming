class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        champagne = [[0] * (query_row + 1) for _ in range(query_row + 1)]
        champagne[0][0] = poured

        for i in range(query_row):
            for j in range(i + 1):
                excess = (champagne[i][j] - 1) / 2
                if excess > 0:
                    champagne[i + 1][j] += excess
                    champagne[i + 1][j + 1] += excess

        return min(1, champagne[query_row][query_glass])
