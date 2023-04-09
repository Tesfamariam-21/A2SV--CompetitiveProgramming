class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        dir = [(1, 0),(-1, 0),(0, 1), (0, -1)]
        source = image[sr][sc]

        def validatePath(r,c):
            return-1 < r < len(image) and -1 < c < len(image[0])
        

        def dfs(r, c):
            nonlocal visited
            nonlocal source

            if validatePath(r,c) and (r,c) not in visited and image[r][c] == source:               
                image[r][c] = color
                visited.add((r, c))
                for d in dir:
                    dfs(r + d[0], c + d[1])

            
        dfs(sr, sc) 

        return image