class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def validatePath(r, c):
            return -1 < r < len(maze) and -1 < c < len(maze[0])

        def exit(r, c):
            if [r, c] == entrance:
                return False
            if r == len(maze) - 1 or c == len(maze[0])-1 or r == 0 or c == 0:
                return True
            return False


        q = deque()
        q.append((entrance))
        path = 1

        while q:
            length = len(q)

            for i in range(length):
                r, c = q.popleft()

                # if exit(r, c):
                #     return path
                
                maze[r][c] = "+"
                for d in direction:
                    x = r + d[0]
                    y = c + d[1]

                    if validatePath(x, y) and maze[x][y] == ".":
                        q.append((x, y))
                        maze[x][y] = "+"
                        if exit(x, y):
                            return path
            path +=1


        return -1