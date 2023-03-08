# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSubTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root:
                return False
            if not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False
            else:
                return isSubTree(root.left, subRoot.left) and isSubTree(root.right, subRoot.right)
               
        
        def search(root, subRoot):
            if not root:
                return root
            if not subRoot:
                return False

            if isSubTree(root, subRoot):
                 return True
            
            return search(root.left, subRoot) or search(root.right, subRoot)


        return search(root, subRoot)