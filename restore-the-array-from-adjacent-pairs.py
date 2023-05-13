class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        prereq = defaultdict(int)
        ans = []
        visited = set()

        for pair1, pair2 in adjacentPairs:
            adjList[pair1].append(pair2)
            adjList[pair2].append(pair1)
            prereq[pair1] +=1
            prereq[pair2] +=1


        def dfs(node):
            ans.append(node)
            visited.add(node)

            for child in adjList[node]:
                if child not in visited:
                    dfs(child)
            

        
        for degree in prereq:
            if prereq[degree] == 1 and degree not in visited:
                dfs(degree)


        return ans