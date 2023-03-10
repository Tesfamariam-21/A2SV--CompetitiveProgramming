# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            ans.append(root.val)
            traverse(root.right)

        traverse(root)
        c = Counter(ans)
        max_ = max(c.values())
        num = []
        for key, val in c.items():
            if val == max_:
                num.append(key)
        return num