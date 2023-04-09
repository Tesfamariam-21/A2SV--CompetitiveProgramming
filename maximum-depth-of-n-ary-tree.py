"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_ = 0

        def dfs(root, h):
            nonlocal max_
            if not root:
                return
            max_ = max(max_, h)

            for i in range(len(root.children)):
                dfs(root.children[i], h+1)
            

        dfs(root, 1)

        return max_