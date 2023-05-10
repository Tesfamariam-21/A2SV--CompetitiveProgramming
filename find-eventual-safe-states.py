class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeNode = []
        res = []
        outdegree = defaultdict(list)
        q = deque()


        for i, num in enumerate(graph):
            if num == []:
                safeNode.append(0)
                q.append(i)
            else:
                safeNode.append(len(graph[i]))

        for i in range(len(graph)):
            for j in range(len(graph[i])):
                outdegree[graph[i][j]].append(i)


        while q:
            length = len(q)
            

            for _ in range(length):
                element = q.popleft()
                res.append(element)

                for i in range(len(outdegree[element])):
                    safeNode[outdegree[element][i]] -=1

                    if safeNode[outdegree[element][i]] == 0:
                        q.append(outdegree[element][i])

        return sorted(res)









            

        return safeNode