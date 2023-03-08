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

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         answer = []
#         maxNum = float("-inf")

#         def traverse(root):
#             nonlocal maxNum
#             if not root:
#                 return True
            
#             left = traverse(root.left)
#             if not left:
#                 return False
#             if maxNum >= root.val:
#                 return False
#             maxNum = max(maxNum, root.val)
#             right = traverse(root.right)
#             if not right:
#                 return False
#             return True

#         return traverse(root)

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         arr=[]
#         def traverse(root):
#            if not root:
#                return
#            traverse(root.left)
#            arr.append(root.val)
#            traverse(root.right)
#         traverse(root)
#         for i in range(len(arr)-1):
#             if arr[i]>=arr[i+1]:
#                 return False
#         return True