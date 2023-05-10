class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        color = [0]*(len(graph))

        def dfs(node):
            if color[node] == 1:
                return False

            if color[node] == 2 or graph[node] == []:
                color[node] = 2             
                return True


            color[node] = 1
            
            for child in graph[node]:
                if not dfs(child):
                    return False
            color[node] = 2
            return True



        for i in range(len(color)):
            if color[i] == 0:
                dfs(i)
        ans = []
        for i in range(len(color)):
            if color[i] == 2:
                ans.append(i)
        return sorted(ans)





        # safeNode = []
        # res = []
        # outdegree = defaultdict(list)
        # q = deque()


        # for i, num in enumerate(graph):
        #     if num == []:
        #         safeNode.append(0)
        #         q.append(i)
        #     else:
        #         safeNode.append(len(graph[i]))

        # for i in range(len(graph)):
        #     for j in range(len(graph[i])):
        #         outdegree[graph[i][j]].append(i)


        # while q:
        #     length = len(q)
            
        #     for _ in range(length):
        #         element = q.popleft()
        #         res.append(element)

        #         for i in range(len(outdegree[element])):
        #             safeNode[outdegree[element][i]] -=1

        #             if safeNode[outdegree[element][i]] == 0:
        #                 q.append(outdegree[element][i])

        # return sorted(res)









            

        return safeNode