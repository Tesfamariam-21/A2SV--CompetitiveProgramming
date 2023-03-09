# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        answer = []
        value=0

        def traverse(root):

            if not root:
                return root

            nonlocal value


            traverse(root.right)
            value+=root.val
            root.val=value
            traverse(root.left)
            

        traverse(root)
        return root