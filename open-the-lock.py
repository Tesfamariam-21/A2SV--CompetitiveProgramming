class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([[0,0,0,0]])
        target = list(map(int, target))
        path = 0
        visited = set()

        increment = [[1, 0, 0, 0], [-1, 0, 0, 0], [0, 1, 0, 0], [0, -1, 0, 0], [0, 0, 1, 0], [0, 0, -1, 0], [0, 0, 0, 1] ,[0, 0, 0, -1]]

        if "0000" in deadends:
            return -1

        while q:
            length = len(q)

            for _ in range(length):
                slots = q.popleft()
                print(slots)

                if slots == target:
                    return path
                
                for inc in increment:
                    a = [0]*4
                    for i in range(4):
                        a[i] = slots[i]+inc[i]
                        if a[i] < 0:
                            a[i] = 9
                        elif a[i] > 9:
                            a[i] = 0
                    if str("".join(map(str,a))) in deadends or str(a) in visited:
                        continue
                    q.append(a)
                    visited.add(str(a))

            path +=1


        return -1