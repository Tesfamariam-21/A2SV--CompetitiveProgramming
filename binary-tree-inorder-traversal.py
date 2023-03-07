# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
        
        # or'   
        # ans = []
        # def traverse(root):

        #     if not root:
        #         return 

        #     traverse(root.left)
        #     ans.append(root.val)
        #     traverse(root.right)

        # traverse(root)
        # return ans