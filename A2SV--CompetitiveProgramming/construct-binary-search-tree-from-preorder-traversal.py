# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        def makeTree(index, index2):
            if index2 < index:
                return None

            # if index2 == index:
            #     return TreeNode(preorder[index2])

            
            node = TreeNode(preorder[index])
            root_index = index2 + 1 
            for i in range(index+1,len(preorder)):
                if preorder[index] <= preorder[i]:
                    root_index = i
                    break
                    
            
            node.left = makeTree(index + 1, root_index-1)
            node.right = makeTree(root_index, index2)

            return node

        return makeTree(0, len(preorder)-1)
