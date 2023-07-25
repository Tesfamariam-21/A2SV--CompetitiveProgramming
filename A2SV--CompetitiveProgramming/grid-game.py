class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        p1, p2 = [grid[0][0]], [grid[1][0]]
        for a, b in zip(grid[0][1:], grid[1][1:]):
            p1.append(p1[-1] + a)
            p2.append(p2[-1] + b)
        
        ans = float("inf")

        for i in range(len(grid[0])):
            right = p1[-1] - p1[i]
            left = p2[i] - grid[1][i]
            ans = min(ans, max(left, right))
        
        return ans