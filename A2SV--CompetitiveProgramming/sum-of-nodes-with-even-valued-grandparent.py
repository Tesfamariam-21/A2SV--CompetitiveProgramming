# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root, father,gp):
            if not root:
                return 0
            x = 0
            if(gp % 2 == 0):
                x = root.val
            x+=dfs(root.left, root.val, father)
            x+=dfs(root.right, root.val, father)
            return x

        return dfs(root,1,1)