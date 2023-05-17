class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rep = {i:i for i in range(1, n+1)}
        rank = [1 for i in range(n+1)]

        def find(element):
            print(element, rep[element])
            if element == rep[element]:
                return element

            rep[element] = find(rep[element])
            return rep[element]

        def union(x, y, xrep, yrep):
            if xrep == yrep:
                return [x, y]

            if rank[xrep] > rank[yrep]:
                rep[yrep] = xrep
                rank[xrep] += rank[yrep]
            else:
                rep[xrep] = yrep
                rank[yrep] += rank[xrep]

        for x, y in edges:
            xrep = find(x)
            yrep = find(y)
            if xrep == yrep:
                return [x, y]
            union(x, y, xrep, yrep)