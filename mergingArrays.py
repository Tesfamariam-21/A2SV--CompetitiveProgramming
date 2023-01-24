n, m = map(int, input().split())
 
arr1 =  list(map(int, input().split()))
arr2 =  list(map(int, input().split()))
ans = []
 
ptr1, ptr2 = 0, 0
 
while ptr1 < n and ptr2 < m:
    if arr1[ptr1] < arr2[ptr2]:
        ans.append(arr1[ptr1])
        ptr1 += 1
    elif arr1[ptr1] == arr2[ptr2]:
        ans.append(arr1[ptr1])
        ans.append(arr2[ptr2])
        ptr1 += 1
        ptr2 += 1
    else:
        ans.append(arr2[ptr2])
        ptr2 +=1
 
while ptr2 < m:
    ans.append(arr2[ptr2])
    ptr2 +=1
 
while ptr1 < n:
    ans.append(arr1[ptr1])
    ptr1 +=1
 
print(*ans)
