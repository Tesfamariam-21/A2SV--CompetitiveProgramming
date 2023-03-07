# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkValid(root, min_, max_):
            if not root:
                return True
            if root.val <= min_ or root.val >= max_:
                return False

            
            return checkValid(root.left, min_, root.val) and checkValid(root.right, root.val, max_)
            

        return checkValid(root, float("-inf"), float("inf"))