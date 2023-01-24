n, m = map(int, input().split())
 
arr1 =  list(map(int, input().split()))
arr2 =  list(map(int, input().split()))
ans = []
 
ptr1, ptr2 = 0, 0
 
for _ in range(m):
    while(ptr1 < n):
        if(arr1[ptr1] < arr2[ptr2]):
            ptr1 += 1
        else:
            break
    ans.append(ptr1)
    ptr2 += 1
 
print(*ans)
