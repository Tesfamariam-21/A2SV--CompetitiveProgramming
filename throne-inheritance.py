class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.familyTree = defaultdict(list)
        self.alive = defaultdict(list)
        self.familyTree[kingName] = []
        self.alive[kingName] = True
        

    def birth(self, parentName: str, childName: str) -> None:
        self.familyTree[parentName].append(childName)
        self.alive[childName] = True
        

    def death(self, name: str) -> None:
        self.alive[name] = False

        

    def getInheritanceOrder(self) -> List[str]:
        visited = set()
        res = []


        def dfs(name):
            visited.add(name)
            if self.alive[name]:
                res.append(name)


            for child in self.familyTree[name]:
                if child not in visited:
                    dfs(child)
            

        dfs(self.king)
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()