testcase = int(input())
answer = []



for i in range(testcase):
    numElements = int(input())
    arr = list(map(int, input().split()))
    start = 0
    ptr2 = 0
    summ = 0

    positive = 0
    negative = float("-inf")

    while ptr2 < len(arr) or start < len(arr):
        if arr[start] > 0:
            positive = arr[start]
            ptr2 = start + 1
            while ptr2 < len(arr):
                if arr[ptr2] > 0:
                    positive = max(positive, arr[ptr2])
                    ptr2 += 1
                else:
                    break
            summ += positive
            start = ptr2
        else:
            negative = arr[start]

            while ptr2 < len(arr):
                if arr[ptr2] < 0:
                    negative = max(negative, arr[ptr2])
                    ptr2 += 1
                else:
                    break
            summ += negative
            start = ptr2

    print(summ)

