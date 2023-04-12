# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        self.ans = ""

        def dfs(root):
            if not root:
                return ""
            if not root.left and root.right:
                self.ans += "(" + str(root.val) + "()"
            else:
                self.ans += "(" + str(root.val)

            dfs(root.left)
            dfs(root.right)
            self.ans +=")"
            

        dfs(root)
        return self.ans[1:len(self.ans)-1]