from collections import Counter

n = int(input())
li = []

for i in range(n): 
    li.append(input())

result = Counter(li)

li.clear()

li = list(result.values())

print(len(result))

for i in range(len(result)):
    print(li[i], end= " ")
