"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = 0
        dict_ = {}
        
        for e in employees:
            dict_[e.id] = e

        def dfs(emp):
            nonlocal importance

            importance += dict_[emp].importance

            for e in dict_[emp].subordinates:
                dfs(e)


        dfs(id)
        return importance