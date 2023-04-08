sz = int(input())
src = [0]
sink = [0]
graph = []

for i in range(sz):
    graph.append(list(map(int, input().split())))
r = 0
for row in graph:
    r +=1
    if 1 not in row:
        sink[0] +=1
        sink.append(r)

g = zip(*graph)
r = 0
for ro in g:
    r += 1
    if 1 not in ro:
        src[0] += 1
        src.append(r)

print(*src)
print(*sink)