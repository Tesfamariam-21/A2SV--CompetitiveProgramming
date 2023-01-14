from collections import defaultdict

test_cases = int(input().strip())

for _ in range(test_cases):
    n, m = map(int, input().split())
    li = []
    diagonal_sum = defaultdict(int)
    anti_diagonal_sum = defaultdict(int)
    max_ = index = -1

    for i in range(n):
        arr = list(map(int, input().split()))
        li.append(arr)

    for i in range(n):
        for j in range(m):
            diagonal_sum[i-j] += li[i][j]
            anti_diagonal_sum[j + i] += li[i][j]

    for i in range(n):
        for j in range(m):
            max_ = max(max_, (diagonal_sum[i-j] + anti_diagonal_sum[j+i] - li[i][j]))

    print(max_)



