n, k = map(int, input().split())
nums = list(map(int, input().split()))
nums = sorted(nums)

if k == n:
    print(nums[k-1])
elif k == 0:
    if nums[k] > 1:
        print(nums[0] - 1)
    else:
        print(-1)
elif nums[k] != nums[k-1]:
    print(nums[k-1])
else:
    print(-1)
