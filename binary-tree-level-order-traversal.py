# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict_ = defaultdict(list)

        def traverse(root, level):
            if not root:
                return 
            dict_[level].append(root.val)

            if root.left:
                traverse(root.left, level + 1)
            if root.right:
                traverse(root.right, level + 1)

        traverse(root, 0)

        return list(dict_.values())








        # ans = []
        # queue = []

        # def breadthFirst(root, qu):
        #     if not root:
        #         return

        #     queue.append(root.val)
        #     # ans.append(queue)

        #     while queue:
        #         q = queue.pop()
        #         if q:
        #             ans.append(q)
        #             breadthFirst(root.right, q)
        
        # breadthFirst(root, [])
        
        # return ans