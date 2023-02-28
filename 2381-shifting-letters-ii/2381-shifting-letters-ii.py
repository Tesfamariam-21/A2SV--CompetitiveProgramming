class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        grid = [0]*(len(s)+1)
      
        for start, end, direction in shifts:
            if direction:
                grid[start] += 1
                grid[end+1] -= 1
            else:
                grid[start] -= 1
                grid[end+1] += 1
          
        start = grid[0]
      
        for i in range(1, len(grid)):
            start += grid[i]
            grid[i] = (start % 26)

        res = []

        for i in range(len(s)):
            res.append(chr((ord(s[i]) - 97 + grid[i]) % 26 + 97))
        
        
        return ''.join(res)
                