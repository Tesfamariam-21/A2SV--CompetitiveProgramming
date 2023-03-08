# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def balance(root):
            if not root:
                return 0
            left = balance(root.left)
            right = balance(root.right)
            # print(left,right)

            if abs(left - right) > 1:
                return -1
            if left == -1:
                return -1
            if right == -1:
                return -1
            
            return 1 + max(left, right)
        
        if balance(root) == -1:
            return False

        return True