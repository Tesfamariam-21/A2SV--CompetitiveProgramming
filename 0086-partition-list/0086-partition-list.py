# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#        dummy nodes
        greaterNode = ListNode()
        lessNode = ListNode()
        lessThan = lessNode
        greaterThan = greaterNode
        iteratorNode = head  #iteratorNode
        cnt = 0
        
        while iteratorNode:
            if iteratorNode.val < x:
                lessThan.next = iteratorNode
                lessThan = lessThan.next
            else:
                greaterThan.next = iteratorNode
                greaterThan = greaterThan.next
            cnt +=1
            
            iteratorNode = iteratorNode.next

        lessThan.next = greaterNode.next
        greaterThan.next = None
        
        return lessNode.next