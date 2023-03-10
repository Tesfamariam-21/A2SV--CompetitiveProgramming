# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_ = 0
        dict_ = defaultdict(list)

        def traverse(root, level, n):
            if not root:
                return
            dict_[level].append(n)

            if root.left:
                traverse(root.left, level + 1, 2*n)
            if root.right:
                traverse(root.right, level + 1, 2*n+1)
        
        traverse(root, 1, 1)

        for key, val in dict_.items():
            if val[-1] - val[0] +1 > max_:
                max_ = val[-1] - val[0] + 1

        return max_