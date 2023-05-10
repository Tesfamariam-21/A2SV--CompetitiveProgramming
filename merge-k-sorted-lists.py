# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        dummy = head = ListNode()

        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i, lists[i]))

        heapify(heap)

        while heap:
            val, index, node = heappop(heap)
            head.next = node
            head = head.next

            if node.next:
                heappush(heap, (node.next.val, index, node.next))


        return dummy.next