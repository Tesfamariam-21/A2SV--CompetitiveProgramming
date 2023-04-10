class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []
        noIn = [True] * n

        for f, t in edges:
            noIn[t] = False

        for i in range(len(noIn)):
            if noIn[i]:
                ans.append(i)

        return ans