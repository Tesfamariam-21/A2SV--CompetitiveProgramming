# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def helper(root):
            nonlocal count
            if not root:
                return [0, 0]
            
            left = helper(root.left)
            right = helper(root.right)
            total = [0, 0]
            total[0] = left[0] + right[0] + root.val
            total[1] = left[1] + right[1] + 1

            if root.val == total[0]// total[1]:
                count +=1
            
            return total

        helper(root)

        return count