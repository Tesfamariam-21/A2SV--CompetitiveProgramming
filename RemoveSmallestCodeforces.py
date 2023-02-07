testCases = int(input())

for _ in range(testCases):
    num = int(input())
    inp = list(set(map(int, input().split())))
    inp = sorted(inp)
    flag = True

    if len(inp) == 1:
        print('YES')
        continue
    for i in range(len(inp) - 1):
        # print(i)
        if inp[i+1] - inp[i] <= 1:
            continue
        else:
            flag = False
            break
        #     del inp[i]
        #     # c +=1

    if flag:
        print("YES")
    else:
        print("NO")
