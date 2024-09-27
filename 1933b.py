for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    while sum(nums) % 3 != 0 and len(nums) > 0:
        if len(nums) == 1:
            while sum(nums) % 3 != 0:
                nums[0] += 1
                ans += 1
        else:
            nums.pop()
            ans += 1
    print(ans)
