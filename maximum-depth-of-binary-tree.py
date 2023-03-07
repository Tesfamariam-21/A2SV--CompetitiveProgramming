# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
        # if not root:
        #     return 0
            
        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)     
        
        # return 1 + max(left, right)


# def depthTraverse(root):
#             if not root:
#                 return 0
            
#             left = depthTraverse(root.left)
#             right = depthTraverse(root.right)
            
#             return 1 + max(left, right)
        
        
#         return depthTraverse(root)