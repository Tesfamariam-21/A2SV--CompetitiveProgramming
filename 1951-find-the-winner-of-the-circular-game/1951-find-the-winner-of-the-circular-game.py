class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        queue = deque(range(1, n + 1))

        while len(queue) > 1:

            for i in range(1, k):
                queue.append(queue.popleft())

            queue.popleft()

        return queue[0]

        

        # arr = [i + 1 for i in range(n)]

        # idx = 0
        # while len(arr) > 1:
        #     idx = (idx + k - 1) % len(arr)
        #     arr.pop(idx)

        # return arr[0]
        