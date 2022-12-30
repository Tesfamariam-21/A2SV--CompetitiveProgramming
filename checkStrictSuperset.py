# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    setA = set(map(int, input().split()))
    numOfSubset = int(input())
    strictSuperset = True
    

    
    for i in range(numOfSubset):
        subset = set(map(int, input().split()))
        if not setA.issuperset(subset):
            strictSuperset = False

    print(strictSuperset)
