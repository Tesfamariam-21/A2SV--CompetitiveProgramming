if __name__ == '__main__':
    N = int(input())
    li = []

    def remove(e):
        li.remove(e)
    
    def append(e):
        li.append(e)
    
    def insertList(i, e):
        li.insert(i, e)
    
    for i in range(N):
        prompt = input()
        
        if prompt.split()[0] == "append":
            append(int(prompt.split()[1]))
        elif prompt.split()[0] == "insert":
            insertList(int(prompt.split()[1]), int(prompt.split()[2]))
        elif prompt.split()[0] == "remove":
            remove(int(prompt.split()[1]))
        elif prompt.split()[0] == "sort":
            li.sort()
        elif prompt.split()[0] == "reverse":
            li.reverse()
        elif prompt.split()[0] == "pop":
            li.pop()
        elif prompt.split()[0] == "print":
            print(li)
