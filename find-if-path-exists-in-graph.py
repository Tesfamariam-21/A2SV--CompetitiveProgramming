class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        rep = {i:i for i in range(n)}
        size = [1 for i in range(n)]

        def representative(member):
            if member == rep[member]:
                return member
            
            rep[member] = representative(rep[member])
            return rep[member]

        def union(member1, member2):
            repMember1 = representative(member1)
            repMember2 = representative(member2)

            if size[repMember1] < size[repMember2]:
                rep[repMember1] = repMember2
                size[repMember2] += size[repMember1]
            else:
                rep[repMember2] = repMember1
                size[repMember1] += size[repMember2]

        for member1, member2 in edges:
            union(member1, member2)
        

        if representative(source) == representative(destination):
            return True
        return False
            




        # adjList = defaultdict(list)

        # for e in edges:
        #     adjList[e[0]].append(e[1])
        #     adjList[e[1]].append(e[0])

        # visited = set()

        # def dfs(s, visited):

        #     if s == destination:
        #         return True

        #     visited.add(s)

        #     for child in adjList[s]:
        #         if child not in visited:
        #             if dfs(child, visited):
        #                 return True

        #     return False

        # return dfs(source, visited)