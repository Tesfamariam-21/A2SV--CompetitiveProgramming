class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.left = ListNode()
        self.right = ListNode()     
        self.left.next = self.right
        self.right.prev = self.left   

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
            
        node = ListNode(value)
        node.prev, node.next  = self.right.prev, self.right
        self.right.prev.next = node     
        self.right.prev = node
        self.count +=1  
        return True         

    def deQueue(self) -> bool:
        if self.isEmpty() :
            return False
        
        delNode = self.left.next
        self.left.next = delNode.next
        self.left.next.prev = self.left
        delNode.next = delNode.prev = None
        self.count -=1
        return True        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val
        
    def isEmpty(self) -> bool:
        return self.count == 0        

    def isFull(self) -> bool:
        return  self.count == self.size
        
# class MyCircularQueue:
#     def __init__(self, k: int):
#         self.stack = [-1] * k
#         self.size = k
#         self.start = 0
#         self.finish = 0
        
#     def enQueue(self, value: int) -> bool:
#         if self.isFull():
#             return False
        
#         self.stack[self.finish % self.size] = value
#         self.finish +=1
#         return True       

#     def deQueue(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.stack[self.start % self.size] = -1
#         self.start +=1
#         return True       

#     def Front(self) -> int:
#         return self.stack[self.start % self.size] if not self.isEmpty() else -1

#     def Rear(self) -> int:
#         return self.stack[(self.finish -1) % self.size] if not self.isEmpty() else -1
     

#     def isEmpty(self) -> bool:
#         return self.finish - self.start == 0 

#     def isFull(self) -> bool:
#         return self.size == self.finish - self.start
        

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()