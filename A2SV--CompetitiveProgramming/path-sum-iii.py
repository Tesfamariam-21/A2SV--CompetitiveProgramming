# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dict_ = defaultdict(int)
        count = 0
        dict_[0] = 1

        def sumPath(root, prefix):
            nonlocal count

            if not root:
                return
            
            prefix += root.val

            if prefix - targetSum in dict_:
                count+= dict_[prefix - targetSum]
            
            dict_[prefix] += 1

            sumPath(root.left, prefix)
            sumPath(root.right, prefix)
            dict_[prefix] -= 1
            return

        sumPath(root, 0)
        return count