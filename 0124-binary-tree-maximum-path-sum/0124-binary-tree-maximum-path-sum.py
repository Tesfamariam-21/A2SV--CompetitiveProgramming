# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_ = float('-inf')
        
        def helperFunc(node):
            nonlocal max_
            if not node:
                return 0
            
            left = helperFunc(node.left)
            right = helperFunc(node.right)
            
            max_left = max(left, 0)
            max_right = max(right, 0)
            
            max_sum_through_node = node.val + max_left + max_right
            
            max_ = max(max_, max_sum_through_node)
            
            return node.val + max(max_left, max_right)
        
        helperFunc(root)
        return max_