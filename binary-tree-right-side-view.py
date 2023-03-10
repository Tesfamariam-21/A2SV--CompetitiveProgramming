# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
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
        for elements in dict_.values():
            ans.append(elements[-1])

        return ans