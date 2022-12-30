# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    numOfElements = int(input())
    tuple_ = tuple(map(int, input().split()))
    print(hash(tuple_))
    
