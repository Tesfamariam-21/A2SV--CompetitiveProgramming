# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        self.ans = 0

        def depth(root,s):
            self.ans
            if root:
                s +=str(root.val)
                depth(root.left, s)
                depth(root.right, s)
                if not root.left and not root.right:
                    self.ans += int(s)
                    return


        depth(root, "")
        return self.ans