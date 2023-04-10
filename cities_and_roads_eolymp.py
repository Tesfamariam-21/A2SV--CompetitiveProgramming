sz = int(input())
graph = []
edges = 0

for i in range(sz):
    graph.append(list(map(int, input().split())))

for i in range(sz):
    for j in range(sz):
        if graph[i][j] == 1:
            edges +=1

print(edges//2)