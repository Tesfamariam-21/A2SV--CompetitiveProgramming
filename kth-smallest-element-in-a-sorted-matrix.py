class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if k > len(heap):
                    heappush(heap, -1 *matrix[i][j])
                else:
                    if -matrix[i][j] > heap[0]:
                        heappop(heap)
                        heappush(heap, -matrix[i][j])
                    

        
        return -heap[0]