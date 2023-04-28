# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        average = []
        visited = set()

        queue = deque([root])
        total = root.val

        while queue:
            l  = len(queue)
            average.append(total/l)
            total = 0
            
            for i in range(l):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    total += node.left.val
                if node.right:
                    queue.append(node.right)
                    total += node.right.val



        return average