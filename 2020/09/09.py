nums = [int(x) for x in open('input').read().splitlines()]

print(
    next(
        nums[i]
        for i in range(25, len(nums))
        if not any(nums[i] - x in nums[i - 25:i] and nums[i] != x * 2 for x in nums[i - 25:i])
    )
)

print(
    next(
        min(nums[start:end + 1]) + max(nums[start:end + 1])
        for i in range(25, len(nums))
        for start in range(i - 25, i - 1)
        for end in range(start + 1, i)
        if sum(nums[start:end + 1]) == 1930745883
    )
)
