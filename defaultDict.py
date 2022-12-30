# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
inputs = list(map(int, input().split()))
wordsA = defaultdict(list)

for i in range(inputs[0]):
    wordsA[input()].append(i+1)  
    
for i in range(inputs[1]):
    wordB = input()
    if(wordB in wordsA):
        print(*wordsA[wordB])
    else:
        print(-1)
