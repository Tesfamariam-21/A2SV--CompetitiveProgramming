class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights)-1):
            if heights[i +1] < heights[i]:
                continue

            heappush(heap, heights[i+1] - heights[i])

            if len(heap) > ladders:
                bricks -= heappop(heap)

            if bricks < 0:
                return i
          
        return len(heights) - 1