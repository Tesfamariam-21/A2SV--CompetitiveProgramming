from collections import Counter

n = int(input())
li = []

li =input().split(" ")
    
result = Counter(li)

for x in result:
    key = x
    value = result[key]
    if value == 1:
        print(key)
