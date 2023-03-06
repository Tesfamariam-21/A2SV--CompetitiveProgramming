t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    num = (a + b)// 4

    print(min(a,b, num))