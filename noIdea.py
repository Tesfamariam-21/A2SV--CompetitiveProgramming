# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    arrayLength, setLength = map(int, input().split())
    array = list(map(int, input().split()))
    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))
    
    happiness = 0
    
    for element in array:
        if element in setA:
            happiness += 1 
        if element in setB:
            happiness -= 1 
    
    
    
    print(happiness)
