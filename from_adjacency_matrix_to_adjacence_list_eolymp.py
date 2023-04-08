from collections import defaultdict

sz = int(input())
src = [0]
sink = [0]
graph = []
li = []

for i in range(sz):
    graph.append(list(map(int, input().split())))

for row in graph:
    l = []
    for i in range(len(row)):
        if row[i] == 1:
            l.append(i+1)

    l.insert(0, len(l))
    li.append(l)


for l in li:
    print(*l)