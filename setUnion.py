# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__== "__main__":
    englishSub = int(input())
    englishSubSet = set(map(int, input().split()))
    frenchSub = int(input())
    frenchSubSet = set(map(int, input().split()))
    
    bothSubs = englishSubSet.union(frenchSubSet)
    
    print(len(bothSubs))
