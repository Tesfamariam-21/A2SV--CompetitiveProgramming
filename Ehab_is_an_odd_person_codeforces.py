n = int(input())
num = list(map(int, input().split()))

nums = sorted(num)
index = -1
evenNum = 0
odd = 0

for i in range(len(nums)):
    if nums[i] % 2 != 0:
        odd +=1
        if evenNum > 0:
            index = i
            break
    elif nums[i] % 2 == 0:
        evenNum +=1

    if odd > 0 and evenNum > 0:
        index = i
        break


if index != -1:
    for i in range(index, 0, -1):
        if nums[index] < nums[i] and nums[index] + nums[i] % 2!= 0:
            nums[i], nums[index] = nums[index], nums[i]
    print(*nums)
else:
    print(*num)
