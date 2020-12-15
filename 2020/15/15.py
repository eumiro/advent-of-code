nums = [0, 3, 6]
nums = [0, 14, 6, 20, 1, 4]

last = {num: i for i, num in enumerate(nums[:-1])}
prev = nums[-1]

for i in range(len(nums), 2020):
    if prev in last:
        num = i - 1 - last[prev]
    else:
        num = 0
    last[prev] = i - 1
    prev = num
print(prev)
