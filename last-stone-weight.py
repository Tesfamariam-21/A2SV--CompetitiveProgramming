class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *=-1
        heapify(stones)
        
        while len(stones) > 1:
            n = -1 * heappop(stones)
            m = -1 * heappop(stones)

            heappush(stones, -1 *(n - m))


        return -1 * stones[0]