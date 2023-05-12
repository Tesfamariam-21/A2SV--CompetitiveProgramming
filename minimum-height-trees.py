class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(set)
        q = deque()
        unvisited = n 

        if n==1:
            return [0]

        for e in edges:
            adjList[e[0]].add(e[1])
            adjList[e[1]].add(e[0])

        for deg in adjList:
            if len(adjList[deg]) == 1:
                q.append(deg)
                unvisited -=1


        while unvisited:
            l = len(q)
            

            for i in range(l):
                ele = q.popleft()
                parent = adjList[ele].pop()
                

                adjList[parent].discard(ele)
                

                if len(adjList[parent]) == 1:
                    q.append(parent)
                    unvisited -=1
                        
                
                

        return q