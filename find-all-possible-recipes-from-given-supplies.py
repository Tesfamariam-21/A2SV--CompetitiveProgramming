class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        q = deque()
        res = []
        prereq = [0 for _ in range(len(recipes))]

        for index, items in enumerate(ingredients):
            for ingredient in items:
                if ingredient not in supplies:
                    prereq[index] += 1

        for index, indeg in enumerate(prereq):
            if indeg == 0:
                q.append(index)

        while q:
            length = len(q)

            for i in range(length):
                element = q.popleft()
                res.append(recipes[element])

                for index, ingred in enumerate(ingredients):
                    if recipes[element] in ingred:
                        prereq[index] -=1
                        if prereq[index] == 0:
                            q.append(index)


        return res