from collections import defaultdict

v = int(input())
t = int(input())
d = defaultdict(list)

for _ in range(t):
    li = list(map(int, input().split()))
    if li[0] == 1:
        d[li[1]].append(li[2])
        d[li[2]].append(li[1])
    else:
        print(*d[li[1]])
