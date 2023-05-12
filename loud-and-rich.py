class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adjList = defaultdict(list)
        indeg = [1] * len(quiet)
        q = deque()
        res = [0] * len(quiet)
        for i in range(len(quiet)):
            res[i] = i

        for r, p in richer:
            adjList[r].append(p)
            indeg[p] +=1

        for i in range(len(quiet)):
            if indeg[i] == 1:  
                q.append(i)

        while q:
            l = len(q)

            for i in range(l):
                ele = q.popleft()

                for child in  adjList[ele]:
                    indeg[child] -=1
                    if quiet[ele] < quiet[child]:
                        res[child] = res[ele]
                        quiet[child] = quiet[ele]
                    if indeg[child] == 1:
                        q.append(child)


        return res