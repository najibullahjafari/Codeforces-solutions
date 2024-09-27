n = int(input())
nums = list(map(int, input().split()))
top = 0
current = 0
for c in range(len(nums)-1):
    while nums[c] <= nums[c+1]:
        top += 1
        c += 1

    if nums[c] >= nums[c+1]:
        if top > current:
            current = 0
            while nums[c] <= nums[c+1]:
                current += 1
                c += 1
        else:
            top = 0
            while nums[c] <= nums[c+1]:
                current += 1
                c += 1
if current > top:
    print(current)
else:
    print(top)
