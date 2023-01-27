class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = Node()

    def get(self, index: int) -> int:
        count = 0
        temp  = self.head
        
        while count < index:
            temp = temp.next
            count += 1
            if temp.next == None:
                return -1
        if not temp or temp.next == None:
            return -1
        return temp.next.value
                  

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node  
        

    def addAtTail(self, val: int) -> None:
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next
        
        new_node = Node(val)
        last_node.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        prev_index = 0
        prev_node = self.head
        
        while prev_index < index:
            prev_node = prev_node.next
            prev_index += 1
            if prev_node == None:
                return
            
        new_node = Node(val)
        new_node.next = prev_node.next
        prev_node.next = new_node  
        

    def deleteAtIndex(self, index: int) -> None:
        prev_index = 0
        prev_node = self.head
        
        while prev_index < index:
            prev_node = prev_node.next
            prev_index +=1
            if  prev_node.next == None:
                return 
        
        if not prev_node or not prev_node.next:
            return 
        prev_node.next = prev_node.next.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)