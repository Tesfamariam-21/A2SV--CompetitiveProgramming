class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
            
        return ans + 1

        # queue = deque(range(1, n + 1))

        # while len(queue) > 1:

        #     for _ in range(1, k):
        #         queue.append(queue.popleft())

        #     queue.popleft()

        # return queue[0]

    # def findTheWinner(self, n: int, k: int) -> int:
    #     return self.winnerHelper(n, k) + 1

    # def winnerHelper(self, n: int, k: int) -> int:
    #     if n == 1:
    #         return 0
    #     return (self.winnerHelper(n - 1, k) + k) % n        

        # arr = [i + 1 for i in range(n)]

        # idx = 0
        # while len(arr) > 1:
        #     idx = (idx + k - 1) % len(arr)
        #     arr.pop(idx)

        # return arr[0]
        