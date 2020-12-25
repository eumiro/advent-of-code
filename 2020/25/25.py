nums = 5764801, 17807724
# nums = 19774466, 7290641

def gen():
    val, step = 1, 0
    while True:
        val = val * 7 % 20201227
        step += 1
        yield step, val

steps, val = next((step, val) for step, val in gen() if val in nums)
print(pow(nums[1 - nums.index(val)], steps, 20201227))
