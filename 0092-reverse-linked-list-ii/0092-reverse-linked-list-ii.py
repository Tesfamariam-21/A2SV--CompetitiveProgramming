# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return None
        if right == left:
            return head
        
        current = head
        nextNode = current.next
        prevNode = None
        cnt = 0
        
        for i in range(left-1):
            prevNode = current
            current = nextNode
            nextNode = current.next
            cnt +=1
        leftNode = current
        prevLeft = prevNode
            # if 
            # i == left-1:
            #     leftNode = 
        # print(cnt, current)
 
        # while nextNode != None and cnt <=right:
        for i in range(right - left + 1 ):
            print(current.val)
            if cnt == right-1:
                if nextNode == None:
                    if prevLeft != None and prevLeft.next != None:
                        prevLeft.next = current
                        leftNode.next = None
                    else:
                        pass
                else:
                    leftNode.next = current.next
                if prevLeft != None:
                    prevLeft.next = current
                else:
                    head = current
                
                     
            current.next = prevNode
            prevNode = current
            current = nextNode
            if right - 1 != cnt:
                nextNode = current.next
            cnt +=1
            
 
        # current.next = prevNode
         
        return head
            
        