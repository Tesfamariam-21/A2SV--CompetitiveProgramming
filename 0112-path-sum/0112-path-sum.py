# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node, s):
            if not node:
                return False

            s += node.val
            if not node.right and not node.left and s == targetSum:
                return True

            return  dfs(node.left, s) or dfs(node.right, s)


        return dfs(root, 0)
