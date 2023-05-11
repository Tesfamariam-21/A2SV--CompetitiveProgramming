class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dict_ = defaultdict(list)
        d = defaultdict(list)
        res = [[] for _ in range(n)]
        q = deque()
        prereq = [0] * n

        for i, j in edges:
            dict_[i].append(j)
            d[j].append(i)
            prereq[j] += 1

        for i, val in enumerate(prereq):
            if val == 0:
                q.append(i)

        while q:
            element = q.popleft()
            for i in d[element]:
                res[element].append(i)
                res[element].extend(res[i])
                res[element] = sorted(set(res[element]))
            for i in dict_[element]:
                prereq[i] -= 1
                if prereq[i] == 0:
                    q.append(i)

        return res