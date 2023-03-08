# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pPath = []
        qPath = []

        def pFind(root, p):
            nonlocal pPath
            if not root:
                return
            if p.val < root.val:
                pPath.extend(pFind(root.left, p))
                return [root]
            elif p.val > root.val:
                pPath.extend(pFind(root.right, p))
                return [root]
            else:
                return [root]
            
       

        def qFind(root, q):
            nonlocal qPath
            if not root:
                return 
            if q.val < root.val:
                qPath.extend(qFind(root.left, q))
                return [root]
            elif q.val > root.val:
                qPath.extend(qFind(root.right, q))
                return [root]
            else:
                return [root]

        pPath.extend(pFind(root, p))
        qPath.extend(qFind(root, q))

        pRight = len(pPath)-1
        qRight = len(qPath)-1
        print(pPath, qPath)

        while pRight >= 0 and qRight >= 0:
            if pPath[pRight] != qPath[qRight]:
                return pPath[pRight+1]
            pRight -=1
            qRight -=1
        
        return pPath[pRight + 1]