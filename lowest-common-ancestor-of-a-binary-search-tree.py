# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

#         if p is None or q is None:
#             return None

#         if root==p or root==q:
#             return root

#         if (root.left==p and root.right==q) and (root.left==q and root.right==p):
#             return root

#         if p.val<root.val and q.val<root.val:
#             return self.lowestCommonAncestor(root.left, p, q)

#         if p.val>root.val and q.val>root.val:
#             return self.lowestCommonAncestor(root.right, p, q)
            
#         return root

        # pPath = []
        # qPath = []

        # def pFind(root, p):
        #     nonlocal pPath
        #     if p.val < root.val:
        #         pPath.extend(pFind(root.left, p))
        #         return [root.val]
        #     elif p.val > root.val:
        #         pPath.extend(pFind(root.right, p))
        #         return [root.val]
        #     else:
        #         return [root.val]
            
       

        # def qFind(root, q):
        #     nonlocal qPath
        #     if q.val < root.val:
        #         qPath.extend(qFind(root.left, q))
        #         return [root.val]
        #     elif q.val > root.val:
        #         qPath.extend(qFind(root.right, q))
        #         return [root.val]
        #     else:
        #         return [root.val]

        # pPath.extend(pFind(root, p))
        # qPath.extend(qFind(root, q))

        # pRight = len(pPath)
        # qRight = len(qPath)
        # print(pPa)

        # while pRight >= 0 and qRight >= 0:
        #     if pPath[pRight] != qPath[qRight]:
        #         return pPath[pRight+1]
        #     pRight -=1
        #     qRight -=1
        
        # return pPath[pRight + 1]