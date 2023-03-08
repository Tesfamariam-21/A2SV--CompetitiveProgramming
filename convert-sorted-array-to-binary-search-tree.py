# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def convert(left, right):
            mid = (left + right)// 2

            node = TreeNode(nums[mid])

            if left == right:
                return node
            if left > right:
                return 
            node.right = convert(mid+1, right)
            node.left = convert(left, mid-1)

            return node

        return convert(0, len(nums)-1)