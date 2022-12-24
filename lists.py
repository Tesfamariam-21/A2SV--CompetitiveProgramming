if __name__ == '__main__':
    N = int(input())
    li = []
    
    def printList():
        print(li)
    
    def remove(e):
        li.remove(e)
    
    def append(e):
        li.append(e)
    
    def insertList(i, e):
        li.insert(i, e)
    
    def sortList():
        li.sort()
    
    def rev():
        li.sort(reverse= True)
    
    def popElement():
        li.pop()
    

    
    for i in range(N):
        prompt = input()
        
        if prompt.split()[0] == "append":
            append(int(prompt.split()[1]))
        elif prompt.split()[0] == "insert":
            insertList(int(prompt.split()[1]), int(prompt.split()[2]))
        elif prompt.split()[0] == "remove":
            remove(int(prompt.split()[1]))
        elif prompt.split()[0] == "sort":
            sortList()
        elif prompt.split()[0] == "reverse":
            rev()
        elif prompt.split()[0] == "pop":
            popElement()
        elif prompt.split()[0] == "print":
            printList()
        else:
            print("incorrect input")
    
     
  
    
        
    
        
